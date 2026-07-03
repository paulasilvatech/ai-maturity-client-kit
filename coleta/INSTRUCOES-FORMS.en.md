# How to create the Microsoft Forms for the AI Maturity Assessment

**`🅰️ ASSESSMENT`** · 📖 [🏠 Index](../README.en.md) · [« Step-by-step guide](../GUIA-PASSO-A-PASSO.md) · You are here · [» Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.md)

> [!TIP]
> This guide shows **3 paths** to create and use Microsoft Forms with the 158 questions. Pick the one that best fits your available time and the team's technical profile.

---

## ⚖️ Quick comparison of the 3 paths

| Path | Setup time | Effort | When to use |
|---|---|---|---|
| **A. Full manual Forms** | 4-6 hours | High (create 158 questions) | You want a 100% native Forms experience, with sections and branding |
| **B. Lean Forms (1 pilot capability)** | 30 minutes | Low | PoC or validation with a few respondents before scaling |
| **C. Directly in Excel/SharePoint** ⭐ | 5 minutes | Minimal | **Recommended**: uses the Excel template that ships with the kit, saves 4h of creation |

---

## 🅰️ Path A: full manual Forms (158 questions)

### Step 1 · Create the Forms

1. Go to https://forms.office.com (sign in with your Microsoft 365 account)
2. Click **+ New Form**
3. Title: `AI Maturity Assessment - <Your organization name>`
4. Subtitle (optional):
   ```
   AI maturity assessment across 3 pillars: Productivity, DevOps, and Platform.
   158 questions on an L0-L4 scale. Estimated time: 45-90 minutes.
   Your answers are confidential and used only to generate the roadmap.
   ```

### Step 2 · Configure 3 sections

Add 3 sections (button **+ Add new** → section icon):

| Section | Title | Suggested subtitle |
|---|---|---|
| 1 | **Pillar P1: Developer Productivity** | 53 questions in 9 capabilities |
| 2 | **Pillar P2: DevOps Lifecycle** | 59 questions in 10 capabilities |
| 3 | **Pillar P3: Application Platform** | 46 questions in 9 capabilities |

### Step 3 · Add the 158 questions

For each question, add **2 elements** in Forms:

1. **Choice (single answer)** with the question + the 6 level options
2. **Long Text** (optional) for evidence

Use the document [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md) as your copy/paste source. It has the 158 questions formatted with IDs (`P1-C1-Q1`, etc.) and the full text.

#### Fixed options for ALL questions (paste them identically)

```
L0 — Initial — No established practice
L1 — Developing — Isolated pilots (<25%)
L2 — Defined — 25-50% coverage with guidelines
L3 — Managed — >75% with impact metrics
L4 — Optimizing — Universal (>95%) with continuous automation
NA — I do not know / Not applicable
```

> ⚠️ **CRITICAL:** the `L0`, `L1`, ..., `L4`, `NA` prefix must be **literally at the beginning** of each option. The import skill uses that prefix to map back to the number (0-4 or null). Do not translate it, do not reformat it.

#### Format of each question title

```
P1-C1-Q1: <question text>
```

> ⚠️ **IMPORTANT:** the ID (`P1-C1-Q1`) must be **literally at the beginning** of the question title, followed by `:`. Example from [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md):
>
> `P1-C1-Q1: Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?`

#### Format of the evidence field

```
Evidence (P1-C1-Q1)
```

Type: **Long Text**, optional (do not mark as required).

### Step 4 · Configure permissions

1. **Settings** button (gear) in the top-right corner
2. **Who can fill out this form**:
   - **Only people in my organization**: recommended for internal use
   - **Anyone with the link**: for cross-company use (consulting)
3. **One response per person**: disabled (we want multiple responses to aggregate)
4. **Email notification of each response**: optional

### Step 5 · Share

1. **Send/Collect responses** button
2. Copy the link
3. Share it via Email/Teams/SharePoint with the team

### Step 6 · Export responses

Once you have enough responses (recommended: 3 or more respondents to reduce bias):

1. **Responses** tab
2. **Open in Excel** button
3. Save the file as **`respostas-forms.xlsx`**
4. Move it to the root of `kit-cliente/`

### Step 7 · Import into the kit

In VS Code, open Copilot Chat (**Agent** mode) and type:

```
/import-assessment-responses
```

The skill:
- Detects `respostas-forms.xlsx` automatically
- Backs up the current `respostas.json`
- Aggregates multiple respondents via a per-question mean
- Overwrites `respostas.json`
- Generates `saida/import-log-<DATE>.md`

Then run `/run-full-pipeline` as usual.

---

## 🅱️ Path B: lean Forms (1 pilot capability)

To **validate the flow end-to-end** before investing in the full creation.

### Step 1 · Pick 1 capability

Pick 1 capability with 5-7 questions. Suggestion: **P1-C1 (AI Coding Assistants)**, the "hottest" topic and one that sparks good team discussion.

### Step 2 · Create the Forms with only those 5 questions

Same process as Path A, but with only **5 questions** instead of 158. Time: 15-30 min.

### Step 3 · Collect 3-5 responses

Share it with your immediate team (not the whole company). Time: 1-2 days.

### Step 4 · Import and run

Since `respostas.json` will have only 5 answered questions, the **threshold will be BLOCKED** (25 or more are required). But:
- You validate that the Forms → Excel → respostas.json flow works
- You see how a capability with real data shows up in the report

To generate a useful report, complete the rest manually via `respostas.json` or expand the Forms.

---

## 🅲 Path C: directly in Excel/SharePoint ⭐ (RECOMMENDED)

Skips Forms and uses the **Excel template** that ships with the kit.

### Step 1 · Get the template

The kit ships with [`coleta/template-export-forms.xlsx`](template-export-forms.xlsx). This file:
- Has the **same format** Forms would export
- Already has the 158 question columns + 158 evidence columns
- Comes with **3 mocked respondents** as an example (you can delete and replace them)

### Step 2 · Upload to SharePoint/OneDrive

1. Clear the 3 mocked respondent rows (rows 2, 3, 4), keeping only the header
2. Rename it: `respostas-forms.xlsx` (or another name)
3. **SharePoint:** upload to the project library and generate an "Anyone with the link can edit" link
4. **OneDrive:** upload and share with edit access
5. **Teams:** attach it in the channel and pin it

### Step 3 · Each respondent fills in one row

Share these instructions:

```
Hello team!

Please fill in ONE row per person in this file:
<SharePoint link>

For each of the 158 question columns:
- Select a level L0-L4 (or leave it blank if you "do not know")
- The text must start with the code (e.g.: "L3 — Managed")
- Use the Evidence column right next to it to describe tool/coverage/metric

Estimated time: 45-90 min. You can pause and come back.

Questions? Check the documents in referencia/P*.md (in kit-cliente).
```

### Step 4 · Download the Excel

Once everyone has filled it in:
1. SharePoint → file → **Download a Copy**
2. Rename it to **`respostas-forms.xlsx`**
3. Move it to the root of `kit-cliente/`

### Step 5 · Import and run

```
/import-assessment-responses
/run-full-pipeline
```

---

## 🆚 Forms vs direct Excel: which one to choose?

| Criterion | Microsoft Forms | Excel/SharePoint |
|---|---|---|
| **Setup time** | 4-6h (create 158 questions) | 5 min (ready-made template) |
| **Respondent UX** | Mobile-friendly, 1 question at a time | Spreadsheet (intimidating for non-technical people) |
| **Data validation** | Fixed (Choice = only 6 options) | Fragile (people can type anything) |
| **Multi-respondent** | Native | Manual (1 row per person) |
| **Later editing** | Hard (each submit is final) | Easy (anyone can change anything at any time) |
| **Audit trail** | Native (timestamp per submit) | SharePoint version history |
| **License cost** | Standard Microsoft 365 | Standard Microsoft 365 |
| **Kit integration** | Identical (`/import-assessment-responses`) | Identical |

**Practical recommendation:**
- **PoC / Small team (3-5 people):** direct Excel (Path C)
- **Organization-wide roll-out (10+ respondents):** Forms (Path A)
- **Demanding client / professional branding:** Forms (Path A)

---

## 🔄 Other formats supported by the skill

The `/import-assessment-responses` skill accepts any Excel/CSV whose question headers start with `P[1-3]-C\d+-Q\d+:`. That includes:

- ✅ **Microsoft Forms** export (official format)
- ✅ **Google Forms** export (Sheets → Download as .xlsx)
- ✅ **Excel/SharePoint** custom (the kit's template or your own)
- ✅ **CSV** (if renamed to .xlsx or converted)
- ⚠️ **Typeform**: works if you adjust the headers to include the IDs

---

## 💡 Practical tips

### Tip 1 · Start with 1 pillar
Do not try to collect answers for all 3 pillars at the same time. Start with P1 (Productivity), the most tangible one for devs. Then P2 (DevOps) with SREs. Then P3 (Platform) with architects.

### Tip 2 · Pre-fill via interview
Instead of sending the link and waiting, run a **1h interview per respondent**, filling it in together. You capture nuances better and produce richer evidence.

### Tip 3 · Train before releasing it
Run a **30 min kick-off** explaining:
- What the assessment is
- How L0-L4 levels are defined
- Why evidence matters
- How long it will take
- When they will receive the report

### Tip 4 · Run short cycles
Do not wait for 100% of the responses to run `/run-full-pipeline`. Run it with 25 (WARNING), then 50 (OK), then 100. With each cycle the report improves and you capture more conversations.

### Tip 5 · Versioning
Every time you import, the skill creates `respostas.json.backup-<timestamp>`. Keep those backups: they are your **evolution history** between assessment rounds.

---

## 🆘 Troubleshooting

| Problem | Diagnosis | Solution |
|---|---|---|
| Skill does not detect `respostas-forms.xlsx` | File is not at the root | Move it to `kit-cliente/respostas-forms.xlsx` (not inside coleta/) |
| "No recognized header" | Excel headers do not start with `P1-C1-Q1:` etc. | Edit headers manually to include the IDs at the beginning |
| A respondent appears duplicated | Forms allows multiple submissions from the same person | Manually edit the Excel to delete the duplicated row before importing |
| Levels became free text | Forms exported options WITHOUT the `L0/L1/...` prefix | Rebuild the Forms including the prefixes at the beginning of each Choice option |
| Excel has 158 columns but only 90 recognized questions | Headers truncated by Forms (4000-char limit) | Shorten the question text in Forms (keep only the ID + a summarized sentence) |

---

## 📚 References

- **Full list of the 158 questions formatted for Forms:** [`perguntas-para-forms.en.md`](perguntas-para-forms.en.md)
- **Ready-made Excel template (3 mocked respondents):** [`template-export-forms.xlsx`](template-export-forms.xlsx)
- **Import skill:** [`../.github/skills/import-assessment-responses/SKILL.md`](../.github/skills/import-assessment-responses/SKILL.md)
- **Multi-respondent aggregation algorithm:** [`../referencia/pontuacao-e-calculo.md`](../referencia/pontuacao-e-calculo.md) section 6

---

**Version:** 1.0 · **Date:** 2026-05-08

---

## Stuck on any of these steps?

<details>
<summary><strong>FAQ: common questions about collection via Forms</strong></summary>

| Symptom | Probable cause | How to fix |
|---|---|---|
| **Open in Excel** is disabled in Forms | Your account has no M365 license / Forms is on a personal account | Ask an admin to move the Forms to the organizational account |
| I have multiple respondents, how do I aggregate them? | Default skill behavior | `/import-assessment-responses` computes an **automatic mean** per question |
| Column headers do not start with `P1-C1-Q1:` | You did not follow the pattern when creating the Forms | Edit the question titles in Forms to include the ID at the beginning |
| Sharing the Forms with people outside the org | Forms Settings restrict access | Settings → **Anyone with the link can respond** |
| The Excel comes with extra columns (ID, Start time, ...) | Default Forms behavior | The skill ignores columns A-E automatically |
| `respostas-forms.xlsx` is not detected | File is inside `coleta/` instead of the root | Move it to the **root** of the kit |

</details>

---

## Continue reading

| ← PREVIOUS | NEXT → |
|:---|---:|
| **[Step-by-step guide](../GUIA-PASSO-A-PASSO.md)** | **[Developer Survey (anonymous)](../survey-devs/INSTRUCOES-FORMS-DEVS.md)** |
| From zero to the executive PDF in 60-90 min. | 75 anonymous questions about Copilot, agents, governance, MCP / A2A. |

↑ [Back to the kit index](../README.en.md)
