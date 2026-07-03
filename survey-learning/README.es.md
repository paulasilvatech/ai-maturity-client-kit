# `survey-learning/`: Learning & Growth Survey (identificada, capacitación)

**Tercer pilar del kit:** después de medir la madurez organizacional (assessment) y el comportamiento real (survey-devs), esta encuesta genera el **roadmap de capacitación personalizado**: workshops, cohorts, Champions Network, mentoría. **Identificada** (nombre+email) para poder invitar a las personas correctas.

## 📐 Diferencia vs. las otras encuestas

| Aspecto | Assessment principal | Developer Survey | **Learning Survey** |
| --- | --- | --- | --- |
| **Audiencia** | Liderazgo | Devs anónimos | **Devs identificados** |
| **¿Anónima?** | No | Sí | **No: necesita nombre+email** |
| **Foco** | Madurez organizacional L0-L4 | Comportamiento real (% adopción) | **Qué quieren APRENDER** |
| **Tiempo por respondiente** | 60-90 min | 22-28 min | **5-8 min** |
| **Cantidad de preguntas** | 158 | 75 | **32** |
| **Output** | 5 PDFs production | Insights + madurez calculada | **Plan de capacitación accionable** |
| **Skills** | `/calculate-scores`, `/generate-reports` | `/import-developer-survey`, `/insights-developer-survey` | `/import-learning-survey`, `/training-plan` |

**Las 3 son complementarias**: correr las 3 da una visión 360°:

```text
Assessment (estrategia del liderazgo)
         ↓
Survey-devs (realidad de comportamiento anónima)
         ↓
Learning Survey (deseo de evolución identificado)
         ↓
IMPLEMENTATION-WIZARD (consolida en el Implementation Guide PDF)
```

## 📋 Las 7 secciones

| # | Sección | Foco | Q |
| --- | --- | --- | --- |
| **L1** | Identificación | Nombre, email, cargo, equipo | 4 |
| **L2** | Auto-percepción de madurez | Auto-evaluación L0-L4 en las 7 dimensiones D2-D8 (rúbrica) | 7 |
| **L3** | Dónde quieres crecer | Top 3 dimensiones prioritarias (próximos 6 meses) | 2 |
| **L4** | Temas específicos | Copilot, Foundry, prácticas (TDD/SDD), agents, seguridad | 5 |
| **L5** | Formato y cadencia | Workshop, cohort vs self-paced, horarios, tiempo/semana | 4 |
| **L6** | Champions y mentoría | ¿Quieres ser Champion? ¿Mentoría? ¿Quién es referencia? | 5 |
| **L7** | Barreras y Wishlist | Qué te bloquea + workshops + speakers deseados | 5 |
| | | **TOTAL** | **32** |

## 🗂️ Archivos en esta carpeta

| Archivo | Qué es |
| --- | --- |
| **[INSTRUCOES-FORMS-LEARNING.es.md](INSTRUCOES-FORMS-LEARNING.es.md)** | Cómo crear el Microsoft Forms IDENTIFICADO (con configuración + buenas prácticas + uso ético de los datos) |
| **[perguntas-para-forms-learning.md](perguntas-para-forms-learning.md)** | Las 32 preguntas formateadas para copy/paste en Forms (original en PT-BR) |
| **[perguntas-para-forms-learning.en.md](perguntas-para-forms-learning.en.md)** | Banco de preguntas en inglés, preservando los IDs `Lx-Qy` para parsing |
| **[perguntas-para-forms-learning.es.md](perguntas-para-forms-learning.es.md)** | Banco de preguntas en español, preservando los IDs `Lx-Qy` para parsing |
| **[template-export-forms-learning.xlsx](template-export-forms-learning.xlsx)** | Template Excel + 5 respondientes simulados (Maria, João, Ana, Pedro, Sofia) |
| **[respostas-mock-learning.json](respostas-mock-learning.json)** | JSON estructurado de ejemplo |

## 🚀 Flujo de uso

```text
1. Crear el Forms siguiendo INSTRUCOES-FORMS-LEARNING.es.md (~30 min)
2. Compartir el link con TODOS los devs (Slack/Teams/Email)
3. Esperar 2 semanas (recordatorios en D+7 y D+12)
4. Responses → Open in Excel
5. Guardar como respostas-survey-learning.xlsx en la raíz del kit
6. /import-learning-survey → survey-learning/respostas-learning.json
7. /training-plan          → saida/plano-capacitacao-FECHA.md (+ .json)
```

## 🧪 Cómo probar / smoke test (sin recolectar respuestas reales)

Antes de crear el Forms para los devs, valida el pipeline con los 5 respondientes simulados:

### Modo A: vía Copilot Chat (recomendado)

```bash
# Desde la raíz del kit:
cp survey-learning/respostas-mock-learning.json survey-learning/respostas-learning.json
```

En Copilot Chat (modo Agent):

```text
/training-plan
```

En ~30 segundos tendrás `saida/plano-capacitacao-2026-05-08.md` generado a partir de los mocks (Maria, João, Ana, Pedro, Sofia). Permite ver "cómo va a quedar" antes de recolectar datos reales.

### Modo B: vía @ai-maturity-assistant (concierge)

```text
@ai-maturity-assistant
```

Elige **[C] Learning & Growth Survey** cuando el agente pregunte. Va a ofrecer 3 opciones y la opción `[C] Smoke test inmediato con mocks` ejecuta el atajo automáticamente.

### Modo C: simulando el ciclo completo vía Excel mock

Para validar end-to-end (incluyendo la skill `/import-learning-survey`):

```bash
# Renombra el template al nombre de archivo que la skill espera detectar
cp survey-learning/template-export-forms-learning.xlsx respostas-survey-learning.xlsx

# En Copilot Chat:
/import-learning-survey      # parsea el Excel mock → respostas-learning.json
/training-plan             # genera el plan de los 5 mocks identificados
```

Después limpia el estado:

```bash
rm respostas-survey-learning.xlsx survey-learning/respostas-learning.json
```

### Qué validar en el smoke test

Después de `/training-plan`, abre `saida/plano-capacitacao-FECHA.md` y confirma:

- [ ] El resumen ejecutivo muestra 5 respondientes
- [ ] Los top 10 temas demandados aparecen con **nombre + email** de los inscritos (Maria, João, Ana, Pedro, Sofia)
- [ ] Champions Network: Maria + João + Sofia listados como "activos" (consistente con los mocks)
- [ ] Calendario de 90 días generado (workshops secuenciados)
- [ ] El apéndice tiene la tabla de respondientes (visible para el liderazgo)

Si falta alguno de estos puntos → repórtalo como bug de la skill `/training-plan` (no del mock).

## 📊 Qué contiene el plan de capacitación

`saida/plano-capacitacao-<DATE>.md` (generado por la skill) tiene **12 secciones**:

1. **Resumen Ejecutivo**: madurez percibida + top 3 dimensiones prioritarias + Champions identificados + 3 quick wins
2. **Top 10 temas demandados**: con lista de inscritos pre-validados (nombre+email)
3. **Cohorts sugeridos por dimensión D2-D8**: con Champions, formato, cadencia
4. **Champions Network**: 3 niveles (activos, con soporte, maybe) + parejas mentor-mentee + referencias naturales
5. **Calendario de workshops próximos 90 días**: semana × workshop × audiencia × Champion
6. **Formato y cadencia preferidos**: agregado del equipo
7. **Barreras a remover**: priorizado
8. **Wishlist del equipo**: workshops, speakers, ideas libres
9. **Conexión con las otras encuestas**: comparación self-perception (L2) vs rúbrica medida (D2-D8) vs assessment principal
10. **Top 5 acciones priorizadas**: impacto × facilidad × alineación con los gaps
11. **Próximos 30 días**: cronograma semana a semana
12. **Apéndice: respondientes (visible solo para el liderazgo)**: tabla con todos los respondientes

## 🔗 Conexión con las otras encuestas y el wizard

### ⭐ Mode D: auto-fill del wizard

Después de que `/training-plan` genera `saida/plano-capacitacao-FECHA.md` (más un gemelo `.json` estructurado), al correr `/implementation-wizard` el Copilot Agent **detecta automáticamente** este plan y ofrece **Mode D: Auto-fill**, que completa **6 de los 9 inputs del wizard** automáticamente. Por debajo ejecuta `wizard/scripts/auto_fill_from_plano.py`, que prefiere el `.json` (existe un fallback regex sobre el `.md`, pero pierde detalle):

```text
saida/plano-capacitacao-FECHA.json (con fallback .md)
    ↓ alimenta automáticamente (Mode D)
.github/skills/implementation-wizard  (Parte 4 del PDF)
    ↓ campos poblados:
- executive_steering_committee  ← Champions Network "activos"
- communication_plan            ← Calendario sugerido
- training_plan                 ← Cohorts por dimensión
- adkar_notes                   ← Top 5 workshops (etapa Knowledge)
- quick_wins_w1_4               ← Calendario 30 días
- quick_wins_w5_8               ← Calendario semanas 5-8
- quick_wins_w9_12              ← Calendario semanas 9-12

Solo completas manualmente: TPO + RACI Matrix
```

**Ahorro estimado del Mode D:** 30-45 min de wizard manual, más datos REALES de tu equipo (no placeholders del sample Acme).

**Cómo invocar Mode D:** simplemente corre `/implementation-wizard` después de `/training-plan`. El agente lo ofrece automáticamente.

## 🔐 Sobre la identificación (no anonimato)

- Microsoft Forms tiene la opción "Anonymous responses": para esta encuesta debe quedar **DESMARCADA**
- Los devs necesitan saber que es identificada AL RESPONDER (transparencia)
- El liderazgo se compromete a usar los datos SOLO para capacitación (no performance review)
- El plan consolidado se comparte con todo el equipo (transparencia)
- El apéndice con nombres/emails es "visible para el liderazgo" en el reporte: no compartirlo públicamente

## 📅 Cadencia sugerida

- **Primera vez:** después de establecer la línea base con el assessment + survey-devs
- **Cada 6 meses:** medir la evolución del deseo + comparar con la madurez real
- **Después de eventos grandes** (rollout de Copilot, cambio de stack, nuevo Champion): volver a correrla para realinear el plan

## 📚 Documentación relacionada

- **Skill que importa Excel → JSON:** [`../.github/skills/import-learning-survey/SKILL.md`](../.github/skills/import-learning-survey/SKILL.md)
- **Skill que genera el plan:** [`../.github/skills/training-plan/SKILL.md`](../.github/skills/training-plan/SKILL.md)
- **Encuesta complementaria (anónima):** [`../survey-devs/`](../survey-devs/)
- **Wizard que consume el plan:** [`../wizard/`](../wizard/) (alimenta la Parte 4 del PDF)
- **Assessment principal:** ver [`../README.es.md`](../README.es.md)

## 🔗 Fuentes de los temas cubiertos en la encuesta

Los temas de aprendizaje listados en L4 vienen de las mismas fuentes oficiales validadas en el Developer Survey:

- **GitHub Copilot** (modos, Spaces, Coding Agent): docs.github.com/copilot
- **Microsoft Foundry**: learn.microsoft.com/azure/foundry
- **MCP / A2A**: protocolos + soporte en Foundry (mar/2026)
- **Spec Kit (SDD)**: github.com/github/spec-kit
- **Agentic DevOps personas**: learn.microsoft.com/azure/well-architected/ai/personas
- **GHAS, CodeQL, SBOM, Defender**: GitHub Advanced Security + docs de Microsoft Defender for DevOps
