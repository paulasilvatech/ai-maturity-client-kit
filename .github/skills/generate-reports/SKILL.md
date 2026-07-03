---
name: generate-reports
description: Renders the 5 client-ready PDF reports (Score Justification, 3 Pillar Roadmaps, Implementation Guide) by invoking relatorios/scripts/build_payload_and_render.py, which merges client data from saida/ into the rich sample payload structure. Use when the user asks to "generate report PDFs", "render PDF", "executive report", "final report", "gerar relatório", "gerar PDFs", "PDF final", "produzir o report executivo", "consolidar resultados", "generar informes", "renderizar los PDF", "informe ejecutivo final".
---

# Skill: Generate executive PDF reports

## When to use
- After `/calculate-scores`, `/gap-analysis`, `/recommend-strategies` (pipeline order).
- After `/implementation-wizard` produced `implementation-guide-inputs.json` (re-renders Part 4).
- After manually editing `saida/payload.json` (re-render with custom narrative, see Customization).

## Pre-flight checks
1. Required inputs exist: `respostas.json`, `saida/scores.json`, `saida/gaps.json`, `saida/recomendacoes.json`. If any is missing, run `/run-full-pipeline` first. The script hard-errors without `saida/scores.json` unless `--allow-sample` is passed.
2. Optional input: `implementation-guide-inputs.json` (output of `/implementation-wizard`). Without it, Part 4 keeps professional sample placeholders.
3. Dependencies: `python3 -c "import jinja2, weasyprint"`; if missing, `python3 -m pip install --user --break-system-packages jinja2 weasyprint`.

## Procedure

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

The script loads `relatorios/sample_payload.json` as base structure, overrides only the fields with client data (organization, overall/pillar/capability scores, gap analysis, wizard inputs), writes `saida/payload.json`, and renders the 5 PDFs. If developer-survey or learning-plan artifacts exist in `saida/`, it also populates `payload.cross_survey_data`.

Useful flags:

| Flag | Effect |
|---|---|
| `--html-only` | Render HTML only, skip PDF conversion (no WeasyPrint needed) |
| `--allow-sample` | Render with fictional sample (Acme) data when client inputs are missing; demos only |
| `--date YYYY-MM-DD` | Pin `generated_date` for reproducible output (also via `REPORT_DATE` env var) |
| `--locale en\|es\|pt-br` | Override report locale (default: `respostas.json::metadata.language`) |

## Outputs (in `saida/`)
- `payload.json` (merged data the templates consumed; edit this to customize)
- `score_justification.pdf`
- `roadmap_part_pillar_p1.pdf`
- `roadmap_part_pillar_p2.pdf`
- `roadmap_part_pillar_p3.pdf`
- `roadmap_part4.pdf`

## Report in chat
Compose in the client language (`respostas.json::metadata.language`, default pt-br), covering:
1. The 5 PDFs plus `payload.json` written to `saida/` (list the file names).
2. Organization, overall score and level, locale, threshold status (from `saida/scores.json`).
3. Which narrative sections still use sample placeholders, and the two personalization routes below.
4. Suggested next step: open `score_justification.pdf` and confirm organization and scores.

## Customization
1. **Part 4 (Implementation Guide):** run `/implementation-wizard`, then re-run this skill.
2. **Narrative fields:** render once, edit `saida/payload.json` (e.g. `capabilities[].scoring_rationale`, `capabilities[].h1_initiatives`, `risks_per_pillar`, `success_metrics_per_pillar`), then re-render WITHOUT re-merging (a full re-run would overwrite your edits):

   ```bash
   python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
   ```
3. **Language:** edit `respostas.json::metadata.language` (en / es / pt-br) and re-run.

## Branding
The script injects the paulasilva-ms branding block into the payload automatically; do not hand-edit it. Rules and canonical strings: `.github/instructions/branding.instructions.md` and `referencia/branding/IDENTITY.md`.

## Constraints
- DO NOT modify files in `relatorios/templates/` (mirrors of official platform code).
- DO NOT build `payload.json` from scratch; always let the script merge from `sample_payload.json`.
- DO NOT bypass the script with manual Jinja2 rendering; it misses i18n, CSS, and WeasyPrint setup.

## Reference example
`referencia/exemplo-saida/` contains the 5 PDFs rendered from `respostas.json.example`; compare against them to confirm fidelity.
