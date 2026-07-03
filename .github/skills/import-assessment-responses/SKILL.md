---
name: import-assessment-responses
description: Runs scripts/import_assessment_responses.py to convert a Microsoft Forms .xlsx export of the 158-question AI Maturity Assessment into respostas.json, averaging multiple respondents per question. Use when the user says "import assessment responses", "convert the Forms export to JSON", "importar respostas do assessment", "converter Excel para JSON", "importar respuestas del assessment", "convertir Excel a JSON", or mentions respostas-forms.xlsx.
argument-hint: optional path to the .xlsx (default: respostas-forms.xlsx at root)
---

# Skill: Import assessment responses (Forms .xlsx to respostas.json)

## When to use
- The client collected the 158-question maturity assessment via Microsoft Forms (or a compatible spreadsheet) and wants to run the pipeline.
- One or many respondents: the script aggregates by mean per question, without rounding.
- Not for the Developer or Learning surveys; those have their own import skills.

## Input file expectations
- Default file: `respostas-forms.xlsx` at the workspace root, or the path the user passes.
- Row 1 is headers; each question header starts with a qid matching `P[1-3]-C\d+-Q\d+:`; evidence columns are headed `Evidência (<qid>)` (literal Forms header).
- The script validates the detected question count against `framework.json` (expects ~158) and exits with a clear error if the file does not look like a Forms export. Do not second-guess its count in chat.

## Run
Decide the report language BEFORE running:
- If `respostas.json` already exists, omit `--language`; the script preserves the configured `metadata.language`.
- If this is the FIRST import (no `respostas.json` yet), ask the user once which language client reports should use (pt-br, en, or es) and pass it explicitly. Never let a new EN or ES client fall through to the pt-br default silently.

```bash
python3 scripts/import_assessment_responses.py --input respostas-forms.xlsx --language en
```

Omit `--input` when the file is at the default location; omit `--language` when preserving an existing configuration.

## Output
- `respostas.json` overwritten (automatic backup `respostas.json.backup-<timestamp>` when a previous file existed).
- `saida/import-log-<DATE>.md`: respondents, coverage per respondent, warnings. Unrecognized cell values become `null`, never invented levels.

## Post-import step
- Read `respostas.json::metadata.organization`. If it is empty or still the sample placeholder ("Cliente Exemplo S.A."), ask the user for the real client organization name and write it into that field; reports print it on every page.
- Confirm the resolved `metadata.language` back to the user.

## Report in chat
Summarize from the script output and the log: respondents imported, questions with at least one answer (X / 158), evidences captured, warning count, backup name, log path, and the next step (`/run-full-pipeline` or `/calculate-scores`). Compose the message in the client language (`respostas.json::metadata.language`).

Example client-facing output (compose in the client language):
```
Importação concluída: respostas.json atualizado (backup: respostas.json.backup-20260703T101500)
3 respondentes, 142 / 158 questões com pelo menos 1 resposta, 117 evidências
Log: saida/import-log-2026-07-03.md
Próximo passo: /run-full-pipeline
```

## Constraints
- NEVER modify `framework.json` or anything under `coleta/` or `referencia/`.
- Do not re-implement parsing in chat; the script owns header matching, level parsing, aggregation, backup, and logging.
- If the script fails (file not found, too few qid headers), relay its message and help the user fix the Forms export; do not hand-edit `respostas.json` to work around it.
