# Cómo crear el Microsoft Forms para el AI Maturity Assessment

**`🅰️ ASSESSMENT`** · 📖 [🏠 Índice](../README.es.md) · [« Guía paso a paso](../GUIA-PASSO-A-PASSO.md) · Estás aquí · [» Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.md)

> [!TIP]
> Esta guía muestra **3 caminos** para crear y usar Microsoft Forms con las 158 preguntas. Elige el que mejor se ajuste al tiempo disponible y al perfil técnico del equipo.

---

## ⚖️ Comparación rápida de los 3 caminos

| Camino | Tiempo de setup | Esfuerzo | Cuándo usarlo |
|---|---|---|---|
| **A. Forms manual completo** | 4-6 horas | Alto (crear 158 preguntas) | Quieres una experiencia Forms 100% nativa, con secciones y branding |
| **B. Forms reducido (1 capability piloto)** | 30 minutos | Bajo | PoC o validación con pocos respondientes antes de escalar |
| **C. Directo en Excel/SharePoint** ⭐ | 5 minutos | Mínimo | **Recomendado**: usa el template Excel que ya viene en el kit, evita 4h de creación |

---

## 🅰️ Camino A: Forms manual completo (158 preguntas)

### Paso 1 · Crear el Forms

1. Ve a https://forms.office.com (inicia sesión con tu cuenta Microsoft 365)
2. Haz clic en **+ New Form**
3. Título: `AI Maturity Assessment - <Nombre de tu organización>`
4. Subtítulo (opcional):
   ```
   Evaluación de madurez de IA en 3 pilares: Productividad, DevOps y Plataforma.
   158 preguntas con escala L0-L4. Tiempo estimado: 45-90 minutos.
   Tus respuestas son confidenciales y se usan solo para generar el roadmap.
   ```

### Paso 2 · Configurar 3 secciones

Agrega 3 secciones (botón **+ Add new** → ícono de sección):

| Sección | Título | Subtítulo sugerido |
|---|---|---|
| 1 | **Pilar P1: Productividad del Desarrollador** | 53 preguntas en 9 capabilities |
| 2 | **Pilar P2: Ciclo de Vida DevOps** | 59 preguntas en 10 capabilities |
| 3 | **Pilar P3: Plataforma de Aplicaciones** | 46 preguntas en 9 capabilities |

### Paso 3 · Agregar las 158 preguntas

Para cada pregunta, agrega **2 elementos** en Forms:

1. **Choice (single answer)** con la pregunta + las 6 opciones de nivel
2. **Long Text** (opcional) para evidencia

Usa el documento [`perguntas-para-forms.es.md`](perguntas-para-forms.es.md) como fuente de copy/paste. Tiene las 158 preguntas formateadas con IDs (`P1-C1-Q1`, etc.) y el texto completo.

#### Opciones fijas para TODAS las preguntas (pégalas idénticas)

```
L0 — Inicial — Sin práctica establecida
L1 — En Desarrollo — Pilotos aislados (<25%)
L2 — Definido — Cobertura 25-50% con directrices
L3 — Gestionado — >75% con métricas de impacto
L4 — Optimizando — Universal (>95%) con automatización continua
NA — No sé / No aplica
```

> ⚠️ **CRÍTICO:** el prefijo `L0`, `L1`, ..., `L4`, `NA` debe estar **literalmente al inicio** de cada opción. La skill de importación usa ese prefijo para mapear de vuelta al número (0-4 o null). No lo traduzcas, no lo reformatees.

#### Formato del título de cada pregunta

```
P1-C1-Q1: <texto de la pregunta>
```

> ⚠️ **IMPORTANTE:** el ID (`P1-C1-Q1`) debe estar **literalmente al inicio** del título de la pregunta, seguido de `:`. Ejemplo de [`perguntas-para-forms.es.md`](perguntas-para-forms.es.md):
>
> `P1-C1-Q1: Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?`

#### Formato del campo de evidencia

```
Evidencia (P1-C1-Q1)
```

Tipo: **Long Text**, opcional (no lo marques como required).

### Paso 4 · Configurar permisos

1. Botón **Settings** (engranaje) en la esquina superior derecha
2. **Who can fill out this form**:
   - **Only people in my organization**: recomendado si es de uso interno
   - **Anyone with the link**: si es entre empresas (consultoría)
3. **One response per person**: deshabilitado (queremos múltiples respuestas para agregar)
4. **Email notification of each response**: opcional

### Paso 5 · Compartir

1. Botón **Send/Collect responses**
2. Copiar el link
3. Compartirlo vía Email/Teams/SharePoint con el equipo

### Paso 6 · Exportar respuestas

Cuando tengas suficientes respuestas (recomendado: 3 o más respondientes para reducir sesgo):

1. Pestaña **Responses**
2. Botón **Open in Excel**
3. Guardar el archivo como **`respostas-forms.xlsx`**
4. Moverlo a la raíz de `kit-cliente/`

### Paso 7 · Importar en el kit

En VS Code, abre Copilot Chat (modo **Agent**) y escribe:

```
/import-assessment-responses
```

La skill:
- Detecta el `respostas-forms.xlsx` automáticamente
- Hace backup del `respostas.json` actual
- Agrega múltiples respondientes vía media por pregunta
- Sobrescribe `respostas.json`
- Genera `saida/import-log-<DATE>.md`

Después ejecuta `/run-full-pipeline` normalmente.

---

## 🅱️ Camino B: Forms reducido (1 capability piloto)

Para **validar el flujo end-to-end** antes de invertir en la creación completa.

### Paso 1 · Elegir 1 capability

Elige 1 capability con 5-7 preguntas. Sugerencia: **P1-C1 (Asistentes de Codificación IA)**, el tema más "caliente" y el que generará buena discusión en el equipo.

### Paso 2 · Crear el Forms solo con esas 5 preguntas

El mismo proceso del Camino A, pero con solo **5 preguntas** en vez de 158. Tiempo: 15-30 min.

### Paso 3 · Recolectar 3-5 respuestas

Compártelo con tu equipo inmediato (no con toda la empresa). Tiempo: 1-2 días.

### Paso 4 · Importar y ejecutar

Como el `respostas.json` tendrá solo 5 preguntas respondidas, el **threshold quedará en BLOCKED** (se necesitan 25 o más). Pero:
- Validas que el flujo Forms → Excel → respostas.json funciona
- Ves cómo aparece en el reporte una capability con datos reales

Para generar un reporte útil, completa manualmente el resto vía `respostas.json` o expande el Forms.

---

## 🅲 Camino C: directo en Excel/SharePoint ⭐ (RECOMENDADO)

Se salta el Forms y usa el **template Excel** que ya viene en el kit.

### Paso 1 · Tomar el template

El kit viene con [`coleta/template-export-forms.xlsx`](template-export-forms.xlsx). Ese archivo:
- Tiene el **mismo formato** que exportaría el Forms
- Ya tiene las 158 columnas de pregunta + 158 de evidencia
- Viene con **3 respondientes mockeados** como ejemplo (puedes borrarlos y reemplazarlos)

### Paso 2 · Subirlo a SharePoint/OneDrive

1. Limpiar las 3 filas de respondientes mockeados (filas 2, 3, 4), manteniendo solo el header
2. Renombrarlo: `respostas-forms.xlsx` (u otro nombre)
3. **SharePoint:** subirlo a la library del proyecto y generar un link "Anyone with the link can edit"
4. **OneDrive:** subirlo y compartirlo con permiso de edición
5. **Teams:** adjuntarlo en el canal y fijarlo

### Paso 3 · Cada respondiente llena una fila

Comparte estas instrucciones:

```
¡Hola equipo!

Por favor llenen UNA fila por persona en este archivo:
<link de SharePoint>

Para cada una de las 158 columnas de pregunta:
- Selecciona un nivel L0-L4 (o déjalo en blanco si "no sabes")
- El texto debe comenzar con el código (ej.: "L3 — Gestionado")
- Usa la columna de Evidencia justo a la derecha para describir herramienta/cobertura/métrica

Tiempo estimado: 45-90 min. Puedes pausar y volver.

¿Dudas? Consulten los documentos en referencia/P*.md (en kit-cliente).
```

### Paso 4 · Descargar el Excel

Cuando todos hayan llenado:
1. SharePoint → archivo → **Download a Copy**
2. Renombrarlo a **`respostas-forms.xlsx`**
3. Moverlo a la raíz de `kit-cliente/`

### Paso 5 · Importar y ejecutar

```
/import-assessment-responses
/run-full-pipeline
```

---

## 🆚 Forms vs Excel directo: ¿cuál elegir?

| Criterio | Microsoft Forms | Excel/SharePoint |
|---|---|---|
| **Tiempo de setup** | 4-6h (crear 158 preguntas) | 5 min (template listo) |
| **UX para el respondiente** | Mobile-friendly, 1 pregunta a la vez | Hoja de cálculo (intimidante para no técnicos) |
| **Validación de datos** | Fija (Choice = solo 6 opciones) | Frágil (la persona puede escribir cualquier cosa) |
| **Multi-respondiente** | Nativo | Manual (1 fila por persona) |
| **Edición posterior** | Difícil (cada submit es final) | Fácil (cualquiera puede cambiar en cualquier momento) |
| **Audit trail** | Nativo (timestamp por submit) | SharePoint version history |
| **Costo de licencia** | Microsoft 365 estándar | Microsoft 365 estándar |
| **Integración con el kit** | Idéntica (`/import-assessment-responses`) | Idéntica |

**Recomendación práctica:**
- **PoC / Equipo pequeño (3-5 personas):** Excel directo (Camino C)
- **Roll-out a la organización (10+ respondientes):** Forms (Camino A)
- **Cliente exigente / branding profesional:** Forms (Camino A)

---

## 🔄 Otros formatos soportados por la skill

La skill `/import-assessment-responses` acepta cualquier Excel/CSV cuyo header de pregunta comience con `P[1-3]-C\d+-Q\d+:`. Eso incluye:

- ✅ **Microsoft Forms** export (formato oficial)
- ✅ **Google Forms** export (Sheets → Download as .xlsx)
- ✅ **Excel/SharePoint** custom (template del kit o el tuyo propio)
- ✅ **CSV** (si lo renombras a .xlsx o lo conviertes)
- ⚠️ **Typeform**: funciona si ajustas los headers para que tengan los IDs

---

## 💡 Consejos prácticos

### Consejo 1 · Comienza con 1 pilar
No intentes recolectar respuestas de los 3 pilares al mismo tiempo. Comienza por P1 (Productividad), que es el más tangible para devs. Después P2 (DevOps) con SREs. Después P3 (Plataforma) con arquitectos.

### Consejo 2 · Pre-llenado por entrevista
En vez de mandar el link y esperar, haz una **entrevista de 1h por respondiente** llenando juntos. Capturas mejor los matices y generas evidencias más ricas.

### Consejo 3 · Entrena antes de soltarlo
Haz un **kick-off de 30 min** explicando:
- Qué es el assessment
- Cómo se definen los niveles L0-L4
- Por qué importa la evidencia
- Cuánto tiempo va a tomar
- Cuándo recibirán el reporte

### Consejo 4 · Ejecuta ciclos cortos
No esperes al 100% de respuestas para ejecutar `/run-full-pipeline`. Ejecútalo con 25 (WARNING), después 50 (OK), después 100. En cada ciclo el reporte mejora y capturas más conversaciones.

### Consejo 5 · Versionado
Cada vez que importas, la skill crea `respostas.json.backup-<timestamp>`. Guarda esos backups: son tu **historial de evolución** entre rondas del assessment.

---

## 🆘 Troubleshooting

| Problema | Diagnóstico | Solución |
|---|---|---|
| La skill no detecta `respostas-forms.xlsx` | El archivo no está en la raíz | Moverlo a `kit-cliente/respostas-forms.xlsx` (no dentro de coleta/) |
| "Ningún header reconocido" | Los headers del Excel no comienzan con `P1-C1-Q1:` etc. | Editar los headers manualmente para incluir los IDs al inicio |
| Un respondiente apareció duplicado | Forms permite múltiples envíos de la misma persona | Editar el Excel manualmente para borrar la fila duplicada antes de importar |
| Los levels quedaron como texto libre | Forms exportó la opción SIN el prefijo `L0/L1/...` | Reconstruir el Forms incluyendo los prefijos al inicio de cada Choice option |
| El Excel tiene 158 columnas pero solo 90 preguntas reconocidas | Headers truncados por Forms (límite de 4000 chars) | Acortar el texto de las preguntas en Forms (mantener solo el ID + frase resumida) |

---

## 📚 Referencias

- **Lista completa de las 158 preguntas formateadas para Forms:** [`perguntas-para-forms.es.md`](perguntas-para-forms.es.md)
- **Template Excel listo (3 respondientes mockeados):** [`template-export-forms.xlsx`](template-export-forms.xlsx)
- **Skill de importación:** [`../.github/skills/import-assessment-responses/SKILL.md`](../.github/skills/import-assessment-responses/SKILL.md)
- **Algoritmo de agregación multi-respondiente:** [`../referencia/pontuacao-e-calculo.md`](../referencia/pontuacao-e-calculo.md) sección 6

---

**Versión:** 1.0 · **Fecha:** 2026-05-08

---

## ¿Te trabaste en alguno de estos pasos?

<details>
<summary><strong>FAQ: dudas comunes en la recolección vía Forms</strong></summary>

| Síntoma | Causa probable | Cómo resolverlo |
|---|---|---|
| **Open in Excel** está deshabilitado en Forms | Tu cuenta no tiene licencia M365 / Forms está en una cuenta personal | Pide a un admin mover el Forms a la cuenta organizacional |
| Tengo múltiples respondientes, ¿cómo los agrego? | Comportamiento por defecto de la skill | `/import-assessment-responses` hace **media automática** por pregunta |
| Los headers de las columnas no comienzan con `P1-C1-Q1:` | No seguiste el patrón al crear el Forms | Edita los títulos de las preguntas en Forms para incluir el ID al comienzo |
| Compartir el Forms con gente de fuera de la org | Los Settings del Forms restringen el acceso | Settings → **Anyone with the link can respond** |
| El Excel llega con columnas extras (ID, Start time, ...) | Comportamiento por defecto del Forms | La skill ignora las columnas A-E automáticamente |
| `respostas-forms.xlsx` no es detectado | El archivo está dentro de `coleta/` en vez de la raíz | Muévelo a la **raíz** del kit |

</details>

---

## Continuar la lectura

| ← ANTERIOR | SIGUIENTE → |
|:---|---:|
| **[Guía paso a paso](../GUIA-PASSO-A-PASSO.md)** | **[Developer Survey (anónimo)](../survey-devs/INSTRUCOES-FORMS-DEVS.md)** |
| De cero al PDF ejecutivo en 60-90 min. | 75 preguntas anónimas sobre Copilot, agentes, gobernanza, MCP / A2A. |

↑ [Volver al índice del kit](../README.es.md)
