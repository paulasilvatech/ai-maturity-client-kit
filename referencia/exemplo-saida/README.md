# Final output examples: AI Maturity Assessment Kit

🌐 English · [Português (Brasil)](README.pt-br.md)

> This folder contains **real PDFs generated from `respostas.json.example`** (profile "Cliente Exemplo S.A.", 46 mocked answers). They are the **exact preview** of what the client will generate when running `/pipeline-completo` with their own data.

> **Language note:** generated reports default to **English**; PT-BR and ES are selected through `metadata.language` in `respostas.json`. The example client data sets `metadata.language` to `"pt-BR"`, so the PDFs at the root of this folder are in PT-BR. The [`en/`](en/) and [`es/`](es/) subfolders hold the EN and ES renders of the same client.

## 📊 The 5 main PDFs: Cliente Exemplo S.A. (PT-BR)

| File | Size | Content |
|---|---|---|
| **[score_justification.pdf](score_justification.pdf)** | 323 KB | Score justification: overall **1.99 (L2 Defined)**, breakdown per pillar, PE Readiness with path recommendation |
| **[roadmap_part_pillar_p1.pdf](roadmap_part_pillar_p1.pdf)** | 405 KB | Pillar P1 deep-dive: 9 Productivity capabilities (average **2.69 L3**) |
| **[roadmap_part_pillar_p2.pdf](roadmap_part_pillar_p2.pdf)** | 407 KB | Pillar P2 deep-dive: 10 DevOps capabilities (average **1.52 L2**) |
| **[roadmap_part_pillar_p3.pdf](roadmap_part_pillar_p3.pdf)** | 409 KB | Pillar P3 deep-dive: 9 Platform capabilities (average **1.92 L2**) |
| **[roadmap_part4.pdf](roadmap_part4.pdf)** | 504 KB | Consolidated Implementation Guide (Three Horizons + committees + RACI + comms + training + ADKAR + quick wins) |

**Total:** 5 PDFs · ~75 equivalent pages · clean branding (no monetary values, no Microsoft confidential, per NFR-REPORT-011).

## 🌐 EN version (same client, locale en)

The [`en/`](en/) subfolder has the same 5 PDFs rendered in English (changing only `respostas.json::metadata.language` to `"en"`). The [`es/`](es/) subfolder has the Spanish render (`"es"`).

## 📦 Auxiliary files (pipeline intermediates)

### Main assessment outputs

| File | Source | What it is for |
|---|---|---|
| **[scores.json](scores.json)** | `/calcular-scores` | Raw scores: overall, 3 pillars, 28 capabilities |
| **[gaps.json](gaps.json)** | `/gap-analysis` | 10 gaps ordered by priority (3 P0, 0 P1, 1 P2, 6 P3) |
| **[recomendacoes.json](recomendacoes.json)** | `/recomendar-estrategias` | 6 ranked strategies + technologies |
| **[payload.json](payload.json)** | `/gerar-relatorio` | Full payload sent to Jinja2 (debugging + customization) |
| **[pontuacao-preenchida-2026-05-08.xlsx](pontuacao-preenchida-2026-05-08.xlsx)** | `/preencher-planilha` | Auditable workbook with SUMPRODUCT |
| **[import-log-2026-05-08.md](import-log-2026-05-08.md)** | `/importar-respostas-excel` | Import log (illustrative) |

### ⭐ Developer Survey outputs (anonymous)

| File | Source | What it is for |
|---|---|---|
| **[insights-developer-survey-EXEMPLO.md](insights-developer-survey-EXEMPLO.md)** | `/insights-developer-survey` | Full PT-BR insights report (12 sections, ~8 KB). Generated from the 5 mocks in `survey-devs/respostas-mock-devs.json` |
| **[maturidade-developer-survey-EXEMPLO.json](maturidade-developer-survey-EXEMPLO.json)** | `/insights-developer-survey` | Maturity calculated by the deterministic L0-L4 rubric across the 7 dimensions D2-D8 |

### ⭐ Learning & Growth Survey outputs (identified)

| File | Source | What it is for |
|---|---|---|
| **[plano-capacitacao-EXEMPLO.md](plano-capacitacao-EXEMPLO.md)** | `/plano-capacitacao` | Capacitation plan with the top 10 topics (attendees pre-validated by name+email), Champions Network, mentor pairs, and a 90-day calendar |
| **[implementation-guide-inputs-EXEMPLO.json](implementation-guide-inputs-EXEMPLO.json)** | `/wizard-implementacao` Mode D | Auto-fill that extracts 6 of the 9 wizard inputs directly from the capacitation plan |

## 🧬 How these PDFs were generated (`gerar-relatorio` algorithm)

```
respostas.json.example          (client input: 46 mocked answers)
    ↓
/calcular-scores  →  saida/scores.json
    ↓
/gap-analysis     →  saida/gaps.json
    ↓
/recomendar-estrategias  →  saida/recomendacoes.json
    ↓
/gerar-relatorio invokes relatorios/scripts/build_payload_and_render.py:
  ├─ Loads relatorios/sample_payload.json (full structure, ~28 caps with rich narrative)
  ├─ OVERWRITES only the fields we have data for:
  │   • organization                    ← respostas::metadata
  │   • scores.overall.weighted_avg     ← scores.json
  │   • scores.pillars[].weighted_avg   ← scores.json
  │   • capabilities[].current_score    ← scores.json (matched by id)
  │   • gap_analysis[]                  ← gaps.json (rebuilt structure)
  │   • implementation_guide_inputs.*   ← implementation-guide-inputs.json (if it exists)
  ├─ KEEPS the sample's professional placeholders for fields without data:
  │   • capabilities[].scoring_rationale, h1_initiatives, evidence_collected
  │   • technology_resources_per_pillar
  │   • risks_per_pillar, success_metrics_per_pillar, next_steps_per_pillar
  │   • horizons (narrative)
  │   • executive_steering_committee, RACI, comm/training plan (if the wizard did not run)
  └─ Renders via render_reports.py:
      Jinja2 + i18n (pt-br/en/es) + WeasyPrint → 5 PDFs
```

## 🎯 Cliente Exemplo S.A. results

### Overall maturity

- **Overall:** **1.99** (L2 Defined)
- **Threshold:** OK (46/158 answered, a realistic lean profile)
- **Coverage per pillar:** P1 = 13/53 · P2 = 18/59 · P3 = 15/46

### Per pillar

| Pillar | Score | Label | Strong/Weak |
|---|---|---|---|
| **P1** Productivity | **2.69** | L3 Managed | 💪 Copilot well adopted |
| **P2** DevOps | **1.52** | L2 Defined | ⚠️ Weak DevSecOps |
| **P3** Platform | **1.92** | L2 Defined | ⚠️ Weak Agentic Applications |

### Top 3 P0 gaps (critical)

1. **P3-C5** Agentic Applications: gap 3.17 → priority 3.17 → strategy **S6**
2. **P2-C4** DevSecOps: gap 2.75 → priority 3.30 → strategy **S7**
3. **P2-C10** Supply Chain Security: gap 2.33 → priority 2.57 → strategy **S7**

### Top 3 recommended strategies

1. **S7** Security & Governance: cumulative priority **5.87** (2 P0 capabilities)
2. **S6** Agentic Activation: cumulative priority **3.92** (2 P0 capabilities)
3. **S5** GitHub Copilot Acceleration: cumulative priority **3.01** (4 capabilities)

### Strategies without relevant gaps

- S1 GitHub Migration · S3 App Modernization · S4 AI Applications

## 🧪 How to reproduce (with your data or mocked data)

```bash
# Use mocked data (same PDFs as this folder)
cp respostas.json.example respostas.json

# OR use your real data (fill in manually)
# edit respostas.json

# Full pipeline
/pipeline-completo
# (or the 5 individual commands, see the root README.md)

# Outputs go to saida/ and should be identical to the ones in this folder
```

## ⚠️ Known limitations (and how to work around them)

Some sections of the PDFs **keep placeholders from sample_payload.json** (Acme Insurance Group) for fields where we have no structured client data. Specifically:

- `executive_steering_committee` (5 Acme names: Maria Santos, James Carter…)
- `tpo`, `raci_matrix`, `communication_plan`, `training_plan`, `adkar_notes`
- `quick_wins_w1_4` / `w5_8` / `w9_12`
- Per capability: `scoring_rationale`, `h1_initiatives`, `evidence_collected`, `h2_key_enabler`, horizons narrative
- Detailed `technology_resources_per_pillar` (H1/H2/H3 tables per pillar)
- `risks_per_pillar` / `success_metrics_per_pillar` / `next_steps_per_pillar`

### How to customize

**For the Implementation Guide (Part 4):**
```
/wizard-implementacao   # 9 steps fill in all of Part 4
/gerar-relatorio        # re-renders with real data
```

**For per-capability narrative (scoring_rationale, h1_initiatives, etc.):**
```bash
# Manually edit saida/payload.json (replace the Acme placeholders)
code saida/payload.json

# Re-render (skips the merge step)
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
```

---

**Renderer:** WeasyPrint 68.1 + Jinja2 · **Templates:** the same as the production platform (`app/src/report-service/templates/`) · **Date:** 2026-05-08
