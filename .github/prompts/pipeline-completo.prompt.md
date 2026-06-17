---
name: pipeline-completo
description: Run the end-to-end AI Maturity Assessment pipeline from respostas.json or respostas-forms.xlsx to spreadsheet, scores, gaps, recommendations, and 5 PDFs. Use when the client finished the organizational assessment input and wants everything in one pass.
agent: agent
---

# Pipeline Completo

This prompt orchestrates only the **AI Maturity Assessment** flow. The Developer Survey and Learning & Growth Survey are separate flows with their own skills, but their latest outputs are detected and attached to `saida/payload.json` by `/gerar-relatorio`.

Inherit repository policies from `.github/copilot-instructions.md`: do not invent data, keep generated artifacts in `saida/`, and stop at the first unresolved error.

## Pre-checks

1. Detect input in this order:
   - If `respostas-forms.xlsx` exists and is newer than `respostas.json`, run `/importar-respostas-excel` first.
   - Else if `respostas.json` exists, use it directly.
   - Else stop and direct the client to `README.md`, `GUIA-PASSO-A-PASSO.md`, or `coleta/INSTRUCOES-FORMS.md`.
2. Validate `respostas.json` parses as JSON. If invalid, stop and run or suggest:
   ```bash
   python3 -m json.tool respostas.json
   ```
3. Count `responses[*].level != null`.
   - `0`: stop and ask the client to fill answers or use `respostas.json.example` for a demo.
   - `1-24`: warn that threshold is BLOCKED; continue only if the client explicitly wants a preliminary draft.
   - `25-39`: warn that threshold is WARNING.
   - `>=40`: continue.
4. Detect complementary artifacts and mention them in the final summary if present:
   - `survey-devs/respostas-devs.json`
   - `survey-learning/respostas-learning.json`
   - latest `saida/insights-developer-survey-*.md`
   - latest `saida/plano-capacitacao-*.md`

## Execution Sequence

Run the skills in this order, verifying each expected output before continuing:

1. Conditional `/importar-respostas-excel`
   - Expected: `respostas.json` and `saida/import-log-*.md`.
2. `/preencher-planilha`
   - Expected: `saida/pontuacao-preenchida-*.xlsx`.
3. `/calcular-scores`
   - Expected: `saida/scores.json`.
   - Report overall score, PE score if present, threshold, and pillar scores.
4. `/gap-analysis`
   - Expected: `saida/gaps.json`.
   - Report P0/P1/P2/P3 distribution.
5. `/recomendar-estrategias`
   - Expected: `saida/recomendacoes.json`.
   - Report top 3 strategies.
6. Optional `/wizard-implementacao`
   - If `implementation-guide-inputs.json` is missing and the client wants personalized Part 4, stop here and route to the wizard.
   - If a latest `saida/plano-capacitacao-*.md` exists, recommend wizard Mode D auto-fill.
   - If the client chooses placeholders, continue.
7. `/gerar-relatorio`
   - Expected: `saida/payload.json` plus 5 PDFs:
     - `saida/score_justification.pdf`
     - `saida/roadmap_part_pillar_p1.pdf`
     - `saida/roadmap_part_pillar_p2.pdf`
     - `saida/roadmap_part_pillar_p3.pdf`
     - `saida/roadmap_part4.pdf`

## Error Recovery

- Excel import fails: stop, explain that headers must start with `P1-C1-Q1:` style IDs, and point to `coleta/perguntas-para-forms.md`.
- JSON invalid: stop and show the `python3 -m json.tool respostas.json` command.
- Invalid levels: stop and list the problematic qids. Accepted values are `null` or numbers from `0` to `4`, including averages like `2.5`.
- Missing prior output: stop and rerun the previous skill instead of skipping ahead.
- WeasyPrint failure: stop, show the Python dependency command and OS-specific dependency note from `GUIA-PASSO-A-PASSO.md`.

## Final Summary

Reply in PT-BR with:

```text
Pipeline completo — AI Maturity Assessment

Arquivos gerados em saida/:
- pontuacao-preenchida-<DATE>.xlsx
- scores.json
- gaps.json
- recomendacoes.json
- payload.json
- score_justification.pdf
- roadmap_part_pillar_p1.pdf
- roadmap_part_pillar_p2.pdf
- roadmap_part_pillar_p3.pdf
- roadmap_part4.pdf

Resumo:
- Overall: <score> (<label>)
- Threshold: <status> (<answered>/158)
- Pillars: P1=<score> · P2=<score> · P3=<score>
- Gaps: P0=<n> · P1=<n> · P2=<n> · P3=<n>
- Estratégias top 3: <Sx>, <Sy>, <Sz>
- Locale: <payload.locale>

Complementos detectados:
- Developer Survey: <yes/no>
- Learning Survey: <yes/no>
- Wizard personalizado: <yes/no>

Próximos passos:
1. Abrir `saida/score_justification.pdf`.
2. Validar scores e evidências com stakeholders.
3. Completar dados faltantes ou personalizar `implementation-guide-inputs.json` se necessário.
```
