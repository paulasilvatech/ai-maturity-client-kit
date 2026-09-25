# `survey-learning/scripts/`

🌐 [English](README.md) · Português (Brasil)

📖 **Navegação:** [🏠 Índice](../../README.pt-br.md) · [« Learning Survey](../README.pt-br.md)

Scripts que constroem o plano de capacitação a partir do Learning & Growth Survey (identificado).

## Conteúdo

| Arquivo | Propósito |
|---|---|
| [`gerar_plano_capacitacao.py`](gerar_plano_capacitacao.py) | Lê `survey-learning/respostas-learning.json` e gera `saida/plano-capacitacao-<DATE>.md` — 12 seções com top 10 tópicos demandados, cohorts por dimensão D2-D8 (com listas nominais de inscritos), Champions Network em 3 tiers, mentor↔mentee pairs, calendário 90 dias, barreiras priorizadas. |

## Uso

```bash
# Inglês (padrão)
python3 survey-learning/scripts/gerar_plano_capacitacao.py

# Português (Brasil)
python3 survey-learning/scripts/gerar_plano_capacitacao.py --lang pt-br
```

> [!IMPORTANT]
> Este script é invocado pela skill `/plano-capacitacao`. O agente concierge faz isso automaticamente; você só roda diretamente se quiser regenerar sem passar pelo chat.

## Output

Markdown completo (~10 páginas equivalentes), gerado em **inglês por padrão** (PT-BR com `--lang pt-br`), pronto para apresentar à liderança ou anexar em proposta de capacitação.
