---
name: implementation-wizard
description: Collects the 9 implementation-guide inputs (steering committee, TPO, RACI, comms plan, training plan, ADKAR, 3 quick-win waves) that feed Part 4 of the PDF report, via HTML wizard, JSON template, chat, or auto-fill from the Learning Survey. Use when the user asks for "wizard", "implementation guide", "guia de implementação", "preencher parte 4", "asistente de implementación", "TPO", "steering committee", "RACI", "ADKAR", "quick wins".
argument-hint: optional "chat" to force conversation mode (default: offer all modes)
---

# Skill: Implementation Guide Wizard

## Purpose
Populate `implementation-guide-inputs.json` at the workspace root. `/generate-reports` merges this file into the payload that renders **Part 4 of the PDF report** (consolidated Implementation Guide). Four modes produce the same artifact.

## The four modes (each explained once)

### Mode A: standalone HTML wizard
Open `wizard/implementation-guide-wizard.html` in a browser. 9 steps, saves progress to localStorage, exports the JSON at the end. Best for visual users. Nothing to do in chat: confirm the path and stop.

### Mode B: edit the JSON template
Copy `wizard/implementation-guide-inputs.template.json` to the workspace root as `implementation-guide-inputs.json` and edit each field. Best for users comfortable in an editor.

**WARNING:** the template field values are instructional prose with embedded examples (fictitious names such as "Maria Santos"). The user must REPLACE each field's text entirely with their own content; shipping the instructions or example names into the PDF is a defect. Validate that no field still starts with instructional text before accepting the file.

### Mode C: guided chat (this skill)
Ask the 9 questions ONE at a time, in the client language, waiting for each answer:
1. Executive steering committee (5-8 members: sponsor, program lead, finance, security, change champion)
2. Technology Product Owner (TPO): program manager, members, decision authority
3. RACI matrix (5-8 key activities with Responsible/Accountable/Consulted/Informed)
4. Communication plan (per audience: channel, frequency, owner)
5. Training plan (per audience: format, cadence, completion criteria)
6. ADKAR change management (1-3 interventions per stage)
7. Quick wins weeks 1-4 (4-6 items with target week)
8. Quick wins weeks 5-8 (expansion wave)
9. Quick wins weeks 9-12 (consolidation before H2 scale)

Then show a summary, ask for confirmation, and write the JSON (schema below). Do not invent answers for vague input: ask for detail or accept and mark minimal. Markdown in answers is fine (it renders in the PDF). Empty fields: warn but allow saving (render-time placeholders kick in).

### Mode D: auto-fill from the Learning Survey
```bash
python3 wizard/scripts/auto_fill_from_plano.py
```
Consumes the latest `saida/plano-capacitacao-*.json` (emitted by `/training-plan`; a `.md` regex fallback exists but loses detail) and writes `implementation-guide-inputs.json` with **6 of 9 inputs** auto-filled: steering committee (from active Champions), communication plan, training plan (cohorts), the ADKAR Knowledge stage, and the 3 quick-win waves (from the 90-day calendar). The user still fills `tpo` and `raci_matrix` manually, then reruns `/generate-reports`.

## Choosing a mode
1. If `saida/plano-capacitacao-*.json` exists, offer Mode D FIRST and recommend it.
2. Otherwise present modes A/B/C and let the user choose (argument "chat" forces Mode C).

## Output
- `implementation-guide-inputs.json` at the workspace root (NOT `saida/`), so it persists across pipeline runs as an input.
- This file is gitignored client data and may contain names/emails: NEVER commit or share it.
- The 9 keys under `implementation_guide_inputs` (mirroring `relatorios/sample_payload.json`): `executive_steering_committee`, `tpo`, `raci_matrix`, `communication_plan`, `training_plan`, `adkar_notes`, `quick_wins_w1_4`, `quick_wins_w5_8`, `quick_wins_w9_12`. Plus `metadata` with `generated_at` (ISO-8601 UTC), `generator`, `completion_pct`.

## Chat report
After writing the file (Mode C or D), report in the client language (`respostas.json::metadata.language`, default pt-br): file path, completion percentage, which fields remain manual, and the next step. Example client-facing output (compose in the client language):
```
Guia de implementação salvo: implementation-guide-inputs.json (6/9 campos, 67%)
Faltam preencher manualmente: tpo, raci_matrix
Próximo passo: editar esses 2 campos e rodar /generate-reports
```

## Constraints
- NEVER modify `framework.json`, `respostas.json`, or `relatorios/templates/`.
- Editing `implementation-guide-inputs.json` later and rerunning `/generate-reports` is enough; no need to redo the wizard.
