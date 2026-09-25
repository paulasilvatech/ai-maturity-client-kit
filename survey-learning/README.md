# `survey-learning/`: Learning & Growth Survey (identified, capacitation)

🌐 English · [Português (Brasil)](README.pt-br.md)

**Third pillar of the kit:** after measuring organizational maturity (assessment) and real behavior (survey-devs), this survey generates the **personalized capacitation roadmap**: workshops, cohorts, Champions Network, and mentoring. **Identified** (name+email) so the right people can be invited.

## 📐 Difference vs. the other surveys

| Aspect | Main assessment | Developer Survey | **Learning Survey** |
| --- | --- | --- | --- |
| **Audience** | Leadership | Anonymous developers | **Identified developers** |
| **Anonymous?** | No | Yes | **No, requires name+email** |
| **Focus** | Organizational L0-L4 maturity | Real behavior (% adoption) | **What they want to LEARN** |
| **Time per respondent** | 60-90 min | 22-28 min | **5-8 min** |
| **Number of questions** | 158 | 75 | **32** |
| **Output** | 5 production PDFs | Insights + computed maturity | **Actionable capacitation plan** |
| **Skills** | `/calcular-scores`, `/gerar-relatorio` | `/importar-survey-devs`, `/insights-developer-survey` | `/importar-survey-learning`, `/plano-capacitacao` |

**The 3 are complementary**: running all 3 gives a 360° view:

```text
Assessment (leadership strategy)
         ↓
Survey-devs (anonymous behavioral reality)
         ↓
Learning Survey (identified desire to grow)
         ↓
WIZARD-IMPLEMENTACAO (consolidates into the Implementation Guide PDF)
```

## 📋 The 7 sections

| # | Section | Focus | Q |
| --- | --- | --- | --- |
| **L1** | Identification | Name, email, role, team | 4 |
| **L2** | Self-perceived maturity | L0-L4 self-assessment in the 7 dimensions D2-D8 (rubric) | 7 |
| **L3** | Where you want to grow | Top 3 priority dimensions (next 6 months) | 2 |
| **L4** | Specific topics | Copilot, Foundry, practices (TDD/SDD), agents, security | 5 |
| **L5** | Format and cadence | Workshop, cohort vs self-paced, time slots, hours/week | 4 |
| **L6** | Champions and mentoring | Want to be a Champion? Mentoring? Who is a reference? | 5 |
| **L7** | Barriers and Wishlist | What gets in the way + workshops + desired speakers | 5 |
| | | **TOTAL** | **32** |

## 🗂️ Files in this folder

| File | What it is |
| --- | --- |
| **[INSTRUCOES-FORMS-LEARNING.md](INSTRUCOES-FORMS-LEARNING.md)** | How to build the IDENTIFIED Microsoft Forms (with settings + best practices + ethical use of data) |
| **[perguntas-para-forms-learning.md](perguntas-para-forms-learning.md)** | The 32 questions formatted for copy/paste into Forms (canonical PT-BR bank) |
| **[perguntas-para-forms-learning.en.md](perguntas-para-forms-learning.en.md)** | Question bank in English, preserving the `Lx-Qy` IDs for parsing |
| **[perguntas-para-forms-learning.es.md](perguntas-para-forms-learning.es.md)** | Question bank in Spanish, preserving the `Lx-Qy` IDs for parsing |
| **[template-export-forms-learning.xlsx](template-export-forms-learning.xlsx)** | Excel template + 5 mock respondents (Maria, João, Ana, Pedro, Sofia) |
| **[respostas-mock-learning.json](respostas-mock-learning.json)** | Sample structured JSON |

## 🚀 Usage flow

```text
1. Build the Forms following INSTRUCOES-FORMS-LEARNING.md (~30 min)
2. Share the link with ALL developers (Slack/Teams/Email)
3. Wait 2 weeks (reminders on D+7 and D+12)
4. Responses → Open in Excel
5. Save as respostas-survey-learning.xlsx at the kit root
6. /importar-survey-learning   → survey-learning/respostas-learning.json
7. /plano-capacitacao          → saida/plano-capacitacao-DATE.md
```

## 🧪 How to test / smoke test (without collecting real answers)

Before building the Forms for developers, validate the pipeline with the 5 mock respondents:

### Mode A: Via Copilot Chat (recommended)

```bash
# From the kit-cliente root:
cp survey-learning/respostas-mock-learning.json survey-learning/respostas-learning.json
```

In Copilot Chat (Agent mode):

```text
/plano-capacitacao
```

In about 30 seconds you will have `saida/plano-capacitacao-2026-05-08.md` generated from the mocks (Maria, João, Ana, Pedro, Sofia). It lets you see "what it will look like" before collecting real data.

### Mode B: Via @ai-maturity-assistant (concierge)

```text
@ai-maturity-assistant
```

Choose **[C] Learning & Growth Survey** when the agent asks. It offers 3 options, and `[C] Smoke test imediato com mocks` takes the shortcut automatically.

### Mode C: Simulating the full cycle via the mock Excel

To validate end to end (including the `/importar-survey-learning` skill):

```bash
# Rename the template to what the skill expects to detect
cp survey-learning/template-export-forms-learning.xlsx respostas-survey-learning.xlsx

# In Copilot Chat:
/importar-survey-learning      # parses the mock Excel → respostas-learning.json
/plano-capacitacao             # generates the plan for the 5 identified mocks
```

Then clean up the state:

```bash
rm respostas-survey-learning.xlsx survey-learning/respostas-learning.json
```

### What to validate in the smoke test

After `/plano-capacitacao`, open `saida/plano-capacitacao-DATE.md` and confirm:

- [ ] Executive summary shows 5 respondents
- [ ] Top 10 requested topics appear with the **name + email** of attendees (Maria, João, Ana, Pedro, Sofia)
- [ ] Champions Network: Maria + João + Sofia listed as "active" (consistent with the mocks)
- [ ] 90-day calendar generated (sequenced workshops)
- [ ] Appendix has the respondents table (visible to leadership)

If any of these is missing → report it as a bug in the `/plano-capacitacao` skill (not in the mock).

## 📊 What the capacitation plan contains

`saida/plano-capacitacao-<DATE>.md` (generated by the skill) is written in **English by default**; run the script with `--lang pt-br` to get it in Portuguese (Brazil). It has **12 sections**:

1. **Executive Summary**: perceived maturity + top 3 priority dimensions + identified Champions + 3 quick wins
2. **Top 10 requested topics**: with a list of pre-validated attendees (name+email)
3. **Suggested cohorts per dimension D2-D8**: with Champions, format, and cadence
4. **Champions Network**: 3 tiers (active, with support, maybe) + mentor pairs + natural references
5. **Workshop calendar for the next 90 days**: week × workshop × audience × Champion
6. **Preferred format and cadence**: team aggregate
7. **Barriers to remove**: prioritized
8. **Team wishlist**: workshops, speakers, free-form ideas
9. **Connection with the other surveys**: self-perception (L2) vs measured rubric (D2-D8) vs main assessment
10. **Top 5 prioritized actions**: impact × ease × alignment with gaps
11. **Next 30 days**: week-by-week schedule
12. **Appendix: respondents (visible to leadership only)**: table with all respondents

## 🔗 Connection with the other surveys and the wizard

### ⭐ Mode D: Wizard auto-fill

After `/plano-capacitacao` generates `saida/plano-capacitacao-DATE.md`, running `/wizard-implementacao` makes the Copilot Agent **automatically detect** this plan and offer **Mode D: Auto-fill**, which fills **6 of the 9 wizard inputs** automatically:

```text
saida/plano-capacitacao.md
    ↓ feeds automatically (Mode D)
.github/skills/wizard-implementacao  (Part 4 of the PDF)
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

**Estimated savings with Mode D:** 30-45 min of manual wizard work + REAL data from your team (not placeholders from the Acme sample).

**How to invoke Mode D:** just run `/wizard-implementacao` after `/plano-capacitacao`. The agent offers it automatically.

## 🔐 About identification (not anonymity)

- Microsoft Forms has an "Anonymous responses" option: for this survey it must stay **UNCHECKED**
- Developers need to know it is identified WHEN ANSWERING (transparency)
- Leadership commits to using the data ONLY for capacitation (not performance review)
- The consolidated plan is shared with the whole team (transparency)
- The appendix with names/emails is "visible to leadership" in the report: do not share it publicly

## 📅 Suggested cadence

- **First time:** after establishing a baseline with the assessment + survey-devs
- **Every 6 months:** measure how the desire evolves + compare with real maturity
- **After major events** (Copilot rollout, stack change, new Champion): rerun to realign the plan

## 📚 Related documentation

- **Skill that imports Excel → JSON:** [`../.github/skills/importar-survey-learning/SKILL.md`](../.github/skills/importar-survey-learning/SKILL.md)
- **Skill that generates the plan:** [`../.github/skills/plano-capacitacao/SKILL.md`](../.github/skills/plano-capacitacao/SKILL.md)
- **Companion survey (anonymous):** [`../survey-devs/`](../survey-devs/)
- **Wizard that consumes the plan:** [`../wizard/`](../wizard/) (feeds Part 4 of the PDF)
- **Main assessment:** see [`../README.md`](../README.md)

## 🔗 Sources for topics covered in the survey

The learning topics listed in L4 come from the same validated official sources used in the Developer Survey:

- **GitHub Copilot** (modes, Spaces, Coding Agent): docs.github.com/copilot
- **Microsoft Foundry**: learn.microsoft.com/azure/foundry
- **MCP / A2A**: protocols + Foundry support (Mar/2026)
- **Spec Kit (SDD)**: github.com/github/spec-kit
- **Agentic DevOps personas**: learn.microsoft.com/azure/well-architected/ai/personas
- **GHAS, CodeQL, SBOM, Defender**: GitHub Advanced Security + Microsoft Defender for DevOps docs
