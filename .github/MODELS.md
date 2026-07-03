# Model guidance per task type

The kit's 14 Copilot primitives fall into 4 task groups. Pick the cheapest model that is first-time-right for the group; step up only when quality actually falls short.

| Task group | Primitives | Model (picker name / CLI slug) | Price per 1M tokens (in/out) | Multiplier / tier |
|---|---|---|---|---|
| Mechanical import | `/import-assessment-responses`, `/import-developer-survey`, `/import-learning-survey`, `/fill-spreadsheet` | Claude Haiku 4.5 / `claude-haiku-4.5` | $1 / $5 | 0.33x (Versatile) |
| Script / compute | `/calculate-scores`, `/gap-analysis`, `/recommend-strategies`, `/generate-reports` | GPT-5 mini / `gpt-5-mini` | $0.25 / $2.00 | 0.33x (Lightweight) |
| Analytical synthesis | `/insights-developer-survey`, `/training-plan` | Claude Sonnet 5 / `claude-sonnet-5` (fallback: Claude Sonnet 4.6) | $2 / $10 | Versatile (no legacy multiplier) |
| Interactive orchestration | `@ai-maturity-assistant` agent, `/run-full-pipeline` prompt, `/implementation-wizard`, `/ai-maturity-reports` | Claude Sonnet 4.6 / `claude-sonnet-4.6` | $3 / $15 | 9x (Versatile) |

## Why these picks

- **Mechanical import**: deterministic openpyxl parsing with explicit column rules. A lightweight model is already first-time-right; anything bigger only adds cost and latency.
- **Script / compute**: fully specified algorithms executed via Python scripts (`SUMPRODUCT`, fixed action tables). GPT-5 mini is the cheapest reliable default for writing/running small deterministic code and checking its output.
- **Analytical synthesis**: client-facing PT-BR narrative reports (12+ sections, quotes, cross-referenced recommendations). Mid-tier synthesis quality pays for itself; use Claude Sonnet 4.6 if narrative quality or capability cross-referencing falls short.
- **Interactive orchestration**: long-horizon multi-step state machines with handoffs. Claude Sonnet 4.6 is the Copilot CLI default for general-purpose work and one of the few cloud-agent models, so one pin works on every surface.

## Where the pin lives

- **Agent** (`.github/agents/*.agent.md`) and **prompt** (`.github/prompts/*.prompt.md`) frontmatter support a `model:` key. Use the **single-string** display-name form (e.g. `model: Claude Sonnet 4.6`): Copilot CLI rejects the VS Code array form (github/copilot-cli#2133).
- **Skills cannot pin a model**: the Agent Skills spec defines no `model` field in `SKILL.md`. Skill rows above are recommendations you apply via the picker, or they inherit the agent/prompt pin when run inside `@ai-maturity-assistant` or `/run-full-pipeline`.

## How to select a model

- **VS Code**: use the model picker dropdown in the Copilot Chat input; pinned `model:` frontmatter overrides the picker for that agent/prompt.
- **Copilot CLI**: `/model` slash command in a session, `--model=<slug>` flag, or the `COPILOT_MODEL` environment variable (slugs, e.g. `--model=claude-haiku-4.5`).
- **Auto**: selecting `auto` on any paid plan gives a 10% credit discount and routes around rate limits; fine whenever you do not care about the specific model.

Model availability varies by plan, client, and admin policy; review pins against the supported-models page periodically.

## Sources

1. Supported models and per-client availability: https://docs.github.com/en/copilot/reference/ai-models/supported-models
2. Task-type guidance: https://docs.github.com/en/copilot/reference/ai-models/model-comparison
3. Pricing and multipliers: https://docs.github.com/en/copilot/reference/ai-models/supported-models and https://github.com/github/docs/blob/main/data/tables/copilot/models-and-pricing.yml
4. Prompt-file and custom-agent `model:` frontmatter: https://code.visualstudio.com/docs/copilot/customization/prompt-files and https://docs.github.com/en/copilot/reference/custom-agents-configuration
5. CLI model selection: https://docs.github.com/en/copilot/how-tos/copilot-cli
