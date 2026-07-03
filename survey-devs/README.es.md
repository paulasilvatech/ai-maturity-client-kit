# `survey-devs/`: Developer Survey (anónimo, conductual, individual)

Esta carpeta contiene un **survey separado** del assessment principal, enfocado en entender **cómo cada desarrollador usa GitHub Copilot, agentes IA, instructions files, modos de Copilot Chat, prácticas (TDD/SDD), gobernanza y seguridad** en su día a día. Anónimo.

> 💡 **Survey complementario a este:** después de ejecutar el **survey-devs** (anónimo, mide comportamiento), considera también el **[survey-learning](../survey-learning/)** (identificado, mide lo que los devs quieren aprender). Los 2 juntos forman un diagnóstico 360° de los devs: conductual + aspiracional.

> 🔄 **Versión 2.0 (actualizada 2026-05-08)**: terminología actualizada con cambios oficiales:
> - **Copilot Workspace** evolucionó a **Copilot Coding Agent** (GA sep/2025)
> - **Copilot Spaces** (GA sep/2025) sustituyó a **Knowledge Bases** (sunset nov/2025)
> - **Azure AI Foundry** renombrado a **Microsoft Foundry** + **Foundry Agent Service** GA
> - Se agregaron preguntas sobre **MCP**, el **protocolo A2A**, las personas Agentic DevOps de Microsoft (**System Designer**, **Agent Operator**), **probar agents antes de usarlos**, **alcance+red-lines**, **JIT permissions**.

## 📐 Diferencia vs. el assessment principal y survey-learning

| Aspecto | Assessment principal | Developer Survey (este) | **survey-learning** |
|---|---|---|---|
| **Audiencia** | Liderazgo / arquitectos / Tech Leads | **Devs individuales** (cualquier cargo) | Devs individuales |
| **¿Anónimo?** | No, identificado por organización | **Sí, Forms anónimo** | **No, IDENTIFICADO (nombre+email)** |
| **Foco** | Madurez organizacional (L0-L4) | Adopción y práctica individual real | **Lo que quieren APRENDER** |
| **Escala** | Likert de 5 puntos por capability | Choice/multi-choice/texto libre | Autopercepción L0-L4 + multi |
| **Cantidad** | 158 preguntas en 28 capabilities | **75 preguntas en 9 secciones** | 32 preguntas en 7 secciones |
| **Tiempo por respondente** | 60-90 min | **22-28 min** | 5-8 min |
| **Multi-respondente** | Posible pero no es el default | **Esencial** (promedio ≥5, ideal ≥15) | **Esencial** (>50% del equipo) |
| **Output** | Reporte ejecutivo + 5 PDFs | Reporte de insights + madurez calculada | Plan de capacitación + Champions |
| **Skills** | `/calculate-scores`, `/generate-reports`, etc. | `/import-developer-survey` + `/insights-developer-survey` | [`/import-learning-survey`](../survey-learning/) + `/training-plan` |

**Los 3 son complementarios:**
- Este **survey-devs** mide COMPORTAMIENTO (anónimo)
- El **[survey-learning](../survey-learning/)** mide DESEO (identificado, complementa a este)
- El **assessment principal** mide ESTRATEGIA (liderazgo)
- Juntos forman un diagnóstico 360°.

## 📋 Las 9 secciones del survey (v2.0, actualizado 2026-05-08)

| # | Sección | Foco | Q |
|---|---|---|---|
| **S1** | Perfil | Cargo, experiencia, stack, modelo de trabajo | 7 |
| **S2** | GitHub Copilot: Adopción y Modos | Licencia, frecuencia, **Ask / Edit / Agent / Coding Agent (autónomo)**, features (incl. **Spaces**), ganancia | 9 |
| **S3** | Otras herramientas Microsoft / GitHub | **Microsoft Foundry** (ex-Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, Spec Kit, **MCP** | 7 |
| **S4** | Prácticas de Desarrollo con IA | TDD con IA, **SDD con Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Conceptos y Estructura de Agentes | Agente vs asistente, modos de Copilot, custom agents/skills/prompts, **A2A**, handoffs, subagentes, **personas Agentic DevOps de Microsoft** (System Designer / Agent Operator), **PROBAR agents antes de usarlos** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions en **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usabilidad y Best Practices | Cómo aprendieron (incl. MS Build / GitHub Universe), Champion, métricas DORA/DX, iteraciones, confianza | 9 |
| **S8** | Seguridad y Gobernanza | Política, datos sensibles, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **alcance+red-lines de agents**, **JIT permissions**, capacitación | 13 |
| **S9** | Pain Points & Wishlist | Frustraciones, ideas, feature requests | 4 |
| | | **TOTAL** | **75** |

## 🗂️ Archivos en esta carpeta

| Archivo | Qué es |
|---|---|
| **[INSTRUCOES-FORMS-DEVS.es.md](INSTRUCOES-FORMS-DEVS.es.md)** | Guía paso a paso para crear el Microsoft Forms (con configuración de anonimato + buenas prácticas de recolección) |
| **[perguntas-para-forms-devs.es.md](perguntas-para-forms-devs.es.md)** | Las 75 preguntas formateadas para copy/paste en Forms (tipos, opciones, IDs) |
| **[template-export-forms-devs.xlsx](template-export-forms-devs.xlsx)** | Template Excel en el formato de export de Forms + 5 respondentes mockeados (perfiles variados) |
| **[respostas-mock-devs.json](respostas-mock-devs.json)** | JSON estructurado de ejemplo (para probar la skill `/insights-developer-survey`) |
| **[RUBRICA-MATURIDADE.es.md](RUBRICA-MATURIDADE.es.md)** ⭐ | **Modelo de scoring**: rúbrica determinística que mapea respuestas → niveles L0-L4 en 7 dimensiones. Espeja la escala del assessment principal |
| **[scripts/rubric.py](scripts/rubric.py)** | Implementación Python de la rúbrica (reglas hardcoded por dimensión) |
| **[scripts/calcular_maturidade.py](scripts/calcular_maturidade.py)** | Script CLI que aplica la rúbrica → `saida/maturidade-developer-survey-DATE.json` |

## 🚀 Flujo de uso (3 caminos)

### Camino A: Microsoft Forms (recomendado para 10+ devs)

```
1. Crear el Forms siguiendo INSTRUCOES-FORMS-DEVS.es.md (~30-45 min)
2. Compartir el link con el equipo (Slack/Teams/Email)
3. Esperar 2 semanas (recordatorios periódicos)
4. Responses → Open in Excel
5. Guardar como respostas-survey-devs.xlsx en la raíz del kit-cliente/
6. /import-developer-survey       → survey-devs/respostas-devs.json
7. /insights-developer-survey  → saida/insights-developer-survey-DATE.md
```

### Camino B: Excel/SharePoint compartido (rápido para 3-5 devs)

```
1. cp survey-devs/template-export-forms-devs.xlsx respostas-survey-devs.xlsx
2. Limpiar las filas de mocks (filas 2-6)
3. Subir a SharePoint con permiso de edición
4. Cada dev llena una fila
5. Descargar y mover a la raíz
6. /import-developer-survey + /insights-developer-survey
```

### Camino C: smoke test inmediato (sin recolección real)

```
1. cp survey-devs/respostas-mock-devs.json survey-devs/respostas-devs.json
2. /insights-developer-survey  → ves cómo quedará el reporte con 5 mocks
```

Útil para presentar al cliente "cómo va a quedar" antes de recolectar.

## 📊 Qué sale en el reporte de insights

`saida/insights-developer-survey-<DATE>.md` (generado por la skill) contiene:

1. **Resumen ejecutivo**: 3 insights + 3 gaps + madurez percibida
2. **Demografía** (S1): quién respondió, distribución
3. **Adopción de Copilot** (S2): % licencias, **adopción por modo (Ask/Edit/Agent)**, features activas, ganancia percibida
4. **Ecosistema MS/GitHub** (S3): tabla de adopción
5. **Prácticas de IA + dev** (S4): TDD, SDD, debugging, onboarding + quotes anonimizadas
6. **Conocimiento de agentes** (S5): matriz de "conoce+usa / conoce / no conoce" para 8 conceptos
7. **Instructions files** (S6): quién los usa, mantiene, actualiza
8. **Usabilidad** (S7): Champion, métricas, confianza, iteraciones
9. **Seguridad** (S8): política, scanners, DLP, audit + **score de gobernanza 0-100**
10. **Pain points** (S9): top 5 frustraciones + wishlist (quotes)
11. **Recomendaciones priorizadas**: quick wins, próximo trimestre, semestre
12. **Conexión con el assessment principal**: capability por capability

## 🔗 Cómo el survey informa el assessment principal

Si ejecutaste ambos:

| Capability del assessment | Señal del survey | Validación |
|---|---|---|
| **P1-C1** Asistentes de Codificación IA | S2-Q1, Q2, Q7 | Score declarado vs. adopción real |
| **P1-C2** Plataforma de DevEx | S6-Q5, S7-Q2 | ¿Existe herramental compartido? |
| **P1-C5** Onboarding y Capacitación | S7-Q1, Q2 | ¿Cómo aprendieron los devs? ¿Hay Champions? |
| **P1-C8** Medición de Productividad | S7-Q4 | ¿DORA/DX/SPACE realmente medidos? |
| **P2-C4** DevSecOps | S8-Q4, Q5, Q11 | Scanners activos vs. vulns vistas |
| **P2-C10** Supply Chain | S8-Q4, Q6 | SBOM, secret scan, DLP |
| **P3-C5** Aplicaciones Agénticas | S5-Q3, Q6, Q9 | Custom agents, MCP: sofisticación técnica |
| **P3-C6** Identidad y Acceso | S8-Q1, Q8, Q9 | Política, DLP, audit |

> 💡 **Caso de uso clásico:** el liderazgo evalúa P1-C1 como L3, pero el survey revela que el 60% de los devs lo usa raramente: gap de adopción real, no de licencia.

## 🔐 Sobre el anonimato

- Microsoft Forms tiene la opción "Anonymous responses": **MARCARLA es obligatorio** para este survey
- Sin eso, Forms captura el email de la cuenta MS365 del respondente (rompe el anonimato)
- La skill `/import-developer-survey` valida que las columnas Email/Name estén vacías y alerta si no lo están
- Las quotes en el reporte se citan por **ID de la pregunta** (ej.: "Respuesta S9-Q1"), nunca por respondent_id o cargo

## 📅 Cadencia sugerida

- **Primera vez:** antes de definir la estrategia de IA en ingeniería (baseline)
- **Después del rollout** de Copilot Enterprise: 30 días después
- **Trimestralmente:** para medir evolución
- **Después de workshops/capacitaciones:** para validar absorción

## 📚 Documentación relacionada

### Otras carpetas del kit
- **Survey complementario (identificado, capacitación):** [`../survey-learning/`](../survey-learning/), el Learning & Growth Survey (32 p, 5-8 min, IDENTIFICADO). Genera un plan de capacitación personalizado con Champions Network y calendario de workshops. Úsalo DESPUÉS de este Developer Survey para pasar de "comportamiento medido" a "plan de acción"
- **Assessment principal (organizacional):** [`../README.es.md`](../README.es.md), 158 preguntas Likert L0-L4, liderado por el liderazgo, genera 5 PDFs production
- **Recolección multi-respondente del assessment principal:** [`../coleta/INSTRUCOES-FORMS.es.md`](../coleta/INSTRUCOES-FORMS.es.md)
- **Wizard que consolida en el PDF ejecutivo:** [`../wizard/`](../wizard/), alimenta la Parte 4 del PDF con datos de este survey + del learning survey

### Skills de este survey
- Skill que importa Excel → JSON: [`../.github/skills/import-developer-survey/SKILL.md`](../.github/skills/import-developer-survey/SKILL.md)
- Skill que genera el reporte + madurez: [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)

### Cómo se conectan los 3 surveys (orden de ejecución recomendado)

```
1. Survey-devs (anónimo, ESTE)      → mide comportamiento real + madurez calculada
2. Survey-learning (identificado)   → mide deseo + barreras + Champions
3. Assessment principal             → el liderazgo evalúa INFORMADO por los 2 anteriores
4. /implementation-wizard            → consolida todo
5. /generate-reports                 → 5 PDFs production-quality
```

## 🔗 Fuentes oficiales validadas (v2.0, 2026-05-08)

Toda la terminología y los conceptos del survey fueron cruzados con documentación oficial. Usa estas fuentes para responder dudas de devs sobre qué significa cada término:

### GitHub Copilot
- **Copilot Spaces** (GA sep/2025): <https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context/>
- **Docs oficiales de Spaces**: <https://docs.github.com/en/copilot/concepts/context/spaces>
- **Knowledge Bases sunset → Spaces** (nov/2025): <https://github.blog/changelog/2025-10-17-copilot-knowledge-bases-can-now-be-converted-to-copilot-spaces/>
- **Copilot Coding Agent** (sucesor de Workspace, GA sep/2025): toma un issue, abre un PR por sí solo

### Microsoft Foundry (ex-Azure AI Foundry)
- **Foundry Agent Service overview**: <https://learn.microsoft.com/en-us/azure/foundry/agents/overview>
- **What's new mar/2026** (MCP, A2A, multi-agent): <https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/>
- **Connectors (1,400+ sistemas de negocio)**: <https://learn.microsoft.com/en-us/connectors/azureagentservice/>

### Agentic DevOps (terminología Microsoft)
- **DevOps Playbook for the Agentic Era**: <https://devblogs.microsoft.com/all-things-azure/agentic-devops-practices-principles-strategic-direction/>
- **Reimagining the developer lifecycle**: <https://developer.microsoft.com/blog/reimagining-every-phase-of-the-developer-lifecycle>
- **Personas (System Designer, Agent Operator)**: <https://learn.microsoft.com/en-us/azure/well-architected/ai/personas>
- **Microsoft Reactor: Agentic DevOps Live**: <https://developer.microsoft.com/en-us/reactor/series/s-1625/>
- **Azure Agentic DevOps Solutions**: <https://azure.microsoft.com/en-us/solutions/devops>

### Spec-Driven Development
- **GitHub Spec Kit**: <https://github.com/github/spec-kit>

### Aplicabilidad al assessment principal
- El assessment de madurez en la carpeta madre usa las 7 estrategias S1-S7 (GitHub Migration, Foundry+SRE, App Modernization, AI Apps, Copilot Acceleration, Agentic Activation, Security & Governance), alineadas con el framework **Agentic DevOps** de Microsoft.
- Los 8 profiles (full-stack, backend-api, platform-eng, security-ops, frontend, data-ml, devops-sre, legacy) cubren las personas de Agentic DevOps.
