---
name: run-full-pipeline
description: Run the end-to-end AI Maturity Assessment pipeline (import, spreadsheet, scores, gaps, strategies, 5 PDFs) using the deterministic scripts. Formerly /pipeline-completo. Trigger on "run the full pipeline", "rodar o pipeline completo", "gerar tudo de uma vez".
agent: agent
model: Claude Sonnet 4.6
---

# Run Full Pipeline

Orchestrates only the AI Maturity Assessment flow. The Developer Survey and Learning & Growth Survey are separate flows; their latest outputs are detected below and attached to the payload by `/generate-reports`.

Inherit repository policies from `.github/copilot-instructions.md`: never invent data, keep every generated artifact in `saida/`, compute scores only via the scripts, and stop at the first unresolved error.

## Pre-checks

1. Input detection, in order:
   - `respostas-forms.xlsx` exists and is newer than `respostas.json` -> run `/import-assessment-responses` first.
   - Else `respostas.json` exists -> use it.
   - Else stop and point the client to `README.md`, `GUIA-PASSO-A-PASSO.md`, or `coleta/INSTRUCOES-FORMS.md`.
2. Validate JSON: `python3 -m json.tool respostas.json`. If it fails, stop and show the failing line.
3. Count `responses[*].level != null` and apply the coverage policy (compute-and-mark; the kit never refuses to compute):
   - `0`: stop; ask the client to fill answers, or to copy `respostas.json.example` for a demo run.
   - `1-24`: BLOCKED. Warn that results are not valid for executive decisions; continue only with the client's explicit consent to a preliminary draft.
   - `25-39`: WARNING. Warn and continue.
   - `>=40`: OK.
4. Detect complementary artifacts (report them in the final summary):
   - `survey-devs/respostas-devs.json` and `survey-learning/respostas-learning.json`
   - latest `saida/insights-developer-survey-*.md`
   - latest `saida/plano-capacitacao-*.md` and `saida/plano-capacitacao-*.json`

## Execution sequence

Verify each expected output file exists before continuing; stop at the first unresolved error.

1. Conditional `/import-assessment-responses` -> `respostas.json` + `saida/import-log-<DATE>.md`. After a first import `metadata.organization` is empty: ask the client for the organization name before rendering reports.
2. `/fill-spreadsheet` -> `saida/pontuacao-preenchida-<DATE>.xlsx`.
3. `python3 scripts/compute_scores.py` (skill `/calculate-scores`) -> `saida/scores.json`. Report overall score, threshold, and pillar scores.
4. `python3 scripts/compute_gaps.py` (skill `/gap-analysis`) -> `saida/gaps.json`. Report the P0/P1/P2/P3 gap distribution.
5. `python3 scripts/recommend_strategies.py --gaps saida/gaps.json` (skill `/recommend-strategies`) -> `saida/recomendacoes.json`. Report the top 3 ranked strategies.
6. Optional gate: `/implementation-wizard`.
   - If any `saida/plano-capacitacao-*.json` exists, recommend wizard Mode D (auto-fill from the learning plan).
   - If `implementation-guide-inputs.json` is missing and the client wants a personalized Part 4, stop here and route to the wizard.
   - If the client accepts sample placeholders, continue.
7. `/generate-reports` -> `saida/payload.json` plus 5 PDFs: `score_justification.pdf`, `roadmap_part_pillar_p1.pdf`, `roadmap_part_pillar_p2.pdf`, `roadmap_part_pillar_p3.pdf`, `roadmap_part4.pdf`.

## Error recovery

| Failure | Action |
|---|---|
| Excel import fails | Column headers must start with qid IDs (`P1-C1-Q1:` style). Point to `coleta/perguntas-para-forms.md`. |
| `respostas.json` invalid JSON | Stop; show the `python3 -m json.tool respostas.json` error and the failing line. |
| Invalid levels | Stop; list the offending qids. Accepted values: `null` or numbers 0-4, floats allowed (e.g. 2.5). |
| WeasyPrint / PDF render fails | Run `make install-deps`, then rerun `/generate-reports` (or use `--html-only` to skip PDF conversion). |
| Missing prior output | Rerun the previous step; never skip ahead or hand-craft the missing file. |

## Final summary

Write the summary in the client language (`respostas.json::metadata.language`, default pt-br). Use exactly this block structure:

1. Header line: pipeline completed + assessment name.
2. Generated files: list every artifact created in `saida/` this run.
3. Results: overall score with its level label; threshold status with `<answered>/158`; pillar scores P1/P2/P3; gap counts P0/P1/P2/P3; top 3 strategies (id + name); report locale (`saida/payload.json::locale`).
4. Complements detected: Developer Survey yes/no, Learning Survey yes/no, personalized wizard input yes/no.
5. Next steps, numbered: open `saida/score_justification.pdf`; validate scores and evidence with stakeholders; fill missing answers or personalize `implementation-guide-inputs.json` if needed.
