#!/usr/bin/env python3
"""Smoke test harness for the Final Report templates.

Renders all 5 report templates from relatorios/sample_payload.json into a
temporary directory (HTML-only by default, so no weasyprint is required) and
validates the NFR-REPORT-011 content-stripping policy against the rendered
HTML. Fails nonzero on any render error, missing i18n key, or forbidden token.

Usage:
  python3 render_smoke.py                 # HTML-only smoke into a temp dir
  python3 render_smoke.py --out /tmp/x    # keep outputs in a chosen dir
  python3 render_smoke.py --locale es     # smoke a specific locale
  python3 render_smoke.py --pdf           # also produce PDFs (needs weasyprint)
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render_reports  # noqa: E402  (shares env/t()/render with the real pipeline)

ROOT = Path(__file__).resolve().parent.parent  # kit-cliente/relatorios/
SAMPLE_PAYLOAD = ROOT / "sample_payload.json"

# ─── Content lint per NFR-REPORT-011 ─────────────────────────────
FORBIDDEN_TOKENS = [
    r"\$\d",                               # $1, $1M, $150K — any digit after $
    r"\bUSD\b",
    r"R\$",
    r"€\d",
    r"Microsoft Confidential",
    r"Microsoft Latam GBB",
    r"paulasilva@microsoft\.com",
]


def lint_content(html_path: Path) -> list[str]:
    """Content scan against forbidden tokens per NFR-REPORT-011.

    Scans the rendered HTML (the source of truth for visible content).
    Scanning compressed PDF byte streams produces false positives because
    PDF object/xref tables contain arbitrary byte sequences.
    """
    text_corpus = html_path.read_text(encoding="utf-8", errors="replace")
    violations = []
    for pattern in FORBIDDEN_TOKENS:
        for m in re.finditer(pattern, text_corpus):
            ctx = text_corpus[max(0, m.start() - 30):m.start() + 50]
            violations.append(f"  ✗ {pattern!r} matched: ...{ctx!r}...")
    return violations


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Smoke-render dos 5 templates a partir do sample_payload.json."
    )
    ap.add_argument("--out", default=None,
                    help="Output dir (default: novo diretório temporário)")
    ap.add_argument("--locale", choices=render_reports.LOCALES, default=None,
                    help="override payload.locale (default: locale do sample)")
    ap.add_argument("--pdf", action="store_true",
                    help="also render PDFs (requires weasyprint; default is HTML-only)")
    args = ap.parse_args()

    out_dir = Path(args.out) if args.out else Path(
        tempfile.mkdtemp(prefix="render-smoke-")
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    html_only = not args.pdf

    payload = render_reports.load_payload(SAMPLE_PAYLOAD)
    if args.locale:
        payload["locale"] = args.locale
    locale = payload.get("locale", "en")

    print(f"Payload: {SAMPLE_PAYLOAD}  ({SAMPLE_PAYLOAD.stat().st_size:,} bytes)")
    print(f"  organization: {payload['organization']['name']}")
    print(f"  capabilities: {len(payload['capabilities'])}")
    print(f"  pillars     : {len(payload['scores']['pillars'])}")
    print(f"  horizons    : {len(payload['horizons'])}")
    print(f"  locale      : {locale}")
    print(f"  out dir     : {out_dir}")
    print(f"  mode        : {'HTML-only' if html_only else 'HTML + PDF'}")
    print()

    strings = render_reports.load_locale(locale)
    missing_keys: set[str] = set()
    env = render_reports.build_env(strings, missing_keys)

    targets = [
        ("score_justification.html.j2", {}, "score_justification"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P1"}, "roadmap_part_pillar_p1"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P2"}, "roadmap_part_pillar_p2"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P3"}, "roadmap_part_pillar_p3"),
        ("roadmap_part4.html.j2", {}, "roadmap_part4"),
    ]

    overall_ok = True
    for tmpl, extra, label in targets:
        print(f"━━━ Rendering {tmpl} {extra} ━━━")
        try:
            out_path = render_reports.render(env, tmpl, payload, extra, out_dir,
                                             label, html_only)
        except Exception as e:
            print(f"  ✗ FAILED: {type(e).__name__}: {e}")
            overall_ok = False
            continue
        print(f"  ✓ {out_path.name}: {out_path.stat().st_size:,} bytes")

        violations = lint_content(out_dir / f"{label}.html")
        if violations:
            print(f"  ✗ Content lint failed for {label}:")
            for v in violations:
                print(v)
            overall_ok = False
        else:
            print("  ✓ Content lint passed (no forbidden tokens)")
        print()

    if missing_keys:
        overall_ok = False
        print(f"✗ Missing i18n key(s) in {locale}.json:")
        for key in sorted(missing_keys):
            print(f"    - {key}")

    print("─" * 60)
    if overall_ok:
        print(f"✓ ALL TEMPLATES RENDERED + LINT PASSED ({out_dir})")
        return 0
    print("✗ FAILURES")
    return 1


if __name__ == "__main__":
    sys.exit(main())
