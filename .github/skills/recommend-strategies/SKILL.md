---
name: recommend-strategies
description: Rank the 7 strategies S1-S7 by cumulative gap impact and generate the prioritized action plan by running the deterministic recommendation script; reads saida/gaps.json and writes saida/recomendacoes.json. Use when the user asks to "recommend strategies", "recomendar estratégias", "mapear ações", "que iniciativas devo priorizar", "recomendar estrategias", "qué iniciativas debo priorizar".
---

# Skill: Recommend strategies

## When to use
- After `/gap-analysis` (requires `saida/gaps.json`).
- When the client wants an actionable plan, not just a diagnosis.

## Inputs
- `saida/gaps.json`: prioritized gaps (run `/gap-analysis` first if missing).
- `framework.json`: strategy definitions, technologies per strategy, capability-to-strategy mapping.

## Run
```bash
python3 scripts/recommend_strategies.py --gaps saida/gaps.json
```
- Optional flags: `--framework <path>`, `--out <path>`, `--now <ISO8601>` (reproducible timestamp).
- The script aggregates gaps per strategy, ranks by `cumulative_priority` (ties broken by `max_priority`, then gap count), attaches technologies from `framework.json` and deterministic first actions, and fills `skipped_strategies`.

## Output
- `saida/recomendacoes.json`. Schema example: `referencia/exemplo-saida/recomendacoes.json`.
- `skipped_strategies` entries are objects (`{"strategy_id": ..., "strategy_name": ...}`), not plain strings.
- Low-impact strategies (`cumulative_priority` < 0.9, only P3 gaps) appear in BOTH `ranked_strategies` and `skipped_strategies`: ranked for completeness, skipped meaning "monitor, do not invest yet". Present them as monitor-only, never as recommendations.

## Chat report
Compose in the client language (`respostas.json::metadata.language`, default pt-br), 5 lines max: output path; top 3 strategies with cumulative priority and first-action gist; skipped or monitor-only strategy ids; next step (`/generate-reports`).

```text
Example client-facing output (compose in the client language):
Recomendações geradas: saida/recomendacoes.json
1. S7 Security & Governance (5.87): habilitar GHAS em todos os repos + SBOM
2. S6 Agentic Activation (3.92): pilot Semantic Kernel para 1 workflow interno
Sem investimento agora (monitorar): S1, S3, S4
Próximo passo: /generate-reports
```

## Constraints
- Actions, outcomes, and technologies come exclusively from the script output (sourced from `framework.json`); NEVER invent them in chat. If detail is missing, say the point needs refinement with a Microsoft GBB architect.
- NEVER hand-aggregate or re-rank strategies in chat; rerun the script after any change to `saida/gaps.json`.
- Never modify `framework.json`, `respostas.json`, or anything under `referencia/`.
