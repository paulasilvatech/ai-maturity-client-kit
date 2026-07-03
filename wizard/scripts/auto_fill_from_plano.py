#!/usr/bin/env python3
"""Mode D do wizard: auto-fill implementation-guide-inputs.json a partir do plano-capacitacao.

Lê (fonte primária): saida/plano-capacitacao-<DATE>.json (output estruturado de /plano-capacitacao)
Fallback (deprecated): saida/plano-capacitacao-<DATE>.md via regex (perde detalhes; use o JSON)
Extrai: Champions, training, calendário, ADKAR-knowledge, quick wins
Gera: implementation-guide-inputs.json (na raiz do kit) com 6 dos 9 campos preenchidos

Uso:
    python3 auto_fill_from_plano.py
    python3 auto_fill_from_plano.py --plano saida/plano-capacitacao-2026-07-03.json
    python3 auto_fill_from_plano.py --plano saida/plano-capacitacao-2026-07-03.md --out Y
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(KIT / "relatorios" / "scripts"))
try:
    import branding
except ImportError:  # partial kit copy without relatorios/: degrade to neutral output
    import types

    branding = types.SimpleNamespace(json_metadata=lambda: {})

MISSING_W1_4 = "(preencher — sem dados suficientes nas semanas 1-4 do calendário)"
MISSING_W5_8 = "(preencher — sem dados suficientes nas semanas 5-8)"
MISSING_W9_12 = "(preencher — sem dados suficientes nas semanas 9-12)"


def find_latest(out_dir: Path, pattern: str) -> Path | None:
    """Find the most recent plano-capacitacao file matching pattern in saida/."""
    candidates = sorted(out_dir.glob(pattern), reverse=True)
    return candidates[0] if candidates else None


# =========================================================
# Primary source: structured JSON emitted by gerar_plano_capacitacao.py
# =========================================================

def steering_from_champions(active: list[dict]) -> str:
    if not active:
        return ""
    lines = ["Comitê Executivo Diretivo (Champions ativos identificados pelo Learning Survey):", ""]
    for person in active:
        lines.append(f"- {person.get('name', '?')} — {person.get('email', '?')}")
    return "\n".join(lines)


def calendar_table_from_entries(entries: list[dict]) -> str:
    if not entries:
        return ""
    lines = [
        "| Semana | Workshop | Audiência | Champion | Formato |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        weeks = ", ".join(f"W{week}" for week in entry.get("weeks", []))
        lines.append(f"| {weeks} | {entry.get('activity', '?')} | {entry.get('audience', '?')} | "
                     f"{entry.get('champion', '?')} | {entry.get('format', '?')} |")
    return "\n".join(lines)


def training_from_cohorts(cohorts: list[dict]) -> str:
    if not cohorts:
        return ""
    lines = []
    for cohort in cohorts:
        lines.extend([
            f"### Cohort {cohort.get('dimension', '?')} ({cohort.get('name', '?')})",
            f"- **{cohort.get('devs', '?')} devs querem evoluir nesta dimensão**",
            f"- **Formato preferido pelo time:** {cohort.get('preferred_format', 'Híbrido')}",
            f"- **Plano:** {cohort.get('plan', 'cohort de 4-6 semanas')}",
            "",
        ])
    return "\n".join(lines).strip()


def quick_wins_from_plan(plan: dict, weeks_range: tuple[int, int]) -> str:
    """Expand EVERY week of every calendar/schedule entry into the range —
    multi-week rows (e.g. weeks [6, 8, 10, 12]) contribute one item per week."""
    items: list[str] = []
    for entry in plan.get("calendar_90_days", []):
        for week in entry.get("weeks", []):
            if weeks_range[0] <= week <= weeks_range[1]:
                items.append(f"- W{week}: {entry.get('activity', '?')} ({entry.get('format', '?')})")
    for row in plan.get("schedule_30_days", []):
        week = row.get("week")
        if week is not None and weeks_range[0] <= week <= weeks_range[1]:
            items.append(f"- W{week}: {row.get('activities', '?')}")
    return "\n".join(items)


def extract_fields_from_json(plan: dict) -> dict:
    """Build the 6 auto-fillable wizard fields from the structured plano JSON."""
    champions = steering_from_champions(plan.get("champions", {}).get("active", []))
    calendar = calendar_table_from_entries(plan.get("calendar_90_days", []))
    training_body = training_from_cohorts(plan.get("cohorts", []))
    top_topics = [(t.get("topic", "?"), t.get("count", 0)) for t in plan.get("top_topics", [])[:5]]
    return {
        "champions": champions,
        "calendar": calendar,
        "training_body": training_body,
        "top_topics": top_topics,
        "quick_w1_4": quick_wins_from_plan(plan, (1, 4)),
        "quick_w5_8": quick_wins_from_plan(plan, (5, 8)),
        "quick_w9_12": quick_wins_from_plan(plan, (9, 12)),
    }


# =========================================================
# Fallback source (DEPRECATED): regex parsing of the .md report
# =========================================================

def extract_section(plano_md: str, section_header_pattern: str) -> str:
    """Extract content of a section by header regex (until next ## or end)."""
    pat = re.compile(
        rf"## {section_header_pattern}.*?\n(.*?)(?=\n## |\Z)",
        re.DOTALL,
    )
    m = pat.search(plano_md)
    return m.group(1).strip() if m else ""


def extract_champions_active(plano_md: str) -> str:
    """Extract Active Champions table from section 4."""
    section = extract_section(plano_md, r"4 · Champions Network")
    # Find the "Ativos" subsection table
    active_block = re.search(
        r"### 🥇 Ativos.*?\n(.*?)(?=\n### |\Z)",
        section,
        re.DOTALL,
    )
    if not active_block:
        return ""
    block = active_block.group(1)
    # Extract names from table (column 1 between |)
    names = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|@]+@[^|\s]+)\s*\|", block, re.MULTILINE)
    if not names:
        return ""
    lines = ["Comitê Executivo Diretivo (Champions ativos identificados pelo Learning Survey):", ""]
    for name, email in names:
        if name.strip().lower() not in ("nome", "---"):
            lines.append(f"- {name.strip()} — {email.strip()}")
    return "\n".join(lines)


def extract_calendar(plano_md: str) -> str:
    """Extract calendar from section 5 (próximos 90 dias)."""
    section = extract_section(plano_md, r"5 · Calendário sugerido")
    if not section:
        return ""
    # Return as markdown table (already in plano)
    table_match = re.search(r"\|.*?\|.*?(?=\n\n|\Z)", section, re.DOTALL)
    return table_match.group(0).strip() if table_match else section[:500]


def extract_top_topics(plano_md: str, n=5) -> list[tuple[str, int]]:
    """Extract top topics from sumário (top 10 listed as 1. **topic** — N devs)."""
    section = extract_section(plano_md, r"1 · Sumário Executivo")
    matches = re.findall(r"^\d+\.\s+\*\*(.+?)\*\* — (\d+) devs", section, re.MULTILINE)
    return [(m[0], int(m[1])) for m in matches[:n]]


def extract_quick_wins_calendar(plano_md: str, weeks_range: tuple[int, int]) -> str:
    """Extract quick wins for a week range from sections 5 and 11, expanding
    multi-week rows like '| W6, W8, W10, W12 | ... |' into one item per week."""
    section_5 = extract_section(plano_md, r"5 · Calendário sugerido")
    section_11 = extract_section(plano_md, r"11 · Cronograma")

    items = []
    for src in [section_5, section_11]:
        for line in src.split("\n"):
            m = re.match(r"\|([^|]*W\d+[^|]*)\|([^|]+)\|", line)
            if not m:
                continue
            weeks = [int(w) for w in re.findall(r"W(\d+)", m.group(1))]
            activity = m.group(2).strip().strip("*").strip()
            if not activity or activity == "Workshop":
                continue
            for week in weeks:
                if weeks_range[0] <= week <= weeks_range[1]:
                    items.append(f"- W{week}: {activity}")
    return "\n".join(items)


def extract_fields_from_md(plano_md: str) -> dict:
    """DEPRECATED fallback: regex extraction from the human-readable report."""
    cohorts_section = extract_section(plano_md, r"3 · Cohorts sugeridos")
    return {
        "champions": extract_champions_active(plano_md),
        "calendar": extract_calendar(plano_md),
        "training_body": cohorts_section[:1500] if cohorts_section else "",
        "top_topics": extract_top_topics(plano_md),
        "quick_w1_4": extract_quick_wins_calendar(plano_md, (1, 4)),
        "quick_w5_8": extract_quick_wins_calendar(plano_md, (5, 8)),
        "quick_w9_12": extract_quick_wins_calendar(plano_md, (9, 12)),
    }


# =========================================================
# Payload assembly
# =========================================================

def build_payload(fields: dict, plano_name: str) -> dict:
    comm_plan = "Plano de Comunicação derivado do calendário sugerido:\n\n"
    comm_plan += fields["calendar"] if fields["calendar"] else "(ver Parte 5 do plano de capacitação)"

    training = "Plano de Treinamento (cohorts por dimensão derivados do Learning Survey):\n\n"
    training += fields["training_body"] if fields["training_body"] else "(ver Parte 3 do plano de capacitação)"

    adkar = """Plano de Mudança ADKAR derivado do Learning Survey:

**Awareness:** Comunicar plano de capacitação consolidado em all-hands; cada dev recebe seu plano personalizado por email.

**Desire:** Tornar visível que workshops têm inscritos pré-validados (não opt-in genérico).

**Knowledge:** Workshops top 5 (do Learning Survey):
"""
    for i, (topic, count) in enumerate(fields["top_topics"][:5], 1):
        adkar += f"{i}. {topic} ({count} inscritos)\n"
    adkar += """
**Ability:** Office hours quinzenal (sem agenda fixa, devs trazem dúvidas práticas).

**Reinforcement:** Métricas de adoção mensais publicadas; reconhecimento dos Champions; revisão trimestral do plano com novo Learning Survey.
"""

    return {
        "metadata": {
            "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "generator": "wizard/scripts/auto_fill_from_plano.py (Mode D)",
            "source_plano": plano_name,
            "completion_pct": 67,  # 6 dos 9 campos preenchidos
            "manual_required": ["tpo", "raci_matrix"],
            "contains_personal_data": True,
            **branding.json_metadata(),
        },
        "implementation_guide_inputs": {
            "executive_steering_committee": fields["champions"] or "(preencher manualmente — sem Champions ativos identificados pelo Learning Survey)",
            "tpo": "(preencher manualmente — Learning Survey não cobre TPO. Liste Programa Manager + escritório + autoridade de decisão)",
            "raci_matrix": "(preencher manualmente — Learning Survey não cobre RACI. Use template em wizard/implementation-guide-inputs.template.json)",
            "communication_plan": comm_plan,
            "training_plan": training,
            "adkar_notes": adkar,
            "quick_wins_w1_4": fields["quick_w1_4"] or MISSING_W1_4,
            "quick_wins_w5_8": fields["quick_w5_8"] or MISSING_W5_8,
            "quick_wins_w9_12": fields["quick_w9_12"] or MISSING_W9_12,
        },
    }


def load_plan_json(path: Path) -> dict | None:
    """Load the structured plano JSON; one-line actionable error on bad input."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido em {path} (linha {e.lineno}: {e.msg}). Re-rode /plano-capacitacao para regenerar.")
        return None
    if not isinstance(data, dict):
        print(f"❌ Estrutura inesperada em {path}: esperado objeto JSON. Re-rode /plano-capacitacao.")
        return None
    return data


def resolve_sources(plano_arg: str | None) -> tuple[Path | None, Path | None]:
    """Return (json_path, md_path); exactly one is set when a source exists."""
    if plano_arg:
        p = Path(plano_arg)
        if p.suffix == ".json":
            return (p, None)
        sibling_json = p.with_suffix(".json")
        if sibling_json.exists():
            print(f"ℹ Encontrado {sibling_json.name} ao lado do .md — usando o JSON estruturado (fonte primária).")
            return (sibling_json, None)
        return (None, p)
    latest_json = find_latest(KIT / "saida", "plano-capacitacao-*.json")
    if latest_json:
        return (latest_json, None)
    return (None, find_latest(KIT / "saida", "plano-capacitacao-*.md"))


def main():
    ap = argparse.ArgumentParser(description="Auto-preenche implementation-guide-inputs.json a partir do plano de capacitação (Mode D).")
    ap.add_argument("--plano", default=None,
                    help="Path para plano-capacitacao-DATE.json ou .md (default: mais recente em saida/)")
    ap.add_argument("--out", default=str(KIT / "implementation-guide-inputs.json"))
    args = ap.parse_args()

    out_path = Path(args.out)
    json_path, md_path = resolve_sources(args.plano)
    source = json_path or md_path

    if not source or not source.exists():
        print(f"❌ Plano de capacitação não encontrado em saida/.")
        print(f"   Rode /plano-capacitacao primeiro (após /importar-survey-learning).")
        return 1

    print(f"📖 Lendo: {source.relative_to(KIT) if source.is_relative_to(KIT) else source}")

    if json_path:
        plan = load_plan_json(json_path)
        if plan is None:
            return 1
        fields = extract_fields_from_json(plan)
    else:
        print("⚠ DEPRECATED: parsing do .md via regex (pode perder detalhes, ex. edições manuais).")
        print("  Re-rode /plano-capacitacao com a versão atual para gerar o JSON estruturado (fonte primária).")
        fields = extract_fields_from_md(source.read_text(encoding="utf-8"))

    payload = build_payload(fields, source.name)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✅ Mode D auto-fill → {out_path.relative_to(KIT) if out_path.is_relative_to(KIT) else out_path}")
    print(f"\n📊 Preenchimento automático:")
    print(f"   ✓ executive_steering_committee  (Champions ativos)")
    print(f"   ✓ communication_plan            (Calendário)")
    print(f"   ✓ training_plan                 (Cohorts por dimensão)")
    print(f"   ✓ adkar_notes                   (Knowledge = Top 5 workshops)")
    print(f"   ✓ quick_wins_w1_4 / w5_8 / w9_12 (Cronograma)")
    print(f"\n⚠ Este arquivo contém dados pessoais (nomes/emails). Não commitar nem compartilhar publicamente.")
    print(f"\n⚠ Você precisa preencher MANUALMENTE (Learning Survey não cobre):")
    print(f"   • tpo (Technology Product Owner)")
    print(f"   • raci_matrix")
    print(f"\n💡 Próximo: /gerar-relatorio  → 5 PDFs com Parte 4 personalizada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
