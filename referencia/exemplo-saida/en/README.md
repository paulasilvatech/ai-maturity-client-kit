# `referencia/exemplo-saida/en/`

📖 **Navigation:** [🏠 Index](../../../README.md) · [« Example output](../README.md)

**English** version of the 5 reference PDFs generated from `respostas.json.example` (Cliente Exemplo S.A., locale forced to `en`).

## Contents

| File | Description |
|---|---|
| `score_justification.pdf` | Score Justification (overall 1.99, L2) |
| `roadmap_part_pillar_p1.pdf` | Developer Productivity pillar deep-dive |
| `roadmap_part_pillar_p2.pdf` | DevOps Lifecycle pillar deep-dive |
| `roadmap_part_pillar_p3.pdf` | Application Platform pillar deep-dive |
| `roadmap_part4.pdf` | Implementation Guide (consolidated) |

## When to use

- Show the end client what **the English PDFs will look like** (if they set `language: "en"` in `respostas.json::metadata`)
- Visually validate that the templates handle longer strings (English tends to expand vs. PT-BR)

> [!NOTE]
> The PT-BR PDFs (default) live in the parent directory: [`../`](../).

## How to regenerate

From the kit root, with the example inputs staged (see [`../README.md`](../README.md), step 1):

```bash
export SOURCE_DATE_EPOCH=1778257208   # pins embedded font timestamps (byte-stable PDFs)
python3 relatorios/scripts/build_payload_and_render.py \
  --date 2026-05-08 --locale en --out referencia/exemplo-saida/en
```

`--locale en` builds a payload with English labels from `relatorios/i18n/en.json` and renders the 5 PDFs. For real client reports in English, set `metadata.language` to `"en"` in `respostas.json` and run `/generate-reports`.
