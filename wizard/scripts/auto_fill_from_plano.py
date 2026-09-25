#!/usr/bin/env python3
"""Wizard Mode D: auto-fill implementation-guide-inputs.json from the plan.

Reads: saida/plano-capacitacao-<DATE>.md (output of /plano-capacitacao),
       in English or Portuguese
Extracts: Champions, training, calendar, ADKAR knowledge, quick wins
Writes: implementation-guide-inputs.json (kit root), 6 of 9 fields filled

Usage:
    python3 auto_fill_from_plano.py
    python3 auto_fill_from_plano.py --plano X --out Y --lang pt-br
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
import branding  # noqa: E402

SUPPORTED_LANGS = ("en", "pt-br")

# Heading patterns accept both the English and the Portuguese plan.
# An optional emoji may precede the heading text.
EMOJI = r"(?:\S+ )?"
H_SUMMARY = r"1 · (?:Sumário Executivo|Executive Summary)"
H_COHORTS = r"3 · (?:Cohorts sugeridos|Suggested cohorts)"
H_CHAMPIONS = r"4 · Champions Network"
H_CALENDAR = r"5 · (?:Calendário sugerido|Suggested calendar)"
H_FORMAT = r"6 · (?:Formato e cadência|Preferred format)"
H_BARRIERS = r"7 · (?:Barreiras|Barriers)"
H_SCHEDULE = rf"11 · {EMOJI}(?:Cronograma|30-day schedule)"
H_ACTIVE = r"### 🥇 (?:Ativos|Active)"
H_FORMATS_SUB = r"### (?:Formatos|Formats)"
# "1. **topic** — N devs" (PT) or "1. **topic**: N devs" (EN)
TOPIC_LINE = r"^\d+\.\s+\*\*(.+?)\*\*(?: —|:) (\d+) devs"

STRINGS = {
    "en": {
        "committee_intro": "Executive Steering Committee (active "
                           "Champions identified by the Learning "
                           "Survey):",
        "person": "- {name}: {email}",
        "comm_intro": "Communication Plan derived from the suggested "
                      "calendar:\n\n",
        "comm_missing": "(see Part 5 of the training plan)",
        "training_intro": "Training Plan (cohorts per dimension derived "
                          "from the Learning Survey):\n\n",
        "training_missing": "(see Part 3 of the training plan)",
        "adkar_head": (
            "ADKAR Change Plan derived from the Learning Survey:\n\n"
            "**Awareness:** Share the consolidated training plan in an "
            "all-hands; each dev receives a personalized plan by "
            "email.\n\n"
            "**Desire:** Make it visible that workshops have "
            "pre-validated attendees (not a generic opt-in).\n\n"
            "**Knowledge:** Top 5 workshops (from the Learning "
            "Survey):\n"
        ),
        "adkar_item": "{i}. {topic} ({count} attendees)\n",
        "adkar_tail": (
            "\n**Ability:** Biweekly office hours (no fixed agenda; devs "
            "bring practical questions).\n\n"
            "**Reinforcement:** Monthly adoption metrics published; "
            "recognition for Champions; quarterly plan review with a "
            "new Learning Survey.\n"
        ),
        "no_committee": "(fill in manually: no active Champions "
                        "identified by the Learning Survey)",
        "no_tpo": "(fill in manually: the Learning Survey does not "
                  "cover the TPO. List the Program Manager, office, and "
                  "decision authority)",
        "no_raci": "(fill in manually: the Learning Survey does not "
                   "cover RACI. Use the template in "
                   "wizard/implementation-guide-inputs.template.json)",
        "no_qw_1_4": "(fill in: not enough data for weeks 1-4 of the "
                     "calendar)",
        "no_qw_5_8": "(fill in: not enough data for weeks 5-8)",
        "no_qw_9_12": "(fill in: not enough data for weeks 9-12)",
        "c_missing": "❌ Training plan not found in saida/.",
        "c_run": "   Run /plano-capacitacao first (after "
                 "/importar-survey-learning).",
        "c_reading": "📖 Reading: {path}",
        "c_done": "\n✅ Mode D auto-fill → {path}",
        "c_filled": "\n📊 Automatically filled:",
        "c_fields": [
            "   ✓ executive_steering_committee  (active Champions)",
            "   ✓ communication_plan            (Calendar)",
            "   ✓ training_plan                 (Cohorts per dimension)",
            "   ✓ adkar_notes                   (Knowledge = Top 5 "
            "workshops)",
            "   ✓ quick_wins_w1_4 / w5_8 / w9_12 (Schedule)",
        ],
        "c_manual": "\n⚠ You must fill in MANUALLY (not covered by the "
                    "Learning Survey):",
        "c_manual_fields": [
            "   • tpo (Technology Product Owner)",
            "   • raci_matrix",
        ],
        "c_next": "\n💡 Next: /gerar-relatorio  → 5 PDFs with a "
                  "personalized Part 4",
    },
    "pt-br": {
        "committee_intro": "Comitê Executivo Diretivo (Champions ativos "
                           "identificados pelo Learning Survey):",
        "person": "- {name} — {email}",
        "comm_intro": "Plano de Comunicação derivado do calendário "
                      "sugerido:\n\n",
        "comm_missing": "(ver Parte 5 do plano de capacitação)",
        "training_intro": "Plano de Treinamento (cohorts por dimensão "
                          "derivados do Learning Survey):\n\n",
        "training_missing": "(ver Parte 3 do plano de capacitação)",
        "adkar_head": (
            "Plano de Mudança ADKAR derivado do Learning Survey:\n\n"
            "**Awareness:** Comunicar plano de capacitação consolidado "
            "em all-hands; cada dev recebe seu plano personalizado por "
            "email.\n\n"
            "**Desire:** Tornar visível que workshops têm inscritos "
            "pré-validados (não opt-in genérico).\n\n"
            "**Knowledge:** Workshops top 5 (do Learning Survey):\n"
        ),
        "adkar_item": "{i}. {topic} ({count} inscritos)\n",
        "adkar_tail": (
            "\n**Ability:** Office hours quinzenal (sem agenda fixa, "
            "devs trazem dúvidas práticas).\n\n"
            "**Reinforcement:** Métricas de adoção mensais publicadas; "
            "reconhecimento dos Champions; revisão trimestral do plano "
            "com novo Learning Survey.\n"
        ),
        "no_committee": "(preencher manualmente — sem Champions ativos "
                        "identificados pelo Learning Survey)",
        "no_tpo": "(preencher manualmente — Learning Survey não cobre "
                  "TPO. Liste Programa Manager + escritório + autoridade "
                  "de decisão)",
        "no_raci": "(preencher manualmente — Learning Survey não cobre "
                   "RACI. Use template em "
                   "wizard/implementation-guide-inputs.template.json)",
        "no_qw_1_4": "(preencher — sem dados suficientes nas semanas 1-4 "
                     "do calendário)",
        "no_qw_5_8": "(preencher — sem dados suficientes nas semanas "
                     "5-8)",
        "no_qw_9_12": "(preencher — sem dados suficientes nas semanas "
                      "9-12)",
        "c_missing": "❌ Plano de capacitação não encontrado em saida/.",
        "c_run": "   Rode /plano-capacitacao primeiro (após "
                 "/importar-survey-learning).",
        "c_reading": "📖 Lendo: {path}",
        "c_done": "\n✅ Mode D auto-fill → {path}",
        "c_filled": "\n📊 Preenchimento automático:",
        "c_fields": [
            "   ✓ executive_steering_committee  (Champions ativos)",
            "   ✓ communication_plan            (Calendário)",
            "   ✓ training_plan                 (Cohorts por dimensão)",
            "   ✓ adkar_notes                   (Knowledge = Top 5 "
            "workshops)",
            "   ✓ quick_wins_w1_4 / w5_8 / w9_12 (Cronograma)",
        ],
        "c_manual": "\n⚠ Você precisa preencher MANUALMENTE (Learning "
                    "Survey não cobre):",
        "c_manual_fields": [
            "   • tpo (Technology Product Owner)",
            "   • raci_matrix",
        ],
        "c_next": "\n💡 Próximo: /gerar-relatorio  → 5 PDFs com Parte 4 "
                  "personalizada",
    },
}


def find_latest_plano(out_dir: Path) -> Path | None:
    """Find the most recent plano-capacitacao-*.md in saida/."""
    candidates = sorted(out_dir.glob("plano-capacitacao-*.md"),
                        reverse=True)
    return candidates[0] if candidates else None


def extract_section(plano_md: str, section_header_pattern: str) -> str:
    """Extract a section body by header regex (until next ## or end)."""
    pat = re.compile(
        rf"## {section_header_pattern}.*?\n(.*?)(?=\n## |\Z)",
        re.DOTALL,
    )
    m = pat.search(plano_md)
    return m.group(1).strip() if m else ""


def extract_active_people(plano_md: str) -> list[tuple[str, str]]:
    """(name, email) rows from the Active Champions table (section 4)."""
    section = extract_section(plano_md, H_CHAMPIONS)
    active_block = re.search(
        rf"{H_ACTIVE}.*?\n(.*?)(?=\n### |\Z)", section, re.DOTALL
    )
    if not active_block:
        return []
    rows = re.findall(
        r"^\|\s*([^|]+?)\s*\|\s*([^|@]+@[^|\s]+)\s*\|",
        active_block.group(1),
        re.MULTILINE,
    )
    return [
        (name.strip(), email.strip()) for name, email in rows
        if name.strip().lower() not in ("nome", "name", "---")
    ]


def extract_champions_active(plano_md: str, t: dict) -> str:
    people = extract_active_people(plano_md)
    if not people:
        return ""
    lines = [t["committee_intro"], ""]
    for name, email in people:
        lines.append(t["person"].format(name=name, email=email))
    return "\n".join(lines)


def extract_calendar(plano_md: str) -> str:
    """Extract the calendar table from section 5 (next 90 days)."""
    section = extract_section(plano_md, H_CALENDAR)
    if not section:
        return ""
    table_match = re.search(r"\|.*?\|.*?(?=\n\n|\Z)", section, re.DOTALL)
    return table_match.group(0).strip() if table_match else section[:500]


def extract_top_topics(plano_md: str, n=5) -> list[tuple[str, int]]:
    """Top topics from the executive summary numbered list."""
    section = extract_section(plano_md, H_SUMMARY)
    matches = re.findall(TOPIC_LINE, section, re.MULTILINE)
    return [(m[0], int(m[1])) for m in matches[:n]]


def extract_format_prefs(plano_md: str) -> str:
    """Extract the format preferences table from section 6."""
    section = extract_section(plano_md, H_FORMAT)
    table_match = re.search(
        rf"{H_FORMATS_SUB}.*?\n(\|.*?\n(?:\|.*?\n)+)", section, re.DOTALL
    )
    return table_match.group(1).strip() if table_match else ""


def extract_barriers(plano_md: str) -> str:
    """Extract the top barriers table from section 7."""
    section = extract_section(plano_md, H_BARRIERS)
    table_match = re.search(r"\|.*?\n(?:\|[-: ]+\|\n)?(\|.*?\n)+", section)
    return table_match.group(0).strip() if table_match else ""


def extract_quick_wins_calendar(plano_md: str,
                                weeks_range: tuple[int, int]) -> str:
    """Quick wins for a week range from sections 5 and 11."""
    section_5 = extract_section(plano_md, H_CALENDAR)
    section_11 = extract_section(plano_md, H_SCHEDULE)

    items = []
    for src in [section_5, section_11]:
        for line in src.split("\n"):
            m = re.search(r"W(\d+)[,\-\s]+W?(\d+)?\s*\|([^|]+)\|", line)
            if m:
                start_week = int(m.group(1))
                if weeks_range[0] <= start_week <= weeks_range[1]:
                    activity = m.group(3).strip()
                    if activity and activity != "Workshop":
                        items.append(f"- W{start_week}: {activity}")
    return "\n".join(items) if items else ""


def build_payload(plano_md: str, plano_name: str, lang: str) -> dict:
    t = STRINGS[lang]
    champions = extract_champions_active(plano_md, t)
    calendar = extract_calendar(plano_md)
    top_topics = extract_top_topics(plano_md)
    quick_w1_4 = extract_quick_wins_calendar(plano_md, (1, 4))
    quick_w5_8 = extract_quick_wins_calendar(plano_md, (5, 8))
    quick_w9_12 = extract_quick_wins_calendar(plano_md, (9, 12))

    comm_plan = t["comm_intro"] + (calendar or t["comm_missing"])

    cohorts_section = extract_section(plano_md, H_COHORTS)
    training = t["training_intro"] + (
        cohorts_section[:1500] if cohorts_section
        else t["training_missing"]
    )

    # ADKAR: the Knowledge stage lists the top topics
    adkar = t["adkar_head"]
    for i, (topic, count) in enumerate(top_topics[:5], 1):
        adkar += t["adkar_item"].format(i=i, topic=topic, count=count)
    adkar += t["adkar_tail"]

    return {
        "metadata": {
            "generated_at": datetime.datetime.now(
                datetime.UTC).isoformat(),
            "generator": "wizard/scripts/auto_fill_from_plano.py (Mode D)",
            "source_plano": plano_name,
            "completion_pct": 67,  # 6 of 9 fields filled
            "manual_required": ["tpo", "raci_matrix"],
            "lang": lang,
            **branding.json_metadata(),
        },
        "implementation_guide_inputs": {
            "executive_steering_committee": champions or t["no_committee"],
            "tpo": t["no_tpo"],
            "raci_matrix": t["no_raci"],
            "communication_plan": comm_plan,
            "training_plan": training,
            "adkar_notes": adkar,
            "quick_wins_w1_4": quick_w1_4 or t["no_qw_1_4"],
            "quick_wins_w5_8": quick_w5_8 or t["no_qw_5_8"],
            "quick_wins_w9_12": quick_w9_12 or t["no_qw_9_12"],
        },
    }


def _display(path: Path) -> Path:
    return path.relative_to(KIT) if path.is_relative_to(KIT) else path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--plano", default=None,
        help="Path to plano-capacitacao-DATE.md (default: latest in "
             "saida/)",
    )
    ap.add_argument("--out",
                    default=str(KIT / "implementation-guide-inputs.json"))
    ap.add_argument("--lang", choices=SUPPORTED_LANGS, default="en",
                    help="Language of the generated text (default: en). "
                         "The plan can be in either language.")
    args = ap.parse_args()
    t = STRINGS[args.lang]

    out_path = Path(args.out)
    if args.plano:
        plano_path = Path(args.plano)
    else:
        plano_path = find_latest_plano(KIT / "saida")

    if not plano_path or not plano_path.exists():
        print(t["c_missing"])
        print(t["c_run"])
        return 1

    plano_md = plano_path.read_text(encoding="utf-8")
    print(t["c_reading"].format(path=_display(plano_path)))

    payload = build_payload(plano_md, plano_path.name, args.lang)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                        encoding="utf-8")

    print(t["c_done"].format(path=_display(out_path)))
    print(t["c_filled"])
    for line in t["c_fields"]:
        print(line)
    print(t["c_manual"])
    for line in t["c_manual_fields"]:
        print(line)
    print(t["c_next"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
