# `formularios/`: HTMLs visuales de las 158 preguntas (referencia offline)

Esta carpeta contiene **3 archivos HTML standalone** (uno por pilar) con todas las 158 preguntas del assessment formateadas como aparecen en la plataforma web. Útil para **consultar visualmente** durante el llenado del `respostas.json` o para presentar/discutir las preguntas en workshops.

## Archivos

| Archivo | Pilar | Capabilities | Preguntas |
|---|---|---|---|
| **[P1-produtividade-do-desenvolvedor.html](P1-produtividade-do-desenvolvedor.html)** | P1: Productividad del Desarrollador | 9 | 53 |
| **[P2-ciclo-de-vida-devops.html](P2-ciclo-de-vida-devops.html)** | P2: Ciclo de Vida DevOps | 10 | 59 |
| **[P3-plataforma-de-aplicações.html](P3-plataforma-de-aplicações.html)** | P3: Plataforma de Aplicaciones | 9 | 46 |

## Cómo usarlos

1. Doble clic en cualquier archivo `.html` para abrirlo en el navegador (no necesita servidor)
2. Cada pregunta muestra:
   - **ID** (`P1-C1-Q1`, etc.): úsalo para mapear en el `respostas.json`
   - **Texto** de la pregunta en PT-BR
   - **5 opciones de nivel** (L0 a L4) con descripción y color
   - **KPI** sugerido (en inglés, término técnico universal)
   - **Contexto** (qué mide / por qué importa)
   - **Evidencias** esperadas por nivel

3. Para llenar `respostas.json`:
   - Identifica el ID de la pregunta en el HTML
   - Ve al `respostas.json` (raíz del kit) y busca ese ID
   - Marca el `level` (0-4) y agrega `evidence` (texto descriptivo)

## Observación importante

Estos HTMLs son una **visualización offline**: no capturan respuestas. Para recolección interactiva (hacer clic y guardar), usa:
- **Microsoft Forms** (ver `coleta/INSTRUCOES-FORMS.es.md`)
- **Wizard React** cuando la plataforma web esté lista
- **Edición manual** del `respostas.json` (formato JSON estructurado)

## Documentación técnica de las preguntas

Para la descripción detallada de las 158 preguntas con KPI/contexto/evidencias por nivel, consulta los MD en [`../referencia/`](../referencia/):
- `referencia/P1-produtividade-do-desenvolvedor.md`
- `referencia/P2-ciclo-de-vida-devops.md`
- `referencia/P3-plataforma-de-aplicações.md`
