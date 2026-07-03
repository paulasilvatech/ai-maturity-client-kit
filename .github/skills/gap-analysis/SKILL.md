---
name: gap-analysis
description: Compute the gap (target minus current score) and P0-P3 priority per capability by running the deterministic gap script; reads saida/scores.json plus respostas.json::target_overrides and writes saida/gaps.json. Use when the user asks for "gap analysis", "where are my gaps", "priorização", "onde estão minhas lacunas", "análisis de brechas", "dónde están mis brechas".
---

# Skill: Gap analysis

## When to use
- After `/calculate-scores` (requires `saida/scores.json`).
- When the client wants to know where to invest first or how to prioritize the roadmap.

## Inputs
- `saida/scores.json`: capability scores (run `/calculate-scores` first if missing or stale).
- `respostas.json::target_overrides`: optional custom target per capability. Default target is 3.0; never invent targets, use only overrides or the default.
- `framework.json`: weights and capability-to-strategy mapping.

## Run
```bash
python3 scripts/compute_gaps.py
```
- Optional flags: `--scores <path>`, `--respostas <path>`, `--framework <path>`, `--out <path>`, `--now <ISO8601>` (reproducible timestamp).
- The script computes `gap_size` and `priority_score` (weight x gap), classifies each gap P0-P3, assigns the suggested horizon, and sorts by `priority_score` descending. Capabilities with no score (unanswered) or already at target are excluded automatically.

## Output
- `saida/gaps.json` (P0 first). Schema example: `referencia/exemplo-saida/gaps.json`.

## Chat report
Compose in the client language (`respostas.json::metadata.language`, default pt-br), 5 lines max: output path; total capabilities with gap; P0-P3 distribution; top 3 gaps with priority; next step (`/recommend-strategies`).

```text
Example client-facing output (compose in the client language):
Gap analysis concluído: saida/gaps.json (10 capabilities com gap)
Distribuição: P0 3 | P1 0 | P2 1 | P3 6
Top 3: P2-C4 DevSecOps (3.30, P0) | P3-C5 Aplicações Agênticas (3.17, P0) | P2-C10 Cadeia de Suprimentos (2.57, P0)
Próximo passo: /recommend-strategies
```

## Constraints
- NEVER hand-compute gaps or priorities in chat; the P0-P3 classification is the script's job.
- Do not re-add capabilities the script excluded (unanswered or target met); if the client asks, mention unanswered capabilities as a coverage warning.
- Never modify `framework.json`, `respostas.json`, or anything under `referencia/`.
