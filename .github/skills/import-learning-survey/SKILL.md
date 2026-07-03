---
name: import-learning-survey
description: Runs survey-learning/scripts/import_learning_survey.py to convert the identified Learning & Growth Survey Forms .xlsx export (32 questions, 7 sections, name+email per respondent) into survey-learning/respostas-learning.json. Use when the user says "import learning survey", "import training survey", "importar survey de aprendizado", "importar Learning & Growth", "importar encuesta de aprendizaje", or mentions respostas-survey-learning.xlsx. Not for the anonymous Developer Survey (use /import-developer-survey).
argument-hint: optional path to the .xlsx (default: respostas-survey-learning.xlsx at root)
---

# Skill: Import Learning & Growth Survey responses (identified)

## When to use
- The client collected the Learning & Growth Survey via Microsoft Forms, IDENTIFIED with name+email (needed to invite people to workshops and pick champions).
- The output feeds `/training-plan` (prioritized training roadmap and wizard auto-fill).
- Not for the anonymous Developer Survey (`S*-Q*` headers) or the maturity assessment (`P*-C*-Q*` headers).

## Input file expectations
- Default file: `respostas-survey-learning.xlsx` at the workspace root, or the path the user passes.
- Row 1 is headers; each question header starts with a qid matching `L[1-7]-Q\d+:`.
- The script validates the detected count against the canonical question bank in `survey-learning/perguntas-para-forms-learning.md` (32 questions) and logs a warning on any mismatch.
- Name/email come from the Forms Email/Name columns, with the `L1-Q1` (name) and `L1-Q2` (email) answers as fallback; rows with neither are skipped and logged.

## Run
```bash
python3 survey-learning/scripts/import_learning_survey.py --input respostas-survey-learning.xlsx
```

Omit `--input` when the file is at the default location. No language flag exists here; the report language is decided later by `/training-plan`.

## Output
- `survey-learning/respostas-learning.json`: metadata (`total_questions: 32`, `anonymous: false`, `contains_pii: true`) plus one identified entry per respondent with raw answer text. Pipeline INPUT, not a client deliverable.
- `saida/import-learning-log-<DATE>.md`: respondent count, questions detected vs expected, skipped rows, warnings.

## Post-import step
Flag the PII explicitly:
- The JSON carries `contains_pii: true` because it holds real names and emails. Remind the user to keep it out of commits, shared drives, and screenshots, and to delete it when the engagement ends.
- Confirm the respondent count and any skipped rows from the log.

## Report in chat
Summarize from the script output and the log: identified respondents imported, questions detected vs expected, skipped rows, the PII notice, log path, and the next step (`/training-plan`). Compose the message in the client language (`respostas.json::metadata.language`, default pt-br).

Example client-facing output (compose in the client language):
```
Survey de Learning & Growth importado: survey-learning/respostas-learning.json
12 respondentes identificados, 32 / 32 questões detectadas
Atenção: o arquivo contém dados pessoais (contains_pii: true), não compartilhe nem faça commit
Log: saida/import-learning-log-2026-07-03.md
Próximo passo: /training-plan
```

## Constraints
- DO NOT anonymize; this survey is identified by design, but treat the JSON as confidential (PII).
- NEVER modify the question banks or the template .xlsx files.
- Do not re-implement parsing in chat; the script owns header matching, name/email fallback, and logging.
- If the script fails, relay its message and help the user fix the export; do not hand-edit the JSON.
