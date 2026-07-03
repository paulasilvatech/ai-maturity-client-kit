#!/usr/bin/env python3
"""Gera plano de capacitação personalizado a partir do Learning Survey.

Lê: survey-learning/respostas-learning.json (output de /import-learning-survey)
Gera:
  - saida/plano-capacitacao-<DATE>.md (12 seções, com nomes/emails dos inscritos)
  - saida/plano-capacitacao-<DATE>.json (dados estruturados: tópicos, cohorts,
    champions, mentores, calendário, barreiras — consumido pelo wizard Mode D)
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(KIT / "relatorios" / "scripts"))
try:
    import branding
except ImportError:  # partial kit copy without relatorios/: degrade to neutral output
    import types

    branding = types.SimpleNamespace(
        md_header=lambda: "", md_footer=lambda: "",
        json_metadata=lambda: {}, META_BAR="", CONTACT="")

PII_NOTICE = "> ⚠️ Esta seção contém nomes e emails. NÃO compartilhar publicamente. Uso restrito à liderança para convites."

DIMENSION_NAMES = {
    "D2": "Copilot Adoption",
    "D3": "MS/GH Tooling Breadth",
    "D4": "AI Dev Practices",
    "D5": "Agent Concepts Mastery",
    "D6": "Instructions Maturity",
    "D7": "Best Practices",
    "D8": "Security & Governance",
}

LEVELS = ["L0", "L1", "L2", "L3", "L4"]
DIMENSION_IDS = list(DIMENSION_NAMES)
TOPIC_QIDS = ["L4-Q1", "L4-Q2", "L4-Q3", "L4-Q4", "L4-Q5"]

SEP_2 = "| --- | --- |"
SEP_3 = "| --- | --- | --- |"
SEP_4 = "| --- | --- | --- | --- |"
SEP_5 = "| --- | --- | --- | --- | --- |"
SEP_7 = "| --- | --- | --- | --- | --- | --- | --- |"


@dataclass
class LearningAggregates:
    self_perception: dict[str, Counter]
    priorities: Counter
    topic_counts: Counter
    topic_attendees: dict[str, list[dict[str, str]]]
    formats: Counter
    time_per_week: Counter
    cohort_pref: Counter
    actives: list[dict[str, str]]
    supported: list[dict[str, str]]
    maybe: list[dict[str, str]]
    mentors: list[dict[str, str]]
    mentees: list[dict[str, str]]
    references: Counter
    barriers: Counter
    pain_quotes: list[tuple[str, str]]
    workshop_wishes: list[tuple[str, str]]
    speaker_wishes: list[tuple[str, str]]


def safe_pct(num, total):
    return round(100 * num / total, 1) if total > 0 else 0


def fold_text(value):
    """Lowercase and remove accents so PT-BR, EN, and ES options match."""
    text = str(value or "").strip().lower()
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def contains_any(value, patterns):
    folded = fold_text(value)
    return any(fold_text(pattern) in folded for pattern in patterns)


def starts_any(value, prefixes):
    folded = fold_text(value)
    return any(folded.startswith(fold_text(prefix)) for prefix in prefixes)


def response_value(respondent, qid):
    return str(respondent.get("responses", {}).get(qid, {}).get("value", "")).strip()


def selected_options(responses, qid):
    raw = responses.get(qid, {}).get("value", "")
    return [option.strip() for option in str(raw).split(";") if option.strip()]


def is_topic_skip_option(topic):
    return contains_any(topic, [
        "Já domino",
        "Não tenho interesse",
        "Não conheço",
        "I already master",
        "I am not interested",
        "I do not know",
        "Ya domino",
        "No tengo interés",
        "No conozco",
    ])


def champion_tier(answer):
    if starts_any(answer, ["Talvez", "Maybe", "Tal vez"]):
        return "maybe"
    if contains_any(answer, [
        "quero ser Champion ativo",
        "active Champion",
        "Champion activo",
    ]):
        return "active"
    if contains_any(answer, [
        "se tiver suporte",
        "support/training",
        "soporte/entrenamiento",
    ]):
        return "supported"
    return None


def is_affirmative(answer):
    return starts_any(answer, ["Sim", "Yes", "Sí"])


def is_no_barrier_option(option):
    return contains_any(option, [
        "sem barreiras",
        "no significant barriers",
        "sin barreras significativas",
    ])


def champion_short_label(value):
    tier = champion_tier(value)
    if tier == "active":
        return "Sim ativo"
    if tier == "supported":
        return "Sim com suporte"
    if tier == "maybe":
        return "Talvez"
    return "Não"


def median_level(counts):
    sorted_levels = []
    for level in LEVELS:
        sorted_levels.extend([level] * counts.get(level, 0))
    if not sorted_levels:
        return "—"
    return sorted_levels[len(sorted_levels) // 2]


def collect_l2_self_perception(respondents):
    """L2-Q1 -> D2, L2-Q2 -> D3, ..., L2-Q7 -> D8."""
    dist = {}
    for index, dimension_id in enumerate(DIMENSION_IDS, start=1):
        counts = Counter()
        for respondent in respondents:
            answer = response_value(respondent, f"L2-Q{index}")
            for level in LEVELS:
                if answer.startswith(level):
                    counts[level] += 1
                    break
        dist[dimension_id] = counts
    return dist


def collect_priorities(respondents):
    counts = Counter()
    for respondent in respondents:
        for option in selected_options(respondent.get("responses", {}), "L3-Q1"):
            for dimension_id in DIMENSION_IDS:
                if option.startswith(dimension_id):
                    counts[dimension_id] += 1
                    break
    return counts


def iter_learning_topics(respondent):
    responses = respondent.get("responses", {})
    for qid in TOPIC_QIDS:
        for topic in selected_options(responses, qid):
            if not is_topic_skip_option(topic):
                yield topic


def collect_topics(respondents):
    topic_counts = Counter()
    topic_attendees = defaultdict(list)
    for respondent in respondents:
        attendee = {
            "name": respondent.get("name", "?"),
            "email": respondent.get("email", "?"),
        }
        for topic in iter_learning_topics(respondent):
            topic_counts[topic] += 1
            topic_attendees[topic].append(attendee)
    return topic_counts, topic_attendees


def collect_format_prefs(respondents):
    formats = Counter()
    time_per_week = Counter()
    cohort_pref = Counter()
    for respondent in respondents:
        responses = respondent.get("responses", {})
        formats.update(selected_options(responses, "L5-Q1"))
        time = response_value(respondent, "L5-Q2")
        cohort = response_value(respondent, "L5-Q4")
        if time:
            time_per_week[time] += 1
        if cohort:
            cohort_pref[cohort] += 1
    return formats, time_per_week, cohort_pref


def collect_champions(respondents):
    actives, supported, maybe = [], [], []
    for respondent in respondents:
        person = {"name": respondent.get("name", "?"), "email": respondent.get("email", "?")}
        tier = champion_tier(response_value(respondent, "L6-Q1"))
        if tier == "active":
            actives.append(person)
        elif tier == "supported":
            supported.append(person)
        elif tier == "maybe":
            maybe.append(person)
    return actives, supported, maybe


def collect_mentors_mentees(respondents):
    mentees, mentors = [], []
    references = Counter()
    for respondent in respondents:
        person = {"name": respondent.get("name", "?"), "email": respondent.get("email", "?")}
        if is_affirmative(response_value(respondent, "L6-Q3")):
            mentees.append(person)
        if is_affirmative(response_value(respondent, "L6-Q4")):
            topic = response_value(respondent, "L6-Q5")
            mentors.append({**person, "topic": topic[:80] if topic else "(não especificou)"})
        reference = response_value(respondent, "L6-Q2")
        if reference and len(reference) > 2 and "[" not in reference:
            references[reference] += 1
    return mentors, mentees, references


def collect_barriers(respondents):
    counts = Counter()
    for respondent in respondents:
        for option in selected_options(respondent.get("responses", {}), "L7-Q1"):
            if not is_no_barrier_option(option):
                counts[option] += 1
    return counts


def collect_quotes(respondents, qid, max_q=5):
    quotes = []
    for respondent in respondents:
        value = response_value(respondent, qid)
        if value and len(value) > 15 and "[" not in value[:5]:
            quotes.append((value, respondent.get("name", "?")))
    return quotes[:max_q]


def collect_aggregates(respondents):
    topic_counts, topic_attendees = collect_topics(respondents)
    formats, time_per_week, cohort_pref = collect_format_prefs(respondents)
    actives, supported, maybe = collect_champions(respondents)
    mentors, mentees, references = collect_mentors_mentees(respondents)
    return LearningAggregates(
        self_perception=collect_l2_self_perception(respondents),
        priorities=collect_priorities(respondents),
        topic_counts=topic_counts,
        topic_attendees=topic_attendees,
        formats=formats,
        time_per_week=time_per_week,
        cohort_pref=cohort_pref,
        actives=actives,
        supported=supported,
        maybe=maybe,
        mentors=mentors,
        mentees=mentees,
        references=references,
        barriers=collect_barriers(respondents),
        pain_quotes=collect_quotes(respondents, "L7-Q4"),
        workshop_wishes=collect_quotes(respondents, "L7-Q2"),
        speaker_wishes=collect_quotes(respondents, "L7-Q3"),
    )


def append_intro(md, respondent_count, date):
    md.extend([
        branding.md_header().rstrip(),
        "",
        "# Plano de Capacitação IA — Roadmap Personalizado",
        "",
        f"**Data:** {date}  ·  **Respondentes:** {respondent_count} (identificados)  ·  Survey: Learning & Growth (32 perguntas)",
        f"**Autor:** {branding.META_BAR}  ·  **Contato:** {branding.CONTACT}",
        "",
    ])


def append_self_perception(md, aggregates):
    md.extend([
        "### Maturidade IA percebida pelo time (auto-avaliação L2)",
        "",
        "| Dimensão | L0 | L1 | L2 | L3 | L4 | Mediana |",
        SEP_7,
    ])
    for dimension_id, name in DIMENSION_NAMES.items():
        counts = aggregates.self_perception[dimension_id]
        values = [counts.get(level, 0) for level in LEVELS]
        md.append(f"| **{dimension_id}** {name} | {values[0]} | {values[1]} | {values[2]} | {values[3]} | {values[4]} | {median_level(counts)} |")
    md.append("")


def append_champions_summary(md, aggregates):
    md.extend(["", "### 👥 Champions Network identificados", ""])
    md.append(f"- **{len(aggregates.actives)} ativos** (querem ser Champion sem precisar suporte)")
    md.append(f"- **{len(aggregates.supported)} com suporte** (querem ser Champion se tiver treino)")
    md.append(f"- **{len(aggregates.maybe)} maybe** (precisam pensar)")
    if aggregates.references:
        md.append("- **Top 3 referências naturais** (mencionados por colegas em L6-Q2):")
        for name, count in aggregates.references.most_common(3):
            md.append(f"  - {name} (mencionado por {count} pessoas)")
    md.append("")


def append_quick_wins_summary(md, aggregates, respondent_count):
    md.extend(["### ⚡ 3 quick wins recomendados (próximos 30 dias)", ""])
    if aggregates.topic_counts:
        top_topic, top_count = aggregates.topic_counts.most_common(1)[0]
        md.append(f"1. **Workshop: {top_topic}** — {top_count} inscritos pré-validados")
    if aggregates.actives:
        md.append(f"2. **Champions Kickoff** — ativar os {len(aggregates.actives)} Champions ativos identificados")
    if aggregates.barriers:
        barrier, count = aggregates.barriers.most_common(1)[0]
        md.append(f"3. **Remover barreira #1: '{barrier}'** — citada por {count}/{respondent_count} devs")
    md.append("")


def append_executive_summary(md, aggregates, respondent_count):
    md.extend(["---", "", "## 1 · Sumário Executivo", ""])
    append_self_perception(md, aggregates)
    md.extend(["### 🎯 Top 3 dimensões PRIORITÁRIAS para crescer (L3-Q1)", ""])
    for dimension_id, count in aggregates.priorities.most_common(3):
        name = DIMENSION_NAMES[dimension_id]
        md.append(f"- **{dimension_id}** {name} — {count}/{respondent_count} devs ({safe_pct(count, respondent_count):.0f}%)")
    md.extend(["", "### 📚 Top 10 tópicos mais demandados (L4)", ""])
    for index, (topic, count) in enumerate(aggregates.topic_counts.most_common(10), 1):
        md.append(f"{index}. **{topic}** — {count} devs ({safe_pct(count, respondent_count):.0f}%)")
    append_champions_summary(md, aggregates)
    append_quick_wins_summary(md, aggregates, respondent_count)


def append_topics_section(md, aggregates, respondent_count):
    md.extend(["---", "", "## 2 · Top 10 tópicos demandados (com inscritos pré-validados)", "", PII_NOTICE, ""])
    for index, (topic, count) in enumerate(aggregates.topic_counts.most_common(10), 1):
        md.extend([
            f"### {index}. {topic} — {count} inscritos",
            "",
            f"**Demanda:** {count}/{respondent_count} devs ({safe_pct(count, respondent_count):.0f}%)",
            "",
            "**Inscritos pré-validados** (já confirmados na resposta):",
        ])
        for attendee in aggregates.topic_attendees[topic]:
            md.append(f"- {attendee['name']} ({attendee['email']})")
        md.append("")


def append_cohorts_section(md, aggregates):
    md.extend(["---", "", "## 3 · Cohorts sugeridos por dimensão da rubrica", ""])
    for dimension_id, name in DIMENSION_NAMES.items():
        priority_count = aggregates.priorities.get(dimension_id, 0)
        if priority_count == 0:
            continue
        cohort_winning = aggregates.cohort_pref.most_common(1)[0][0] if aggregates.cohort_pref else "Híbrido"
        md.extend([
            f"### Cohort {dimension_id} ({name})",
            f"- **{priority_count} devs querem evoluir nesta dimensão**",
            f"- **Formato preferido pelo time:** {cohort_winning}",
            "- **Plano:** cohort de 4-6 semanas com sessões síncronas + lab self-paced",
            "",
        ])


def append_people_table(md, rows, header, empty_message=None):
    if rows:
        md.extend([header, SEP_3])
        md.extend(rows)
    elif empty_message:
        md.append(empty_message)
    md.append("")


def append_champions_section(md, aggregates):
    md.extend(["---", "", "## 4 · Champions Network (3 tiers)", "", PII_NOTICE, ""])
    md.append("### 🥇 Ativos (já querem ser Champion)")
    active_rows = [f"| {person['name']} | {person['email']} | Convidar para train-the-trainer |" for person in aggregates.actives]
    append_people_table(md, active_rows, "| Nome | Email | Próximo passo |", "_Nenhum dev se candidatou diretamente. Considere ativar tier 'com suporte'._")

    md.append("### 🥈 Com suporte (querem se tiver treino dedicado)")
    supported_rows = [f"| {person['name']} | {person['email']} | Workshop de capacitação Champion + materiais |" for person in aggregates.supported]
    append_people_table(md, supported_rows, "| Nome | Email | Suporte necessário |", "_(nenhum)_")

    md.append("### 🤝 Mentor candidates (se ofereceram em L6-Q4)")
    mentor_rows = [f"| {person['name']} | {person['email']} | {person['topic']} |" for person in aggregates.mentors]
    append_people_table(md, mentor_rows, "| Nome | Email | Tópico que ensina |")

    md.append("### 🎓 Mentees (querem mentoria 1:1)")
    if aggregates.mentees:
        md.extend(["| Nome | Email |", SEP_2])
        for person in aggregates.mentees:
            md.append(f"| {person['name']} | {person['email']} |")
    md.append("")


def build_calendar_entries(aggregates):
    """90-day calendar as structured data (single source for the .md table
    and the .json output — multi-week rows keep every week explicit)."""
    champion_count = len(aggregates.actives) + len(aggregates.supported)
    champion_name = aggregates.actives[0]["name"] if aggregates.actives else "TBD"
    entries = [{
        "weeks": [1], "activity": "Champions Kickoff",
        "audience": str(champion_count), "champion": "Líder Eng", "format": "2h síncrono",
    }]
    for week, (topic, count) in enumerate(aggregates.topic_counts.most_common(3), 2):
        entries.append({
            "weeks": [week], "activity": topic,
            "audience": str(count), "champion": champion_name, "format": "4h hands-on",
        })
    entries.append({
        "weeks": [4], "activity": "Office hours #1",
        "audience": "Todos", "champion": "Champions", "format": "1h Q&A",
    })
    entries.append({
        "weeks": [6, 8, 10, 12], "activity": "Office hours quinzenal",
        "audience": "Todos", "champion": "Champions", "format": "1h Q&A",
    })
    return entries


def build_30_day_schedule(aggregates):
    """30-day schedule as structured data (single source for .md and .json)."""
    rows = [{
        "week": 1,
        "activities": f"Champions Kickoff ({len(aggregates.actives)} pessoas) + agendamento de workshops",
    }]
    if aggregates.topic_counts:
        topic, count = aggregates.topic_counts.most_common(1)[0]
        rows.append({"week": 2, "activities": f"Workshop {topic} ({count} inscritos)"})
    rows.append({"week": 3, "activities": "Office hours #1 + remoção de barreira top"})
    rows.append({"week": 4, "activities": "Retrospectiva + revisão do plano"})
    return rows


def append_calendar_section(md, aggregates):
    md.extend(["---", "", "## 5 · Calendário sugerido (próximos 90 dias)", ""])
    md.extend(["| Semana | Workshop | Audiência | Champion | Formato |", SEP_5])
    for entry in build_calendar_entries(aggregates):
        weeks = ", ".join(f"W{week}" for week in entry["weeks"])
        md.append(f"| {weeks} | {entry['activity']} | {entry['audience']} | {entry['champion']} | {entry['format']} |")
    md.append("")


def append_counter_table(md, title, header, counter, respondent_count):
    md.extend([title, header, SEP_3])
    for key, value in counter.most_common():
        md.append(f"| {key} | {value} | {safe_pct(value, respondent_count):.0f}% |")
    md.append("")


def append_format_section(md, aggregates, respondent_count):
    md.extend(["---", "", "## 6 · Formato e cadência preferidos", ""])
    top_formats = Counter(dict(aggregates.formats.most_common(5)))
    append_counter_table(md, "### Formatos (top 5 — L5-Q1 multi)", "| Formato | N | % |", top_formats, respondent_count)
    append_counter_table(md, "### Tempo disponível por semana (L5-Q2)", "| Tempo | N | % |", aggregates.time_per_week, respondent_count)
    append_counter_table(md, "### Cohort vs self-paced (L5-Q4)", "| Preferência | N | % |", aggregates.cohort_pref, respondent_count)


def barrier_action(barrier):
    if contains_any(barrier, ["Falta de tempo", "Lack of time", "Falta de tiempo"]):
        return "Bloquear 2h/sem no calendário"
    if contains_any(barrier, ["licença Copilot", "Copilot license", "licencia Copilot"]):
        return "Revisar licenças com TI, target 100%"
    if contains_any(barrier, ["Champion"]):
        return "Ativar Champions Network identificados"
    if contains_any(barrier, ["por onde começar", "where to start", "por donde empezar"]):
        return "Criar learning path em Copilot Space"
    return "Discutir com líder"


def append_barriers_section(md, aggregates, respondent_count):
    md.extend(["---", "", "## 7 · Barreiras a remover (priorizado)", ""])
    md.extend(["| Barreira | Devs afetados | % | Ação sugerida |", SEP_4])
    for barrier, count in aggregates.barriers.most_common(8):
        md.append(f"| {barrier} | {count} | {safe_pct(count, respondent_count):.0f}% | {barrier_action(barrier)} |")
    md.append("")


def append_quote_block(md, title, quotes):
    if not quotes:
        return
    md.append(title)
    for quote, name in quotes:
        md.append(f"> _\"{quote}\"_ — sugerido por {name}")
        md.append("")


def append_wishlist_section(md, aggregates):
    md.extend(["---", "", "## 8 · Wishlist do time", ""])
    append_quote_block(md, "### Workshops sugeridos pelo time (L7-Q2)", aggregates.workshop_wishes)
    append_quote_block(md, "### Palestrantes externos sugeridos (L7-Q3)", aggregates.speaker_wishes)
    append_quote_block(md, "### Outras sugestões (L7-Q4)", aggregates.pain_quotes[:3])


def append_connection_section(md, aggregates):
    md.extend([
        "---",
        "",
        "## 9 · 🔗 Conexão com outros surveys",
        "",
        "Se você rodou também o **Developer Survey** (anônimo) e o **Assessment principal**, compare:",
        "",
        "| Dimensão | Auto-perception (este survey, L2) | Rubrica medida (survey-devs, D-X) | Capability assessment |",
        SEP_4,
    ])
    for dimension_id, name in DIMENSION_NAMES.items():
        median = median_level(aggregates.self_perception[dimension_id])
        md.append(f"| {dimension_id} {name} | mediana {median} | (rodar /insights-developer-survey) | (rodar /calculate-scores) |")
    md.append("")


def ranked_actions(aggregates):
    actions = []
    if aggregates.topic_counts:
        topic, count = aggregates.topic_counts.most_common(1)[0]
        actions.append((f"Workshop: {topic}", f"{count} inscritos pré-validados", "30 dias"))
    if aggregates.actives:
        actions.append(("Champions Kickoff", f"{len(aggregates.actives)} Champions ativos identificados", "30 dias"))
    if aggregates.barriers:
        barrier, count = aggregates.barriers.most_common(1)[0]
        actions.append((f"Remover barreira: {barrier}", f"{count} devs afetados", "60 dias"))
    if aggregates.mentors and aggregates.mentees:
        actions.append(("Programa de mentoria 1:1", f"{len(aggregates.mentors)} mentores × {len(aggregates.mentees)} mentees", "60 dias"))
    actions.append(("Office hours quinzenal", "Atende todas as barreiras de baixa adoção", "Contínuo a partir de W2"))
    return actions[:5]


def append_actions_section(md, aggregates):
    md.extend(["---", "", "## 10 · 🎯 Top 5 ações priorizadas (impacto × facilidade)", ""])
    md.extend(["| # | Ação | Impacto | Horizonte |", SEP_4])
    for index, (action, impact, horizon) in enumerate(ranked_actions(aggregates), 1):
        md.append(f"| {index} | {action} | {impact} | {horizon} |")
    md.append("")


def append_30_day_schedule(md, aggregates):
    md.extend(["---", "", "## 11 · 📅 Cronograma 30 dias", ""])
    md.extend(["| Semana | Atividades |", SEP_2])
    for row in build_30_day_schedule(aggregates):
        md.append(f"| **W{row['week']}** | {row['activities']} |")
    md.append("")


def append_respondents_appendix(md, respondents):
    md.extend([
        "---",
        "",
        "## 12 · 📋 Apêndice — Respondentes (para liderança usar para convites)",
        "",
        "> ⚠️ Esta tabela contém nomes/emails. **NÃO compartilhar publicamente** — só usar para convites de workshops.",
        "",
        "| Nome | Email | Quer Champion? |",
        SEP_3,
    ])
    for respondent in respondents:
        name = respondent.get("name", "?")
        email = respondent.get("email", "?")
        label = champion_short_label(response_value(respondent, "L6-Q1"))
        md.append(f"| {name} | {email} | {label} |")
    md.append("")


def build_report(respondents, aggregates, date):
    respondent_count = len(respondents)
    md = []
    append_intro(md, respondent_count, date)
    append_executive_summary(md, aggregates, respondent_count)
    append_topics_section(md, aggregates, respondent_count)
    append_cohorts_section(md, aggregates)
    append_champions_section(md, aggregates)
    append_calendar_section(md, aggregates)
    append_format_section(md, aggregates, respondent_count)
    append_barriers_section(md, aggregates, respondent_count)
    append_wishlist_section(md, aggregates)
    append_connection_section(md, aggregates)
    append_actions_section(md, aggregates)
    append_30_day_schedule(md, aggregates)
    append_respondents_appendix(md, respondents)
    md.extend([
        "---",
        "",
        f"*Plano gerado pela skill `/training-plan` · {date} · Sobrescreva editando manualmente o .md*",
        branding.md_footer(),
    ])
    return "\n".join(md)


def parse_now(value):
    """Validate an ISO-8601 --now override; default to the current UTC time.

    Mirrors scripts/compute_scores.py so reruns with a fixed --now are
    byte-identical (CI comparison / reference-example regeneration).
    """
    if value is None:
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        print(f"❌ --now deve ser um timestamp ISO-8601 como 2026-05-08T16:20:08Z, recebido: {value}")
        raise SystemExit(1)
    return value


def date_from_now(now_iso):
    """YYYY-MM-DD date used in output filenames, derived from --now."""
    return datetime.datetime.fromisoformat(now_iso.replace("Z", "+00:00")).date().isoformat()


def build_plan_data(respondents, aggregates, date, input_path, generated_at):
    """Structured JSON payload (mirrors the .md report; consumed by
    wizard/scripts/auto_fill_from_plano.py as primary source)."""
    respondent_count = len(respondents)
    preferred_format = aggregates.cohort_pref.most_common(1)[0][0] if aggregates.cohort_pref else "Híbrido"
    cohorts = [
        {
            "dimension": dimension_id,
            "name": name,
            "devs": aggregates.priorities[dimension_id],
            "preferred_format": preferred_format,
            "plan": "cohort de 4-6 semanas com sessões síncronas + lab self-paced",
        }
        for dimension_id, name in DIMENSION_NAMES.items()
        if aggregates.priorities.get(dimension_id, 0) > 0
    ]
    return {
        "metadata": {
            "generated_at": generated_at,
            "generator": "survey-learning/scripts/gerar_plano_capacitacao.py",
            "source": input_path.name,
            "date": date,
            "n_respondents": respondent_count,
            "contains_personal_data": True,
            "distribution": "restrita à liderança (nomes e emails de respondentes identificados)",
            **branding.json_metadata(),
        },
        "top_topics": [
            {
                "topic": topic,
                "count": count,
                "pct": safe_pct(count, respondent_count),
                "attendees": aggregates.topic_attendees[topic],
            }
            for topic, count in aggregates.topic_counts.most_common(10)
        ],
        "priorities": {did: aggregates.priorities[did] for did, _ in DIMENSION_NAMES.items() if aggregates.priorities.get(did)},
        "cohorts": cohorts,
        "champions": {
            "active": aggregates.actives,
            "supported": aggregates.supported,
            "maybe": aggregates.maybe,
            "references": [
                {"name": name, "mentions": count}
                for name, count in aggregates.references.most_common(3)
            ],
        },
        "mentorship": {
            "mentors": aggregates.mentors,
            "mentees": aggregates.mentees,
        },
        "calendar_90_days": build_calendar_entries(aggregates),
        "schedule_30_days": build_30_day_schedule(aggregates),
        "barriers": [
            {
                "barrier": barrier,
                "count": count,
                "pct": safe_pct(count, respondent_count),
                "action": barrier_action(barrier),
            }
            for barrier, count in aggregates.barriers.most_common(8)
        ],
        "format_preferences": {
            "formats": dict(aggregates.formats.most_common()),
            "time_per_week": dict(aggregates.time_per_week.most_common()),
            "cohort_vs_self_paced": dict(aggregates.cohort_pref.most_common()),
        },
    }


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(KIT / "survey-learning/respostas-learning.json"))
    parser.add_argument("--out", default=str(KIT / "saida"))
    parser.add_argument("--now", default=None, metavar="ISO8601",
                        help="Override do timestamp (ex.: 2026-05-08T16:20:08Z) para saída reprodutível")
    return parser.parse_args()


def load_respondents(path):
    """Returns the respondents list, or None (after printing a one-line
    actionable error) when the JSON is malformed."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido em {path} (linha {e.lineno}: {e.msg}). Corrija o arquivo ou re-rode /import-learning-survey.")
        return None
    if not isinstance(data, dict) or not isinstance(data.get("respondents", []), list):
        print(f"❌ Estrutura inesperada em {path}: esperado objeto com lista 'respondents'. Re-rode /import-learning-survey.")
        return None
    return data.get("respondents", [])


def print_summary(out_path, json_path, respondent_count, aggregates):
    display_path = out_path.relative_to(KIT) if out_path.is_relative_to(KIT) else out_path
    display_json = json_path.relative_to(KIT) if json_path.is_relative_to(KIT) else json_path
    print(f"\n✅ Plano de capacitação → {display_path}")
    print(f"✅ Dados estruturados   → {display_json} (fonte primária do wizard Mode D)")
    print(f"\n📊 {respondent_count} respondentes IDENTIFICADOS")
    if aggregates.topic_counts:
        print("\n📚 Top 3 tópicos demandados:")
        for index, (topic, count) in enumerate(aggregates.topic_counts.most_common(3), 1):
            print(f"   {index}. {topic[:60]} — {count} inscritos")
    print(f"\n👥 Champions: {len(aggregates.actives)} ativos · {len(aggregates.supported)} com suporte · {len(aggregates.maybe)} maybe")
    print(f"\n🎓 Mentor pairs: {len(aggregates.mentors)} mentores · {len(aggregates.mentees)} mentees")
    if aggregates.barriers:
        barrier, count = aggregates.barriers.most_common(1)[0]
        print(f"\n⚠ Top barreira: {barrier} ({count}/{respondent_count} devs)")


def main():
    args = parse_args()
    input_path = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"❌ {input_path} não encontrado. Rode /import-learning-survey primeiro.")
        return 1

    respondents = load_respondents(input_path)
    if respondents is None:
        return 1
    respondent_count = len(respondents)
    if respondent_count < 3:
        print(f"⚠ Apenas {respondent_count} respondentes. Plano será preliminar.")

    generated_at = parse_now(args.now)
    date = date_from_now(generated_at)
    aggregates = collect_aggregates(respondents)
    out_path = out_dir / f"plano-capacitacao-{date}.md"
    out_path.write_text(build_report(respondents, aggregates, date), encoding="utf-8")
    json_path = out_dir / f"plano-capacitacao-{date}.json"
    plan_data = build_plan_data(respondents, aggregates, date, input_path, generated_at)
    json_path.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print_summary(out_path, json_path, respondent_count, aggregates)
    return 0


if __name__ == "__main__":
    sys.exit(main())
