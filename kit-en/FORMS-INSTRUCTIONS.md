# Microsoft Forms Instructions · English Edition

> How to publish the 3 surveys as Microsoft Forms and aggregate the responses back into the kit.

🏠 [README](README.md) · 📘 [Step-by-step](STEP-BY-STEP.md) · 🇧🇷 [PT-BR](../coleta/INSTRUCOES-FORMS.md)

---

## Why Microsoft Forms?

The 3 HTML surveys at `formularios/` are convenient for individual fill, but you usually want **multiple respondents** (3-5 from leadership, 5+ devs anonymous, 3+ devs identified for learning). Microsoft Forms makes that easy:

- ✅ Native multi-respondent collection
- ✅ Excel export with all responses in one file
- ✅ Anonymous mode (for the Developer Survey)
- ✅ Required fields validation
- ✅ Mobile-friendly

## Form A · AI Maturity Assessment (158 questions)

### Create the form

1. Go to <https://forms.office.com> and create a new form.
2. Use the question bank in `coleta/perguntas-para-forms.md` (Portuguese) — copy each question.
3. For each question:
   - Set type to **Choice** with 5 options: `L0 (Initial)`, `L1 (Developing)`, `L2 (Defined)`, `L3 (Managed)`, `L4 (Optimizing)`.
   - Add an optional **Long text** for evidence/comments.
4. Use **Sections** to group by pillar (P1, P2, P3).
5. Recommended fill time: 60-90 minutes for the full survey, or distribute across leaders by pillar.

### Collect responses

1. Share the link with **3 to 5 leadership members**.
2. Wait until the response window closes.
3. Click **Open in Excel** → save as `respostas-forms.xlsx` at the kit workspace root.

### Aggregate into the kit

```
/importar-respostas-excel
```

The skill computes a **simple average per question** across all respondents (same behavior as the production platform) and writes `respostas.json` ready for `/pipeline-completo`.

## Form B · Developer Survey (75 questions, anonymous)

1. Create the form using questions from `survey-devs/perguntas-para-forms-devs.md`.
2. In **Settings**: enable **anonymous responses** (do NOT require email or sign-in).
3. Share with all developers in scope (5+ minimum recommended).
4. Export as `respostas-survey-devs.xlsx` to the workspace root.
5. Run:

```
/importar-survey-devs
/insights-developer-survey
```

Output: `saida/insights-developer-survey-<DATE>.md` with adoption metrics, governance gaps, anonymized quotes, and recommendations linked to the maturity capabilities.

## Form C · Learning & Growth Survey (32 questions, identified)

> [!IMPORTANT]
> This survey requires **name + email** because the output includes attendee lists, cohort assignments, and mentor↔mentee pairs. Make sure participants consent to this in advance.

1. Create the form using questions from `survey-learning/perguntas-para-forms-learning.en.md` (English). The canonical PT-BR bank is also available at `survey-learning/perguntas-para-forms-learning.md`.
2. In **Settings**: require **name and email** as mandatory fields. Disable anonymous mode.
3. Share with all developers who will receive training (3+ minimum recommended).
4. Export as `respostas-survey-learning.xlsx` to the workspace root.
5. Run:

```
/importar-survey-learning
/plano-capacitacao
```

Output: `saida/plano-capacitacao-<DATE>.md` with top 10 demanded topics, cohorts per dimension D2-D8 with attendee names, Champions Network candidates, mentor↔mentee pairs, and a 90-day workshop calendar.

## Recommended workflow

For serious consulting engagements, run all 3 in this order:

```
1. Survey B (anonymous devs)    → behavioral baseline
2. Survey C (identified devs)   → capacitation roadmap with attendees
3. Survey A (leadership)        → informed organizational assessment
4. /wizard-implementacao         → cross-validates and auto-fills the Implementation Guide
5. /pipeline-completo            → generates the final 5 PDFs
```

This sequence makes the leadership assessment **data-informed** rather than aspirational, and produces a capacitation plan with concrete names.

## Translating the questions

The Assessment and Developer Survey question banks (`coleta/perguntas-para-forms.md`, `survey-devs/perguntas-para-forms-devs.md`) are still canonical Portuguese (Brazil) because they map to validated framework IDs and need human review for native translations. The Learning & Growth Survey already has English and Spanish banks:

- `survey-learning/perguntas-para-forms-learning.en.md`
- `survey-learning/perguntas-para-forms-learning.es.md`

You can:

- **Translate for the respondents** when typing into Microsoft Forms — the IDs stay the same in the Excel export.
- **Keep the IDs in PT-BR** in the JSON output — the PDFs are rendered in English via `relatorios/i18n/en.json`.

If you want a fully translated question bank, open an issue: <https://github.com/paulanunes85/ai-maturity-client-kit/issues/new>

## Stuck on a step?

| Problem | Fix |
|---|---|
| Excel columns don't match question IDs | Check that you didn't reorder questions in Forms — IDs are positional |
| `/importar-respostas-excel` fails | Make sure file is at workspace root and named exactly `respostas-forms.xlsx` |
| Anonymous responses missing for survey C | Survey C requires name+email — re-publish without anonymous mode |
| Empty responses break aggregation | The skill skips empty cells; leave them blank rather than putting "N/A" |

## Continue reading

| ⬅ Previous                       | Next ➡                                           |
| :------------------------------- | -----------------------------------------------: |
| [📘 Step-by-step](STEP-BY-STEP.md) | [🌐 Site](https://paulanunes85.github.io/ai-maturity-client-kit/en/) |

---

**Paula Silva** — Software Global Black Belt | paulasilva@microsoft.com
