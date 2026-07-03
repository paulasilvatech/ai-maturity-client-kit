#!/usr/bin/env python3
"""Compute maturity scores from respostas.json using the official SUMPRODUCT algorithm.

Reads:  respostas.json (client answers) + framework.json (weights, questions)
Writes: saida/scores.json (schema documented in .github/skills/calcular-scores/SKILL.md)

Algorithm reference: referencia/pontuacao-e-calculo.md (1:1 with the platform).
Three layers, all weighted averages (SUMPRODUCT):
  1. capability score = sum(level x q.weight) / sum(q.weight) over answered questions
  2. pillar score     = sum(cap_score x cap.weight) / sum(cap.weight) over scored caps
  3. overall score    = same SUMPRODUCT over ALL capabilities (NOT mean of pillars)

No rounding during computation; outputs are rounded to 3 decimals for display only.

Usage:
    python3 scripts/compute_scores.py
    python3 scripts/compute_scores.py --respostas respostas.json --out saida/scores.json
    python3 scripts/compute_scores.py --now 2026-05-08T16:20:08Z   # deterministic timestamp
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT_ROOT = SCRIPT_DIR.parent

# Maturity label cuts (referencia/pontuacao-e-calculo.md section 7).
# Labels are client-facing PT-BR strings and must match the platform verbatim.
LABEL_L0 = "L0 — Inicial"
LABEL_L1 = "L1 — Em Desenvolvimento"
LABEL_L2 = "L2 — Definido"
LABEL_L3 = "L3 — Gerenciado"
LABEL_L4 = "L4 — Otimizando"
LABEL_NO_ANSWER = "Sem resposta"


def fail(msg: str) -> None:
    """Print a one-line actionable error and exit with status 1."""
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def warn(msg: str) -> None:
    print(f"WARNING: {msg}", file=sys.stderr)


def rel_to_kit(path: Path) -> str:
    """Kit-root-relative path (forward slashes) when possible, else absolute."""
    try:
        return path.resolve().relative_to(KIT_ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path, hint: str) -> dict:
    if not path.exists():
        fail(f"{rel_to_kit(path)} missing: {hint}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{rel_to_kit(path)} is not valid JSON (line {exc.lineno}): fix the syntax and retry")
    return {}  # unreachable; keeps type checkers happy


def parse_now(value: str | None) -> str:
    """Return the timestamp to stamp into metadata.computed_at (UTC, second precision)."""
    if value is None:
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        fail(f"--now must be an ISO-8601 timestamp like 2026-05-08T16:20:08Z, got: {value}")
    return value


def label_for(score: float) -> str:
    """Map an unrounded score to its maturity label (0.5 / 1.5 / 2.5 / 3.5 cuts)."""
    if score < 0.5:
        return LABEL_L0
    if score < 1.5:
        return LABEL_L1
    if score < 2.5:
        return LABEL_L2
    if score < 3.5:
        return LABEL_L3
    return LABEL_L4


def threshold_status(answered: int) -> str:
    """Coverage threshold (referencia/pontuacao-e-calculo.md section 5).

    The kit still computes scores when BLOCKED; the status flags reliability.
    """
    if answered >= 40:
        return "OK"
    if answered >= 25:
        return "WARNING"
    return "BLOCKED"


def r3(value: float | None) -> float | None:
    """Round for output only (3 decimals). Computation stays full precision."""
    return None if value is None else round(value, 3)


def validate_level(qid: str, level) -> None:
    """Levels may be null or any numeric value in [0, 4] (floats like 2.5 are
    legal: multi-respondent imports average levels). Booleans are rejected."""
    if level is None:
        return
    if isinstance(level, bool) or not isinstance(level, (int, float)):
        fail(f"respostas: question {qid} has non-numeric level {level!r}: use null or a number in [0, 4]")
    if not (0 <= level <= 4):
        fail(f"respostas: question {qid} has level {level} outside [0, 4]: fix the answer and retry")


def validate_framework(framework: dict) -> None:
    if not isinstance(framework.get("pillars"), list) or not framework["pillars"]:
        fail("framework.json has no 'pillars' list: the file is corrupted or is not the kit framework")
    for pillar in framework["pillars"]:
        for cap in pillar.get("capabilities", []):
            if not cap.get("questions"):
                fail(f"framework.json capability {cap.get('id')} has no questions: framework is corrupted")


def check_framework_version(respostas: dict, framework: dict) -> None:
    """Preflight: warn (never block) when the answers were filled against a
    different framework version (weights/questions may have changed)."""
    rf = respostas.get("metadata", {}).get("framework_version")
    ff = framework.get("version")
    if rf and ff and rf != ff:
        warn(
            f"respostas.json was filled against framework {rf}, but framework.json is version {ff}. "
            "Weights and questions may have changed. Recommended: revalidate answers before publishing."
        )


def sumproduct(pairs: list[tuple[float, float]]) -> float | None:
    """Weighted average over (value, weight) pairs; None when there is no weight."""
    wt = sum(w for _, w in pairs)
    if wt <= 0:
        return None
    return sum(v * w for v, w in pairs) / wt


def compute(framework: dict, responses: dict) -> dict:
    """Run the full 3-layer scoring. Returns UNROUNDED scores.

    Result shape:
      capabilities: list (framework order) of dicts with id, name_pt_br, pillar_id,
                    weight, score (float|None), pe_score, answered, applicable, strategies
      pillars:      list of dicts with id, name_pt_br, score, answered, applicable
      overall / pe_overall: float | None
      answered / applicable: totals
    """
    capabilities = []
    known_qids = set()

    for pillar in framework["pillars"]:
        for cap in pillar["capabilities"]:
            pairs: list[tuple[float, float]] = []
            pe_pairs: list[tuple[float, float]] = []
            answered = 0
            for question in cap["questions"]:
                known_qids.add(question["id"])
                entry = responses.get(question["id"])
                if entry is not None and not isinstance(entry, dict):
                    fail(f"respostas: question {question['id']} must be an object like "
                         f"{{\"level\": 2, \"evidence\": \"...\"}}, got {entry!r}")
                level = entry.get("level") if entry else None
                validate_level(question["id"], level)
                if level is None:
                    continue
                weight = question.get("weight", 1.0)
                answered += 1
                pairs.append((float(level), weight))
                if question.get("pe"):
                    pe_pairs.append((float(level), weight))
            capabilities.append({
                "id": cap["id"],
                "name_pt_br": cap.get("name_pt_br", cap.get("name", cap["id"])),
                "pillar_id": pillar["id"],
                "weight": cap.get("weight", 1.0),
                "score": sumproduct(pairs),
                "pe_score": sumproduct(pe_pairs),
                "answered": answered,
                "applicable": len(cap["questions"]),
                "strategies": cap.get("strategies", []),
            })

    unknown = sorted(set(responses) - known_qids)
    if unknown:
        warn(f"respostas contains {len(unknown)} question id(s) not in framework.json "
             f"(ignored): {', '.join(unknown[:5])}{'...' if len(unknown) > 5 else ''}")

    pillars = []
    for pillar in framework["pillars"]:
        caps = [c for c in capabilities if c["pillar_id"] == pillar["id"]]
        scored = [(c["score"], c["weight"]) for c in caps if c["score"] is not None]
        # Pillar with zero scored capabilities is defined as 0.0 (edge case).
        pillars.append({
            "id": pillar["id"],
            "name_pt_br": pillar.get("name_pt_br", pillar.get("name", pillar["id"])),
            "score": sumproduct(scored) if scored else 0.0,
            "answered": sum(c["answered"] for c in caps),
            "applicable": sum(c["applicable"] for c in caps),
        })

    # Overall: direct SUMPRODUCT over ALL capabilities, NOT the mean of pillars.
    scored_all = [(c["score"], c["weight"]) for c in capabilities if c["score"] is not None]
    overall = sumproduct(scored_all) if scored_all else 0.0

    # PE score: same SUMPRODUCT restricted to questions flagged pe=true.
    pe_scored = [(c["pe_score"], c["weight"]) for c in capabilities if c["pe_score"] is not None]
    pe_overall = sumproduct(pe_scored)

    return {
        "capabilities": capabilities,
        "pillars": pillars,
        "overall": overall,
        "pe_overall": pe_overall,
        "answered": sum(c["answered"] for c in capabilities),
        "applicable": sum(c["applicable"] for c in capabilities),
    }


def build_scores_document(result: dict, respostas: dict, framework: dict, computed_at: str) -> dict:
    """Assemble saida/scores.json (rounded to 3 decimals for output only)."""
    pe = result["pe_overall"]
    return {
        "metadata": {
            "computed_at": computed_at,
            "respondent": respostas.get("metadata", {}).get("respondent_name"),
            "framework_version": framework.get("version"),
        },
        "overall": {
            "score": r3(result["overall"]),
            "label": label_for(result["overall"]),
            "pe_score": r3(pe),
            "pe_label": label_for(pe) if pe is not None else None,
        },
        "threshold": {
            "status": threshold_status(result["answered"]),
            "answered": result["answered"],
            "applicable": result["applicable"],
        },
        "pillars": [
            {
                "id": p["id"],
                "name_pt_br": p["name_pt_br"],
                "score": r3(p["score"]),
                "label": label_for(p["score"]),
                "answered": p["answered"],
                "applicable": p["applicable"],
            }
            for p in result["pillars"]
        ],
        "capabilities": [
            {
                "id": c["id"],
                "name_pt_br": c["name_pt_br"],
                "pillar_id": c["pillar_id"],
                "weight": c["weight"],
                "score": r3(c["score"]),
                "label": label_for(c["score"]) if c["score"] is not None else LABEL_NO_ANSWER,
                "answered": c["answered"],
                "applicable": c["applicable"],
                "strategies": c["strategies"],
            }
            for c in result["capabilities"]
        ],
    }


def write_json(path: Path, document: dict) -> None:
    # No trailing newline: byte-compatible with referencia/exemplo-saida/*.json.
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute capability/pillar/overall maturity scores (official SUMPRODUCT algorithm)."
    )
    parser.add_argument("--respostas", default=str(KIT_ROOT / "respostas.json"),
                        help="Path to respostas.json (default: kit root respostas.json)")
    parser.add_argument("--framework", default=str(KIT_ROOT / "framework.json"),
                        help="Path to framework.json (default: kit root framework.json)")
    parser.add_argument("--out", default=str(KIT_ROOT / "saida" / "scores.json"),
                        help="Output path (default: saida/scores.json)")
    parser.add_argument("--now", default=None, metavar="ISO8601",
                        help="Override metadata.computed_at for deterministic output "
                             "(e.g. 2026-05-08T16:20:08Z; default: current UTC time)")
    args = parser.parse_args()

    computed_at = parse_now(args.now)
    respostas = load_json(Path(args.respostas),
                          "copy respostas.json.example to respostas.json and fill it in first")
    framework = load_json(Path(args.framework), "the kit framework file was not found")
    validate_framework(framework)

    responses = respostas.get("responses")
    if not isinstance(responses, dict) or not responses:
        fail(f"{rel_to_kit(Path(args.respostas))} has no 'responses' object: fill it in "
             "(see respostas.json.example) or run /importar-respostas-excel")

    check_framework_version(respostas, framework)

    result = compute(framework, responses)
    document = build_scores_document(result, respostas, framework, computed_at)
    out_path = Path(args.out)
    write_json(out_path, document)

    ov = document["overall"]
    th = document["threshold"]
    print(f"Scores computed -> {rel_to_kit(out_path)}")
    print(f"  Overall: {ov['score']} ({ov['label']})")
    if ov["pe_score"] is not None:
        print(f"  PE: {ov['pe_score']} ({ov['pe_label']})")
    print(f"  Threshold: {th['status']} ({th['answered']}/{th['applicable']} answered)")
    print("  Pillars: " + " | ".join(f"{p['id']}={p['score']} {p['label']}" for p in document["pillars"]))
    if th["status"] == "BLOCKED":
        warn("fewer than 25 questions answered: scores were computed, but the executive "
             "report should not be used for decisions (insufficient coverage)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
