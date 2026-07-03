---
name: insights-developer-survey
description: Generates the aggregated Developer Survey insights report by running survey-devs/scripts/gerar_insights.py. Reads survey-devs/respostas-devs.json and produces saida/insights-developer-survey-<DATE>.md (adoption, mode usage, agent/MCP awareness, governance gaps, anonymized pain quotes, prioritized recommendations) plus the team maturity JSON (dimensions D2-D8). Use after /import-developer-survey, or when the user asks for "developer survey insights", "insights do survey de devs", "relatório de insights dos devs", "maturidade do time dev", "team maturity from the survey", "insights de la encuesta de desarrolladores" or similar.
argument-hint: optional path different from survey-devs/respostas-devs.json
---

# Skill: Developer Survey insights report

## When to use
- After `/import-developer-survey` produced `survey-devs/respostas-devs.json`.
- Team wants aggregated insights or team maturity (dimensions D2-D8) from the developer survey.
- To feed real developer voice into `/implementation-wizard` and the maturity assessment capabilities (P1-C1, P1-C5, P1-C8, P2-C4, P3-C6).

## Inputs
- `survey-devs/respostas-devs.json` — output of `/import-developer-survey` (anonymous)
- `survey-devs/RUBRICA-MATURIDADE.md` — read only if the client asks how a dimension score was computed

## Expected output
- `saida/maturidade-developer-survey-<DATE>.json` — team-aggregate rubric scores (anonymous)
- `saida/insights-developer-survey-<DATE>.md` — 12-section report (the script emits it in PT-BR)
- Brief chat summary in the client language (`respostas.json::metadata.language`, default pt-br): N respondents, team maturity, top insights and gaps.

## Procedure

1. **Run the single entry point** (it computes maturity via `rubric.py` AND writes the report):
   ```bash
   python3 survey-devs/scripts/gerar_insights.py
   # optional: --input <path.json> --out <dir>  (defaults: survey-devs/respostas-devs.json, saida/)
   ```
   Do NOT run `calcular_maturidade.py` first — `gerar_insights.py` emits the identical maturity JSON, so running both is redundant.

2. **Check the match-coverage guardrail.** The rubric matches the canonical PT answer options. In the maturity JSON, if `metadata.match_coverage.avg_pct` < 70, warn that answer text deviates from the canonical options (typical when Forms options were translated to EN/ES) and scores are silently deflated; fix the import instead of trusting the numbers. The maturity-only variant, `python3 survey-devs/scripts/calcular_maturidade.py`, enforces this hard: it aborts below 40% coverage unless run with `--force`.

3. **Report language.** The script emits the report in PT-BR today. For EN/ES clients, offer to translate the generated markdown on request, preserving all numbers, tables and quotes.

4. **Summarize in chat.** Example client-facing output (compose in the client language):
   ```
   ✓ Insights gerados: saida/insights-developer-survey-2026-07-03.md
   • Respondentes: 5 (anônimos) · Maturidade do time: 2.29, nível L2 (Definido)
   • Top insight: Coding Agent subutilizado (1 de 5 devs usa)
   • Próximo passo: usar os insights no /implementation-wizard (Training Plan, Quick Wins)
   ```

## Error handling
- Input file missing → run `/import-developer-survey` first.
- Fewer than 3 respondents → the script warns; present insights as preliminary (recommend 5+).

## Constraints
- DO NOT reimplement aggregation, scoring or the report template in chat — the script owns them deterministically.
- Anonymity: never attribute quotes or scores to an individual; the survey is anonymous by design.
- Outputs ALWAYS in `saida/` with ISO date; same-day reruns overwrite (idempotent).
