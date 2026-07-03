---
name: ai-maturity-reports
description: High-level wrapper that produces the complete report bundle for the AI Maturity Assessment, 5 client-ready PDFs plus the auditable XLSX workbook, by delegating to /run-full-pipeline. Use when the user asks for "full reports pipeline", "complete pack", "all PDFs", "AI Maturity report", "generate the bundle", "pacote completo de relatórios", "gerar todos os PDFs", "rodar tudo de ponta a ponta", "paquete completo de informes", "generar todos los PDF", "ejecutar el pipeline completo".
---

# Skill: ai-maturity-reports

High-level orchestrator for the full set of client deliverables: 5 PDFs (Score Justification, 3 Pillar Roadmaps, Implementation Guide) plus the auditable XLSX workbook. Use it for the end-to-end bundle; use the granular skills below to iterate on one piece.

## Standard pipeline

Delegate to the prompt, which owns the step sequence:

```
/run-full-pipeline
```

## Direct invocation (scores already computed)

If `saida/scores.json`, `saida/gaps.json`, and `saida/recomendacoes.json` already exist:

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

The script hard-errors without `saida/scores.json` unless `--allow-sample` is passed. See `/generate-reports` for flags (`--html-only`, `--allow-sample`, `--date`, `--locale`), pre-flight checks, and customization patterns.

## Outputs (in `saida/`)
- `payload.json`
- `score_justification.pdf`
- `roadmap_part_pillar_p1.pdf`, `roadmap_part_pillar_p2.pdf`, `roadmap_part_pillar_p3.pdf`
- `roadmap_part4.pdf`
- Plus the auditable workbook from `/fill-spreadsheet`.

Report locale follows `respostas.json::metadata.language` (en / es / pt-br). Branding is injected by the script; rules in `.github/instructions/branding.instructions.md`.

## Granular skills
- `/import-assessment-responses`, `/fill-spreadsheet`, `/calculate-scores`, `/gap-analysis`, `/recommend-strategies`, `/implementation-wizard`, `/generate-reports`

## Constraints
- DO NOT modify `relatorios/templates/*.html.j2` in place; template updates follow the "Maintainer sync" process in `CONTRIBUTING.md`.
- DO NOT bypass `build_payload_and_render.py` with manual Jinja2 rendering.

## Reference example
`referencia/exemplo-saida/` holds the 5 PDFs rendered from `respostas.json.example` (EN versions in `referencia/exemplo-saida/en/`), useful as a before/after demo for the client.
