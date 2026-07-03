#!/usr/bin/env python3
"""End-to-end smoke test for the AI Maturity Assessment kit.

What it exercises:
  1. The deterministic scoring pipeline (scripts/compute_scores.py ->
     scripts/compute_gaps.py -> scripts/recommend_strategies.py) against the
     bundled example answers, asserting the outputs EQUAL the ground truth in
     referencia/exemplo-saida/ (overall score/label, threshold, P0-P3 counts).
  2. The report build (relatorios/scripts/build_payload_and_render.py) with
     the example inputs, asserting payload shape and (when jinja2 is
     available) that wizard data from implementation-guide-inputs shows up in
     the rendered Part 4 HTML. PDF rendering is never attempted, so
     WeasyPrint is not required.
  3. Optionally (--with-cross-survey) the cross-survey enrichment path.

All generated artifacts live under saida/.smoke/. The few user files the
pipeline reads from fixed locations (respostas.json,
implementation-guide-inputs.json, saida/scores.json|gaps.json|
recomendacoes.json) are backed up before the run and restored afterwards.
Nothing else in saida/ is touched.

Pure stdlib — no pytest/openpyxl required; jinja2 is optional.

Usage:
    python3 scripts/smoke_test.py
    python3 scripts/smoke_test.py --with-cross-survey   # also exercises survey artifacts
    make smoke / make smoke-cross                        # convenience wrappers
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
SAIDA = KIT / "saida"
SMOKE_DIR = SAIDA / ".smoke"
EXEMPLOS = KIT / "referencia" / "exemplo-saida"

# Matches referencia/exemplo-saida/*.json metadata for byte-comparable output.
GROUND_TRUTH_NOW = "2026-05-08T16:20:08Z"
REPORT_DATE = "2026-05-08"

# String that can ONLY appear in the Part 4 HTML when the wizard inputs from
# implementation-guide-inputs-EXEMPLO.json were merged into the payload.
WIZARD_MARKER = "Champions Kickoff"

SUBPROCESS_TIMEOUT = 180  # seconds per script invocation

# Files we will mutate; every one of them is backed up and restored on exit.
SENTINEL_FILES = [
    KIT / "respostas.json",
    KIT / "implementation-guide-inputs.json",
    SAIDA / "scores.json",
    SAIDA / "gaps.json",
    SAIDA / "recomendacoes.json",
]


class SmokeError(RuntimeError):
    pass


def _color(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if sys.stdout.isatty() else text


def _ok(msg: str) -> None:
    print(_color("32", f"  ✓ {msg}"))


def _info(msg: str) -> None:
    print(_color("36", f"  • {msg}"))


def _notice(msg: str) -> None:
    print(_color("33", f"  ! NOTICE: {msg}"))


def _fail(msg: str) -> None:
    print(_color("31", f"  ✗ {msg}"), file=sys.stderr)


def _backup(path: Path) -> Path | None:
    if not path.exists():
        return None
    backup = path.with_suffix(path.suffix + ".smoketest-backup")
    shutil.copy2(path, backup)
    return backup


def _restore(path: Path, backup: Path | None) -> None:
    if backup is None:
        path.unlink(missing_ok=True)
        return
    shutil.move(str(backup), str(path))


def run_script(cmd: list[str], what: str) -> subprocess.CompletedProcess[str]:
    """Run a kit script with a timeout; raise SmokeError on failure."""
    try:
        result = subprocess.run(
            [sys.executable, *cmd],
            cwd=str(KIT),
            capture_output=True,
            text=True,
            timeout=SUBPROCESS_TIMEOUT,
        )
    except subprocess.TimeoutExpired as exc:
        raise SmokeError(
            f"{what} timed out after {SUBPROCESS_TIMEOUT}s: {' '.join(cmd)}"
        ) from exc
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SmokeError(f"{what} exited with code {result.returncode}")
    return result


def load_json(path: Path, what: str) -> dict:
    if not path.exists():
        raise SmokeError(f"{what} was not generated: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SmokeError(f"{what} is not valid JSON ({path}): {exc}") from exc


# ─── Staging / cleanup ────────────────────────────────────────────


def stage_example_inputs(with_cross: bool) -> dict[str, object]:
    """Stage example respostas + wizard inputs (+ optional survey artifacts)."""
    state: dict[str, object] = {}

    for f in SENTINEL_FILES:
        state[f"backup:{f}"] = _backup(f)

    shutil.copy2(KIT / "respostas.json.example", KIT / "respostas.json")
    _ok("Copied respostas.json.example → respostas.json")

    shutil.copy2(
        EXEMPLOS / "implementation-guide-inputs-EXEMPLO.json",
        KIT / "implementation-guide-inputs.json",
    )
    _ok("Staged implementation-guide-inputs-EXEMPLO.json → implementation-guide-inputs.json")

    SMOKE_DIR.mkdir(parents=True, exist_ok=True)

    staged: list[Path] = []
    if with_cross:
        for src_name, dest_name in [
            ("maturidade-developer-survey-EXEMPLO.json", "maturidade-developer-survey-smoketest.json"),
            ("insights-developer-survey-EXEMPLO.md", "insights-developer-survey-smoketest.md"),
            ("plano-capacitacao-EXEMPLO.md", "plano-capacitacao-smoketest.md"),
        ]:
            src = EXEMPLOS / src_name
            if not src.exists():
                continue
            dest = SAIDA / dest_name
            shutil.copy2(src, dest)
            staged.append(dest)
        if staged:
            _ok(f"Staged {len(staged)} cross-survey artifact(s) in saida/")
    state["staged"] = staged
    return state


def cleanup(state: dict[str, object]) -> None:
    print()
    _info("Cleaning up...")
    for f in SENTINEL_FILES:
        _restore(f, state.get(f"backup:{f}"))  # type: ignore[arg-type]
    for staged in state.get("staged") or []:  # type: ignore[union-attr]
        Path(staged).unlink(missing_ok=True)
    shutil.rmtree(SMOKE_DIR, ignore_errors=True)
    _ok("Workspace restored (only saida/.smoke/ and staged files were touched)")


# ─── Step 1: deterministic scoring pipeline ───────────────────────


def run_compute_pipeline() -> None:
    _info("Running compute_scores → compute_gaps → recommend_strategies")
    smoke = SMOKE_DIR
    run_script(
        ["scripts/compute_scores.py", "--respostas", "respostas.json",
         "--out", str(smoke / "scores.json"), "--now", GROUND_TRUTH_NOW],
        "compute_scores.py",
    )
    run_script(
        ["scripts/compute_gaps.py", "--scores", str(smoke / "scores.json"),
         "--respostas", "respostas.json",
         "--out", str(smoke / "gaps.json"), "--now", GROUND_TRUTH_NOW],
        "compute_gaps.py",
    )
    run_script(
        ["scripts/recommend_strategies.py", "--gaps", str(smoke / "gaps.json"),
         "--out", str(smoke / "recomendacoes.json"), "--now", GROUND_TRUTH_NOW],
        "recommend_strategies.py",
    )


def assert_compute_outputs() -> None:
    scores = load_json(SMOKE_DIR / "scores.json", "scores.json")
    gaps = load_json(SMOKE_DIR / "gaps.json", "gaps.json")
    recomendacoes = load_json(SMOKE_DIR / "recomendacoes.json", "recomendacoes.json")

    gt_scores = load_json(EXEMPLOS / "scores.json", "ground-truth scores.json")
    gt_gaps = load_json(EXEMPLOS / "gaps.json", "ground-truth gaps.json")

    if scores.get("overall") != gt_scores.get("overall"):
        raise SmokeError(
            "computed overall does not match ground truth:\n"
            f"    computed: {scores.get('overall')}\n"
            f"    expected: {gt_scores.get('overall')}"
        )
    overall = scores["overall"]
    _ok(f"overall matches ground truth (score={overall['score']}, label={overall['label']})")

    if scores.get("threshold") != gt_scores.get("threshold"):
        raise SmokeError(
            "computed threshold does not match ground truth:\n"
            f"    computed: {scores.get('threshold')}\n"
            f"    expected: {gt_scores.get('threshold')}"
        )
    _ok(f"threshold matches ground truth ({scores['threshold']})")

    if gaps.get("summary") != gt_gaps.get("summary"):
        raise SmokeError(
            "computed P0-P3 counts do not match ground truth:\n"
            f"    computed: {gaps.get('summary')}\n"
            f"    expected: {gt_gaps.get('summary')}"
        )
    _ok(f"gap P0-P3 counts match ground truth ({gaps['summary']})")

    if not recomendacoes.get("ranked_strategies"):
        raise SmokeError("recomendacoes.json has no 'ranked_strategies' entries")
    _ok(
        "recomendacoes.json generated "
        f"({len(recomendacoes['ranked_strategies'])} ranked strategies)"
    )


# ─── Step 2: payload build + HTML render ──────────────────────────


def run_build(html: bool) -> None:
    """Stage computed outputs where the report builder reads them, then build."""
    for name in ("scores.json", "gaps.json", "recomendacoes.json"):
        shutil.copy2(SMOKE_DIR / name, SAIDA / name)

    mode = "--html-only" if html else "--no-render"
    _info(f"Running build_payload_and_render.py {mode}")
    result = run_script(
        ["relatorios/scripts/build_payload_and_render.py", mode,
         "--out", str(SMOKE_DIR), "--date", REPORT_DATE],
        "build_payload_and_render.py",
    )
    for line in result.stdout.splitlines():
        if line.strip().startswith(("✓", "⚠️")):
            print("   ", line)


def assert_payload(with_cross: bool) -> None:
    payload_path = SMOKE_DIR / "payload.json"
    payload = load_json(payload_path, "payload.json")
    size = payload_path.stat().st_size
    if size < 20_000:
        raise SmokeError(f"payload.json suspiciously small ({size} bytes)")
    _ok(f"payload.json present ({size:,} bytes)")

    required = ["organization", "assessment", "scores", "capabilities", "gap_analysis"]
    missing = [k for k in required if k not in payload]
    if missing:
        raise SmokeError(f"payload missing required keys: {missing}")
    _ok(f"all required keys present: {', '.join(required)}")

    overall = payload["scores"]["overall"].get("weighted_avg")
    if not isinstance(overall, (int, float)):
        raise SmokeError(f"scores.overall.weighted_avg is not numeric: {overall!r}")
    gt_overall = load_json(EXEMPLOS / "scores.json", "ground-truth scores.json")["overall"]["score"]
    if abs(overall - gt_overall) > 0.005:
        raise SmokeError(
            f"payload weighted_avg {overall} diverges from ground-truth overall {gt_overall}"
        )
    _ok(f"scores.overall.weighted_avg = {overall} (ground truth: {gt_overall})")

    pillars = payload["scores"].get("pillars") or []
    pillar_ids = {p.get("id") for p in pillars}
    if not {"P1", "P2", "P3"} <= pillar_ids:
        raise SmokeError(f"missing pillar ids; got {pillar_ids}")
    _ok(f"pillars P1/P2/P3 present (n={len(pillars)})")

    if with_cross:
        cross = payload.get("cross_survey_data")
        if not cross or not cross.get("available"):
            raise SmokeError("cross_survey_data was expected but not attached")
        dsm = cross.get("developer_survey_maturity", {})
        dims = dsm.get("dimensions") or []
        if len(dims) < 5:
            raise SmokeError(f"expected ≥5 dimensions from rubric, got {len(dims)}")
        _ok(
            f"cross_survey_data attached "
            f"(respondents={dsm.get('respondents')}, dimensions={len(dims)})"
        )


def assert_part4_html() -> None:
    html_path = SMOKE_DIR / "roadmap_part4.html"
    if not html_path.exists():
        raise SmokeError("roadmap_part4.html was not generated")
    html = html_path.read_text(encoding="utf-8")
    if WIZARD_MARKER not in html:
        raise SmokeError(
            f"wizard marker {WIZARD_MARKER!r} (from implementation-guide-inputs-"
            f"EXEMPLO.json) not found in roadmap_part4.html — wizard merge broken"
        )
    _ok(f"Part 4 HTML contains wizard data ({WIZARD_MARKER!r})")


# ─── Entry point ──────────────────────────────────────────────────


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--with-cross-survey",
        action="store_true",
        help="Also stage developer/learning survey artifacts and assert cross_survey_data",
    )
    args = ap.parse_args()

    print(_color("1", "AI Maturity kit — smoke test"))
    print(_color("90", f"  kit: {KIT}"))
    print()

    has_jinja2 = importlib.util.find_spec("jinja2") is not None

    state: dict[str, object] = {}
    try:
        state = stage_example_inputs(args.with_cross_survey)
        run_compute_pipeline()
        assert_compute_outputs()
        run_build(html=has_jinja2)
        assert_payload(args.with_cross_survey)
        if has_jinja2:
            assert_part4_html()
        else:
            _notice("jinja2 not installed — skipping HTML render check "
                    "(install with: make install-deps)")
        print()
        print(_color("32", "✓ SMOKE TEST PASSED"))
        return 0
    except SmokeError as exc:
        print()
        _fail(str(exc))
        print(_color("31", "✗ SMOKE TEST FAILED"))
        return 1
    finally:
        cleanup(state)


if __name__ == "__main__":
    sys.exit(main())
