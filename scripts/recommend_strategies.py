#!/usr/bin/env python3
"""Map capability gaps to the 7 strategies (S1-S7) and rank them by impact.

Reads:  saida/gaps.json (from compute_gaps.py) + framework.json
        (strategies, technologies_per_strategy, cap -> strategies mapping)
Writes: saida/recomendacoes.json (schema in .github/skills/recommend-strategies/SKILL.md)

Rules:
  - Each gap contributes its priority_score to every strategy it maps to.
  - ranked_strategies: every strategy with at least one related gap, sorted by
    cumulative_priority desc (tie: most critical max_priority, then more related
    capabilities, then strategy id).
  - skipped_strategies: strategies with no related gap, plus strategies whose
    cumulative_priority is below 0.9 (only P3 gaps: monitor, do not invest yet).
  - Technologies come exclusively from framework.json::technologies_per_strategy.
  - first_action / expected_outcome are fixed deterministic templates (PT-BR,
    client-facing) — never invented per run.

Usage:
    python3 scripts/recommend_strategies.py
    python3 scripts/recommend_strategies.py --gaps saida/gaps.json --out saida/recomendacoes.json
    python3 scripts/recommend_strategies.py --now 2026-05-08T16:20:08Z   # deterministic timestamp
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from compute_scores import (  # noqa: E402
    KIT_ROOT,
    fail,
    load_json,
    parse_now,
    r3,
    rel_to_kit,
    write_json,
)
from compute_gaps import HORIZON_BY_PRIORITY, PRIORITY_ORDER  # noqa: E402

# Strategies whose cumulative_priority stays below this cutoff (only P3 gaps)
# are additionally listed under skipped_strategies ("monitor, do not invest yet").
LOW_IMPACT_CUTOFF = 0.9

# Deterministic action templates per strategy (client-facing PT-BR; fixed by the
# kit playbook — see .github/skills/recommend-strategies/SKILL.md).
FIRST_ACTION = {
    "S1": "Inventário de repositórios atuais → plano de migração para GitHub Enterprise Cloud em 3 ondas.",
    "S2": "Definir SLOs/SLIs para serviços críticos; implantar Azure Monitor + dashboards Grafana.",
    "S3": "Selecionar 1–2 apps piloto; replatforming para Azure Container Apps + IaC com Terraform.",
    "S4": "Identificar 2 casos de uso de alto ROI; PoC com Azure OpenAI + Prompt Flow.",
    "S5": "Rollout Copilot Enterprise em 2 squads piloto; medir adoção e produtividade DORA por 8 semanas.",
    "S6": "Pilot Semantic Kernel para 1 workflow interno; estabelecer guardrails e observabilidade.",
    "S7": "Habilitar GitHub Advanced Security em todos repos; gerar SBOM dos serviços críticos.",
}

EXPECTED_OUTCOME = {
    "S1": "Consolidar 100% dos repositórios no GitHub Enterprise Cloud em 2-3 trimestres.",
    "S2": "Atingir SLOs documentados em 100% dos serviços críticos em 2 trimestres.",
    "S3": "Modernizar 5-8 apps legacy para cloud-native em 12 meses.",
    "S4": "Lançar 2-3 features IA em produção com OKRs claros em 6 meses.",
    "S5": "Subir capabilities de produtividade para L3 em ~2 trimestres com ganho DORA mensurado.",
    "S6": "Operar 1-2 agentes em produção com guardrails sólidos em 6 meses.",
    "S7": "Reduzir vulnerabilidades críticas em 80%+ em 1 trimestre via GHAS + SBOM.",
}

FALLBACK_ACTION = "Detalhar com arquiteto Microsoft GBB."


def priority_rank(priority: str) -> int:
    """0 = most critical (P0). Unknown labels sort last."""
    try:
        return PRIORITY_ORDER.index(priority)
    except ValueError:
        return len(PRIORITY_ORDER)


def aggregate(gaps: list[dict], framework: dict) -> tuple[list[dict], list[dict]]:
    """Group gaps per strategy and rank. Returns (ranked, skipped)."""
    strategies = framework.get("strategies") or []
    if not strategies:
        fail("framework.json has no 'strategies' list: the file is corrupted or is not the kit framework")
    technologies = framework.get("technologies_per_strategy") or {}

    buckets = {s["id"]: [] for s in strategies}
    for gap in gaps:  # gaps.json is already sorted by priority_score desc
        for strategy_id in gap.get("strategies", []):
            if strategy_id not in buckets:
                fail(f"gaps.json references unknown strategy {strategy_id}: "
                     "re-run compute_gaps.py against the current framework.json")
            buckets[strategy_id].append(gap)

    entries = []
    for strategy in strategies:
        related = buckets[strategy["id"]]
        if not related:
            continue
        cumulative = sum(g["priority_score"] for g in related)
        max_priority = min((g["priority"] for g in related), key=priority_rank)
        entries.append({
            "strategy_id": strategy["id"],
            "strategy_name": strategy.get("name", strategy["id"]),
            "cumulative_priority": r3(cumulative),
            "max_priority": max_priority,
            "horizon": HORIZON_BY_PRIORITY.get(max_priority, "Backlog / monitorar"),
            "related_capabilities": [
                {
                    "id": g["capability_id"],
                    "name_pt_br": g["capability_name_pt_br"],
                    "gap_size": g["gap_size"],
                    "priority": g["priority"],
                }
                for g in related
            ],
            "related_capabilities_count": len(related),
            "technologies": technologies.get(strategy["id"], []),
            "first_action": FIRST_ACTION.get(strategy["id"], FALLBACK_ACTION),
            "expected_outcome": EXPECTED_OUTCOME.get(strategy["id"], FALLBACK_ACTION),
        })

    entries.sort(key=lambda e: (
        -e["cumulative_priority"],
        priority_rank(e["max_priority"]),
        -e["related_capabilities_count"],
        e["strategy_id"],
    ))
    ranked = [{"rank": i, **entry} for i, entry in enumerate(entries, 1)]

    low_impact = {e["strategy_id"] for e in entries if e["cumulative_priority"] < LOW_IMPACT_CUTOFF}
    skipped = [
        {"strategy_id": s["id"], "strategy_name": s.get("name", s["id"])}
        for s in strategies
        if not buckets[s["id"]] or s["id"] in low_impact
    ]
    return ranked, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rank strategies S1-S7 by cumulative gap priority and generate the action plan."
    )
    parser.add_argument("--gaps", default=str(KIT_ROOT / "saida" / "gaps.json"),
                        help="Path to gaps.json (default: saida/gaps.json)")
    parser.add_argument("--framework", default=str(KIT_ROOT / "framework.json"),
                        help="Path to framework.json (default: kit root framework.json)")
    parser.add_argument("--out", default=str(KIT_ROOT / "saida" / "recomendacoes.json"),
                        help="Output path (default: saida/recomendacoes.json)")
    parser.add_argument("--now", default=None, metavar="ISO8601",
                        help="Override metadata.computed_at for deterministic output "
                             "(e.g. 2026-05-08T16:20:08Z; default: current UTC time)")
    args = parser.parse_args()

    computed_at = parse_now(args.now)
    gaps_path = Path(args.gaps)
    gaps_doc = load_json(gaps_path, "run compute_gaps.py first")
    framework = load_json(Path(args.framework), "the kit framework file was not found")

    gaps = gaps_doc.get("gaps")
    if not isinstance(gaps, list):
        fail(f"{rel_to_kit(gaps_path)} has no 'gaps' list: re-run compute_gaps.py first")

    ranked, skipped = aggregate(gaps, framework)
    document = {
        "metadata": {
            "computed_at": computed_at,
            "based_on": rel_to_kit(gaps_path),
        },
        "ranked_strategies": ranked,
        "skipped_strategies": skipped,
    }
    out_path = Path(args.out)
    write_json(out_path, document)

    print(f"Recommendations -> {rel_to_kit(out_path)}")
    if ranked:
        print("  Top strategies by cumulative impact:")
        for entry in ranked[:3]:
            print(f"    {entry['rank']}. {entry['strategy_id']} {entry['strategy_name']} "
                  f"(priority {entry['cumulative_priority']}, "
                  f"{entry['related_capabilities_count']} capabilities, {entry['max_priority']})")
    else:
        print("  No strategy has related gaps (all targets met or no answers).")
    if skipped:
        print("  Skipped (no relevant gaps or low impact): "
              + ", ".join(s["strategy_id"] for s in skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main())
