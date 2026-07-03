# Cómo crear el Microsoft Forms para el Developer Survey

**`🅱️ SURVEY-DEVS`** · _anónimo_ · 📖 [🏠 Índice](../README.es.md) · [« Recolección principal](../coleta/INSTRUCOES-FORMS.es.md) · Estás aquí · [» Learning Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md)

> [!IMPORTANT]
> Survey **anónimo** de **75 preguntas** en 9 secciones para entender cómo los desarrolladores de tu organización usan GitHub Copilot, los modos de Copilot Chat (Ask/Edit/Agent/**Coding Agent**), **Copilot Spaces**, **Microsoft Foundry**, agentes IA + **MCP / A2A**, instructions files, prácticas (TDD/SDD con Spec Kit), **personas Agentic DevOps** (System Designer / Agent Operator), gobernanza y seguridad (incl. **JIT permissions** y **alcance+red-lines de agents**). Tiempo estimado por respondente: **22-28 min**.

**Versión 2.0 (2026-05-08)**: términos actualizados con los docs oficiales más recientes de Microsoft/GitHub.

**Diferente del assessment principal** (Likert L0-L4 organizacional). Este es **conductual e individual**: cuantos más devs respondan, más rica la foto.

---

## 🎯 Cuándo usar este survey

- ✅ Antes de definir la estrategia de adopción de IA en ingeniería
- ✅ Después del rollout de GitHub Copilot, para medir la adopción real
- ✅ Como input para el `/implementation-wizard` (Implementation Guide del assessment principal)
- ✅ Trimestralmente, para acompañar la evolución cultural
- ✅ Antes de workshops de Copilot/IA, para identificar gaps

---

## 🔐 Anonimato: CRÍTICO

Este survey es **anónimo por diseño**:
- ❌ No pedimos nombre, email ni ID corporativo
- ✅ Recolectamos solo: cargo, años de experiencia, patrones de uso, opiniones
- ✅ Los devs responden con más honestidad cuando saben que es anónimo
- ⚠️ En Microsoft Forms, **MARCAR "Anonymous responses"** en Settings (sin eso, captura el email de la cuenta MS365)

---

## 📋 Los 9 temas cubiertos (v2.0)

| # | Sección | Foco | Preguntas |
|---|---|---|---|
| **S1** | Perfil del respondente | Cargo, experiencia, stack, modelo de trabajo | 7 |
| **S2** | GitHub Copilot: Adopción y Modos | Licencia, frecuencia, **Ask / Edit / Agent / Coding Agent (autónomo)**, features (incl. **Spaces**), ganancia | 9 |
| **S3** | Otras herramientas Microsoft / GitHub AI | **Microsoft Foundry** (ex-Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, **Spec Kit**, **MCP** | 7 |
| **S4** | Prácticas de Desarrollo con IA | **TDD con IA**, **SDD con Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Conceptos y Estructura de Agentes | Agente vs asistente, modos de Copilot, **custom agents/skills/prompts**, **A2A**, handoffs, subagentes, **personas Agentic DevOps** (System Designer / Agent Operator), **PROBAR agents antes de usarlos** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions en **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usabilidad y Best Practices | Cómo aprendió (incl. MS Build / GitHub Universe), Champion, métricas DORA/DX, iteraciones, confianza | 9 |
| **S8** | Seguridad y Gobernanza | Política de IA, datos sensibles, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **alcance+red-lines de agents**, **JIT permissions**, capacitación | 13 |
| **S9** | Pain Points & Wishlist | Frustraciones, ideas, feature requests | 4 |
| | | **TOTAL** | **75** |

---

## 🛠️ Cómo crear el Forms (paso a paso)

### Paso 1 · Crear el formulario

1. Accede a <https://forms.office.com>
2. Haz clic en **+ New Form**
3. Título sugerido: `Developer Survey: Cómo mi equipo usa GitHub e IA hoy`
4. Subtítulo (pega esto):

```
Survey ANÓNIMO (20-25 min) sobre tus prácticas con GitHub Copilot,
modos de Copilot Chat (Ask/Edit/Agent), agentes IA, instructions files,
mejores prácticas de IA + Dev y seguridad.

Tus respuestas alimentarán el roadmap de adopción de IA en el equipo.
NO pedimos nombre ni email, solo cargo, años de experiencia y patrones.

Tiempo estimado: 20-25 min.
```

### Paso 2 · ⚠️ CONFIGURAR EL ANONIMATO

**Settings (engranaje ⚙️ en la esquina superior derecha):**

| Setting | Valor |
|---|---|
| **Anonymous responses** | ☑ **MARCADO** (CRÍTICO: sin esto captura el email!) |
| **Who can respond** | "Anyone with the link" (si es cross-org) o "Only people in my organization" |
| **One response per person** | ☐ DESMARCADO (queremos múltiples) |
| **Accept responses** | ☑ MARCADO |
| **Email notification** | ☑ MARCADO (opcional: te avisa con cada respuesta) |
| **Customize thank you message** | "¡Gracias! Tus respuestas se están agregando con las del equipo." |

> 🔍 **Cómo confirmar el anonimato:** después de crearlo, abre el link en una ventana de incógnito. Si NO aparece "Logged in as [tu email]" arriba, es anónimo.

### Paso 3 · Crear 9 secciones

En Forms, botón **+ Add new** → ícono de sección (o "Add section"):

```
Section 1: S1 — Perfil del respondente           (7 preguntas)
Section 2: S2 — GitHub Copilot                   (9 preguntas)
Section 3: S3 — Otras herramientas Microsoft/GH  (7 preguntas)
Section 4: S4 — Prácticas de Desarrollo         (9 preguntas)
Section 5: S5 — Conceptos de Agentes             (11 preguntas)
Section 6: S6 — Markdown / Instructions          (6 preguntas)
Section 7: S7 — Usabilidad                       (9 preguntas)
Section 8: S8 — Seguridad y Gobernanza          (13 preguntas)
Section 9: S9 — Pain Points & Wishlist           (4 preguntas)
```

### Paso 4 · Agregar las 75 preguntas

Usa el documento [`perguntas-para-forms-devs.es.md`](perguntas-para-forms-devs.es.md) como **fuente de copy/paste**. Cada pregunta tiene:
- **Tipo** (`choice`, `multi`, `text`)
- **ID** (`S2-Q1`, `S5-Q3`, etc.)
- **Texto de la pregunta**
- **Opciones** (para choice/multi)

**Para cada pregunta en Forms:**

1. Tipo:
   - `choice` (Single answer) → **Choice** con "Multiple answers" DESMARCADO
   - `multi` (Multiple answers) → **Choice** con "Multiple answers" MARCADO
   - `text` (Long Text) → **Long answer**

2. **El TÍTULO de la pregunta DEBE comenzar con el ID + dos puntos**:
   ```
   S2-Q1: Tienes una licencia activa de GitHub Copilot?
   ```
   > ⚠️ **CRÍTICO:** el ID es usado por la skill `/import-developer-survey` para mapear de vuelta al schema. No remuevas ni alteres el formato `SX-QY:`.

3. **Opciones** (para choice/multi): pega las opciones listadas en el MD, **una por línea**, en orden.

4. **Required**: marca como required solo las 7 preguntas de Perfil (S1-Q1 a S1-Q7). Las demás opcionales (los devs pueden saltarlas).

### Paso 5 · Compartir

1. Botón **+ Send / Collect responses** arriba
2. Elegir **Link** (no Email, que rompe el anonimato)
3. Copiar la URL
4. Compartir vía:
   - **Slack/Teams:** canal #engineering o #copilot-users
   - **Email a todos los devs:** "Survey anónimo de 20 min, tu opinión cuenta"
   - **All-hands:** proyectar el código QR de la URL para que los devs lo escaneen
5. **Deadline sugerido:** 2 semanas. Recordar 1× por semana.

### Paso 6 · Acompañar las respuestas

- La pestaña **Responses** muestra el conteo en tiempo real
- Recomendado: **mínimo 5 respondentes**, ideal **15+** para insights ricos
- Si hay baja adhesión: 1-on-1 con los líderes para incentivar

### Paso 7 · Exportar cuando tengas respuestas suficientes

1. Pestaña **Responses** → botón **Open in Excel**
2. Guarda el archivo como **`respostas-survey-devs.xlsx`**
3. Muévelo a la **raíz del `kit-cliente/`** (no dentro de `survey-devs/`)
4. **Anonimato confirmado:** las columnas D (Email) y E (Name) deben estar vacías

### Paso 8 · Analizar con el kit

En Copilot Chat (modo Agent):

```
/import-developer-survey
```

La skill:
- Detecta `respostas-survey-devs.xlsx`
- Parsea 75 preguntas × N respondentes
- Genera `survey-devs/respostas-devs.json`
- Genera `saida/import-survey-log-<DATE>.md`

Después:

```
/insights-developer-survey
```

Genera el reporte agregado en `saida/insights-developer-survey-<DATE>.md` con:
- Distribución de cargos
- Top 5 features más usadas de Copilot
- % de adopción por modo (Ask/Edit/Agent/Workspace)
- Conocimiento de conceptos (agentes, MCP, handoffs)
- Madurez de instructions files
- Gaps de gobernanza y seguridad
- Citas de pain points (anonimizadas)
- Recomendaciones priorizadas para el roadmap

---

## 🅱️ Camino alternativo: Excel/SharePoint directo (sin Forms)

Más rápido si el equipo es pequeño (3-5 devs) y técnico.

1. Abre `survey-devs/template-export-forms-devs.xlsx`
2. Borra las 5 filas de respondentes mockeados (filas 2-6), manteniendo la fila 1 (headers)
3. Guarda como `respostas-survey-devs.xlsx` y súbelo a SharePoint con link "Anyone can edit"
4. Cada dev llena **una fila** con sus respuestas (texto libre en las celdas de respuesta)
5. Cuando todos hayan llenado: descarga → mueve a la raíz del kit → `/import-developer-survey`

**Trade-off:** menos visual que Forms, pero cero setup. Adecuado para equipos técnicos.

---

## 💡 Buenas prácticas de la recolección

### Lanza con contexto
No tires el link en Slack sin contexto. Crea el momento:

> "Equipo, antes de definir la estrategia de IA en ingeniería para el próximo trimestre, queremos escuchar cómo usan IA hoy. Survey anónimo de 20-25 min con 75 preguntas (Copilot, agentes, seguridad…). Sus respuestas van directamente al roadmap. Link: <URL>. Deadline: 2 semanas."

### Garantiza el anonimato (de verdad)
- Confirma que Settings → Anonymous está MARCADO
- No fuerces login MS365 (en caso de compartir externamente)
- En el reporte agregado nunca cites respondentes específicos, solo patrones

### Recuerda periódicamente
- D+3: recordatorio suave en el canal
- D+7: recap "X respuestas hasta ahora, faltan Y días"
- D+10: 1-on-1 con los líderes para empujar
- D+14: deadline final + comienza el análisis

### Comparte los insights
Los devs responden más un próximo survey si ven que el anterior generó acción. Después de `/insights-developer-survey`:
- Preséntalo en el all-hands
- Genera quick wins (workshop, prompt library, etc.)
- Repite trimestralmente para medir la evolución

---

## 🆘 Troubleshooting

| Problema | Diagnóstico | Solución |
|---|---|---|
| La skill no detecta el archivo | No está en la raíz | Mover `respostas-survey-devs.xlsx` a `kit-cliente/` (raíz) |
| La skill dice "0 respondentes" | Email/Name no vacíos pero preguntas vacías | Verificar que los respondentes llenaron al menos 1 pregunta |
| Headers no reconocidos | Falta "SX-QY:" al inicio | Editar los headers manualmente para incluir el ID |
| Aparece email en el Excel | Anonimato OFF | Reconfigurar Forms → Settings → Anonymous Responses ON y re-enviar |
| Poca adhesión (< 5 respuestas) | Lanzamiento sin contexto | Re-lanzar con mensaje del líder, deadline, propósito |

---

## 📚 Referencias

- **Las 75 preguntas formateadas:** [`perguntas-para-forms-devs.es.md`](perguntas-para-forms-devs.es.md)
- **Template Excel listo (5 mocks):** [`template-export-forms-devs.xlsx`](template-export-forms-devs.xlsx)
- **JSON estructurado de ejemplo:** [`respostas-mock-devs.json`](respostas-mock-devs.json)
- **Skill de import:** [`../.github/skills/import-developer-survey/SKILL.md`](../.github/skills/import-developer-survey/SKILL.md)
- **Skill de insights:** [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)
- **Relación con el assessment principal:** este survey COMPLEMENTA el assessment de madurez. Los insights de aquí informan las preguntas P1-C1, P1-C5, P1-C8 (Copilot, Onboarding, Métricas) y la gobernanza en P2-C4 / P3-C6.

---

**Versión:** 1.0 · **Fecha:** 2026-05-08

---

## ¿Te trabaste en alguno de estos pasos?

<details>
<summary><strong>FAQ: dudas comunes en el Developer Survey (anónimo)</strong></summary>

| Síntoma | Causa probable | Cómo resolver |
|---|---|---|
| El Excel exportado tiene **Email** y **Name** llenos | **Anonymous responses** NO fue marcado en Forms | Settings del Forms → ✅ **Anonymous responses** → recolectar de nuevo |
| Los devs se quejan de que es demasiado largo (20-25 min) | Muchas preguntas marcadas como required | Marca required **solo en S1** (perfil); las demás opcionales |
| Tengo menos de 5 respondentes | Los insights se vuelven poco confiables | Mínimo absoluto: 3. Ideal: 5+. Óptimo: 15+, extiende la campaña 1 semana |
| La skill calcula la madurez pero el número parece bajo | Rúbrica determinística L0-L4, refleja la realidad | Ver [`RUBRICA-MATURIDADE.es.md`](RUBRICA-MATURIDADE.es.md) para entender la escala |
| Quiero saltarme este survey | Está bien, es opcional | Salta directo al Learning Survey o ejecuta solo el Assessment principal |

</details>

---

## Continuar la lectura

| ← ANTERIOR | SIGUIENTE → |
|:---|---:|
| **[Recolección del assessment principal](../coleta/INSTRUCOES-FORMS.es.md)** | **[Learning & Growth Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md)** |
| 3 caminos para recolectar las 158 preguntas del assessment vía Forms / Excel. | 32 preguntas identificadas: plan de capacitación con Champions y workshops. |

↑ [Volver al Índice del kit](../README.es.md)
