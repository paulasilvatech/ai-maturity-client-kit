#!/usr/bin/env python3
"""Report multilingual coverage for the AI Maturity client kit.

This is intentionally advisory. Packaging must keep working even while full
human-reviewed EN/ES question banks are being prepared, but contributors need a
single command that makes remaining localization gaps visible.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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


def print_group(title: str, paths: list[str], *, advisory: bool = False) -> int:
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


def main() -> int:
    print("AI Maturity kit language coverage")
    required_missing = 0
    required_missing += print_group("Required package docs", REQUIRED_LANGUAGE_PACKAGE_DOCS)
    required_missing += print_group("Canonical question banks included in all packages", REQUIRED_SHARED_CANONICAL_BANKS)
    required_missing += print_group("Localized survey question banks", REQUIRED_LOCALIZED_QUESTION_BANKS)
    required_missing += print_group("Reference PDF examples", REQUIRED_REFERENCE_OUTPUTS)

    advisory_missing = print_group(
        "Human-reviewed localized question banks (advisory)",
        EXPECTED_LOCALIZED_QUESTION_BANKS,
        advisory=True,
    )

    print("\nSummary")
    print(f"  Required missing: {required_missing}")
    print(f"  Advisory localized banks missing: {advisory_missing}")
    if advisory_missing:
        print("  Note: EN/ES packages remain executable because canonical PT-BR question banks are included.")
        print("        For full native-language Forms creation, add the advisory localized banks above.")
    return 1 if required_missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
