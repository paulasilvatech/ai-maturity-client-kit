# Puntuación y Cálculo del Assessment de Madurez IA

> **Documento técnico de referencia**: describe con precisión cómo cada respuesta se convierte en score, cómo se agregan capabilities/pillars/overall, reglas de threshold, multi-respondiente, gap analysis y PE score. Todas las fórmulas coinciden 1:1 con el código Rust en `app/backend/src/scoring.rs` (archivo del repositorio de la plataforma, no incluido en este kit).
>
> **Implementaciones ejecutables en este kit:** [`scripts/compute_scores.py`](../scripts/compute_scores.py), [`scripts/compute_gaps.py`](../scripts/compute_gaps.py) y [`scripts/recommend_strategies.py`](../scripts/recommend_strategies.py) implementan exactamente estas fórmulas de forma determinística. La planilla auditable `pontuacao-e-calculo.xlsx` es generada por [`scripts/generate_scoring_workbook.py`](../scripts/generate_scoring_workbook.py). Los pesos reales de preguntas y capabilities vienen de [`framework.json`](../framework.json), la fuente única de la verdad.

**Versión del algoritmo:** 1.0.0 · **Última auditoría del código:** 2026-05-08

---

## Índice

1. [Modelo conceptual en 3 capas](#1-modelo-conceptual-en-3-capas)
2. [Cómo cada respuesta se convierte en número](#2-cómo-cada-respuesta-se-convierte-en-número)
3. [Fórmulas oficiales](#3-fórmulas-oficiales)
4. [Tratamiento de respuestas faltantes](#4-tratamiento-de-respuestas-faltantes)
5. [Umbral de cobertura mínima](#5-umbral-de-cobertura-mínima)
6. [Agregación multi-respondiente](#6-agregación-multi-respondiente)
7. [Etiquetas de madurez (mapeo de score)](#7-etiquetas-de-madurez-mapeo-de-score)
8. [Gap analysis y priorización](#8-gap-analysis-y-priorización)
9. [PE Score (Production Engineering Readiness)](#9-pe-score-production-engineering-readiness)
10. [Persistencia (tablas y materialización)](#10-persistencia-tablas-y-materialización)
11. [**Ejemplo end-to-end: Pilar P1**](#11-ejemplo-end-to-end-pilar-p1)
12. [**Ejemplo end-to-end: Pilar P2**](#12-ejemplo-end-to-end-pilar-p2)
13. [**Ejemplo end-to-end: Pilar P3**](#13-ejemplo-end-to-end-pilar-p3)
14. [Edge cases y garantías](#14-edge-cases-y-garantías)
15. [Glosario](#15-glosario)

---

## 1. Modelo conceptual en 3 capas

```
┌─────────────────────────────────────────────────────────────┐
│                    OVERALL SCORE (0–4)                      │
│  = promedio ponderado de TODAS las capabilities (no pillars)│
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                  PILLAR SCORE (P1, P2, P3)                  │
│      = promedio ponderado de las capabilities del pillar    │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                CAPABILITY SCORE (P1-C1 … P3-C9)             │
│       = promedio ponderado de las preguntas de la capability│
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│              QUESTION RESPONSE (L0=0 … L4=4)                │
│     = nivel seleccionado por el respondiente (multi → prom.)│
└─────────────────────────────────────────────────────────────┘
```

**Característica importante:** el **overall** se calcula directamente sobre las capabilities (SUMPRODUCT), **no** es el promedio de los 3 pillar scores. Esto evita que un pilar con pocas capabilities pese igual que uno con muchas.

---

## 2. Cómo cada respuesta se convierte en número

| Nivel seleccionado | Etiqueta | Valor numérico |
|---|---|---|
| L0 | Inicial | **0** |
| L1 | En Desarrollo | **1** |
| L2 | Definido | **2** |
| L3 | Gestionado | **3** |
| L4 | Optimizando | **4** |

La escala es **discreta en la entrada (entero 0–4)** pero las agregaciones producen valores **continuos en punto flotante (`f64`)**, sin redondeo. Solo la presentación (UI/informe) decide la precisión visual (generalmente 2 decimales).

---

## 3. Fórmulas oficiales

### 3.1 Capability score
> Código de referencia: `scoring.rs:205-225` (repositorio de la plataforma)

$$
\text{capability\_score} = \frac{\sum_{q \in \text{respondidas}} (\text{nivel}_q \times \text{peso}_q)}{\sum_{q \in \text{respondidas}} \text{peso}_q}
$$

- Si ninguna pregunta de la capability fue respondida → `capability_score = None` (no entra en los cálculos superiores).
- Pesos default: **1.0**. Rango permitido: **[0.5, 2.0]**.

### 3.2 Pillar score
> Código de referencia: `scoring.rs:227-247` (repositorio de la plataforma)

$$
\text{pillar\_score} = \frac{\sum_{c \in \text{pillar}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{pillar}} \text{peso}_c}
$$

Solo participan las capabilities con `score = Some(_)` (las capabilities sin ninguna respuesta se omiten).

### 3.3 Overall score
> Código de referencia: `scoring.rs:250-263` (repositorio de la plataforma)

$$
\text{overall\_score} = \frac{\sum_{c \in \text{TODAS las capabilities}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{TODAS las capabilities}} \text{peso}_c}
$$

**Atención:** SUMPRODUCT directo sobre todas las capabilities, **no** es `mean(P1, P2, P3)`.

---

## 4. Tratamiento de respuestas faltantes

| Situación | Comportamiento |
|---|---|
| Pregunta no respondida | **Ignorada**. No suma en `wsum` ni en `wtotal`. Sin penalización. |
| Capability sin ninguna respuesta | `score = None`. No entra en el pillar ni en el overall. |
| Pillar sin capabilities respondidas | `pillar_score = 0.0` (caso de borde raro). |
| Overall sin capabilities respondidas | `overall_score = 0.0`. |

> **Regla de oro:** "las respondidas pesan, las faltantes desaparecen". Esto incentiva al respondiente a *no adivinar* cuando no sabe: el sistema solo penaliza vía `threshold_status`, no vía un score deflactado.

---

## 5. Umbral de cobertura mínima

> Código de referencia: `scoring.rs:351-359` (repositorio de la plataforma)

| Preguntas aplicables | Status | Comportamiento |
|---|---|---|
| **≥ 40** | `Ok` | Scoring normal, sin aviso. |
| **25–39** | `Warning` | Scoring calculado, pero el informe muestra el banner "Resultado preliminar: confiabilidad limitada". |
| **< 25** | `Blocked` | En la plataforma: scoring **rechazado**, la API responde 422 `InsufficientData`. En este kit: calculado igualmente y marcado `BLOCKED` (ver nota abajo). |

"Aplicables" = preguntas visibles para la audience configurada del respondiente (después del filtro `audience`). Si un respondiente es Backend, las preguntas solo de Frontend no cuentan.

> **Kit vs. plataforma:** la plataforma de producción **rechaza** el scoring por debajo de 25 respuestas (HTTP 422 `InsufficientData`). Este kit, vía `scripts/compute_scores.py`, **calcula de todos modos** y marca `threshold_status = BLOCKED` en el `scores.json` (comportamiento "compute-and-mark"). El resultado marcado como BLOCKED sirve solo como borrador preliminar y no debe sustentar decisiones ejecutivas.

---

## 6. Agregación multi-respondiente

> Código de referencia: `repos/scoring.rs:354-368` (repositorio de la plataforma)

Cuando más de una persona responde el mismo assessment:

1. Para cada `question_id`, el sistema computa **`AVG(selected_level)`** sobre todos los respondientes que respondieron esa pregunta.
2. Ese valor promedio (que puede ser fraccionario, ej.: 2.67) entra como `nivel_q` en la fórmula de capability score.
3. **No hay peso por respondiente**: todo respondiente vale igual.
4. **No hay estratificación por audience**: si Backend y Frontend responden la misma Q, el promedio mezcla ambos.

**Ejemplo:** 3 respondientes para Q1 con niveles 2, 4, 3 → `Q1 = (2+4+3)/3 = 3.0`.

---

## 7. Etiquetas de madurez (mapeo de score)

> Código de referencia: `scoring.rs:361-373` (repositorio de la plataforma)

Aplicado a cualquier score (capability, pillar u overall):

| Rango de score | Etiqueta | Color (token) |
|---|---|---|
| `score < 0.5` | **L0, Inicial** | `--color-l0` (rojo) |
| `0.5 ≤ score < 1.5` | **L1, En Desarrollo** | `--color-l1` (ámbar) |
| `1.5 ≤ score < 2.5` | **L2, Definido** | `--color-l2` (azul) |
| `2.5 ≤ score < 3.5` | **L3, Gestionado** | `--color-l3` (verde) |
| `score ≥ 3.5` | **L4, Optimizando** | `--color-l4` (morado) |

> **Dos taxonomías de etiquetas, ambas correctas:** los JSONs de scoring (`saida/scores.json`, `saida/gaps.json`) usan las etiquetas PT-BR de la plataforma en el estilo `L2 — Definido`, los equivalentes en PT-BR de las etiquetas de la tabla de arriba. En cambio, los catálogos del informe PDF (`relatorios/i18n/{pt-br,en,es}.json`) usan la nomenclatura de exhibición propia de los informes (ej.: `Mejorado por IA` para L2 en el catálogo en español). Cada superficie usa su taxonomía: los JSONs de datos siguen la plataforma, los PDFs siguen el catálogo i18n. Los cortes numéricos (0.5 / 1.5 / 2.5 / 3.5) son idénticos en las dos.

---

## 8. Gap analysis y priorización

> Código de referencia: `scoring.rs:307-349` (repositorio de la plataforma)

Para cada capability:

```
target_level   = target_overrides.get(capability_id) o 3.0 (default L3)
gap_size       = target_level − current_score
priority_score = peso_capability × gap_size

Si gap_size ≤ 1e-9 (epsilon flotante) → se descarta (ya alcanzó la meta)
```

### Clasificación de prioridad

| `priority_score` | Etiqueta | Significado |
|---|---|---|
| ≥ 2.4 | **P0** | Crítico: abordar en los próximos 30 días |
| ≥ 1.6 y < 2.4 | **P1** | Alto: incluir en el próximo trimestre |
| ≥ 0.9 y < 1.6 | **P2** | Medio: backlog del semestre |
| < 0.9 | **P3** | Bajo: monitorear |

**¿Por qué `weight × gap`?** Ejemplo ilustrativo: capabilities con peso 2.0 y gap 1.5 (priority_score = 3.0) son más urgentes que peso 1.0 y gap 2.0 (priority_score = 2.0): el peso refleja el impacto estratégico en el overall. (Los pesos reales de cada capability están en el `framework.json`.)

---

## 9. PE Score (Production Engineering Readiness)

> Código de referencia: `scoring.rs:266-304` (repositorio de la plataforma)

Sub-score calculado **solo con las preguntas marcadas `pe = true`** en el seed.

- Filtra → recalcula capability/pillar/overall con el subconjunto.
- Mismo SUMPRODUCT.
- Si ninguna pregunta tiene `pe = true` → retorna `None`.
- Se muestra lado a lado con el overall general, señalando la preparación para producción (resiliencia, observabilidad, runbooks, SLOs etc.).

---

## 10. Persistencia (tablas y materialización)

> Migration de referencia: `migrations/20260417000000_initial.sql` (repositorio de la plataforma)

| Tabla | Columnas clave | Cuándo se puebla |
|---|---|---|
| `assessment_scores` | `overall_score`, `pe_score`, `total_applicable`, `total_answered`, `scored_at` | `POST /api/scoring/trigger` |
| `pillar_scores` | `pillar_id`, `score` | ídem |
| `capability_scores` | `capability_id`, `score` (NULL si sin respuesta), `weight` | ídem |
| `gap_analysis` | `capability_id`, `current_score`, `target_level`, `gap_size`, `priority`, `priority_score` | ídem |

`GET /api/scoring/results/{assessment_id}` lee **directamente de las tablas materializadas**, no recalcula. Esto garantiza consistencia entre informes y roadmaps generados.

---

## 11. Ejemplo end-to-end: Pilar P1

### Escenario
Capability **P1-C1: Asistentes de Codificación IA** (5 preguntas). Evaluación respondida por **2 desarrolladores** (R1 y R2). Los pesos de abajo son los **pesos reales del `framework.json`**: `P1-C1-Q3 = 0.8`, `P1-C1-Q5 = 1.1`, las demás preguntas `1.0` (default).

### Respuestas reales

| Pregunta | Pregunta (resumida) | Peso | R1 | R2 | **Prom** |
|---|---|---:|---|---|---|
| `P1-C1-Q1` | Adopción de herramientas de completado de código con IA | 1.0 | L3 (3) | L4 (4) | **3.5** |
| `P1-C1-Q2` | IA para revisión de código y mejora de calidad | 1.0 | L2 (2) | L3 (3) | **2.5** |
| `P1-C1-Q3` | IA para generación y mantenimiento de pruebas | **0.8** | L1 (1) | L2 (2) | **1.5** |
| `P1-C1-Q4` | Ingeniería de prompts y gestión de templates | 1.0 | L2 (2) | L2 (2) | **2.0** |
| `P1-C1-Q5` | Gobernanza y seguridad de las herramientas IA | **1.1** | L3 (3) | L4 (4) | **3.5** |

### Paso 1: Capability score (P1-C1)

```
wsum   = (3.5×1.0) + (2.5×1.0) + (1.5×0.8) + (2.0×1.0) + (3.5×1.1)
       = 3.5 + 2.5 + 1.2 + 2.0 + 3.85
       = 13.05

wtotal = 1.0 + 1.0 + 0.8 + 1.0 + 1.1 = 4.9

P1-C1.score = 13.05 / 4.9 = 2.6633 (2.663265…)   →   Etiqueta: L3 — Gestionado
```

El cálculo lleva precisión total (`f64`, sin redondeo); los valores mostrados aquí están redondeados a 4 decimales.

> **Efecto de los pesos reales:** con pesos uniformes 1.0 el promedio sería `13.0 / 5.0 = 2.60`. El peso menor en Q3 (0.8, la respuesta más débil) y el peso mayor en Q5 (1.1, una respuesta fuerte) elevan el score a 2.6633.

### Paso 2: Pillar score (P1)

Suponga que P1-C1 es la única capability respondida del pilar P1. En el `framework.json`, P1-C1 tiene `weight_capability = 1.2`:

```
ws = 2.663265… × 1.2 = 3.195918…
wt = 1.2
P1.score = 3.195918… / 1.2 = 2.6633   →   Etiqueta: L3 — Gestionado
```

> Con una única capability respondida, el peso de la capability se cancela en la división. En un assessment real, P1 tiene 9 capabilities y el cálculo sería un SUMPRODUCT sobre todas las que tengan al menos 1 respuesta.

### Paso 3: Gap analysis

Default `target_level = 3.0` y `weight_capability = 1.2` (valor real de P1-C1 en el `framework.json`):

```
gap_size       = 3.0 − 2.663265… = 0.336734… ≈ 0.3367
priority_score = 1.2 × 0.336734… = 0.404081… ≈ 0.4041
clasificación  = P3 (Bajo)   ← pues 0.4041 < 0.9
```

### Paso 4: Threshold

5 preguntas respondidas << 25 → **`threshold_status = Blocked`** si esa fuera la única capability evaluada. En producción, se esperan ≥ 40 preguntas respondidas en el assessment entero.

---

## 12. Ejemplo end-to-end: Pilar P2

> **Ejemplo hipotético con pesos personalizados.** Los pesos 1.5 de abajo son didácticos, para mostrar el efecto del SUMPRODUCT con pesos no uniformes. El `framework.json` real usa `weight = 1.0` en **todas** las preguntas de P2-C1. Los pesos de capability 1.0 usados en los Pasos 2 y 3 también son ilustrativos (en el `framework.json` real, P2-C1 tiene `weight = 1.2`). El rango permitido para pesos personalizados de pregunta es [0.5, 2.0] (sección 3.1).

### Escenario
Capability **P2-C1: Inteligencia de Pipeline CI/CD** (6 preguntas). Respondida por **1 SRE** + **1 Platform Engineer**. Mezcla de pesos **hipotéticos**: Q1 y Q5 con `weight = 1.5` (preguntas de impacto directo en DORA metrics).

### Respuestas

| Pregunta | Pregunta (resumida) | Peso | SRE | PltEng | **Prom** |
|---|---|---:|---:|---:|---:|
| `P2-C1-Q1` | Optimización de pipeline CI/CD con IA | **1.5** | L4 (4) | L3 (3) | **3.5** |
| `P2-C1-Q2` | Self-healing builds y autocorrección | 1.0 | L2 (2) | L2 (2) | **2.0** |
| `P2-C1-Q3` | Análisis predictivo de fallas | 1.0 | L1 (1) | L2 (2) | **1.5** |
| `P2-C1-Q4` | Optimización inteligente de caché | 1.0 | L2 (2) | L3 (3) | **2.5** |
| `P2-C1-Q5` | Métricas DORA e insights | **1.5** | L3 (3) | L4 (4) | **3.5** |
| `P2-C1-Q6` | Triaje automatizado de pruebas flaky | 1.0 | L2 (2) | L1 (1) | **1.5** |

### Paso 1: Capability score (P2-C1)

```
wsum   = (3.5×1.5) + (2.0×1.0) + (1.5×1.0) + (2.5×1.0) + (3.5×1.5) + (1.5×1.0)
       = 5.25 + 2.0 + 1.5 + 2.5 + 5.25 + 1.5
       = 18.00

wtotal = 1.5 + 1.0 + 1.0 + 1.0 + 1.5 + 1.0 = 7.0

P2-C1.score = 18.00 / 7.0 = 2.5714…   →   Etiqueta: L3 — Gestionado
```

> **Observación:** sin los pesos extras en Q1 y Q5, el promedio simple sería `(3.5+2.0+1.5+2.5+3.5+1.5)/6 = 2.4167` → caía a L2. El peso 1.5 refleja que esas dos dimensiones importan más para el resultado de un DevOps maduro.

### Paso 2: Pillar score (P2) con 2 capabilities

Agregue P2-C2 (IaC) con score = 1.80, peso = 1.0:

```
ws = (2.5714 × 1.0) + (1.80 × 1.0) = 4.3714
wt = 1.0 + 1.0 = 2.0
P2.score = 4.3714 / 2.0 = 2.1857   →   Etiqueta: L2 — Definido
```

### Paso 3: Gap analysis (target personalizado)

Para P2-C1, el equipo de SRE definió `target_level = 3.5` (por encima del default):

```
gap_size       = 3.5 − 2.5714 = 0.9286
priority_score = 1.0 × 0.9286 = 0.9286
clasificación  = P2 (Medio)   ← pues 0.9 ≤ 0.9286 < 1.6
```

---

## 13. Ejemplo end-to-end: Pilar P3

> **Ejemplo hipotético con pesos personalizados.** Los pesos 2.0 (preguntas) y 1.5 (capability, en los Pasos 2 y 3) son didácticos. El `framework.json` real usa `weight = 1.0` en **todas** las preguntas de P3-C5 y `weight = 1.0` en la propia capability P3-C5.

### Escenario
Capability **P3-C5: Aplicaciones Agénticas** (6 preguntas). Respondida por **1 Arquitecto** + **1 ML Engineer** + **1 Security**. Pesos **hipotéticos**: Q1, Q3 y Q6 con `weight = 2.0` (pesos máximos, la frontera de innovación).

### Respuestas

| Pregunta | Pregunta (resumida) | Peso | Arq | ML | Sec | **Prom** |
|---|---|---:|---:|---:|---:|---:|
| `P3-C5-Q1` | Implementación de agentes IA autónomos | **2.0** | L2 (2) | L3 (3) | L1 (1) | **2.0** |
| `P3-C5-Q2` | Coordinación multi-agente (orquestación) | 1.0 | L1 (1) | L2 (2) | L1 (1) | **1.33** |
| `P3-C5-Q3` | Frameworks de tool-use y function calling | **2.0** | L3 (3) | L4 (4) | L2 (2) | **3.0** |
| `P3-C5-Q4` | Memoria persistente de agentes | 1.0 | L2 (2) | L2 (2) | L1 (1) | **1.67** |
| `P3-C5-Q5` | Evaluación continua y safety guardrails | 1.0 | L1 (1) | L2 (2) | L3 (3) | **2.0** |
| `P3-C5-Q6` | Gobernanza y auditoría de acciones de agentes | **2.0** | L1 (1) | L1 (1) | L3 (3) | **1.67** |

### Paso 1: Capability score (P3-C5)

```
wsum   = (2.00×2.0) + (1.33×1.0) + (3.00×2.0) + (1.67×1.0) + (2.00×1.0) + (1.67×2.0)
       = 4.00 + 1.33 + 6.00 + 1.67 + 2.00 + 3.34
       = 18.34

wtotal = 2.0 + 1.0 + 2.0 + 1.0 + 1.0 + 2.0 = 9.0

P3-C5.score = 18.34 / 9.0 = 2.0378…   →   Etiqueta: L2 — Definido
```

### Paso 2: Gap analysis (capability estratégica)

El liderazgo definió `target_level = 4.0` (ambición: liderar en el espacio agéntico) y la capability tiene `weight = 1.5`:

```
gap_size       = 4.0 − 2.0378 = 1.9622
priority_score = 1.5 × 1.9622 = 2.9433
clasificación  = P0 (Crítico)   ← pues 2.9433 ≥ 2.4
```

→ Esta capability **entra en el roadmap de los próximos 30 días** con prioridad máxima.

### Paso 3: Contribución al overall

Si el assessment completo tiene 28 capabilities activas, P3-C5 con `score = 2.0378` y `weight = 1.5` contribuye:
- Numerador del overall: `+ 2.0378 × 1.5 = +3.0567`
- Denominador del overall: `+ 1.5`

→ Subir P3-C5 de 2.04 a 3.5 (target práctico L3) sumaría `(3.5 − 2.04) × 1.5 = 2.19` al numerador y elevaría el overall en ~`2.19 / wtotal_overall` puntos.

---

## 14. Edge cases y garantías

| Situación | Garantía |
|---|---|
| `wtotal = 0` (ninguna pregunta respondida) | Retorna `None` (capability) o `0.0` (pillar/overall). Nunca divide por cero. |
| Score por encima de 4.0 | Imposible por construcción: todos los niveles ∈ [0,4] y los promedios ponderados preservan el rango. |
| Score por debajo de 0.0 | Imposible: `selected_level ∈ [0,4]`. |
| `gap_size` negativo (ya superó la meta) | Filtrado (no aparece en el roadmap). |
| Multi-respondiente con 0 respuestas | La capability queda en `None`, sin error. |
| Respondiente fuera de la audience | Sus respuestas a preguntas no aplicables son **ignoradas en el scoring** pero almacenadas para auditoría. |
| Reprocesamiento (recalcular tras una nueva respuesta) | Idempotente: `POST /api/scoring/trigger` reemplaza las 4 tablas materializadas en una transacción. |

---

## 15. Glosario

| Término | Definición |
|---|---|
| **Question** | Ítem de evaluación concreto. ID estándar `P[1-3]-C[1-19]-Q[1-99]`. |
| **Capability** | Subdominio funcional. Agrupa 5–7 preguntas. |
| **Pillar** | Dimensión estratégica. Agrupa 9–10 capabilities. P1, P2 o P3. |
| **Level (L0–L4)** | Madurez de una respuesta individual. Entero 0–4. |
| **Score** | Resultado continuo `f64 ∈ [0,4]` producido por agregación. |
| **Weight** | Peso de la pregunta (`[0.5, 2.0]`, default 1.0) o de la capability. |
| **Threshold** | Cobertura mínima de preguntas respondidas: 25 (warning), 40 (ok). |
| **PE flag** | Marca preguntas críticas para Production Engineering. Generan un sub-score paralelo. |
| **Gap** | `target − current` por capability. |
| **Priority score** | `weight × gap` que clasifica la capability en P0/P1/P2/P3. |
| **Audience** | Públicos objetivo de la pregunta (developer, sre, security…). Filtra la visibilidad en el formulario. |
| **`threshold_status`** | `Ok` / `Warning` / `Blocked`, devuelto junto con el resultado. |

---

**Archivos relacionados:**
- 🐍 `scripts/compute_scores.py`, `scripts/compute_gaps.py`, `scripts/recommend_strategies.py`: implementaciones ejecutables y determinísticas de estas fórmulas (leen `respostas.json` + `framework.json`, escriben `saida/*.json`)
- 📄 `pontuacao-e-calculo.xlsx`: planilla auditable con fórmulas SUMPRODUCT visibles (mismos ejemplos de este doc); generada por `scripts/generate_scoring_workbook.py`
- 🌐 `calculadora-pontuacao.html`: calculadora interactiva standalone (seleccionar respuestas, ver scores en vivo)
- 📚 `P1-…md`, `P2-…md`, `P3-…md`: preguntas reales del assessment con KPI/contexto/evidencias por nivel
