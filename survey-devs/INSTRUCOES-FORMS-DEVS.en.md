# How to create the Microsoft Forms for the Developer Survey

**`🅱️ SURVEY-DEVS`** · _anonymous_ · 📖 [🏠 Index](../README.en.md) · [« Main collection](../coleta/INSTRUCOES-FORMS.en.md) · You are here · [» Learning Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.en.md)

> [!IMPORTANT]
> An **anonymous** survey of **75 questions** in 9 sections to understand how the developers in your organization use GitHub Copilot, Copilot Chat modes (Ask/Edit/Agent/**Coding Agent**), **Copilot Spaces**, **Microsoft Foundry**, AI agents + **MCP / A2A**, instructions files, practices (TDD/SDD with Spec Kit), **Agentic DevOps personas** (System Designer / Agent Operator), governance, and security (incl. **JIT permissions** and **agent scope+red-lines**). Estimated time per respondent: **22-28 min**.

**Version 2.0 (2026-05-08)**: terms updated with the latest official Microsoft/GitHub docs.

**Different from the main assessment** (organizational L0-L4 Likert). This one is **individual and behavioral**: the more devs respond, the richer the picture.

---

## 🎯 When to use this survey

- ✅ Before defining the engineering AI adoption strategy
- ✅ After a GitHub Copilot rollout, to measure real adoption
- ✅ As input for the `/implementation-wizard` (the main assessment's Implementation Guide)
- ✅ Quarterly, to track cultural evolution
- ✅ Before Copilot/AI workshops, to identify gaps

---

## 🔐 Anonymity: CRITICAL

This survey is **anonymous by design**:
- ❌ We do not ask for name, email, or corporate ID
- ✅ We collect only: role, years of experience, usage patterns, opinions
- ✅ Devs answer more honestly when they know it is anonymous
- ⚠️ In Microsoft Forms, **CHECK "Anonymous responses"** in Settings (without it, Forms captures the MS365 account email)

---

## 📋 The 9 topics covered (v2.0)

| # | Section | Focus | Questions |
|---|---|---|---|
| **S1** | Respondent profile | Role, experience, stack, work model | 7 |
| **S2** | GitHub Copilot: Adoption and Modes | License, frequency, **Ask / Edit / Agent / Coding Agent (autonomous)**, features (incl. **Spaces**), gain | 9 |
| **S3** | Other Microsoft / GitHub AI tools | **Microsoft Foundry** (ex-Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, **Spec Kit**, **MCP** | 7 |
| **S4** | AI Development Practices | **TDD with AI**, **SDD with Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Agent Concepts and Structure | Agent vs assistant, Copilot modes, **custom agents/skills/prompts**, **A2A**, handoffs, subagents, **Agentic DevOps personas** (System Designer / Agent Operator), **TESTING agents before using them** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions in **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usability and Best Practices | How they learned (incl. MS Build / GitHub Universe), Champion, DORA/DX metrics, iterations, trust | 9 |
| **S8** | Security and Governance | AI policy, sensitive data, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **agent scope+red-lines**, **JIT permissions**, training | 13 |
| **S9** | Pain Points & Wishlist | Frustrations, ideas, feature requests | 4 |
| | | **TOTAL** | **75** |

---

## 🛠️ How to create the Forms (step by step)

### Step 1 · Create the form

1. Go to <https://forms.office.com>
2. Click **+ New Form**
3. Suggested title: `Developer Survey: How my team uses GitHub & AI today`
4. Subtitle (paste this):

```
ANONYMOUS survey (20-25 min) about your practices with GitHub Copilot,
Copilot Chat modes (Ask/Edit/Agent), AI agents, instructions files,
AI + Dev best practices, and security.

Your answers will feed the team's AI adoption roadmap.
We do NOT ask for name or email, only role, years of experience, and patterns.

Estimated time: 20-25 min.
```

### Step 2 · ⚠️ CONFIGURE ANONYMITY

**Settings (gear ⚙️ in the top right corner):**

| Setting | Value |
|---|---|
| **Anonymous responses** | ☑ **CHECKED** (CRITICAL: without this it captures email!) |
| **Who can respond** | "Anyone with the link" (if cross-org) or "Only people in my organization" |
| **One response per person** | ☐ UNCHECKED (we want multiple) |
| **Accept responses** | ☑ CHECKED |
| **Email notification** | ☑ CHECKED (optional: you are notified on each response) |
| **Customize thank you message** | "Thank you! Your answers are being aggregated with the team's." |

> 🔍 **How to confirm anonymity:** after creating it, open the link in an incognito window. If "Logged in as [your email]" does NOT appear at the top, it is anonymous.

### Step 3 · Create 9 sections

In Forms, **+ Add new** button → section icon (or "Add section"):

```
Section 1: S1 — Respondent profile               (7 questions)
Section 2: S2 — GitHub Copilot                   (9 questions)
Section 3: S3 — Other Microsoft/GH tools         (7 questions)
Section 4: S4 — AI Development Practices        (9 questions)
Section 5: S5 — Agent Concepts                   (11 questions)
Section 6: S6 — Markdown / Instructions          (6 questions)
Section 7: S7 — Usability                        (9 questions)
Section 8: S8 — Security and Governance         (13 questions)
Section 9: S9 — Pain Points & Wishlist           (4 questions)
```

### Step 4 · Add the 75 questions

Use the document [`perguntas-para-forms-devs.en.md`](perguntas-para-forms-devs.en.md) as your **copy/paste source**. Each question has:
- **Type** (`choice`, `multi`, `text`)
- **ID** (`S2-Q1`, `S5-Q3`, etc.)
- **Question text**
- **Options** (for choice/multi)

**For each question in Forms:**

1. Type:
   - `choice` (Single answer) → **Choice** with "Multiple answers" UNCHECKED
   - `multi` (Multiple answers) → **Choice** with "Multiple answers" CHECKED
   - `text` (Long Text) → **Long answer**

2. **The question TITLE MUST start with the ID + a colon**:
   ```
   S2-Q1: Do you have an active GitHub Copilot license?
   ```
   > ⚠️ **CRITICAL:** the ID is used by the `/import-developer-survey` skill to map back to the schema. Do not remove or change the `SX-QY:` format.

3. **Options** (for choice/multi): paste the options listed in the MD, **one per line**, in order.

4. **Required**: mark as required only the 7 Profile questions (S1-Q1 to S1-Q7). The rest are optional (devs can skip).

### Step 5 · Share

1. **+ Send / Collect responses** button at the top
2. Choose **Link** (not Email, which breaks anonymity)
3. Copy the URL
4. Share via:
   - **Slack/Teams:** #engineering or #copilot-users channel
   - **Email to all devs:** "Anonymous 20-min survey, your opinion counts"
   - **All-hands:** project a QR code of the URL for devs to scan
5. **Suggested deadline:** 2 weeks. Remind 1× per week.

### Step 6 · Track responses

- The **Responses** tab shows the count in real time
- Recommended: **minimum 5 respondents**, ideally **15+** for rich insights
- If uptake is low: 1-on-1 with leaders to encourage participation

### Step 7 · Export when you have enough responses

1. **Responses** tab → **Open in Excel** button
2. Save the file as **`respostas-survey-devs.xlsx`**
3. Move it to the **`kit-cliente/` root** (not inside `survey-devs/`)
4. **Anonymity confirmed:** columns D (Email) and E (Name) must be empty

### Step 8 · Analyze with the kit

In Copilot Chat (Agent mode):

```
/import-developer-survey
```

The skill:
- Detects `respostas-survey-devs.xlsx`
- Parses 75 questions × N respondents
- Generates `survey-devs/respostas-devs.json`
- Generates `saida/import-survey-log-<DATE>.md`

Then:

```
/insights-developer-survey
```

Generates an aggregated report at `saida/insights-developer-survey-<DATE>.md` with:
- Role distribution
- Top 5 most used Copilot features
- % adoption per mode (Ask/Edit/Agent/Workspace)
- Concept knowledge (agents, MCP, handoffs)
- Instructions files maturity
- Governance and security gaps
- Pain point citations (anonymized)
- Prioritized recommendations for the roadmap

---

## 🅱️ Alternative path: Excel/SharePoint directly (no Forms)

Faster if the team is small (3-5 devs) and technical.

1. Open `survey-devs/template-export-forms-devs.xlsx`
2. Delete the 5 mocked respondent rows (rows 2-6), keeping row 1 (headers)
3. Save as `respostas-survey-devs.xlsx` and upload to SharePoint with an "Anyone can edit" link
4. Each dev fills in **one row** with their answers (free text in the answer cells)
5. When everyone has filled it in: download → move to the kit root → `/import-developer-survey`

**Trade-off:** less visual than Forms, but zero setup. Suitable for technical teams.

---

## 💡 Collection best practices

### Launch with context
Do not drop the link in Slack without context. Create a moment:

> "Folks, before we define the engineering AI strategy for next quarter, we want to hear how you use AI today. Anonymous 20-25 min survey with 75 questions (Copilot, agents, security…). Your answers go straight into the roadmap. Link: <URL>. Deadline: 2 weeks."

### Guarantee anonymity (for real)
- Confirm that Settings → Anonymous is CHECKED
- Do not force MS365 login (in case you share externally)
- In the aggregated report, never cite specific respondents, only patterns

### Remind periodically
- D+3: gentle reminder in the channel
- D+7: recap "X responses so far, Y days left"
- D+10: 1-on-1 with leaders to push
- D+14: final deadline + analysis begins

### Share the insights
Devs are more likely to answer the next survey if they see the previous one led to action. After `/insights-developer-survey`:
- Present it at an all-hands
- Generate quick wins (workshop, prompt library, etc.)
- Repeat quarterly to measure evolution

---

## 🆘 Troubleshooting

| Problem | Diagnosis | Solution |
|---|---|---|
| Skill does not detect the file | It is not in the root | Move `respostas-survey-devs.xlsx` to `kit-cliente/` (root) |
| Skill says "0 respondents" | Email/Name not empty but questions empty | Check that respondents answered at least 1 question |
| Headers not recognized | Missing "SX-QY:" at the start | Edit the headers manually to include the ID |
| Email appears in the Excel | Anonymity OFF | Reconfigure Forms → Settings → Anonymous Responses ON and re-send |
| Low uptake (< 5 responses) | Launch without context | Re-launch with a message from the leader, deadline, purpose |

---

## 📚 References

- **The 75 formatted questions:** [`perguntas-para-forms-devs.en.md`](perguntas-para-forms-devs.en.md)
- **Ready-made Excel template (5 mocks):** [`template-export-forms-devs.xlsx`](template-export-forms-devs.xlsx)
- **Structured example JSON:** [`respostas-mock-devs.json`](respostas-mock-devs.json)
- **Import skill:** [`../.github/skills/import-developer-survey/SKILL.md`](../.github/skills/import-developer-survey/SKILL.md)
- **Insights skill:** [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)
- **Relation to the main assessment:** this survey COMPLEMENTS the maturity assessment. The insights here inform the P1-C1, P1-C5, P1-C8 questions (Copilot, Onboarding, Metrics) and the governance in P2-C4 / P3-C6.

---

**Version:** 1.0 · **Date:** 2026-05-08

---

## Stuck on one of these steps?

<details>
<summary><strong>FAQ: common questions in the Developer Survey (anonymous)</strong></summary>

| Symptom | Likely cause | How to fix |
|---|---|---|
| Exported Excel has **Email** and **Name** filled in | **Anonymous responses** was NOT checked in Forms | Forms Settings → ✅ **Anonymous responses** → re-collect |
| Devs complain it is too long (20-25 min) | Too many questions marked as required | Mark required **only in S1** (profile); the rest optional |
| I have fewer than 5 respondents | Insights become unreliable | Absolute minimum: 3. Ideal: 5+. Great: 15+, extend the campaign 1 week |
| The skill computes maturity but the number seems low | Deterministic L0-L4 rubric, it reflects reality | See [`RUBRICA-MATURIDADE.en.md`](RUBRICA-MATURIDADE.en.md) to understand the scale |
| I want to skip this survey | That is fine, it is optional | Skip straight to the Learning Survey or run only the main Assessment |

</details>

---

## Continue reading

| ← PREVIOUS | NEXT → |
|:---|---:|
| **[Main assessment collection](../coleta/INSTRUCOES-FORMS.en.md)** | **[Learning & Growth Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.en.md)** |
| 3 paths to collect the assessment's 158 questions via Forms / Excel. | 32 identified questions: training plan with Champions and workshops. |

↑ [Back to the kit Index](../README.en.md)
