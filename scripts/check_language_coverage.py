#!/usr/bin/env python3
"""Report multilingual coverage for the AI Maturity client kit.

Most groups are required: a missing file fails the check. The localized
assessment question banks stay advisory, because packaging must keep working
while human-reviewed EN/ES banks are prepared. The translated-docs group
checks that every `X.pt-br.md` / `X.pt-br.html` has its English base file and
vice versa for the docs that have a Portuguese copy.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_BR_TAG = ".pt-br"
TRANSLATED_DOC_PATTERNS = ["*.pt-br.md", "*.pt-br.html"]
EXCLUDED_PARTS = {".git", "dist", "saida"}

EXPECTED_LOCALIZED_QUESTION_BANKS = [
    "coleta/perguntas-para-forms.en.md",
    "coleta/perguntas-para-forms.es.md",
]

REQUIRED_LOCALIZED_QUESTION_BANKS = [
    "survey-learning/perguntas-para-forms-learning.en.md",
    "survey-learning/perguntas-para-forms-learning.es.md",
    "survey-devs/perguntas-para-forms-devs.en.md",
    "survey-devs/perguntas-para-forms-devs.es.md",
]

REQUIRED_SHARED_CANONICAL_BANKS = [
    "coleta/perguntas-para-forms.md",
    "survey-devs/perguntas-para-forms-devs.md",
    "survey-learning/perguntas-para-forms-learning.md",
]

REQUIRED_LANGUAGE_PACKAGE_DOCS = [
    "kit-en/README.md",
    "kit-en/STEP-BY-STEP.md",
    "kit-en/FORMS-INSTRUCTIONS.md",
    "kit-es/README.md",
    "kit-es/PASO-A-PASO.md",
    "kit-es/INSTRUCCIONES-FORMS.md",
]

REQUIRED_REFERENCE_OUTPUTS = [
    "referencia/exemplo-saida/en/score_justification.pdf",
    "referencia/exemplo-saida/es/score_justification.pdf",
    "referencia/exemplo-saida/score_justification.pdf",
]


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def print_group(
    title: str,
    paths: list[str],
    *,
    advisory: bool = False,
) -> int:
    print(f"\n{title}")
    missing = 0
    for rel in paths:
        ok = exists(rel)
        if ok:
            marker = "OK"
        elif advisory:
            marker = "WARN"
        else:
            marker = "MISS"
        print(f"  {marker} {rel}")
        if not ok:
            missing += 1
    return missing


def translated_doc_pairs() -> list[tuple[str, str]]:
    """Return (base, pt_br_copy) pairs for every Portuguese doc copy."""
    pairs: set[tuple[str, str]] = set()
    for pattern in TRANSLATED_DOC_PATTERNS:
        for copy in ROOT.rglob(pattern):
            rel_path = copy.relative_to(ROOT)
            if set(rel_path.parts) & EXCLUDED_PARTS:
                continue
            base_name = copy.name.replace(f"{PT_BR_TAG}.", ".", 1)
            base = rel_path.with_name(base_name)
            pairs.add((base.as_posix(), rel_path.as_posix()))
    return sorted(pairs)


def print_translated_docs() -> int:
    pairs = translated_doc_pairs()
    title = f"Translated docs: EN base + PT-BR copy ({len(pairs)} pairs)"
    print(f"\n{title}")
    missing = 0
    for base, copy in pairs:
        # The glob found the copy, so only the base can be missing.
        if exists(base):
            print(f"  OK {base} <-> {copy}")
        else:
            print(f"  MISS {base} (EN base missing for {copy})")
            missing += 1
    return missing


def main() -> int:
    print("AI Maturity kit language coverage")
    required_missing = 0
    required_missing += print_group(
        "Required package docs",
        REQUIRED_LANGUAGE_PACKAGE_DOCS,
    )
    required_missing += print_group(
        "Canonical question banks included in all packages",
        REQUIRED_SHARED_CANONICAL_BANKS,
    )
    required_missing += print_group(
        "Localized survey question banks",
        REQUIRED_LOCALIZED_QUESTION_BANKS,
    )
    required_missing += print_group(
        "Reference PDF examples",
        REQUIRED_REFERENCE_OUTPUTS,
    )
    required_missing += print_translated_docs()

    advisory_missing = print_group(
        "Human-reviewed localized question banks (advisory)",
        EXPECTED_LOCALIZED_QUESTION_BANKS,
        advisory=True,
    )

    print("\nSummary")
    print(f"  Required missing: {required_missing}")
    print(f"  Advisory localized banks missing: {advisory_missing}")
    if advisory_missing:
        print(
            "  Note: EN/ES packages remain executable because the canonical"
            " PT-BR question banks are included."
        )
        print(
            "        For full native-language Forms creation, add the"
            " advisory localized banks above."
        )
    return 1 if required_missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
