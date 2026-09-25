# `survey-learning/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Learning Survey](../README.md)

Scripts that build the capacitation plan from the Learning & Growth Survey (identified).

## Contents

| File | Purpose |
|---|---|
| [`gerar_plano_capacitacao.py`](gerar_plano_capacitacao.py) | Reads `survey-learning/respostas-learning.json` and generates `saida/plano-capacitacao-<DATE>.md`: 12 sections with the top 10 requested topics, cohorts per dimension D2-D8 (with named attendee lists), a 3-tier Champions Network, mentor↔mentee pairs, a 90-day calendar, and prioritized barriers. |

## Usage

```bash
# English (default)
python3 survey-learning/scripts/gerar_plano_capacitacao.py

# Portuguese (Brazil)
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang pt-br
```

> [!IMPORTANT]
> This script is invoked by the `/plano-capacitacao` skill. The concierge agent does it automatically; you only run it directly if you want to regenerate without going through chat.

## Output

Full Markdown (~10 equivalent pages), written in **English by default** (PT-BR with `--lang pt-br`), ready to present to leadership or attach to a capacitation proposal.
