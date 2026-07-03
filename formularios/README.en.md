# `formularios/`: visual HTMLs of the 158 questions (offline reference)

This folder contains **3 standalone HTML files** (one per pillar) with all 158 assessment questions formatted as they appear on the web platform. Useful for **visual reference** while filling in `respostas.json` or for presenting/discussing the questions in workshops.

## Files

| File | Pillar | Capabilities | Questions |
|---|---|---|---|
| **[P1-produtividade-do-desenvolvedor.html](P1-produtividade-do-desenvolvedor.html)** | P1: Developer Productivity | 9 | 53 |
| **[P2-ciclo-de-vida-devops.html](P2-ciclo-de-vida-devops.html)** | P2: DevOps Lifecycle | 10 | 59 |
| **[P3-plataforma-de-aplicações.html](P3-plataforma-de-aplicações.html)** | P3: Application Platform | 9 | 46 |

## How to use

1. Double-click any `.html` file to open it in the browser (no server needed)
2. Each question shows:
   - **ID** (`P1-C1-Q1`, etc.): use it to map into `respostas.json`
   - **Text** of the question in PT-BR
   - **5 level options** (L0 to L4) with description and color
   - **Suggested KPI** (in English, a universal technical term)
   - **Context** (what it measures / why it matters)
   - **Expected evidence** per level

3. To fill in `respostas.json`:
   - Identify the question ID in the HTML
   - Go to `respostas.json` (kit root) and search for that ID
   - Set the `level` (0-4) and add `evidence` (descriptive text)

## Important note

These HTMLs are an **offline visualization**: they do not capture responses. For interactive collection (click and save), use:
- **Microsoft Forms** (see `coleta/INSTRUCOES-FORMS.en.md`)
- **React Wizard** once the web platform is ready
- **Manual editing** of `respostas.json` (structured JSON format)

## Technical documentation of the questions

For the detailed description of the 158 questions with KPI/context/evidence per level, see the MD files in [`../referencia/`](../referencia/):
- `referencia/P1-produtividade-do-desenvolvedor.md`
- `referencia/P2-ciclo-de-vida-devops.md`
- `referencia/P3-plataforma-de-aplicações.md`
