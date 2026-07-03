# AI Maturity Assessment Kit

Self-service consulting kit with three complementary surveys, run with a client before the web platform is ready:
AI Maturity Assessment (158 questions, organizational, produces 5 executive PDFs), Developer Survey (75 questions,
anonymous, behavioral maturity per dimension D2-D8), and Learning & Growth Survey (32 questions, identified,
produces a personalized capacitation plan). A concierge agent, one pipeline prompt, and 12 skills drive the flows.

## Critical files

| Path | Role |
|---|---|
| `framework.json` | Immutable: 3 pillars, 28 capabilities, 158 questions, weights, strategy mapping |
| `respostas.json` (+ `.example`) | Client input: `level` (0-4, floats allowed) and `evidence` per question |
| `saida/` | Every generated artifact goes here |
| `referencia/pontuacao-e-calculo.md` | The ONLY algorithm reference (formulas, labels, thresholds, priorities) |
| `scripts/` | Deterministic pipeline: `compute_scores.py`, `compute_gaps.py`, `recommend_strategies.py`, `import_assessment_responses.py` |
| `relatorios/scripts/build_payload_and_render.py` | Merges pipeline outputs into the payload and renders the 5 PDFs |
| `relatorios/templates/` + `relatorios/i18n/` | Production mirrors: 3 page templates + 1 shared partial + `_print.css`; pt-br/en/es catalogs |
| `wizard/` | Implementation Guide wizard, 4 modes: A (HTML), B (JSON), C (chat), D (auto-fill from the learning plan) |
| `implementation-guide-inputs.json` | Wizard output, feeds Part 4 of the report |
| `.github/MODELS.md` | Which Copilot model to use per task |

## Language policy

- Copilot primitives (this file, `.github/instructions/`, agents, prompts, skills) are written 100% in English.
- User-facing documentation is trilingual: PT (root), EN (`kit-en/`), ES (`kit-es/`).
- Client-facing outputs (reports, chat replies, generated artifacts) follow `respostas.json::metadata.language`, default pt-br.

## Output conventions

- Everything generated goes to `saida/`. Canonical outputs (`scores.json`, `gaps.json`, `recomendacoes.json`, `payload.json`, the 5 PDFs) overwrite the same filename; audit artifacts (import logs, insights, plans, spreadsheets) carry a date in the filename.
- Never invent data: report an unanswered question as "sem resposta" (localized), never guess a level or evidence.
- Do not modify: `framework.json`, `referencia/`, `relatorios/templates/`, `relatorios/i18n/`, `formularios/`, `coleta/`, `docs/`. `.github/hooks` enforces this deterministically on Copilot CLI and the cloud agent; VS Code relies on these instructions.

## Scoring

- Scores are computed only by the script chain: `scripts/compute_scores.py`, then `compute_gaps.py`, then `recommend_strategies.py`. Never recompute scores by hand or in chat.
- Coverage below 25 answered questions is BLOCKED: scores are still computed but flagged as not valid for executive decisions (the kit never refuses to compute).

## Model selection

Model selection per task: see `.github/MODELS.md`.

## Contributors

Run `make smoke` (assessment pipeline) and `make smoke-cross` (all three surveys) before opening a PR.
See `CONTRIBUTING.md` for the full checklist.

## When the client asks "how do I..."

Point to `README.md` (quick start), `GUIA-PASSO-A-PASSO.md` (detailed walkthrough), `coleta/INSTRUCOES-FORMS.md` (Microsoft Forms collection), and `wizard/` (Implementation Guide personalization).
