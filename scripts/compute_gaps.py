#!/usr/bin/env python3
"""Compute gap analysis (target vs current score) per capability.

Reads:  saida/scores.json (from compute_scores.py) + respostas.json (target_overrides)
        + framework.json
Writes: saida/gaps.json (schema documented in .github/skills/gap-analysis/SKILL.md)

Rules (referencia/pontuacao-e-calculo.md section 8):
    target_level   = target_overrides[capability_id] or 3.0 (default)
    gap_size       = max(0, target_level - current_score)
    priority_score = capability_weight x gap_size
    priority       >= 2.4 P0 | >= 1.6 P1 | >= 0.9 P2 | else P3
Capabilities without answers or that already met the target are excluded.

Capability scores are recomputed at full precision from respostas.json (the values
in scores.json are rounded to 3 decimals for display); scores.json is required and
cross-checked so the pipeline never runs on stale data.

Usage:
    python3 scripts/compute_gaps.py
    python3 scripts/compute_gaps.py --respostas respostas.json --out saida/gaps.json
    python3 scripts/compute_gaps.py --now 2026-05-08T16:20:08Z   # deterministic timestamp
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from compute_scores import (  # noqa: E402
    KIT_ROOT,
    compute,
    fail,
    label_for,
    load_json,
    parse_now,
    r3,
    rel_to_kit,
    validate_framework,
    warn,
    write_json,
)

DEFAULT_TARGET = 3.0
GAP_EPSILON = 1e-9

# Priority labels and suggested horizons are client-facing PT-BR strings
# (must match the platform verbatim).
PRIORITY_P0 = "P0 — Crítico"
PRIORITY_P1 = "P1 — Alto"
PRIORITY_P2 = "P2 — Médio"
PRIORITY_P3 = "P3 — Baixo"

HORIZON_BY_PRIORITY = {
    PRIORITY_P0: "30 dias",
    PRIORITY_P1: "Próximo trimestre",
    PRIORITY_P2: "Semestre",
    PRIORITY_P3: "Backlog / monitorar",
}

# For "most critical first" comparisons in downstream scripts.
PRIORITY_ORDER = [PRIORITY_P0, PRIORITY_P1, PRIORITY_P2, PRIORITY_P3]


def classify_priority(priority_score: float) -> str:
    if priority_score >= 2.4:
        return PRIORITY_P0
    if priority_score >= 1.6:
        return PRIORITY_P1
    if priority_score >= 0.9:
        return PRIORITY_P2
    return PRIORITY_P3


def validate_targets(target_overrides: dict, known_cap_ids: set[str]) -> None:
    for cap_id, target in target_overrides.items():
        if isinstance(target, bool) or not isinstance(target, (int, float)) or not (0 <= target <= 4):
            fail(f"respostas: target_overrides[{cap_id}] = {target!r} is invalid: "
                 "use a number in [0, 4]")
        if cap_id not in known_cap_ids:
            warn(f"respostas: target_overrides has unknown capability id {cap_id} (ignored)")


def cross_check_scores(capabilities: list[dict], scores_doc: dict, scores_path: Path) -> None:
    """Ensure scores.json matches the recomputed values (stale-file guard)."""
    published = {c.get("id"): c.get("score") for c in scores_doc.get("capabilities", [])}
    for cap in capabilities:
        if cap["id"] not in published:
            fail(f"{rel_to_kit(scores_path)} has no entry for {cap['id']}: "
                 "re-run compute_scores.py first")
        if published[cap["id"]] != r3(cap["score"]):
            fail(f"{rel_to_kit(scores_path)} is stale ({cap['id']}: {published[cap['id']]} "
                 f"vs {r3(cap['score'])}): re-run compute_scores.py first")


def build_gaps(capabilities: list[dict], target_overrides: dict) -> list[dict]:
    """Gap entries sorted by priority_score desc (framework order breaks ties)."""
    gaps = []
    for cap in capabilities:
        if cap["score"] is None:
            continue  # no answers: flagged as coverage warning in the report, not a gap
        target = float(target_overrides.get(cap["id"], DEFAULT_TARGET))
        gap_size = max(0.0, target - cap["score"])
        if gap_size <= GAP_EPSILON:
            continue  # target already met
        priority_score = cap["weight"] * gap_size
        priority = classify_priority(priority_score)
        gaps.append({
            "capability_id": cap["id"],
            "capability_name_pt_br": cap["name_pt_br"],
            "pillar_id": cap["pillar_id"],
            "current_score": r3(cap["score"]),
            "current_label": label_for(cap["score"]),
            "target_level": target,
            "gap_size": r3(gap_size),
            "weight": cap["weight"],
            "priority_score": r3(priority_score),
            "priority": priority,
            "horizon_suggested": HORIZON_BY_PRIORITY[priority],
            "strategies": cap["strategies"],
            "_priority_score_raw": priority_score,
        })
    gaps.sort(key=lambda g: -g["_priority_score_raw"])
    for rank, gap in enumerate(gaps, 1):
        del gap["_priority_score_raw"]
        gaps[rank - 1] = {"rank": rank, **gap}
    return gaps


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute gap analysis and P0-P3 prioritization per capability."
    )
    parser.add_argument("--scores", default=str(KIT_ROOT / "saida" / "scores.json"),
                        help="Path to scores.json (default: saida/scores.json)")
    parser.add_argument("--respostas", default=str(KIT_ROOT / "respostas.json"),
                        help="Path to respostas.json (default: kit root respostas.json)")
    parser.add_argument("--framework", default=str(KIT_ROOT / "framework.json"),
                        help="Path to framework.json (default: kit root framework.json)")
    parser.add_argument("--out", default=str(KIT_ROOT / "saida" / "gaps.json"),
                        help="Output path (default: saida/gaps.json)")
    parser.add_argument("--now", default=None, metavar="ISO8601",
                        help="Override metadata.computed_at for deterministic output "
                             "(e.g. 2026-05-08T16:20:08Z; default: current UTC time)")
    args = parser.parse_args()

    computed_at = parse_now(args.now)
    scores_doc = load_json(Path(args.scores), "run compute_scores.py first")
    respostas = load_json(Path(args.respostas),
                          "copy respostas.json.example to respostas.json and fill it in first")
    framework = load_json(Path(args.framework), "the kit framework file was not found")
    validate_framework(framework)

    responses = respostas.get("responses")
    if not isinstance(responses, dict) or not responses:
        fail(f"{rel_to_kit(Path(args.respostas))} has no 'responses' object: fill it in "
             "(see respostas.json.example)")

    result = compute(framework, responses)
    cross_check_scores(result["capabilities"], scores_doc, Path(args.scores))

    target_overrides = respostas.get("target_overrides") or {}
    if not isinstance(target_overrides, dict):
        fail("respostas: 'target_overrides' must be an object mapping capability id to target level")
    validate_targets(target_overrides, {c["id"] for c in result["capabilities"]})

    gaps = build_gaps(result["capabilities"], target_overrides)
    document = {
        "metadata": {
            "computed_at": computed_at,
            "default_target": DEFAULT_TARGET,
            "total_capabilities_with_gap": len(gaps),
        },
        "summary": {
            "P0": sum(1 for g in gaps if g["priority"] == PRIORITY_P0),
            "P1": sum(1 for g in gaps if g["priority"] == PRIORITY_P1),
            "P2": sum(1 for g in gaps if g["priority"] == PRIORITY_P2),
            "P3": sum(1 for g in gaps if g["priority"] == PRIORITY_P3),
        },
        "gaps": gaps,
    }
    out_path = Path(args.out)
    write_json(out_path, document)

    summary = document["summary"]
    print(f"Gap analysis -> {rel_to_kit(out_path)}")
    print(f"  Capabilities with gap: {len(gaps)}")
    print(f"  Distribution: P0={summary['P0']} | P1={summary['P1']} | "
          f"P2={summary['P2']} | P3={summary['P3']}")
    top = [g for g in gaps if g["priority"] in (PRIORITY_P0, PRIORITY_P1)][:5]
    if top:
        print("  Top priorities (P0/P1):")
        for gap in top:
            print(f"    {gap['rank']}. {gap['capability_id']} {gap['capability_name_pt_br']} "
                  f"gap {gap['gap_size']} -> priority {gap['priority_score']} ({gap['priority']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
