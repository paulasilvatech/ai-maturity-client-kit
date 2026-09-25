# `survey-devs/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Developer Survey](../README.md)

Scripts that compute developer AI maturity from the Developer Survey (anonymous).

## Contents

| File | Purpose |
|---|---|
| [`rubric.py`](rubric.py) | **Deterministic L0-L4 rubric** across 7 dimensions (D2-D8). Maps answers → scores. Importable as a module. |
| [`calcular_maturidade.py`](calcular_maturidade.py) | Reads `survey-devs/respostas-devs.json`, applies `rubric.py`, and generates `saida/maturidade-developer-survey-<DATE>.json` with aggregated team scores. |
| [`gerar_insights.py`](gerar_insights.py) | Generates the full Markdown report (`saida/insights-developer-survey-<DATE>.md`): demographics, Copilot adoption, governance, anonymized quotes, and recommendations linked to capabilities (P1-C1, P1-C5, P1-C8, P2-C4, P3-C6). The report is written in **English by default**; pass `--lang pt-br` for Portuguese (Brazil). |

## Usage

```bash
# Maturity scores only
python3 survey-devs/scripts/calcular_maturidade.py

# Scores + full report (recommended), in English by default
python3 survey-devs/scripts/gerar_insights.py

# Same report in Portuguese (Brazil)
python3 survey-devs/scripts/gerar_insights.py --lang pt-br
```

> [!IMPORTANT]
> These scripts are invoked by the `/insights-developer-survey` skill. You normally do not need to run them directly: the concierge agent does it.

## Rubric documentation

See [`../RUBRICA-MATURIDADE.md`](../RUBRICA-MATURIDADE.md) for the scoring rules per dimension.
