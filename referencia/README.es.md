# `referencia/`: Documentación técnica y ejemplos

Esta carpeta contiene **documentación read-only**: algoritmo oficial, descripción de las 158 preguntas, planilla auditable, calculadora interactiva y ejemplos finales de output.

## Archivos

### 📊 Documentación del algoritmo de scoring

| Archivo | Qué es |
|---|---|
| **[pontuacao-e-calculo.md](pontuacao-e-calculo.md)** | Referencia oficial de scoring: todas las fórmulas (capability/pillar/overall), threshold (25/40), multi-respondiente, gap analysis (P0-P3), mapeo de etiquetas, edge cases, glosario. **Refleja 1:1** el código `app/backend/src/scoring.rs` (repositorio de la plataforma, no incluido en este kit) |
| **[pontuacao-e-calculo.xlsx](pontuacao-e-calculo.xlsx)** | Planilla Excel auditable con 3 pestañas: Léeme, Respuestas (las 158 preguntas, pesos del framework.json) y Cálculo (28 capabilities, pilares, overall, threshold). Fórmulas SUMPRODUCT visibles celda por celda. Generada por `scripts/generate_scoring_workbook.py` |
| **[calculadora-pontuacao.html](calculadora-pontuacao.html)** | Calculadora interactiva standalone (Tailwind + JavaScript): 17 preguntas reales (1 capability por pilar), edite niveles y pesos, vea los scores recalcularse en vivo. Se abre en el navegador |

### 📚 Documentación de las 158 preguntas

| Archivo | Contenido |
|---|---|
| **[P1-produtividade-do-desenvolvedor.md](P1-produtividade-do-desenvolvedor.md)** | Las 53 preguntas de P1 con: KPI, contexto (qué mide / por qué importa), descripción completa de cada nivel L0-L4 con evidencias esperadas |
| **[P2-ciclo-de-vida-devops.md](P2-ciclo-de-vida-devops.md)** | Las 59 preguntas de P2 (mismo formato) |
| **[P3-plataforma-de-aplicações.md](P3-plataforma-de-aplicações.md)** | Las 46 preguntas de P3 (mismo formato) |

### 🎯 Ejemplos finales (output del pipeline)

| Carpeta | Qué es |
|---|---|
| **[exemplo-saida/](exemplo-saida/)** | **5 PDFs reales** + JSONs intermedios generados a partir de `respostas.json.example` (Cliente Exemplo S.A.). Incluye la versión PT-BR (raíz), EN (`exemplo-saida/en/`) y ES (`exemplo-saida/es/`). Es el **preview exacto** de lo que el cliente va a generar. Tiene un README detallado adentro. |

## Cuándo usar cada archivo

- **¿Quiere entender cómo se calculan los scores?** → `pontuacao-e-calculo.md`
- **¿El cliente preguntó "¿cómo salió este score?" y quiere ver la fórmula?** → abra `pontuacao-e-calculo.xlsx` en Excel
- **¿Quiere jugar con diferentes respuestas y ver los scores en vivo?** → abra `calculadora-pontuacao.html` en el navegador
- **¿Va a responder una pregunta y tiene dudas sobre qué significa cada nivel?** → consulte `P1/P2/P3-…md` (más detalle que los HTMLs visuales en `formularios/`)
- **¿Quiere ver "cómo va a quedar el informe final"?** → abra los PDFs en `exemplo-saida/`

## ⚠️ Importante

**No modifique** ningún archivo de esta carpeta: son **read-only** (referencia técnica que debe permanecer canónica). Si necesita personalizar para su cliente, copie a otro lugar y edite la copia.

La única excepción: la subcarpeta `exemplo-saida/` puede regenerarse ejecutando el pipeline con `respostas.json.example`.
