# `survey-devs/`: Developer Survey (anonymous, behavioral, individual)

This folder contains a **survey that is separate** from the main assessment, focused on understanding **how each developer uses GitHub Copilot, AI agents, instructions files, Copilot Chat modes, practices (TDD/SDD), governance, and security** in their day-to-day work. Anonymous.

> 💡 **Companion survey to this one:** after running the **survey-devs** (anonymous, measures behavior), also consider the **[survey-learning](../survey-learning/)** (identified, measures what devs want to learn). Together, the 2 form a 360° diagnostic of the devs: behavioral + aspirational.

> 🔄 **Version 2.0 (updated 2026-05-08)**: terminology updated with official changes:
> - **Copilot Workspace** evolved into **Copilot Coding Agent** (GA Sep/2025)
> - **Copilot Spaces** (GA Sep/2025) replaced **Knowledge Bases** (sunset Nov/2025)
> - **Azure AI Foundry** renamed to **Microsoft Foundry** + **Foundry Agent Service** GA
> - Added questions about **MCP**, the **A2A protocol**, Microsoft Agentic DevOps personas (**System Designer**, **Agent Operator**), **testing agents before using them**, **scope+red-lines**, **JIT permissions**.

## 📐 Difference vs. the main assessment and survey-learning

| Aspect | Main assessment | Developer Survey (this one) | **survey-learning** |
|---|---|---|---|
| **Audience** | Leadership / architects / Tech Leads | **Individual devs** (any role) | Individual devs |
| **Anonymous?** | No, identified by organization | **Yes, anonymous Forms** | **No, IDENTIFIED (name+email)** |
| **Focus** | Organizational maturity (L0-L4) | Real individual adoption and practice | **What they want to LEARN** |
| **Scale** | 5-point Likert per capability | Choice/multi-choice/free text | Self-perception L0-L4 + multi |
| **Volume** | 158 questions across 28 capabilities | **75 questions across 9 sections** | 32 questions across 7 sections |
| **Time per respondent** | 60-90 min | **22-28 min** | 5-8 min |
| **Multi-respondent** | Possible but not the default | **Essential** (average ≥5, ideally ≥15) | **Essential** (>50% of the team) |
| **Output** | Executive report + 5 PDFs | Insights report + computed maturity | Training plan + Champions |
| **Skills** | `/calculate-scores`, `/generate-reports`, etc. | `/import-developer-survey` + `/insights-developer-survey` | [`/import-learning-survey`](../survey-learning/) + `/training-plan` |

**The 3 are complementary:**
- This **survey-devs** measures BEHAVIOR (anonymous)
- The **[survey-learning](../survey-learning/)** measures DESIRE (identified, complements this one)
- The **main assessment** measures STRATEGY (leadership)
- Together they form a 360° diagnostic.

## 📋 The 9 survey sections (v2.0, updated 2026-05-08)

| # | Section | Focus | Q |
|---|---|---|---|
| **S1** | Profile | Role, experience, stack, work model | 7 |
| **S2** | GitHub Copilot: Adoption and Modes | License, frequency, **Ask / Edit / Agent / Coding Agent (autonomous)**, features (incl. **Spaces**), gain | 9 |
| **S3** | Other Microsoft / GitHub tools | **Microsoft Foundry** (ex-Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, Spec Kit, **MCP** | 7 |
| **S4** | AI Development Practices | TDD with AI, **SDD with Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Agent Concepts and Structure | Agent vs assistant, Copilot modes, custom agents/skills/prompts, **A2A**, handoffs, subagents, **Microsoft Agentic DevOps personas** (System Designer / Agent Operator), **TESTING agents before using them** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions in **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usability and Best Practices | How they learned (incl. MS Build / GitHub Universe), Champion, DORA/DX metrics, iterations, trust | 9 |
| **S8** | Security and Governance | Policy, sensitive data, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **agent scope+red-lines**, **JIT permissions**, training | 13 |
| **S9** | Pain Points & Wishlist | Frustrations, ideas, feature requests | 4 |
| | | **TOTAL** | **75** |

## 🗂️ Files in this folder

| File | What it is |
|---|---|
| **[INSTRUCOES-FORMS-DEVS.en.md](INSTRUCOES-FORMS-DEVS.en.md)** | Step-by-step guide to create the Microsoft Forms (with anonymity configuration + collection best practices) |
| **[perguntas-para-forms-devs.en.md](perguntas-para-forms-devs.en.md)** | The 75 questions formatted for copy/paste into Forms (types, options, IDs) |
| **[template-export-forms-devs.xlsx](template-export-forms-devs.xlsx)** | Excel template in the Forms export format + 5 mocked respondents (varied profiles) |
| **[respostas-mock-devs.json](respostas-mock-devs.json)** | Structured example JSON (for testing the `/insights-developer-survey` skill) |
| **[RUBRICA-MATURIDADE.en.md](RUBRICA-MATURIDADE.en.md)** ⭐ | **Scoring model**: a deterministic rubric that maps answers → L0-L4 levels across 7 dimensions. Mirrors the main assessment's scale |
| **[scripts/rubric.py](scripts/rubric.py)** | Python implementation of the rubric (hardcoded rules per dimension) |
| **[scripts/calcular_maturidade.py](scripts/calcular_maturidade.py)** | CLI script that applies the rubric → `saida/maturidade-developer-survey-DATE.json` |

## 🚀 Usage flow (3 paths)

### Path A: Microsoft Forms (recommended for 10+ devs)

```
1. Create the Forms following INSTRUCOES-FORMS-DEVS.en.md (~30-45 min)
2. Share the link with the team (Slack/Teams/Email)
3. Wait 2 weeks (periodic reminders)
4. Responses → Open in Excel
5. Save as respostas-survey-devs.xlsx in the kit-cliente/ root
6. /import-developer-survey       → survey-devs/respostas-devs.json
7. /insights-developer-survey  → saida/insights-developer-survey-DATE.md
```

### Path B: shared Excel/SharePoint (fast for 3-5 devs)

```
1. cp survey-devs/template-export-forms-devs.xlsx respostas-survey-devs.xlsx
2. Clear the mock rows (rows 2-6)
3. Upload to SharePoint with edit permission
4. Each dev fills in one row
5. Download and move to the root
6. /import-developer-survey + /insights-developer-survey
```

### Path C: immediate smoke test (no real collection)

```
1. cp survey-devs/respostas-mock-devs.json survey-devs/respostas-devs.json
2. /insights-developer-survey  → see what the report will look like with 5 mocks
```

Useful for showing the client "what it will look like" before collecting.

## 📊 What comes out in the insights report

`saida/insights-developer-survey-<DATE>.md` (generated by the skill) contains:

1. **Executive summary**: 3 insights + 3 gaps + perceived maturity
2. **Demographics** (S1): who responded, distribution
3. **Copilot adoption** (S2): % licenses, **adoption per mode (Ask/Edit/Agent)**, active features, perceived gain
4. **MS/GitHub ecosystem** (S3): adoption table
5. **AI + dev practices** (S4): TDD, SDD, debugging, onboarding + anonymized quotes
6. **Agent knowledge** (S5): "knows+uses / knows / does not know" matrix for 8 concepts
7. **Instructions files** (S6): who uses, maintains, updates
8. **Usability** (S7): Champion, metrics, trust, iterations
9. **Security** (S8): policy, scanners, DLP, audit + **governance score 0-100**
10. **Pain points** (S9): top 5 frustrations + wishlist (quotes)
11. **Prioritized recommendations**: quick wins, next quarter, semester
12. **Connection to the main assessment**: capability by capability

## 🔗 How the survey informs the main assessment

If you ran both:

| Assessment capability | Survey signal | Validation |
|---|---|---|
| **P1-C1** AI Coding Assistants | S2-Q1, Q2, Q7 | Declared score vs. real adoption |
| **P1-C2** DevEx Platform | S6-Q5, S7-Q2 | Is there shared tooling? |
| **P1-C5** Onboarding and Training | S7-Q1, Q2 | How did devs learn? Are there Champions? |
| **P1-C8** Productivity Measurement | S7-Q4 | Are DORA/DX/SPACE actually measured? |
| **P2-C4** DevSecOps | S8-Q4, Q5, Q11 | Active scanners vs. vulns seen |
| **P2-C10** Supply Chain | S8-Q4, Q6 | SBOM, secret scan, DLP |
| **P3-C5** Agentic Applications | S5-Q3, Q6, Q9 | Custom agents, MCP: technical sophistication |
| **P3-C6** Identity and Access | S8-Q1, Q8, Q9 | Policy, DLP, audit |

> 💡 **Classic use case:** leadership rates P1-C1 as L3, but the survey reveals 60% of devs rarely use it: a gap of real adoption, not of licensing.

## 🔐 About anonymity

- Microsoft Forms has an "Anonymous responses" option: **CHECKING it is mandatory** for this survey
- Without it, Forms captures the respondent's MS365 account email (breaks anonymity)
- The `/import-developer-survey` skill validates that the Email/Name columns are empty and alerts if they are not
- Quotes in the report are cited by **question ID** (e.g. "Answer S9-Q1"), never by respondent_id or role

## 📅 Suggested cadence

- **First time:** before defining the engineering AI strategy (baseline)
- **After a Copilot Enterprise rollout:** 30 days later
- **Quarterly:** to measure evolution
- **After workshops/trainings:** to validate absorption

## 📚 Related documentation

### Other kit folders
- **Companion survey (identified, training):** [`../survey-learning/`](../survey-learning/), the Learning & Growth Survey (32 q, 5-8 min, IDENTIFIED). Generates a personalized training plan with a Champions Network and a workshop calendar. Use it AFTER this Developer Survey to move from "measured behavior" to "action plan"
- **Main assessment (organizational):** [`../README.en.md`](../README.en.md), 158 Likert L0-L4 questions, leadership-driven, generates 5 production PDFs
- **Multi-respondent collection for the main assessment:** [`../coleta/INSTRUCOES-FORMS.en.md`](../coleta/INSTRUCOES-FORMS.en.md)
- **Wizard that consolidates into the executive PDF:** [`../wizard/`](../wizard/), feeds Part 4 of the PDF with data from this survey + the learning survey

### Skills for this survey
- Skill that imports Excel → JSON: [`../.github/skills/import-developer-survey/SKILL.md`](../.github/skills/import-developer-survey/SKILL.md)
- Skill that generates the report + maturity: [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)

### How the 3 surveys connect (recommended run order)

```
1. Survey-devs (anonymous, THIS ONE)  → measures real behavior + computed maturity
2. Survey-learning (identified)     → measures desire + barriers + Champions
3. Main assessment                  → leadership evaluates INFORMED by the 2 above
4. /implementation-wizard            → consolidates everything
5. /generate-reports                 → 5 production-quality PDFs
```

## 🔗 Validated official sources (v2.0, 2026-05-08)

All survey terminology and concepts were cross-checked against official documentation. Use these sources to answer dev questions about what each term means:

### GitHub Copilot
- **Copilot Spaces** (GA Sep/2025): <https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context/>
- **Official Spaces docs**: <https://docs.github.com/en/copilot/concepts/context/spaces>
- **Knowledge Bases sunset → Spaces** (Nov/2025): <https://github.blog/changelog/2025-10-17-copilot-knowledge-bases-can-now-be-converted-to-copilot-spaces/>
- **Copilot Coding Agent** (successor to Workspace, GA Sep/2025): picks up an issue, opens a PR by itself

### Microsoft Foundry (ex-Azure AI Foundry)
- **Foundry Agent Service overview**: <https://learn.microsoft.com/en-us/azure/foundry/agents/overview>
- **What's new Mar/2026** (MCP, A2A, multi-agent): <https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/>
- **Connectors (1,400+ business systems)**: <https://learn.microsoft.com/en-us/connectors/azureagentservice/>

### Agentic DevOps (Microsoft terminology)
- **DevOps Playbook for the Agentic Era**: <https://devblogs.microsoft.com/all-things-azure/agentic-devops-practices-principles-strategic-direction/>
- **Reimagining the developer lifecycle**: <https://developer.microsoft.com/blog/reimagining-every-phase-of-the-developer-lifecycle>
- **Personas (System Designer, Agent Operator)**: <https://learn.microsoft.com/en-us/azure/well-architected/ai/personas>
- **Microsoft Reactor: Agentic DevOps Live**: <https://developer.microsoft.com/en-us/reactor/series/s-1625/>
- **Azure Agentic DevOps Solutions**: <https://azure.microsoft.com/en-us/solutions/devops>

### Spec-Driven Development
- **GitHub Spec Kit**: <https://github.com/github/spec-kit>

### Applicability to the main assessment
- The maturity assessment in the parent folder uses the 7 strategies S1-S7 (GitHub Migration, Foundry+SRE, App Modernization, AI Apps, Copilot Acceleration, Agentic Activation, Security & Governance), aligned with the Microsoft **Agentic DevOps** framework.
- The 8 profiles (full-stack, backend-api, platform-eng, security-ops, frontend, data-ml, devops-sre, legacy) cover the Agentic DevOps personas.
