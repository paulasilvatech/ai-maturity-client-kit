---
name: training-plan
description: Generates a prioritized training plan (plano de capacitação) from the Learning & Growth Survey by running survey-learning/scripts/gerar_plano_capacitacao.py. Reads survey-learning/respostas-learning.json (IDENTIFIED respondents, name+email) and produces saida/plano-capacitacao-<DATE>.md plus a structured .json (top topics, cohorts per dimension D2-D8, Champions Network, mentor pairs, 90-day calendar) that feeds /implementation-wizard Mode D auto-fill. Use after /import-learning-survey, or when the user asks for a "training plan", "plano de capacitação", "Champions Network", "workshops priorizados", "capacitation roadmap", "plan de capacitación", "plan de formación" or similar.
argument-hint: optional path different from survey-learning/respostas-learning.json
---

# Skill: Training plan from the Learning Survey

## When to use
- After `/import-learning-survey` produced `survey-learning/respostas-learning.json`.
- Leadership wants an actionable plan: prioritized topics, cohorts, Champions, workshop calendar.
- Before `/implementation-wizard` — its Mode D auto-fills from this skill's JSON output.

## Inputs
- `survey-learning/respostas-learning.json` — output of `/import-learning-survey` (identified respondents)

## Expected output
- `saida/plano-capacitacao-<DATE>.md` — 12-section plan: top topics with attendees, cohorts per dimension D2-D8, Champions Network tiers, mentor pairs, 90-day calendar, barriers, prioritized actions (the script emits it in PT-BR).
- `saida/plano-capacitacao-<DATE>.json` — same data structured; primary source for `/implementation-wizard` Mode D (`wizard/scripts/auto_fill_from_plano.py` prefers it over the markdown).
- Brief chat summary in the client language (`respostas.json::metadata.language`, default pt-br): N respondents, top topics, Champions count, top barrier.

## Procedure

1. **Run the script:**
   ```bash
   python3 survey-learning/scripts/gerar_plano_capacitacao.py
   # optional: --input <path.json> --out <dir>  (defaults: survey-learning/respostas-learning.json, saida/)
   ```

2. **Report language.** Outputs are PT-BR today. For EN/ES clients, offer to translate the generated markdown on request, preserving names, numbers and the calendar.

3. **Summarize in chat.** Example client-facing output (compose in the client language):
   ```
   ✓ Plano de capacitação gerado: saida/plano-capacitacao-2026-07-03.md (+ .json para o wizard)
   • Respondentes: 5 (identificados) · Top tópico: Copilot Spaces (5 inscritos)
   • Champions: 3 ativos · Mentores: 2 · Barreira nº 1: "Não sei por onde começar"
   • Próximo passo: /implementation-wizard (Modo D preenche automaticamente a partir do plano)
   ```

## Privacy (identified data)
- Outputs contain PII: respondent names and emails (attendee lists, Champions, mentor pairs). The JSON metadata is flagged `contains_personal_data: true`.
- Share only with client leadership, and only with the respondents' knowledge (identification is disclosed in the survey form itself).
- Never paste names/emails into public channels, slides or commits; use anonymized aggregates for broader audiences.

## Error handling
- Input file missing → run `/import-learning-survey` first.
- Fewer than 3 respondents → the script warns; present the plan as preliminary.

## Constraints
- DO NOT reimplement aggregation or the plan template in chat — the script owns them deterministically.
- Artifact filenames stay in PT (`plano-capacitacao-...`): they are client-facing deliverables.
- Outputs ALWAYS in `saida/` with ISO date; same-day reruns overwrite (idempotent).
