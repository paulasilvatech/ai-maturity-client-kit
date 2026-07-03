#!/usr/bin/env python3
"""Check trilingual (PT-BR / EN / ES) coverage of user-facing documentation.

The inventory is auto-derived instead of hand-maintained: every *.md under
the kit root counts as a user-facing PT-BR doc, excluding
contributor/maintainer areas (.github/, docs/, kit-en/, kit-es/, tooling and
output dirs) and an explicit EXEMPT list of English-only engineering docs.

Each non-exempt PT-BR doc must have an EN and an ES counterpart, provided
either as a sibling variant (<name>.en.md / <name>.es.md) or as an explicit
kit-en/ / kit-es/ mapping.

The script also verifies i18n key parity across the three report string
catalogs in relatorios/i18n/ (pt-br.json, en.json, es.json).

Exit code is 1 when anything is missing (default, CI-friendly); use
--warn-only to always exit 0 while still printing the full report.

Usage:
    python3 scripts/check_language_coverage.py
    python3 scripts/check_language_coverage.py --warn-only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Directories whose *.md files are never client-facing documentation.
EXCLUDED_DIR_PARTS = {
    ".git",
    ".github",
    ".mypy_cache",
    "__pycache__",
    "build",
    "docs",
    "kit-en",
    "kit-es",
    "node_modules",
    "saida",
}

# English-only engineering/maintainer docs, exempt from translation by the
# repo language policy (code, tooling docs, and governance stay in English).
EXEMPT_DOCS = {
    "AUDITORIA-KIT-COPILOT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "MODELS.md",
    "docs/README.md",
    "referencia/branding/README.md",
    "relatorios/i18n/README.md",
    "relatorios/scripts/README.md",
    "relatorios/templates/README.md",
    "scripts/README.md",
    "survey-devs/scripts/README.md",
    "survey-learning/scripts/README.md",
    "wizard/scripts/README.md",
}

# PT-BR docs whose translations live in kit-en/ / kit-es/ under other names.
KIT_DOC_MAP = {
    "README.md": {"en": "kit-en/README.md", "es": "kit-es/README.md"},
    "GUIA-PASSO-A-PASSO.md": {
        "en": "kit-en/STEP-BY-STEP.md",
        "es": "kit-es/PASO-A-PASO.md",
    },
    "coleta/INSTRUCOES-FORMS.md": {
        "en": "kit-en/FORMS-INSTRUCTIONS.md",
        "es": "kit-es/INSTRUCCIONES-FORMS.md",
    },
}

LANGUAGE_SUFFIXES = (".en.md", ".es.md")

I18N_CATALOGS = {
    "pt-br": "relatorios/i18n/pt-br.json",
    "en": "relatorios/i18n/en.json",
    "es": "relatorios/i18n/es.json",
}


def discover_pt_docs() -> list[str]:
    """All PT-BR user-facing markdown docs, kit-root-relative, sorted."""
    docs: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIR_PARTS for part in parts[:-1]):
            continue
        # Output/staging dirs created by the packager and validators.
        if parts[0].startswith(("dist", ".")):
            continue
        if rel.endswith(LANGUAGE_SUFFIXES):
            continue  # this IS a translation, not a base doc
        if any(part in ("en", "es") for part in parts[:-1]):
            continue  # language-dir translation tree (e.g. exemplo-saida/en/)
        docs.append(rel)
    return docs


def translation_for(rel: str, lang: str) -> str | None:
    """Return the existing EN/ES counterpart path for a PT doc, or None."""
    sibling = f"{rel[: -len('.md')]}.{lang}.md"
    if (ROOT / sibling).exists():
        return sibling
    path = Path(rel)
    lang_dir = (path.parent / lang / path.name).as_posix()
    if (ROOT / lang_dir).exists():
        return lang_dir
    mapped = KIT_DOC_MAP.get(rel, {}).get(lang)
    if mapped and (ROOT / mapped).exists():
        return mapped
    return None


def check_docs() -> int:
    docs = discover_pt_docs()
    exempt = [d for d in docs if d in EXEMPT_DOCS]
    required = [d for d in docs if d not in EXEMPT_DOCS]

    print(f"\nUser-facing docs (auto-derived): {len(required)} PT-BR docs "
          f"require EN+ES; {len(exempt)} English-only engineering docs exempt")

    missing_count = 0
    report: list[tuple[str, list[str]]] = []
    for rel in required:
        missing_langs = [lang for lang in ("en", "es") if translation_for(rel, lang) is None]
        if missing_langs:
            missing_count += 1
            report.append((rel, missing_langs))

    if report:
        print(f"\nMissing translations ({missing_count} docs):")
        for rel, langs in report:
            base = rel[: -len(".md")]
            hint = " / ".join(f"{base}.{lang}.md" for lang in langs)
            print(f"  MISS {rel:<55} needs: {', '.join(l.upper() for l in langs)}  (add {hint})")
    else:
        print("\n  OK: every user-facing PT-BR doc has EN and ES counterparts")
    return missing_count


def flatten_keys(obj: object, prefix: str = "") -> set[str]:
    if not isinstance(obj, dict):
        return {prefix}
    keys: set[str] = set()
    for key, value in obj.items():
        dotted = f"{prefix}.{key}" if prefix else str(key)
        keys |= flatten_keys(value, dotted)
    return keys


def check_i18n_parity() -> int:
    print("\ni18n catalogs (relatorios/i18n):")
    catalogs: dict[str, set[str]] = {}
    for lang, rel in I18N_CATALOGS.items():
        path = ROOT / rel
        if not path.exists():
            print(f"  MISS {rel} (catalog file not found)")
            return 1
        try:
            catalogs[lang] = flatten_keys(json.loads(path.read_text(encoding="utf-8")))
        except json.JSONDecodeError as exc:
            print(f"  FAIL {rel} is not valid JSON: {exc}")
            return 1

    union = set().union(*catalogs.values())
    mismatches = 0
    for lang, keys in catalogs.items():
        missing = sorted(union - keys)
        if missing:
            mismatches += len(missing)
            print(f"  MISS {I18N_CATALOGS[lang]}: {len(missing)} key(s) absent:")
            for key in missing:
                print(f"       - {key}")
    if not mismatches:
        sizes = ", ".join(f"{lang}={len(keys)}" for lang, keys in catalogs.items())
        print(f"  OK: key parity across the 3 catalogs ({sizes})")
    return mismatches


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check PT/EN/ES documentation coverage and i18n key parity."
    )
    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="Always exit 0; print the full report as warnings only.",
    )
    args = parser.parse_args()

    print("AI Maturity kit language coverage")

    docs_missing = check_docs()
    i18n_mismatches = check_i18n_parity()

    print("\nSummary")
    print(f"  Docs missing EN/ES translations: {docs_missing}")
    print(f"  i18n catalog key mismatches:     {i18n_mismatches}")

    failed = bool(docs_missing or i18n_mismatches)
    if failed and args.warn_only:
        print("  Result: WARN (issues found; --warn-only forces exit 0)")
        return 0
    print(f"  Result: {'FAIL' if failed else 'OK'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
