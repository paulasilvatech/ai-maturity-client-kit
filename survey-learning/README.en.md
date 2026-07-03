# `survey-learning/`: Learning & Growth Survey (identified, capacitation)

**Third pillar of the kit:** after measuring organizational maturity (assessment) and real behavior (survey-devs), this survey produces the **personalized capacitation roadmap**: workshops, cohorts, Champions Network, mentoring. **Identified** (name+email) so you can invite the right people.

## 📐 Difference vs. the other surveys

| Aspect | Main assessment | Developer Survey | **Learning Survey** |
| --- | --- | --- | --- |
| **Audience** | Leadership | Anonymous devs | **Identified devs** |
| **Anonymous?** | No | Yes | **No: requires name+email** |
| **Focus** | Organizational L0-L4 maturity | Real behavior (% adoption) | **What they want to LEARN** |
| **Time per respondent** | 60-90 min | 22-28 min | **5-8 min** |
| **Number of questions** | 158 | 75 | **32** |
| **Output** | 5 production PDFs | Insights + computed maturity | **Actionable training plan** |
| **Skills** | `/calculate-scores`, `/generate-reports` | `/import-developer-survey`, `/insights-developer-survey` | `/import-learning-survey`, `/training-plan` |

**The 3 are complementary**: running all 3 gives a 360° view:

```text
Assessment (leadership strategy)
         ↓
Survey-devs (anonymous behavioral reality)
         ↓
Learning Survey (identified desire to grow)
         ↓
IMPLEMENTATION-WIZARD (consolidates into the Implementation Guide PDF)
```

## 📋 The 7 sections

| # | Section | Focus | Q |
| --- | --- | --- | --- |
| **L1** | Identification | Name, email, role, team | 4 |
| **L2** | AI maturity self-perception | L0-L4 self-assessment across the 7 dimensions D2-D8 (rubric) | 7 |
| **L3** | Where you want to grow | Top 3 priority dimensions (next 6 months) | 2 |
| **L4** | Specific topics | Copilot, Foundry, practices (TDD/SDD), agents, security | 5 |
| **L5** | Preferred format and cadence | Workshop, cohort vs self-paced, schedules, time/week | 4 |
| **L6** | Champions and mentoring | Want to be a Champion? Mentoring? Who is a reference? | 5 |
| **L7** | Barriers and Wishlist | What blocks you + desired workshops + speakers | 5 |
| | | **TOTAL** | **32** |

## 🗂️ Files in this folder

| File | What it is |
| --- | --- |
| **[INSTRUCOES-FORMS-LEARNING.en.md](INSTRUCOES-FORMS-LEARNING.en.md)** | How to create the IDENTIFIED Microsoft Forms (with configuration + best practices + ethical use of the data) |
| **[perguntas-para-forms-learning.md](perguntas-para-forms-learning.md)** | The 32 questions formatted for copy/paste into Forms (PT-BR original) |
| **[perguntas-para-forms-learning.en.md](perguntas-para-forms-learning.en.md)** | Question bank in English, preserving the `Lx-Qy` IDs for parsing |
| **[perguntas-para-forms-learning.es.md](perguntas-para-forms-learning.es.md)** | Question bank in Spanish, preserving the `Lx-Qy` IDs for parsing |
| **[template-export-forms-learning.xlsx](template-export-forms-learning.xlsx)** | Excel template + 5 mocked respondents (Maria, João, Ana, Pedro, Sofia) |
| **[respostas-mock-learning.json](respostas-mock-learning.json)** | Structured example JSON |

## 🚀 Usage flow

```text
1. Create the Forms following INSTRUCOES-FORMS-LEARNING.en.md (~30 min)
2. Share the link with ALL devs (Slack/Teams/Email)
3. Wait 2 weeks (reminders at D+7 and D+12)
4. Responses → Open in Excel
5. Save as respostas-survey-learning.xlsx at the kit root
6. /import-learning-survey → survey-learning/respostas-learning.json
7. /training-plan          → saida/plano-capacitacao-DATE.md (+ .json)
```

## 🧪 How to test / smoke test (without collecting real responses)

Before creating the Forms for the devs, validate the pipeline with the 5 mocked respondents:

### Mode A: via Copilot Chat (recommended)

```bash
# From the kit root:
cp survey-learning/respostas-mock-learning.json survey-learning/respostas-learning.json
```

In Copilot Chat (Agent mode):

```text
/training-plan
```

In about 30 seconds you will have `saida/plano-capacitacao-2026-05-08.md` generated from the mocks (Maria, João, Ana, Pedro, Sofia). It lets you see "what it will look like" before collecting real data.

### Mode B: via @ai-maturity-assistant (concierge)

```text
@ai-maturity-assistant
```

Choose **[C] Learning & Growth Survey** when the agent asks. It will offer 3 options and the `[C] Immediate smoke test with mocks` option runs the shortcut automatically.

### Mode C: simulating the full cycle via the mock Excel

To validate end-to-end (including the `/import-learning-survey` skill):

```bash
# Rename the template to the filename the skill expects to detect
cp survey-learning/template-export-forms-learning.xlsx respostas-survey-learning.xlsx

# In Copilot Chat:
/import-learning-survey      # parses the mock Excel → respostas-learning.json
/training-plan             # generates the plan for the 5 identified mocks
```

Then clean up the state:

```bash
rm respostas-survey-learning.xlsx survey-learning/respostas-learning.json
```

### What to validate in the smoke test

After `/training-plan`, open `saida/plano-capacitacao-DATE.md` and confirm:

- [ ] Executive summary shows 5 respondents
- [ ] Top 10 requested topics appear with the **name + email** of the attendees (Maria, João, Ana, Pedro, Sofia)
- [ ] Champions Network: Maria + João + Sofia listed as "active" (consistent with the mocks)
- [ ] 90-day calendar generated (sequenced workshops)
- [ ] Appendix has the respondents table (visible to leadership)

If any of these is missing → report it as a bug of the `/training-plan` skill (not of the mock).

## 📊 What the training plan contains

`saida/plano-capacitacao-<DATE>.md` (generated by the skill) has **12 sections**:

1. **Executive Summary**: perceived maturity + top 3 priority dimensions + identified Champions + 3 quick wins
2. **Top 10 requested topics**: with the list of pre-validated attendees (name+email)
3. **Suggested cohorts per dimension D2-D8**: with Champions, format, cadence
4. **Champions Network**: 3 tiers (active, with support, maybe) + mentor pairs + natural references
5. **Workshop calendar for the next 90 days**: week × workshop × audience × Champion
6. **Preferred format and cadence**: aggregated for the team
7. **Barriers to remove**: prioritized
8. **Team wishlist**: workshops, speakers, free-form ideas
9. **Connection with the other surveys**: comparison of self-perception (L2) vs measured rubric (D2-D8) vs main assessment
10. **Top 5 prioritized actions**: impact × ease × alignment with gaps
11. **Next 30 days**: week-by-week schedule
12. **Appendix: respondents (visible to leadership only)**: table with all respondents

## 🔗 Connection with the other surveys and the wizard

### ⭐ Mode D: wizard auto-fill

After `/training-plan` generates `saida/plano-capacitacao-DATE.md` (plus a structured `.json` twin), running `/implementation-wizard` makes the Copilot Agent **automatically detect** this plan and offer **Mode D: Auto-fill**, which fills **6 of the 9 wizard inputs** automatically. Under the hood it runs `wizard/scripts/auto_fill_from_plano.py`, which prefers the `.json` (a `.md` regex fallback exists but loses detail):

```text
saida/plano-capacitacao-DATE.json (with .md fallback)
    ↓ feeds automatically (Mode D)
.github/skills/implementation-wizard  (Part 4 of the PDF)
    ↓ populated fields:
- executive_steering_committee  ← Champions Network "active"
- communication_plan            ← Suggested calendar
- training_plan                 ← Cohorts per dimension
- adkar_notes                   ← Top 5 workshops (Knowledge stage)
- quick_wins_w1_4               ← 30-day calendar
- quick_wins_w5_8               ← Calendar weeks 5-8
- quick_wins_w9_12              ← Calendar weeks 9-12

You only fill in manually: TPO + RACI Matrix
```

**Estimated savings with Mode D:** 30-45 min of manual wizard work, plus REAL data from your team (not placeholders from the Acme sample).

**How to invoke Mode D:** simply run `/implementation-wizard` after `/training-plan`. The agent offers it automatically.

## 🔐 About identification (not anonymity)

- Microsoft Forms has an "Anonymous responses" option: for this survey it must stay **UNCHECKED**
- Devs need to know it is identified WHEN ANSWERING (transparency)
- Leadership commits to using the data ONLY for capacitation (not performance review)
- The consolidated plan is shared with the whole team (transparency)
- The appendix with names/emails is "visible to leadership" in the report: do not share it publicly

## 📅 Suggested cadence

- **First time:** after establishing the baseline with the assessment + survey-devs
- **Every 6 months:** measure the evolution of the desire + compare with real maturity
- **After big events** (Copilot rollout, stack change, new Champion): re-run to realign the plan

## 📚 Related documentation

- **Skill that imports Excel → JSON:** [`../.github/skills/import-learning-survey/SKILL.md`](../.github/skills/import-learning-survey/SKILL.md)
- **Skill that generates the plan:** [`../.github/skills/training-plan/SKILL.md`](../.github/skills/training-plan/SKILL.md)
- **Companion survey (anonymous):** [`../survey-devs/`](../survey-devs/)
- **Wizard that consumes the plan:** [`../wizard/`](../wizard/) (feeds Part 4 of the PDF)
- **Main assessment:** see [`../README.en.md`](../README.en.md)

## 🔗 Sources for the topics covered in the survey

The learning topics listed in L4 come from the same official sources validated in the Developer Survey:

- **GitHub Copilot** (modes, Spaces, Coding Agent): docs.github.com/copilot
- **Microsoft Foundry**: learn.microsoft.com/azure/foundry
- **MCP / A2A**: protocols + Foundry support (Mar/2026)
- **Spec Kit (SDD)**: github.com/github/spec-kit
- **Agentic DevOps personas**: learn.microsoft.com/azure/well-architected/ai/personas
- **GHAS, CodeQL, SBOM, Defender**: GitHub Advanced Security + Microsoft Defender for DevOps docs
