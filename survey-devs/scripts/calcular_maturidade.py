#!/usr/bin/env python3
"""Calcula maturidade IA dos devs a partir das respostas do survey.

Lê: survey-devs/respostas-devs.json (output do /importar-survey-devs)
Aplica: rubric.py (regras determinísticas L0-L4 por dimensão)
Gera:
  - saida/maturidade-developer-survey-<DATE>.json (estruturado, para programs)
  - Resumo no stdout

Uso:
    python3 calcular_maturidade.py
    python3 calcular_maturidade.py --input survey-devs/respostas-devs.json
    python3 calcular_maturidade.py --out saida/
    python3 calcular_maturidade.py --force   # ignora guardrail de cobertura
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

# Allow running from any directory
SCRIPT_DIR = Path(__file__).resolve().parent
KIT_ROOT = SCRIPT_DIR.parent.parent  # kit-cliente/
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(KIT_ROOT / "relatorios" / "scripts"))
from rubric import (
    RUBRIC_VERSION,
    score_respondent,
    aggregate_team,
    match_coverage,
    DIMENSIONS,
    label_for,
)

try:
    import branding
except ImportError:  # partial kit copy without relatorios/: degrade to neutral output
    branding = None

# Match-coverage guardrail thresholds (see RUBRICA-MATURIDADE.md).
COVERAGE_WARN_PCT = 70.0
COVERAGE_ABORT_PCT = 40.0


def load_respondents(inp: Path) -> list | None:
    """Load and validate the survey JSON. Returns None (after printing a
    one-line actionable error) on malformed input."""
    try:
        data = json.loads(inp.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido em {inp} (linha {e.lineno}: {e.msg}). Corrija o arquivo ou re-rode /importar-survey-devs.")
        return None
    if not isinstance(data, dict) or not isinstance(data.get("respondents", []), list):
        print(f"❌ Estrutura inesperada em {inp}: esperado objeto com lista 'respondents'. Re-rode /importar-survey-devs.")
        return None
    return data.get("respondents", [])


def coverage_stats(respondents: list) -> dict:
    """Per-respondent rubric match coverage, aggregated (avg/min in %)."""
    per_respondent = []
    for r in respondents:
        matched, answered = match_coverage(r.get("responses", {}))
        if answered:
            per_respondent.append(round(100.0 * matched / answered, 1))
    if not per_respondent:
        return {"avg_pct": 0.0, "min_pct": 0.0, "n_measured": 0}
    return {
        "avg_pct": round(sum(per_respondent) / len(per_respondent), 1),
        "min_pct": min(per_respondent),
        "n_measured": len(per_respondent),
    }


def build_maturity_output(respondents: list, team: dict, source_path: Path,
                          kit_root: Path = KIT_ROOT) -> dict:
    """Single output schema shared by calcular_maturidade.py and gerar_insights.py."""
    metadata = {
        "computed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source": str(source_path.relative_to(kit_root)) if source_path.is_relative_to(kit_root) else str(source_path),
        "n_respondents": len(respondents),
        "rubric_version": f"{RUBRIC_VERSION} (deterministic)",
        "match_coverage": coverage_stats(respondents),
        "anonymous": True,
        "scope": "team aggregate (no individual scores in output)",
    }
    if branding is not None:
        metadata.update(branding.json_metadata())
    return {
        "metadata": metadata,
        "team_overall": {
            "score": team["team_overall_score"],
            "label": team["team_overall_label"],
            "respondents_with_overall": team["n_with_overall"],
        },
        "dimensions": team["dimensions"],
        "ranking": _ranking(team["dimensions"]),
    }


def check_coverage_guardrail(respondents: list, force: bool) -> bool:
    """Warn below COVERAGE_WARN_PCT; abort below COVERAGE_ABORT_PCT unless --force.

    Low coverage means the answer text does not match the canonical rubric
    options (e.g. options translated to EN/ES in Forms), which silently
    deflates scores. Returns True when it is OK to proceed."""
    stats = coverage_stats(respondents)
    avg = stats["avg_pct"]
    if avg >= COVERAGE_WARN_PCT:
        return True
    if avg < COVERAGE_ABORT_PCT and not force:
        print("═" * 60)
        print(f"❌ ABORTADO: cobertura de match da rubrica muito baixa — média {avg:.0f}% (mínimo {stats['min_pct']:.0f}%).")
        print("   As respostas não batem com as opções canônicas do question bank (PT-BR).")
        print("   Causa provável: opções traduzidas/alteradas no Forms. Scores seriam deflacionados para L0/None.")
        print("   Corrija o import (mantenha as opções canônicas) ou rode novamente com --force para prosseguir assim mesmo.")
        print("═" * 60)
        return False
    print("═" * 60)
    print(f"⚠️  ATENÇÃO: cobertura de match da rubrica baixa — média {avg:.0f}% (mínimo {stats['min_pct']:.0f}%).")
    print("   Parte das respostas não bate com as opções canônicas do question bank (PT-BR).")
    print("   Os scores abaixo podem estar SUBESTIMADOS. Verifique se as opções foram traduzidas/alteradas no Forms.")
    if force and avg < COVERAGE_ABORT_PCT:
        print("   (--force ativo: prosseguindo apesar de cobertura abaixo de 40%.)")
    print("═" * 60)
    return True


def main():
    ap = argparse.ArgumentParser(description="Calcula a maturidade IA do time (rubrica determinística L0-L4).")
    ap.add_argument("--input", default=str(KIT_ROOT / "survey-devs/respostas-devs.json"),
                    help="Path to respostas-devs.json")
    ap.add_argument("--out", default=str(KIT_ROOT / "saida"),
                    help="Output directory")
    ap.add_argument("--force", action="store_true",
                    help="Prossegue mesmo com cobertura de match da rubrica abaixo de 40%%")
    args = ap.parse_args()

    inp = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not inp.exists():
        print(f"❌ Input não encontrado: {inp}")
        print(f"   Rode /importar-survey-devs primeiro.")
        return 1

    respondents = load_respondents(inp)
    if respondents is None:
        return 1
    n = len(respondents)
    print(f"\n📊 Calculando maturidade IA — {n} respondentes (anônimos)\n")

    if n == 0:
        print("❌ Nenhum respondente.")
        return 1

    if not check_coverage_guardrail(respondents, args.force):
        return 1

    # Score each respondent (internal — never shown individually in output report)
    individual_scores = []
    for r in respondents:
        scores = score_respondent(r.get("responses", {}))
        individual_scores.append(scores)

    # Aggregate
    team = aggregate_team(individual_scores)

    # Build output JSON
    date = datetime.date.today().isoformat()
    output = build_maturity_output(respondents, team, inp)

    out_path = out_dir / f"maturidade-developer-survey-{date}.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Output: {out_path.relative_to(KIT_ROOT) if out_path.is_relative_to(KIT_ROOT) else out_path}\n")

    # Console summary
    print("═" * 60)
    print(f"MATURIDADE IA DO TIME (n={n} devs anônimos)")
    print("═" * 60)
    if team["team_overall_score"] is not None:
        print(f"\n🎯 Overall: {team['team_overall_score']:.2f} ({team['team_overall_label']})\n")
    else:
        print("\n⚠ Sem cobertura suficiente para calcular overall.\n")

    print(f"{'Dimensão':<10} {'Score':<8} {'Rótulo':<28} {'Distribuição (% devs)':<35}")
    print("-" * 90)
    for did, _, _, _ in DIMENSIONS:
        d = team["dimensions"][did]
        if d["team_score"] is None:
            print(f"{did:<10} {'—':<8} {'Sem dados':<28}")
            continue
        dist = d["distribution_pct"]
        dist_str = f"L0={dist['L0']}% L1={dist['L1']}% L2={dist['L2']}% L3={dist['L3']}% L4={dist['L4']}%"
        score_str = f"{d['team_score']:.2f}"
        print(f"{did:<10} {score_str:<8} {d['label']:<28} {dist_str:<35}")
    print()

    print(f"🏆 Top 3 dimensões mais fortes:")
    for i, (did, name, score) in enumerate(_ranking(team["dimensions"])["top"], 1):
        print(f"   {i}. {did} {name} — {score:.2f} ({label_for(score)})")
    print()

    print(f"⚠ Top 3 dimensões mais fracas (oportunidades):")
    for i, (did, name, score) in enumerate(_ranking(team["dimensions"])["bottom"], 1):
        print(f"   {i}. {did} {name} — {score:.2f} ({label_for(score)})")
    print()

    print("Próximo: /insights-developer-survey gera o relatório completo em PT-BR.")
    return 0


def _ranking(dims: dict) -> dict:
    """Top/bottom 3 dimensions by team score."""
    scored = [
        (did, d["name"], d["team_score"])
        for did, d in dims.items()
        if d["team_score"] is not None
    ]
    sorted_desc = sorted(scored, key=lambda x: x[2], reverse=True)
    return {
        "top": sorted_desc[:3],
        "bottom": list(reversed(sorted_desc[-3:])) if len(sorted_desc) >= 3 else sorted_desc,
    }


if __name__ == "__main__":
    sys.exit(main())
