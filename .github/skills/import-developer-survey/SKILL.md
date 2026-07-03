---
name: import-developer-survey
description: Runs survey-devs/scripts/import_developer_survey.py to convert the anonymous Developer Survey Forms .xlsx export (75 behavioral questions, 9 sections) into survey-devs/respostas-devs.json. Use when the user says "import developer survey", "importar survey de devs", "importar respostas dos desenvolvedores", "importar encuesta de desarrolladores", or mentions respostas-survey-devs.xlsx. Not for the 158-question maturity assessment (use /import-assessment-responses).
argument-hint: optional path to the .xlsx (default: respostas-survey-devs.xlsx at root)
---

# Skill: Import Developer Survey responses (anonymous)

## When to use
- The client collected the anonymous, individual Developer Survey via Microsoft Forms and wants team insights.
- The output feeds `/insights-developer-survey` (which runs the deterministic rubric and report).
- Not for the maturity assessment (`P*-C*-Q*` headers) or the Learning Survey (`L*-Q*` headers).

## Input file expectations
- Default file: `respostas-survey-devs.xlsx` at the workspace root, or the path the user passes.
- Row 1 is headers; each question header starts with a qid matching `S[1-9]-Q\d+:`.
- The script validates the detected count against the canonical question bank in `survey-devs/perguntas-para-forms-devs.md` (75 questions) and logs a warning on any mismatch. Trust the script's count, not older docs that mention 69.
- Email and Name columns should contain "anonymous" (proper anonymous Forms export).

## Run
```bash
python3 survey-devs/scripts/import_developer_survey.py --input respostas-survey-devs.xlsx
```

Omit `--input` when the file is at the default location. No language flag exists here; the report language is decided later by `/insights-developer-survey`.

## Output
- `survey-devs/respostas-devs.json`: metadata (`total_questions: 75`, `anonymous: true`) plus one entry per respondent with raw answer text. This is pipeline INPUT, not a client deliverable.
- `saida/import-survey-log-<DATE>.md`: respondent count, questions detected vs expected, per-section coverage, warnings.

## Post-import step
Confirm anonymity was preserved:
- The output JSON must contain no names or emails (the script never writes them).
- If the log warns that Email/Name columns were filled, the Forms was not configured as anonymous. The script already discarded the identities; tell the user, and recommend fixing the Forms setting before the next collection round.

## Report in chat
Summarize from the script output and the log: respondents imported (and that they are anonymous), questions detected vs expected, warning count, log path, and the next step (`/insights-developer-survey`). Compose the message in the client language (`respostas.json::metadata.language`, default pt-br).

Example client-facing output (compose in the client language):
```
Survey de desenvolvedores importado: survey-devs/respostas-devs.json
12 respondentes anônimos, 75 / 75 questões detectadas, 0 alertas
Log: saida/import-survey-log-2026-07-03.md
Próximo passo: /insights-developer-survey
```

## Constraints
- NEVER capture, store, or echo respondent names/emails; the survey is anonymous by design.
- NEVER modify `survey-devs/perguntas-para-forms-devs.md` or the template .xlsx files.
- Do not re-implement parsing in chat; the script owns header matching, anonymity checks, and logging.
- If the script fails, relay its message and help the user fix the export; do not hand-edit the JSON.
