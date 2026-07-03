#!/usr/bin/env python3
"""Render the 5 client-ready reports for AI Maturity Assessment.

Renders Jinja2 templates → HTML → (optionally) WeasyPrint → PDF.

Inputs:
  - templates/  (5 .html.j2 files + _print.css)
  - i18n/       (en.json, es.json, pt-br.json)
  - <payload>   (default: sample_payload.json — adapt to your data)

Outputs (in --out dir, default <kit>/saida/):
  - score_justification.pdf
  - roadmap_part_pillar_p1.pdf
  - roadmap_part_pillar_p2.pdf
  - roadmap_part_pillar_p3.pdf
  - roadmap_part4.pdf
  (plus the intermediate .html for each; with --html-only, HTML only)

Usage:
  python3 render_reports.py                            # uses sample_payload.json
  python3 render_reports.py --payload other.json       # custom payload
  python3 render_reports.py --out /path/to/output      # custom output
  python3 render_reports.py --locale pt-br             # override i18n strings
  python3 render_reports.py --html-only                # no weasyprint required
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError:
    sys.exit("✗ dependência ausente: jinja2. Instale com: python3 -m pip install jinja2 "
             "(ou: make install-deps)")

ROOT = Path(__file__).resolve().parent.parent  # kit-cliente/relatorios/
TEMPLATES = ROOT / "templates"
I18N = ROOT / "i18n"
LOCALES = ("en", "es", "pt-br")

# Top-level payload fields the 5 templates dereference. Missing any of them
# would crash mid-render with an opaque Jinja2 error, so we check upfront.
REQUIRED_PAYLOAD_KEYS = (
    "locale",
    "organization",
    "assessment",
    "scores",
    "capabilities",
    "horizons",
    "three_horizons",
    "technology_resources_per_pillar",
    "success_metrics_per_pillar",
    "risks_per_pillar",
    "next_steps_per_pillar",
    "key_evidence_sources",
    "implementation_guide_inputs",
    "branding",
)


def import_weasyprint():
    try:
        from weasyprint import CSS, HTML
        return HTML, CSS
    except ImportError:
        sys.exit("✗ dependência ausente: weasyprint (necessária para PDF). Instale com: "
                 "python3 -m pip install weasyprint (ou: make install-deps), "
                 "ou use --html-only para gerar apenas os HTMLs.")


def load_locale(locale: str) -> dict[str, str]:
    path = I18N / f"{locale}.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"✗ {path}: catálogo i18n não encontrado — locales suportados: "
                 f"{', '.join(LOCALES)}.")
    except json.JSONDecodeError as exc:
        sys.exit(f"✗ {path}: JSON inválido (linha {exc.lineno}): {exc.msg}")


def make_t(strings: dict[str, str], missing_keys: set[str]):
    """t() with {placeholder} substitution. Missing catalog keys are recorded
    in ``missing_keys`` so the run can fail nonzero instead of shipping a PDF
    with visible ⟨key⟩ markers."""
    pat = re.compile(r"\{(\w+)\}")

    def t(key: str, **kw) -> str:
        s = strings.get(key)
        if not isinstance(s, str):
            missing_keys.add(key)
            s = f"⟨{key}⟩"
        return pat.sub(lambda m: str(kw.get(m.group(1), m.group(0))), s) if kw else s

    return t


def build_env(strings: dict[str, str], missing_keys: set[str]) -> Environment:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    t = make_t(strings, missing_keys)
    env.globals["t"] = t
    env.filters["t"] = t
    return env


def render(env: Environment, template_name: str, payload: dict, extra_ctx: dict | None,
           out_dir: Path, label: str, html_only: bool) -> Path:
    template = env.get_template(template_name)
    ctx = {**payload, **(extra_ctx or {})}
    html_str = template.render(**ctx)

    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / f"{label}.html"
    html_path.write_text(html_str, encoding="utf-8")
    if html_only:
        return html_path

    HTML, CSS = import_weasyprint()
    css_path = TEMPLATES / "_print.css"
    pdf_bytes = HTML(string=html_str, base_url=str(TEMPLATES)).write_pdf(
        stylesheets=[CSS(filename=str(css_path))]
    )
    pdf_path = out_dir / f"{label}.pdf"
    pdf_path.write_bytes(pdf_bytes)
    return pdf_path


def load_payload(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"✗ {path}: payload não encontrado — gere-o com "
                 f"relatorios/scripts/build_payload_and_render.py (ou use o "
                 f"sample_payload.json padrão).")
    except json.JSONDecodeError as exc:
        sys.exit(f"✗ {path}: JSON inválido (linha {exc.lineno}): {exc.msg}")
    if not isinstance(payload, dict):
        sys.exit(f"✗ {path}: o payload deve ser um objeto JSON.")
    missing = [key for key in REQUIRED_PAYLOAD_KEYS if key not in payload]
    if missing:
        sys.exit(f"✗ {path}: campo(s) de nível superior ausente(s): {', '.join(missing)} "
                 f"— gere o payload com relatorios/scripts/build_payload_and_render.py.")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Renderiza os 5 relatórios (HTML/PDF) a partir de um payload JSON."
    )
    ap.add_argument("--payload", default=str(ROOT / "sample_payload.json"))
    # Default deliberately points at <kit>/saida/ — never at referencia/
    # (the shipped reference examples must not be overwritten by a no-args run).
    ap.add_argument("--out", default=str(ROOT.parent / "saida"))
    ap.add_argument("--locale", choices=LOCALES, default=None,
                    help="override payload.locale (i18n strings only; labels baked "
                         "into the payload keep the locale it was built with)")
    ap.add_argument("--html-only", action="store_true",
                    help="render HTML only, skip PDF conversion (no weasyprint needed)")
    args = ap.parse_args()

    if not args.html_only:
        import_weasyprint()  # fail fast with an actionable message

    payload_path = Path(args.payload)
    payload = load_payload(payload_path)
    if args.locale:
        payload["locale"] = args.locale
    locale = payload.get("locale", "en")
    if locale not in LOCALES:
        sys.exit(f"✗ {payload_path}: locale '{locale}' não suportado — use um de: "
                 f"{', '.join(LOCALES)}.")

    out_dir = Path(args.out)

    print(f"Payload:  {payload_path}  ({payload_path.stat().st_size:,} bytes)")
    print(f"Locale:   {locale}")
    print(f"Org:      {payload.get('organization', {}).get('name', '?')}")
    print(f"Out dir:  {out_dir}")
    print(f"Modo:     {'HTML apenas (--html-only)' if args.html_only else 'HTML + PDF'}")
    print()

    strings = load_locale(locale)
    missing_keys: set[str] = set()
    env = build_env(strings, missing_keys)

    targets = [
        ("score_justification.html.j2", {}, "score_justification"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P1"}, "roadmap_part_pillar_p1"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P2"}, "roadmap_part_pillar_p2"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P3"}, "roadmap_part_pillar_p3"),
        ("roadmap_part4.html.j2", {}, "roadmap_part4"),
    ]

    ok = True
    for tmpl, extra, label in targets:
        try:
            out_path = render(env, tmpl, payload, extra, out_dir, label, args.html_only)
            print(f"  ✓ {out_path.name}: {out_path.stat().st_size:,} bytes")
        except Exception as e:
            print(f"  ✗ {label}: {type(e).__name__}: {e}")
            ok = False

    print()
    if missing_keys:
        print(f"✗ Chave(s) i18n ausente(s) no catálogo {locale}.json "
              f"({len(missing_keys)}):", file=sys.stderr)
        for key in sorted(missing_keys):
            print(f"    - {key}", file=sys.stderr)
        print("  Adicione as chaves às 3 línguas (en/es/pt-br) e re-renderize.",
              file=sys.stderr)
        return 1
    if ok:
        what = "HTMLs" if args.html_only else "PDFs"
        print(f"✓ Todos os 5 {what} gerados em {out_dir}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
