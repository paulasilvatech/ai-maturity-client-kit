# How to create the Microsoft Forms for the Learning & Growth Survey

**`🅲️ SURVEY-LEARNING`** · _identified_ · 📖 [🏠 Index](../README.en.md) · [« Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.md) · You are here · [» Wizard](../wizard/README.en.md)

> [!WARNING]
> Unlike the other 2 surveys, this one is **IDENTIFIED** (name + email required). It has 32 questions in 7 sections to build the team's **personalized capacitation roadmap**: workshops, cohorts, Champions Network, mentoring. Estimated time per dev: **5-8 min**.

**Different from the other 2 surveys:**
- Main assessment: organizational maturity (Likert L0-L4 declared by leadership)
- Developer Survey: ANONYMOUS real behavior
- **This Learning Survey: IDENTIFIED capacitation roadmap**; it needs name+email to invite the right people to the right workshops

---

## ⚠️ Why IDENTIFIED (not anonymous)?

To generate actionable value, this survey **needs to know who is who**:
- Invite **the right people** to each workshop (10 pre-validated attendees beats "70% showed interest")
- Build the **Champions Network** with names (not anonymous)
- Map **mentor-mentee pairs** (you need a name on both sides)
- Assign an **owner** to the identified quick wins

**Honest trade-off:** some questions (e.g. "what is your level in D8 Security?") may be answered less honestly if devs feel judged. Therefore:
- Leadership must **communicate clearly**: "answers are used to TRAIN, not to EVALUATE performance"
- Do not use the answers in performance reviews
- Share the consolidated plan with the whole team (transparency)

If your organization prefers **pure anonymity**: run the **Developer Survey** (`survey-devs/`) in parallel and use the deterministic rubric as an "objective thermometer".

---

## 📋 The 7 topics covered

| # | Section | Focus | Q |
|---|---|---|---|
| **L1** | Identification | Name, email, role, team | 4 |
| **L2** | AI maturity self-perception | L0-L4 self-assessment across the 7 dimensions D2-D8 | 7 |
| **L3** | Where you want to grow | Top 3 priority dimensions (next 6 months) + why | 2 |
| **L4** | Specific topics | Copilot, Foundry, practices (TDD/SDD), agents, security; checkbox | 5 |
| **L5** | Format and cadence | Hands-on workshop, cohort, self-paced, schedules, time/week | 4 |
| **L6** | Champions and mentoring | Want to be a Champion? Mentoring? Who is a reference? | 5 |
| **L7** | Barriers and Wishlist | What blocks you + desired workshops + speakers | 5 |
| | | **TOTAL** | **32** |

---

## 🛠️ How to create the Forms (step by step)

### Step 1 · Create the form

1. Go to <https://forms.office.com> → **+ New Form**
2. Title: `AI Learning & Growth — What do you want to learn in the next 6 months?`
3. Subtitle (paste):

```
5-8 min survey about your AI capacitation plan.

⚠️ IDENTIFIED: we will use your name+email to INVITE you to the right
workshops/cohorts. Individual answers will NOT be shared publicly;
only aggregated insights + attendee lists per workshop.

Output: personalized capacitation plan + cohorts + Champions Network.
```

### Step 2 · ⚠️ CONFIGURE as IDENTIFIED (not anonymous)

**Settings (⚙️):**

| Setting | Value |
|---|---|
| **Anonymous responses** | ☐ **UNCHECKED** (we want identification) |
| **Who can respond** | "Only people in my organization" (recommended) |
| **One response per person** | ☑ CHECKED (1 per dev) |
| **Accept responses** | ☑ CHECKED |
| **Customize thank you message** | "Thank you! You will receive workshop invitations based on your answers." |

> 🔍 **Different from the Developer Survey** (`survey-devs/INSTRUCOES-FORMS-DEVS.md`): there you turn Anonymous ON, here you leave it OFF.

### Step 3 · Create the 7 sections

```
Section 1: L1 — Identification                 (4 questions)
Section 2: L2 — Self-perception (D2-D8)        (7 questions)
Section 3: L3 — Where you want to grow         (2 questions)
Section 4: L4 — Specific topics                (5 questions)
Section 5: L5 — Format and cadence             (4 questions)
Section 6: L6 — Champions and mentoring        (5 questions)
Section 7: L7 — Barriers and Wishlist          (5 questions)
```

### Step 4 · Add the 32 questions

Use [`perguntas-para-forms-learning.en.md`](perguntas-para-forms-learning.en.md) as the copy/paste source.

**For each question:**

1. Type:
   - `choice` (Single answer) → **Choice**
   - `multi` (Multiple answers) → **Choice** with Multiple answers CHECKED
   - `text-short` (Short Text, one line) → **Short answer**
   - `text` (Long Text) → **Long answer**

2. **The TITLE ALWAYS starts with the ID + colon**:
   ```
   L4-Q1: Which GitHub Copilot topics do you want to master?
   ```

3. **Required**: mark **L1-Q1 (name) + L1-Q2 (email)** as required. All others are optional (devs can skip).

### Step 5 · Customize L1-Q4 (squad list)

Question L1-Q4 ("Team / Squad") has the placeholder `[Customize with the organization's team list]`; replace it with the real squad names of your organization. Example:

```
- Payments Squad
- Onboarding Squad
- Platform Squad
- SRE Core
- Data Platform
- Other / I do not belong to a fixed squad
```

### Step 6 · Share

1. **+ Send / Collect responses** → **Link**
2. Share with **ALL devs**:
   - Email from the engineering leader: "Over the next 2 weeks we want to hear what you want to learn in AI. It is a 5-8 min survey, IDENTIFIED. Output: a personalized capacitation plan."
   - Slack/Teams channel #engineering
   - All-hands (present the link)

3. **Deadline:** 2 weeks. Reminders at D+7 and D+12.

### Step 7 · Track responses

- The **Responses** tab shows the count in real time
- Recommended: **minimum 5 devs**, ideally **>50% of the team**
- Since it is identified, you can see "X of Y devs have not answered yet" and follow up 1-on-1

### Step 8 · Export

1. **Responses → Open in Excel**
2. Save as **`respostas-survey-learning.xlsx`**
3. Move it to the **root of `kit-cliente/`**
4. Verify: columns D (Email) and E (Name) must be FILLED IN

### Step 9 · Analyze with the kit

In Copilot Chat (Agent mode):

```
/import-learning-survey
```

Generates `survey-learning/respostas-learning.json` (structured).

```
/training-plan
```

Generates `saida/plano-capacitacao-<DATE>.md` (plus a structured `.json` twin) with:
- Top 10 requested topics (with the list of pre-validated attendees)
- Suggested cohorts per dimension D2-D8
- Identified Champions Network (3 tiers)
- Mentor-mentee pairs
- Workshop calendar (next 90 days)
- Prioritized barriers
- 5 prioritized actions (impact × ease)
- Connection with /insights-developer-survey + /calculate-scores

### Step 10 · ⭐ Wizard auto-fill (Mode D)

After generating the plan, when you run `/implementation-wizard` the Copilot Agent **automatically detects** `saida/plano-capacitacao-*.json` (the structured twin of the `.md`; a markdown fallback exists but loses detail) and offers **Mode D: Auto-fill**, which fills **6 of the 9 wizard inputs** automatically via `wizard/scripts/auto_fill_from_plano.py`:

| Wizard input (Part 4 of the PDF) | Comes from |
|---|---|
| `executive_steering_committee` | Champions Network "active" |
| `communication_plan` | Workshop calendar |
| `training_plan` | Cohorts per dimension |
| `adkar_notes` | Top 5 workshops (Knowledge stage) |
| `quick_wins_w1_4` / `quick_wins_w5_8` / `quick_wins_w9_12` | 90-day calendar |

You only need to fill in manually: **TPO** + **RACI Matrix** (which the learning survey does not cover).

**Estimated savings:** 30-45 min of manual wizard work. And the data is REAL from your team, not sample placeholders.

### Step 11 · Re-render the PDFs with the plan + wizard auto-fill

```
/generate-reports
```

The skill detects:
- ✅ `implementation-guide-inputs.json` (from the wizard Mode D auto-fill) → populates Part 4 with your Champions and workshops
- ✅ `saida/plano-capacitacao-*.md` (from this survey) → enriches roadmap_part4.pdf
- ✅ `saida/insights-developer-survey-*.md` (if you ran it) → cross-references in the appendix
- ✅ `saida/maturidade-developer-survey-*.json` (if you ran it) → score_justification.pdf includes "maturity vs declared"

**Output:** 5 production-quality PDFs with the REAL learning survey data embedded.

---

## 🅱️ Alternative path: direct Excel/SharePoint

For small teams (3-5 devs):

```bash
cp survey-learning/template-export-forms-learning.xlsx respostas-survey-learning.xlsx
# Clear the mock rows (rows 2-6)
# Upload to SharePoint with edit access
# Each dev fills in one row (including name+email)
# Download and move to the kit root
/import-learning-survey + /training-plan
```

---

## 💡 Best practices

### Ethical data-use commitment
Communicate before launching:

> "Your answers will be used to: (1) build our capacitation roadmap, (2) invite you to the specific workshops you asked for, (3) build the Champions Network. They will **NOT** be used for performance reviews, comparisons between devs, or shared with external clients."

### Relaunch cadence
- **Every 6 months** or after big events (Copilot rollout, stack change, etc.)
- **Compare evolutions**: a dev who was L1 in D5 and now self-assesses as L3? A natural Champion

### Plan transparency
- Present the `plano-capacitacao-DATE.md` at an all-hands
- People who asked for workshop X receive an invitation; close the loop
- Identified Champions are recognized publicly (with consent)

---

## 🆘 Troubleshooting

| Problem | Solution |
|---|---|
| The skill does not detect the file | Move it to the root of `kit-cliente/` |
| Email/Name empty in some rows | Forms config: Anonymous OFF + L1-Q1/Q2 required |
| Headers not recognized | Make sure every question starts with `L[1-7]-Q\d+:` |
| A dev refused to identify | Accept the partial answer; redirect to `survey-devs` (anonymous) |
| Low participation (< 50% of the team) | The engineering leader must ENDORSE it explicitly |

---

## 📚 References

- **The 32 formatted questions:** [`perguntas-para-forms-learning.en.md`](perguntas-para-forms-learning.en.md)
- **Ready-made Excel template:** [`template-export-forms-learning.xlsx`](template-export-forms-learning.xlsx)
- **Structured example JSON:** [`respostas-mock-learning.json`](respostas-mock-learning.json)
- **Import skill:** [`../.github/skills/import-learning-survey/SKILL.md`](../.github/skills/import-learning-survey/SKILL.md)
- **Plan skill:** [`../.github/skills/training-plan/SKILL.md`](../.github/skills/training-plan/SKILL.md)
- **Cross-reference with the Developer Survey** (anonymous): [`../survey-devs/`](../survey-devs/)

---

**Version:** 1.0 · **Date:** 2026-05-08

---

## Stuck on any of these steps?

<details>
<summary><strong>FAQ: common questions about the Learning & Growth Survey (identified)</strong></summary>

| Symptom | Likely cause | How to fix |
|---|---|---|
| The Excel arrives without name/email | **Anonymous responses** is checked (this survey needs to be identified) | Forms Settings → ❌ UNcheck **Anonymous responses** |
| How do I use the plan to invite people? | The plan carries name+email per workshop | Copy the attendee list from the markdown → paste into an Outlook/Teams meeting invite |
| Champions Network is empty in the generated plan | Nobody answered "yes" to L6-Q1 | No self-declared Champions; use the per-dimension ranking as a proxy |
| Cohorts are empty in some dimensions | Fewer than 3 respondents per dimension | Ask for a campaign push or accept smaller cohorts |
| Can I re-run the plan when more answers arrive? | Yes, it is idempotent | Re-export the Excel → `/import-learning-survey` → `/training-plan` |

</details>

---

## Continue reading

| ← PREVIOUS | NEXT → |
|:---|---:|
| **[Developer Survey (anonymous)](../survey-devs/INSTRUCOES-FORMS-DEVS.md)** | **[Wizard: Part 4](../wizard/README.en.md)** |
| 75 anonymous questions: Copilot, agents, governance. | Personalize the Steering Committee, RACI, ADKAR, Quick Wins of the executive PDF. |

↑ [Back to the kit index](../README.en.md)
