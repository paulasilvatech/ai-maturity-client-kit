---
name: calculate-scores
description: Compute capability, pillar, and overall maturity scores from respostas.json by running the official deterministic SUMPRODUCT script; writes saida/scores.json. Use when the user asks to "calculate scores", "run the scoring", "calcular scores", "computar pontuação", "rodar o scoring", "calcular puntajes", "ejecutar el scoring".
---

# Skill: Calculate scores

## When to use
- After the client fills `respostas.json` (manually or via Excel import).
- Whenever `respostas.json` changes.
- Prerequisite for `/gap-analysis`, `/recommend-strategies`, and report generation.

## Inputs
- `respostas.json` (workspace root): responses; each `level` may be `null` or any number in `0..4` (multi-respondent imports produce averages such as `2.5`).
- `framework.json`: question and capability weights.

## Run
```bash
python3 scripts/compute_scores.py
```
- Optional flags: `--respostas <path>`, `--framework <path>`, `--out <path>`, `--now <ISO8601>` (pins `metadata.computed_at` for reproducible output).
- The script validates levels, applies the official SUMPRODUCT algorithm, assigns L0-L4 labels, computes the coverage threshold, and warns if `respostas.json::metadata.framework_version` differs from `framework.json::version` (warning only, never blocks).

## Output
- `saida/scores.json`. Schema example: `referencia/exemplo-saida/scores.json`.
- Threshold: answered >= 40 is OK, 25-39 is WARNING, below 25 is BLOCKED. BLOCKED results are still computed, only marked; tell the client that at that coverage the executive report should not drive decisions.

## Chat report
Compose in the client language (`respostas.json::metadata.language`, default pt-br), 5 lines max: output path; overall score and label (plus PE score if present); threshold with answered/applicable; pillar scores; next step (`/gap-analysis`).

```text
Example client-facing output (compose in the client language):
Scores calculados: saida/scores.json
Overall: 1.99 (L2, Definido) | PE: 2.60 (L3, Gerenciado)
Threshold: OK (46/158 respondidas)
Pilares: P1 2.69 | P2 1.52 | P3 1.92
Próximo passo: /gap-analysis
```

## Constraints
- NEVER hand-compute scores in chat; always run the script. Algorithm reference: `referencia/pontuacao-e-calculo.md`.
- Never modify `framework.json`, `respostas.json`, or anything under `referencia/`.
- If the script errors (missing file, invalid level), relay its message and the fix; do not fall back to manual math.
