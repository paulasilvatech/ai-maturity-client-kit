# Kit AI Maturity Assessment · Edición Español

> Kit de autoservicio para ejecutar la Evaluación de Madurez en IA con GitHub Copilot.
> **3 encuestas complementarias · 5 PDFs production-quality · plan de capacitación personalizado.**

[![Open in VS Code](https://img.shields.io/badge/Abrir%20en-VS%20Code-007ACC?logo=visualstudiocode)](https://github.com/paulanunes85/ai-maturity-client-kit)
[![Sitio](https://img.shields.io/badge/sitio-paulanunes85.github.io-00A4EF)](https://paulanunes85.github.io/ai-maturity-client-kit/es/)
[![Descargar ZIP](https://img.shields.io/badge/descargar-ES%20kit.zip-7FBA00)](https://github.com/paulanunes85/ai-maturity-client-kit/releases/latest/download/ai-maturity-kit-es.zip)

---

## Qué es este kit

Un **kit autocontenido** para ejecutar una evaluación end-to-end de madurez en IA **sin depender de una plataforma web**. Incluye:

- **Framework de 158 preguntas** organizado en 3 pilares × 28 capabilities × 7 estrategias
- **3 encuestas complementarias**: Assessment organizacional + Developer Survey anónima + Learning & Growth Survey identificada
- **14 skills custom de Copilot Chat** que orquestan el pipeline completo
- **5 PDFs ejecutivos** renderizados con branding paulasilva-ms (paleta Microsoft 4 colores) — ya localizados en ES vía `relatorios/i18n/es.json`
- **Hoja Excel auditable** con fórmulas SUMPRODUCT nativas
- **Plan de capacitación** con nombres + emails de inscritos

## ⚠ Nota importante sobre idioma

Este folder `kit-es/` contiene la **documentación cliente en Español**. El resto del kit (`framework.json`, skills, scripts, encuestas) queda en Portugués (Brasil) por estas razones:

1. **GitHub Copilot Chat es multilingüe** — puedes interactuar con el agente y las skills en Español; te responden en tu idioma.
2. **Los PDFs ya se renderizan en Español** vía `relatorios/i18n/es.json` — define `report_lang: "es"` en `respostas.json` y los 5 PDFs salen en Español.
3. **Las preguntas quedan en PT-BR** porque están validadas contra la plataforma de producción. Los Forms pueden presentarse en Español a los respondentes pero se mapean a los IDs en PT-BR.

Si necesitas el framework JSON totalmente traducido, abre un issue: <https://github.com/paulanunes85/ai-maturity-client-kit/issues/new>

## Inicio rápido

```bash
# 1. Clona el repo
git clone https://github.com/paulanunes85/ai-maturity-client-kit.git
cd ai-maturity-client-kit

# 2. Valida prerequisitos
make smoke

# 3. Copia los datos de ejemplo y ejecuta el pipeline completo
cp respostas.json.example respostas.json

# Abre VS Code, en Copilot Chat (modo Agent):
#   @ai-maturity-assistant
# o:
#   /pipeline-completo
```

Los resultados aparecen en `saida/` (5 PDFs + scores.json + gaps.json + recomendacoes.json + Excel auditable).

## Las 3 encuestas

| Encuesta | Audiencia | Preguntas | Tiempo | Output |
|---|---|---|---|---|
| 🅰️ **AI Maturity Assessment** | Liderazgo / org | 158 | 60-90 min | 5 PDFs ejecutivos |
| 🅱️ **Developer Survey** | Devs anónimos | 75 | 22-28 min/dev | Insights comportamentales + madurez L0-L4 por dimensión |
| 🅲 **Learning & Growth** | Devs identificados | 32 | 5-8 min/dev | Roadmap de capacitación con listas de inscritos |

Orden recomendado para consultoría seria: **B (anónimo) → C (identificado) → A (liderazgo)**. Cada encuesta informa la siguiente; el agente concierge cruza resultados automáticamente.

## Pipeline en una línea

```
INPUT (respostas.json o Forms .xlsx)
  → /calcular-scores          (SUMPRODUCT 3 capas)
  → /gap-analysis             (prioridades P0 / P1 / P2 / P3)
  → /recomendar-estrategias   (S1 a S7 + tecnologías)
  → /wizard-implementacao     (9 inputs para PDF Parte 4)
  → /gerar-relatorio          (Jinja2 + WeasyPrint)
OUTPUT (5 PDFs + XLSX auditable)
```

## Qué está traducido en este folder

| Archivo | Estado |
|---|---|
| [README.md](README.md) | ✅ Traducido |
| [GUIA-PASSO-A-PASSO.md](../GUIA-PASSO-A-PASSO.md) | ✅ Traducido como `PASO-A-PASO.md` |
| [INSTRUCOES-FORMS.md](../coleta/INSTRUCOES-FORMS.md) | ✅ Traducido como `INSTRUCCIONES-FORMS.md` |
| Framework JSON, skills, scripts | ⏸ Quedan en PT-BR (Copilot Chat interpreta) |
| PDFs de reporte | ✅ Ya en ES vía `relatorios/i18n/es.json` |

## Continuar leyendo

| ⬅ Anterior                                                                | Siguiente ➡                                       |
| :------------------------------------------------------------------------ | -------------------------------------------------: |
| [🏠 Sitio principal (multi-idioma)](https://paulanunes85.github.io/ai-maturity-client-kit/) | [📘 Paso a paso detallado](PASO-A-PASO.md) |

---

**Paula Silva** — Software Global Black Belt | paulasilva@microsoft.com
*Building the future of software development with AI and Agentic DevOps*
