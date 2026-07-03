# Rúbrica de Madurez IA: Developer Survey

> **Modelo determinístico** que mapea respuestas del survey a niveles L0-L4 en **7 dimensiones**, espejando la escala del assessment principal de madurez. Score por equipo (sin scores individuales en el reporte, preserva el anonimato).

**Versión de la rúbrica:** 1.1 · **Fecha:** 2026-07-03 · Constante `RUBRIC_VERSION` en [`scripts/rubric.py`](scripts/rubric.py)
**Implementación:** [`scripts/rubric.py`](scripts/rubric.py) · **Ejecutor:** [`scripts/calcular_maturidade.py`](scripts/calcular_maturidade.py)

---

## 🎯 Principios

1. **Determinística**: la misma respuesta siempre produce el mismo nivel. Sin LLM, sin aleatoriedad.
2. **Auditable**: cada regla está documentada en este archivo, y el código la replica 1:1.
3. **Conservadora**: ante la duda, baja el nivel (evita inflar la madurez declarada).
4. **Anónima**: calcula por respondente individualmente, pero **solo agregados** salen en el reporte (promedio, distribución).
5. **Espejo del assessment principal**: usa la misma escala L0-L4 (Inicial → Optimizando) para comparación directa.

## 🧭 Escala (igual al assessment principal)

| Rango | Etiqueta | Descripción |
|---|---|---|
| `< 0.5` | **L0: Inicial** | Sin práctica, sin conocimiento, sin herramienta |
| `[0.5, 1.5)` | **L1: En Desarrollo** | Adopción puntual, conocimiento básico |
| `[1.5, 2.5)` | **L2: Definido** | Uso regular, conoce conceptos clave |
| `[2.5, 3.5)` | **L3: Gestionado** | Adopción amplia, conoce conceptos avanzados, mide impacto |
| `≥ 3.5` | **L4: Optimizando** | Dominio completo, crea primitivos, optimización continua |

## 📊 Las 7 dimensiones

| ID | Dimensión | Viene de | Qué mide |
|---|---|---|---|
| **D2** | **Copilot Adoption** | S2 (9 p) | Frecuencia + amplitud de modos + features + ganancia medida |
| **D3** | **MS/GH Tooling Breadth** | S3 (7 p) | Cuántas herramientas avanzadas (Foundry, Spaces, Coding Agent, MCP, Spec Kit) usa |
| **D4** | **AI Dev Practices** | S4 (9 p) | TDD con IA, SDD, pair programming, debugging, onboarding |
| **D5** | **Agent Concepts Mastery** | S5 (11 p) | Conocimiento de 9 conceptos clave + creación de primitives + pruebas |
| **D6** | **Instructions Maturity** | S6 (6 p) | Uso de instructions files, mantenimiento, prompt library compartida |
| **D7** | **Best Practices** | S7 (9 p) | Champion, métricas DORA/DX, comunidad, compartir |
| **D8** | **Security & Governance** | S8 (13 p) | Política, GHAS, scanners, SBOM, JIT, red-lines, audit, capacitación |

> **Excluidas del score:** S1 (perfil: solo categoriza) y S9 (texto libre: se vuelve quotes).

## ⚖️ Reglas detalladas por dimensión

> Las opciones de respuesta citadas abajo son las cadenas canónicas en PT-BR del banco de preguntas, que es lo que la rúbrica compara (ver el guardrail de cobertura de match); los bancos de preguntas localizados ([EN](perguntas-para-forms-devs.en.md), [ES](perguntas-para-forms-devs.es.md)) traducen los títulos de las preguntas pero mantienen las opciones canónicas.

### D2: Copilot Adoption

| Respuesta clave | Señala |
|---|---|
| `S2-Q1: Não tenho licença` OR `Tenho mas não uso` | **Hard L0** |
| `S2-Q2: Nunca` | **Hard L0** |
| `S2-Q2: Raramente` | L1 |
| `S2-Q2: Diariamente` + `S2-Q5: 2+ features` + `S2-Q3: 1+ modo` | **L2** |
| Lo anterior + `S2-Q3: usa Agent o Coding Agent` + `S2-Q5: 4+ features` + ganancia positiva | **L3** |
| Lo anterior + `S2-Q3: Coding Agent` + `S2-Q5: Spaces` + `S2-Q7: ganancia >40%` + `S2-Q5: 5+ features` | **L4** |

Notas (conservadoras):
- "Ganancia positiva" = respuesta explícita de `+10%` o más en S2-Q7. Una ganancia no respondida o "Não sei medir" NO concede L3.
- Cada nivel exige la base del nivel anterior (L3 y L4 exigen uso diario).

### D3: MS/GH Tooling Breadth

Score punto a punto: `n_tools (S3-Q1) + advanced_signals (S3-Q3, Q4, Q6, Q2)`

- `n_tools` = cuántas herramientas marcadas en S3-Q1 (excluyendo "Nenhuma")
- `advanced_signals` = +1 por cada:
  - Coding Agent: "Uso ativamente"
  - Spaces: "Uso e crio"
  - MCP: "Uso servidores" o "Configurei custom"
  - Foundry usado para "MCP", "multi-agent" o "agentes autônomos"

**Mapping:**
- `score ≥ 8` → **L4** (5+ herramientas + 3+ señales avanzadas)
- `score 5-7` → **L3**
- `score 3-4` → **L2**
- `score 1-2` → **L1**
- `score 0` → **L0**

### D4: AI Dev Practices

Suma ponderada (máx ~10 puntos), mapeada a 0-4:

| Pregunta | Señal | Puntos |
|---|---|---|
| `S4-Q1` TDD con IA | "Sempre" | +2 |
|  | "Frequentemente" | +1.5 |
|  | "Não sei TDD" | -1 |
| `S4-Q2` SDD | "Uso ativamente" | +2 |
|  | "Já testei" | +1 |
|  | "Nunca ouvi falar" | -0.5 |
| `S4-Q3` Momentos en que consulta IA (multi) | n_momentos × 0.4 (cap 2.0) | hasta +2 |
| `S4-Q4` Mentalidad de pair programmer | "Trato como par" | +1.5 |
|  | "Às vezes" | +0.5 |
| `S4-Q5` Refactoring | "Toda semana" | +1 |
| `S4-Q7` Debugging primero con IA | "Pergunto Copilot" | +0.5 |
| `S4-Q8` Onboarding con IA | "Sempre" | +1 |

**Mapping:** `score / 10 × 4` → redondeado.

### D5: Agent Concepts Mastery

3 componentes:

**(a) Coverage de 9 conceptos** (60% del peso): por cada uno, +1.0 si "usa/explica", si no 0:
- S5-Q1 AI agent
- S5-Q2 Modos de Copilot
- S5-Q3 Custom agents
- S5-Q4 Skills
- S5-Q5 Prompt files
- S5-Q6 A2A
- S5-Q7 Handoffs
- S5-Q8 Subagentes
- S5-Q9 Personas Agentic DevOps

**(b) Primitives creados (S5-Q11 multi)** (25% del peso): n_primitivos × 0.25 (cap 1.0)

**(c) Pruebas de agents (S5-Q10)** (15% del peso):
- "Sempre" (test suite) → +1.0
- "Frequentemente" → +0.5
- "Não crio agents" → 0 (neutro)

**Fórmula:** `(coverage × 0.6 × 4) + min(n_primitivos × 0.25, 1.0) + (test_bonus × 0.6)`. Cap en 4.0.

> Los tres componentes suman exactamente 4.0 (2.4 + 1.0 + 0.6), así que L4 es alcanzable.

**Cobertura mínima:** si hay `<5` preguntas respondidas → retorna `None` (no scored).

### D6: Instructions Maturity

| Pregunta | Señal | Puntos |
|---|---|---|
| `S6-Q1` Files (multi) | "Nenhum" o vacío | **Hard L0** |
|  | 4+ tipos | +2 |
|  | 2-3 tipos | +1.5 |
|  | 1 tipo | +1 |
| `S6-Q2` Maintainer | "Time inteiro contribui" | +2 |
|  | "1-2 dedicadas" | +1.5 |
|  | "Eu mantenho sozinho" | +1 |
|  | "Ninguém mantém" / "Não temos" | -1 |
| `S6-Q3` Update freq | "Toda semana" | +1 |
|  | "Mensalmente" | +0.7 |
|  | "Trimestralmente" | +0.4 |
|  | "Nunca" | -0.5 |
| `S6-Q4` Content (multi) | n_tipos × 0.3 (cap 2.0) | hasta +2 |
| `S6-Q5` Library shared | "Copilot Space" / "repo dedicado" | +1 |
|  | "wiki/Confluence" | +0.5 |
|  | "Não compartilhamos" | -0.5 |

**Mapping:** `score / 8 × 4` (8 es el máximo real alcanzable: 2 + 2 + 1 + 2 + 1).

### D7: Best Practices

| Pregunta | Señal | Puntos |
|---|---|---|
| `S7-Q1` Learning sources (multi) | n_fontes × 0.3 (cap 1.5) | hasta +1.5 |
| `S7-Q2` Champion | "eu sou" / "outra pessoa" | +1.5 |
|  | "Cada um se vira" | -0.5 |
| `S7-Q3` Internal channel | ">5 mensagens/sem" | +1 |
|  | "pouco ativo" | +0.5 |
| `S7-Q4` Métricas (multi) | conteo DORA/DX/SPACE/Copilot × 0.5 (cap 2.0) | hasta +2 |
|  | "Não medimos" | -1 |
| `S7-Q5` Iteraciones | "1ª tentativa" / "2-3" | +1 |
|  | "7+" | -0.5 |
| `S7-Q9` Comparte prompts | "Frequentemente" | +1 |
|  | "Nunca" | -0.5 |

**Mapping:** `score / 8 × 4`.

### D8: Security & Governance (CRÍTICO, conservadora)

El mayor número de reglas + penalizaciones por red flags:

| Pregunta | Señal | Puntos |
|---|---|---|
| `S8-Q1` Política + `S8-Q4` (Sec tools) | ("Não temos política" OR "Não sei") + "Nenhuma ferramenta" | **Hard L0** |
| `S8-Q1` | "formal e clara" | +2 |
|  | "pouco clara" | +1 |
|  | "informal" | +0.5 |
| `S8-Q2` Sabe qué datos son sensibles | "Sei claramente" | +1 |
| `S8-Q3` Forbidden (multi) | n_tipos × 0.2 (cap 1.0) | hasta +1 |
|  | "Nenhuma restrição" | -1 |
| `S8-Q4` Sec tools (multi) | n_tools × 0.3 (cap 2.0) | hasta +2 |
| `S8-Q5` Code scan en el PR | "gate obrigatório" | +1 |
| `S8-Q6` SBOM | "automatizado" | +0.5 |
| `S8-Q7` Review formal de IA | "obrigatório humano + scanner" | +1 |
| `S8-Q8` Red-lines de agents | "Sempre" | +1 |
| `S8-Q9` JIT permissions | "JIT obrigatório" | +1 |
| `S8-Q10` DLP | "bloqueia" | +0.5 |
| `S8-Q11` Audit | "ativos e revisados" | +0.5 |
| `S8-Q12` Capacitación | "obrigatório anual" | +0.5 |

**Mapping:** `score / 12 × 4`.

## 🧮 Score overall del respondente

```
overall = promedio(D2..D8)  # solo dimensiones con score != None
```

## 🛡️ Guardrail de cobertura de match

El matching de las reglas es por substring case-insensitive sobre las opciones canónicas en PT-BR (con sinónimos EN/ES para las opciones de mayor señal, ej.: licencia, frecuencia, política). Si un cliente traduce o altera las opciones en Forms, las reglas dejan de reconocer las respuestas y los scores se deflactan silenciosamente.

Para proteger contra esto, `calcular_maturidade.py` mide por respondente la **cobertura de match**: % de las preguntas puntuables respondidas cuyo texto coincide con alguna opción canónica conocida (`rubric.match_coverage`). Comportamiento sobre el promedio del equipo:

| Cobertura promedio | Comportamiento |
|---|---|
| ≥ 70% | Procede normalmente |
| 40% a 70% | Procede con **aviso destacado** (los scores pueden estar subestimados) |
| < 40% | **Aborta** con error accionable; usa `--force` para proceder de todos modos |

La cobertura medida (promedio/mínimo) sale en `metadata.match_coverage` en el JSON de salida.

## 🧮 Agregación para el equipo

```
team_score(D) = promedio(D en todos los respondentes)  # ignora None
team_overall  = promedio(overall de todos los respondentes)
distribución(D) = % de respondentes en cada L0-L4
```

## 📤 Output

`saida/maturidade-developer-survey-<DATE>.json`:

```jsonc
{
  "metadata": {
    "computed_at": "2026-07-03T12:00:00+00:00",
    "source": "survey-devs/respostas-devs.json",
    "n_respondents": 12,
    "rubric_version": "1.1 (deterministic)",
    "match_coverage": {"avg_pct": 100.0, "min_pct": 100.0, "n_measured": 12},
    "anonymous": true,
    "scope": "team aggregate (no individual scores in output)"
  },
  "team_overall": {
    "score": 2.22,
    "label": "L2 — Definido",
    "respondents_with_overall": 12
  },
  "dimensions": {
    "D2": {
      "name": "Copilot Adoption",
      "team_score": 0.80,
      "label": "L1 — Em Desenvolvimento",
      "respondents_with_score": 12,
      "distribution_count": {"L0": 5, "L1": 5, "L2": 2, "L3": 0, "L4": 0},
      "distribution_pct": {"L0": 41.7, "L1": 41.7, "L2": 16.7, "L3": 0, "L4": 0}
    },
    "D3": {...}, "D4": {...}, "D5": {...},
    "D6": {...}, "D7": {...}, "D8": {...}
  },
  "ranking": {
    "top": [["D7", "Best Practices", 2.91], ...],
    "bottom": [["D2", "Copilot Adoption", 0.80], ...]
  }
}
```

## 🔄 Cómo ejecutar

### Vía skill en Copilot Chat

```
/insights-developer-survey   # invoca el script automáticamente
```

### Vía CLI

```bash
python3 survey-devs/scripts/calcular_maturidade.py
# Output:
#   - saida/maturidade-developer-survey-DATE.json
#   - resumen en stdout (overall + tabla por dimensión + ranking)
```

## 🔗 Cross-reference con el assessment principal

La madurez individual (del survey) **alimenta y valida** las capabilities del assessment organizacional:

| Dimensión del survey | Capability del assessment | Qué validar |
|---|---|---|
| **D2** Copilot Adoption | `P1-C1` Asistentes de Codificación IA | Score declarado vs. adopción real declarada por los devs |
| **D3** MS/GH Tooling | `P3-C3` Aplicaciones IA + `P3-C5` Apps Agénticas | Sofisticación técnica en IA |
| **D4** AI Dev Practices | `P1-C2` DevEx + `P1-C8` Métricas de Productividad | Prácticas estructuradas |
| **D5** Agent Concepts | `P3-C5` Apps Agénticas | Conocimiento avanzado |
| **D6** Instructions | `P1-C7` Documentación automatizada | Mantenimiento del contexto de IA |
| **D7** Best Practices | `P1-C5` Onboarding + `P1-C8` Métricas | Cultura de adopción |
| **D8** Security & Governance | `P2-C4` DevSecOps + `P2-C10` Supply Chain | Gobernanza real |

> 💡 **Patrón clásico:** el liderazgo evalúa P1-C1 como L3, pero el survey D2 muestra L1 (60% de los devs lo usa raramente) → **disonancia** entre estrategia y práctica. La skill `/insights-developer-survey` destaca esto en la sección 12 del reporte.

## 📝 Changelog

### v1.1 (2026-07-03) · reconciliación código vs. documento

Una auditoría encontró divergencias entre `rubric.py` y este documento (que es el contrato). Decisiones tomadas, una por divergencia:

1. **D2, gate de L3** · el código concedía L3 para uso semanal + Agent + (3+ modos OR 4+ features) sin exigir ganancia positiva (una ganancia no respondida pasaba). **Decisión: código corregido para seguir el documento** (uso diario + Agent o Coding Agent + 4+ features + ganancia positiva explícita), que es la regla conservadora. L4 también pasa a exigir la base de L3 (uso diario), como el "Lo anterior +" de la tabla siempre indicó.
2. **D5, peso de las pruebas** · el código daba peso máximo 0.36 (9%) al componente de pruebas, contradiciendo el "15% del peso" declarado, y hacía L4 inalcanzable (máximo 3.76). **Decisión: código corregido a 0.6** (15% de 4.0); los tres componentes ahora suman exactamente 4.0.
3. **D6, divisor del mapping** · código y documento usaban `/9`, pero el máximo real de puntos es 8 (2+2+1+2+1), haciendo L4 inalcanzable (máximo 3.56). **Decisión: ambos corregidos a `/8`.**
4. **Reglas existentes en el código y ausentes del documento** · documentadas sin cambio de comportamiento: el hard-L0 de D8 incluye "Não sei" (no saber si existe una política es, conservadoramente, equivalente a no tenerla); D6 "Trimestralmente" +0.4, "Eu mantenho sozinho" +1 y "wiki/Confluence" +0.5.
5. **Novedades** · constante `RUBRIC_VERSION` en `rubric.py` (exportada al metadata de los JSON); sinónimos EN/ES para las opciones de mayor señal; guardrail de cobertura de match (sección arriba).

## 📊 Calibración y revisión de la rúbrica

Esta es la **versión 1.1**. Se recomienda revisar trimestralmente con base en:

- Casos donde el score parece sub/sobreestimado (calibrar pesos)
- Cambios en el ecosistema (ej.: Copilot lanza un modo nuevo → agregarlo en S2-Q3 + actualizar D2)
- Feedback de respondentes ("esa pregunta era ambigua")

**Cómo proponer un cambio:**
1. Editar `scripts/rubric.py` con la regla actualizada
2. Documentar el porqué en este archivo
3. Incrementar `RUBRIC_VERSION` y re-ejecutar con datos anteriores para comparar

## 🔐 Política de anonimato en el scoring

La rúbrica calcula el score POR respondente individualmente, pero el JSON de salida y el reporte:

- ✅ Muestran **scores agregados del equipo** (promedio, distribución %)
- ✅ Muestran **distribución por nivel** (% de devs en cada L0-L4)
- ❌ NO muestran score por respondent_id
- ❌ NO muestran cargo/perfil junto con el score (agregación por cargo solo si hay ≥3 devs del mismo cargo)

Esto preserva el pacto de anonimato del survey mientras permite insights útiles para el equipo.
