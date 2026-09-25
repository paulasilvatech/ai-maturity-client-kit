# `relatorios/templates/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Reports](../README.md)

Jinja2 templates for the **5 PDFs** the client receives. **Do not modify** without coordination: they mirror the web platform templates exactly (`app/src/report-service/templates/`).

## Contents

| File | Renders | Approx. size |
|---|---|---|
| [`score_justification.html.j2`](score_justification.html.j2) | `score_justification.pdf`: executive justification + PE Readiness + recommended path | ~330 KB |
| [`roadmap_part_pillar.html.j2`](roadmap_part_pillar.html.j2) | Rendered **3 times** (P1/P2/P3) → `roadmap_part_pillar_p{1,2,3}.pdf`: deep dive per pillar | ~410 KB each |
| [`roadmap_part4.html.j2`](roadmap_part4.html.j2) | `roadmap_part4.pdf`: consolidated Implementation Guide (Steering Committee, RACI, ADKAR, Quick Wins) | ~510 KB |
| [`_components.html.j2`](_components.html.j2) | Shared macros (cards, badges, score meters, gauges), included in the 3 templates above | — |
| [`_print.css`](_print.css) | Print CSS with `@page` rules, MS 4-color palette via `:root`, Inter + JetBrains Mono typography | — |

## How to customize

> [!CAUTION]
> Editing the `.html.j2` files here **affects ALL clients** who use the kit. For per-client customization, edit `saida/payload.json` and re-render with `render_reports.py`.

If you really want to change a template:
1. Work on a branch
2. Run `make smoke` before committing
3. Compare visually: `python3 relatorios/scripts/build_payload_and_render.py` vs the PDFs in `referencia/exemplo-saida/`

## Key variables consumed

Each template expects specific fields from `payload.json`. For the full schema, see:
- [`../sample_payload.json`](../sample_payload.json): populated example
- [`../scripts/build_payload_and_render.py`](../scripts/build_payload_and_render.py): code that builds the payload

## i18n

Localizable strings live in [`../i18n/`](../i18n/) (`en.json`, `es.json`, `pt-br.json`). Templates read them via `{{ t('key') }}`.
