# AI Maturity Assessment, Pillar P1: Produtividade do Desenvolvedor (Developer Productivity)

> Measures how much engineering adopts AI to accelerate the coding, documentation, review, onboarding, and internal collaboration cycle.

> [!IMPORTANT]
> Runtime-safe localized edition: structural labels are in English and all IDs are preserved.
> The canonical question wording (the text in each `P1-Cx-Qy` heading) stays in Portuguese, byte-identical to the Microsoft Forms question bank, to keep strict scoring and audit parity with the workbook.

## Overview

- **Pillar:** `P1`, Produtividade do Desenvolvedor (Developer Productivity)
- **Capabilities:** 9
- **Total questions:** 53
- **Scale:** Likert L0–L4 (Initial → Optimizing)
- **Question language:** Portuguese (Brazil), canonical wording preserved in every edition
- **KPI/context/evidence language:** English (universal technical terms)
- **Expected answer per question:** 1 selected level + evidence text (recommended minimum 80 characters) + optional attachment

## How to interpret the scale

| Level | Label | Meaning |
|---|---|---|
| **L0** | Initial | No established practice; ad-hoc actions, no tool or policy. |
| **L1** | Developing | Isolated pilots, coverage <25%, no governance. |
| **L2** | Defined | Adoption in 25–50% of teams, with guidelines and basic training. |
| **L3** | Managed | Coverage >75% with impact metrics and shared libraries/templates. |
| **L4** | Optimizing | Near-universal coverage (>95%), automation, fine-tuning, measured continuous improvement. |

## Types of information collected per question

Each question simultaneously captures **three types of data**:

1. **Quantitative (KPI):** an explicit numeric metric (e.g., % active developers, MTTR, lead time, coverage rate). Use the suggested KPI to standardize comparison across teams.

2. **Qualitative (level description):** the respondent selects the L0–L4 level whose description best represents the reality observed today (not the aspirational one).

3. **Evidence (text + attachments):** documentary proof: pipeline link, dashboard screenshot, policy, runbook, license contract, exported metric. The more specific, the higher the evidence quality (scale: none → minimal → adequate → detailed → exemplary).

## Evidence quality criteria

- **Minimal (<80 characters):** generic text, no tool name, metric, or link.
- **Adequate (80–250):** mentions tool + approximate coverage/scope.
- **Detailed (250–500):** includes numeric metric + link/attachment + measurement period.
- **Exemplary (>500 or multiple attachments):** multiple corroborating sources, time series, before/after comparison.

## Capabilities of pillar P1

- **P1-C1**: Assistentes de Codificação IA (AI Coding Assistants), 5 questions
- **P1-C2**: Plataforma de Experiência do Desenvolvedor (Developer Experience Platform), 6 questions
- **P1-C3**: Gestão do Conhecimento (Knowledge Management), 6 questions
- **P1-C4**: Automação de Revisão de Código (Code Review Automation), 7 questions
- **P1-C5**: Onboarding e Treinamento de Desenvolvedores (Developer Onboarding & Training), 7 questions
- **P1-C6**: Inner Source e Colaboração (Inner Source & Collaboration), 6 questions
- **P1-C7**: Automação de Documentação (Documentation Automation), 5 questions
- **P1-C8**: Medição de Produtividade do Desenvolvedor (Developer Productivity Measurement), 6 questions
- **P1-C9**: Automação de Ambientes e Espaços de Trabalho (Environment & Workspace Automation), 5 questions

---

## P1-C1: Assistentes de Codificação IA (AI Coding Assistants)

**5 questions in this capability.**

### P1-C1-Q1: Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% developers using AI completion`

**Context**

- **What it measures:** Measures adoption of AI-powered code completion and suggestion tools across the development team.
- **Why it matters:** AI coding assistants can increase developer velocity by 30-55% on routine coding tasks, reducing time-to-market.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No AI coding tools implemented. All code is written manually without AI assistance. | • No AI tool licenses<br>• No AI tool policies<br>• Manual-only coding workflows |
| **L1** | Developing | Pilot implementation of an AI coding assistant for <10% of developers. Ad-hoc use without guidelines. | • Pilot program documentation<br>• < 10% license allocation<br>• No usage policy defined |
| **L2** | Defined | AI coding assistant deployed to 25-50% of developers with usage guidelines and basic training. | • 25-50% license coverage<br>• Written usage guidelines<br>• Completion training materials |
| **L3** | Managed | AI coding assistant deployed to >75% of developers with measured productivity gains >15% and prompt libraries. | • >75% active users<br>• Productivity metrics showing >15% gain<br>• Shared prompt library repository |
| **L4** | Optimizing | Universal AI coding assistant (>95%) with custom model fine-tuning and measured velocity improvement >30%. | • >95% daily active usage<br>• Custom model fine-tuning config<br>• Measured >30% velocity improvement<br>• Automated suggestion quality tracking |

---

### P1-C1-Q2: Quão efetivamente sua equipe aproveita IA para revisão de código e melhoria de qualidade?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs with AI review`

**Context**

- **What it measures:** Measures use of AI in code review processes to catch bugs, suggest improvements, and enforce standards.
- **Why it matters:** AI-assisted code review reduces review time by 40% and catches 20% more defects than manual-only review.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No AI participation in code review. All reviews are manual peer reviews. | • Manual-only review process<br>• No AI review tools<br>• No automated quality gates |
| **L1** | Developing | Basic linting and static analysis tools in CI. No AI-driven review suggestions. | • CI linting configuration<br>• Static analysis tool setup<br>• No AI review bot configured |
| **L2** | Defined | AI review bot configured on 30-60% of repositories, providing automated code suggestions. | • AI review bot on 30-60% of repos<br>• PR suggestion examples<br>• Review bot configuration docs |
| **L3** | Managed | AI review integrated in >80% of repositories with custom rules aligned to team standards. | • >80% repo coverage<br>• Custom rule configuration<br>• Measured >25% review cycle reduction |
| **L4** | Optimizing | AI performs the first review on all PRs, automatically approving low-risk changes and escalating critical ones. | • 100% PR AI first-pass<br>• Auto-approval policy documented<br>• Risk classification model<br>• >50% cycle time reduction |

---

### P1-C1-Q3: Como sua organização mede e rastreia o impacto das ferramentas de codificação IA na produtividade?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 0.8
- **Professional Edition:** No
- **Primary KPI:** `Productivity measurement maturity`

**Context**

- **What it measures:** Measures the organization's ability to quantify the value of AI coding tools.
- **Why it matters:** Without measurement, organizations cannot justify AI tool investment or optimize adoption strategies.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No measurement of AI tool impact. No baseline productivity metrics captured. | • No DORA metrics<br>• No productivity dashboards<br>• No AI tool usage tracking |
| **L1** | Developing | Anecdotal developer feedback on AI tool usefulness. No quantitative measurement. | • Developer survey results<br>• Informal feedback collection<br>• No quantitative data |
| **L2** | Defined | Basic DORA metrics tracked (deployment frequency, lead time). AI tool usage analytics available. | • DORA metrics dashboard<br>• Monthly usage analytics report<br>• Baseline measurements established |
| **L3** | Managed | Comprehensive developer productivity metrics including AI-specific measures: acceptance rate, time saved. | • >40% suggestion acceptance rate<br>• >20% time-to-merge improvement<br>• Defect density trend analysis |
| **L4** | Optimizing | Real-time productivity intelligence platform correlating AI tool usage with business outcomes. | • Real-time productivity dashboard<br>• Automated ROI reports<br>• Business outcome correlation analysis<br>• Per-team optimization recommendations |

---

### P1-C1-Q4: Qual nível de capacidades de testes assistidos por IA sua organização emprega?

**Metadata**

- **Target audience:** Developer, qa-test, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% test coverage from AI generation`

**Context**

- **What it measures:** Measures use of AI to generate, maintain, and optimize test suites.
- **Why it matters:** AI-generated tests can increase coverage from 40% to 80% in weeks, catching regressions that manual tests miss.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | All tests written manually. Test coverage below 40% in most projects. | • Manual test writing only<br>• <40% average coverage<br>• No AI test generation tools |
| **L1** | Developing | Occasional use of AI to generate unit test skeletons. Coverage remains below 50%. | • Ad-hoc AI test generation<br>• <50% coverage rate measured<br>• No systematic approach |
| **L2** | Defined | AI test generation integrated into the development flow for 30-50% of new code. Coverage >60%. | • AI test generation in 30-50% of new code<br>• 60% coverage gates in CI<br>• Test generation guidelines |
| **L3** | Managed | AI generates >70% of unit tests with human review. Coverage >75%. AI identifies edge cases. | • >70% AI-generated tests<br>• >75% coverage across projects<br>• Edge case suggestion examples |
| **L4** | Optimizing | AI-driven test optimization: automatically generates regression suites, identifies flaky tests, optimizes coverage. | • >85% coverage rate measured<br>• <5% flaky test rate<br>• Automated regression suite generation<br>• Mutation testing integration |

---

### P1-C1-Q5: Como sua organização governa o código gerado por IA em termos de segurança e conformidade?

**Metadata**

- **Target audience:** Developer, Security, product-owner, qa-test
- **Weight:** 1.1
- **Professional Edition:** No
- **Primary KPI:** `AI code governance maturity`

**Context**

- **What it measures:** Measures policies and controls around AI-generated code quality, security, and IP compliance.
- **Why it matters:** Without governance, AI-generated code can introduce vulnerabilities, license violations, and compliance risks.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No governance over AI-generated code. No policy exists. Developers use AI tools without restrictions. | • No AI code policy<br>• No security scanning of AI code<br>• No license compliance checks |
| **L1** | Developing | A basic policy exists prohibiting AI use in security-sensitive modules. No automation. | • Written AI usage policy<br>• Security-sensitive module list<br>• No automated enforcement |
| **L2** | Defined | AI-generated code goes through standard security analysis (SAST/DAST). License compliance checks in CI. | • SAST/DAST pipeline includes AI code<br>• License compliance scanning<br>• Policy enforcement in CI |
| **L3** | Managed | Dedicated AI code quality gates: vulnerability scanning, license auditing, code quality review. | • AI-specific quality gates<br>• Code provenance tracking<br>• <2% security flag rate<br>• Quarterly audit reports |
| **L4** | Optimizing | Real-time AI code governance: every suggestion scanned before display, blocked licenses enforced, and quality metrics tracked. | • Pre-display content scanning enabled<br>• Auto-rejection of blocked licenses<br>• Zero unreviewed AI code policy<br>• Compliance certification achieved |

---

## P1-C2: Plataforma de Experiência do Desenvolvedor (Developer Experience Platform)

**6 questions in this capability.**

### P1-C2-Q1: Quão maduro é seu portal ou plataforma interna para desenvolvedores?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** Yes
- **Primary KPI:** `Developer portal adoption %`

**Context**

- **What it measures:** Measures the maturity of centralized developer portal for service catalog, docs, and self-service.
- **Why it matters:** A mature developer portal reduces onboarding time by 60% and eliminates context-switching between tools.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No developer portal. Documentation scattered across wikis, Slack, and email. | • No centralized portal<br>• Documentation in multiple tools<br>• No service catalog |
| **L1** | Developing | Basic wiki or Confluence space with some documentation. No service catalog or self-service capabilities. | • Central wiki exists<br>• Some API docs<br>• No service catalog |
| **L2** | Defined | Developer portal deployed (Backstage or similar) with service catalog covering >50% of services. Basic documentation templates. | • >50% services cataloged<br>• Portal deployment docs<br>• Documentation templates published |
| **L3** | Managed | Developer portal covers >80% of services with self-service scaffolding, automated API docs, and integrated CI/CD status. Onboarding time reduced >40%. | • >80% service coverage<br>• Self-service scaffolding tooling<br>• >40% onboarding time reduction |
| **L4** | Optimizing | AI-powered developer portal: natural language search across all docs, auto-generated architecture diagrams, predictive issue detection. >95% developer satisfaction. | • AI-powered search enabled<br>• Auto-generated architecture diagrams<br>• >95% satisfaction score<br>• Predictive issue detection |

---

### P1-C2-Q2: Quão efetivamente suas equipes usam ambientes de desenvolvimento padronizados?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 0.9
- **Professional Edition:** Yes
- **Primary KPI:** `Environment setup time (minutes)`

**Context**

- **What it measures:** Measures standardization of development environments across teams.
- **Why it matters:** Standardized environments eliminate 'works on my machine' issues and reduce setup time from days to minutes.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Each developer maintains their own environment setup. No standardization. Setup takes >4 hours for new team members. | • No environment standardization<br>• Setup time >4 hours<br>• Manual dependency installation |
| **L1** | Developing | README with setup instructions. Some teams use Docker for local development. Setup time 1-4 hours. | • README setup guide<br>• Some Docker usage<br>• 1-4 hour setup time |
| **L2** | Defined | Docker Compose or devcontainer for >50% of projects. Setup time <30 minutes. Shared configurations. | • >50% projects with containers<br>• <30 min setup time<br>• Shared dev configs |
| **L3** | Managed | Standardized devcontainers for >80% of projects. Cloud-based dev environments available (Codespaces). Setup time <10 minutes. | • >80% devcontainer coverage<br>• Cloud dev environment available<br>• <10 min setup time |
| **L4** | Optimizing | One-click ephemeral dev environments with AI-configured dependencies. Zero manual setup. Environment parity with production guaranteed. | • One-click environment creation<br>• Zero manual setup steps<br>• Production parity verification documented<br>• AI dependency configuration |

---

### P1-C2-Q3: Em que medida Plataforma de Experiência do Desenvolvedor (self-service IDP) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `Self-service catalog coverage`

**Context**

- **What it measures:** Internal developer platform (IDP) provides paved paths with self-service provisioning.
- **Why it matters:** IDPs reduce cognitive load and accelerate onboarding by 50-70%.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No self-service idp implemented. Teams operate without this capability. | • No self-service IDP deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of self-service idp with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | self-service IDP adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | self-service IDP standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | self-service IDP is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q4: Em que medida Plataforma de Experiência do Desenvolvedor (golden paths and templates) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services from templates`

**Context**

- **What it measures:** Golden-path templates encode opinionated defaults for new services.
- **Why it matters:** Standard templates reduce time-to-first-commit and enforce security baselines.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No golden paths and templates implemented. Teams operate without this capability. | • No golden paths and templates deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of golden paths and templates with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | golden paths and templates adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | golden paths and templates standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | golden paths and templates is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q5: Em que medida Plataforma de Experiência do Desenvolvedor (developer portal) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `Portal MAU (monthly active users)`

**Context**

- **What it measures:** A developer portal centralizes docs, APIs, and service catalog.
- **Why it matters:** A single pane of glass reduces context switching and improves discovery.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No developer portal implemented. Teams operate without this capability. | • No developer portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of developer portal with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | developer portal adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | developer portal standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | developer portal is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q6: Em que medida Plataforma de Experiência do Desenvolvedor (paved road policy enforcement) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Security, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `services on paved road`

**Context**

- **What it measures:** Platform policies are codified so teams must opt-out explicitly.
- **Why it matters:** Policy-as-code turns governance into an enabler, not a blocker.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No paved road policy enforcement implemented. Teams operate without this capability. | • No paved road policy enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of paved road policy enforcement with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | paved road policy enforcement adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | paved road policy enforcement standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | paved road policy enforcement is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C3: Gestão do Conhecimento (Knowledge Management)

**6 questions in this capability.**

### P1-C3-Q1: Quão efetivamente sua organização captura e compartilha conhecimento de desenvolvimento?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `Knowledge retrieval success rate %`

**Context**

- **What it measures:** Measures how well development knowledge is captured, organized, and accessible.
- **Why it matters:** Poor knowledge management causes 20% of developer time wasted searching for information or reinventing solutions.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | Knowledge lives in individual developers' heads. No documentation culture. High bus-factor risk. | • No documentation policy<br>• Knowledge in individuals<br>• High bus-factor risk |
| **L1** | Developing | Basic documentation exists for critical systems. Knowledge sharing through ad-hoc meetings and Slack threads. | • Some critical system docs<br>• Ad-hoc knowledge sharing<br>• Slack-based Q&A channel |
| **L2** | Defined | Structured documentation in central wiki. Regular tech talks or knowledge sharing sessions. Decision records for major changes. | • Central wiki with structure<br>• Regular tech talks<br>• ADR practice established |
| **L3** | Managed | Searchable knowledge base covering >70% of systems. AI-assisted documentation generation. Automated runbooks for common issues. | • >70% system documentation<br>• AI-assisted doc generation<br>• Automated runbooks published |
| **L4** | Optimizing | AI-powered knowledge graph linking code, docs, incidents, and decisions. Natural language queries return contextual answers. Knowledge freshness auto-monitored. | • Knowledge graph implementation<br>• NL query interface<br>• Automated freshness monitoring enabled<br>• Contextual answer system |

---

### P1-C3-Q2: Em que medida Gestão do Conhecimento (semantic code search) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos indexed`

**Context**

- **What it measures:** Organization-wide semantic search across repos, docs, and chats.
- **Why it matters:** Semantic search cuts duplicate work by making prior solutions discoverable.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No semantic code search implemented. Teams operate without this capability. | • No semantic code search deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of semantic code search with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | semantic code search adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | semantic code search standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | semantic code search is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q3: Em que medida Gestão do Conhecimento (RAG-based docs assistant) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `queries per developer/month`

**Context**

- **What it measures:** LLM-backed assistant answers dev questions from internal knowledge base.
- **Why it matters:** RAG assistants reduce interrupt load on senior engineers.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No rag-based docs assistant implemented. Teams operate without this capability. | • No RAG-based docs assistant deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of rag-based docs assistant with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | RAG-based docs assistant adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | RAG-based docs assistant standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | RAG-based docs assistant is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q4: Em que medida Gestão do Conhecimento (runbook and playbook coverage) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% critical services with runbook`

**Context**

- **What it measures:** Automated runbooks capture operational knowledge.
- **Why it matters:** Documented runbooks shorten MTTR and enable on-call rotation.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No runbook and playbook coverage implemented. Teams operate without this capability. | • No runbook and playbook coverage deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of runbook and playbook coverage with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | runbook and playbook coverage adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | runbook and playbook coverage standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | runbook and playbook coverage is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q5: Em que medida Gestão do Conhecimento (ADR (architecture decision records)) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with ADRs`

**Context**

- **What it measures:** Architecture decisions are captured as ADRs in the repo.
- **Why it matters:** ADRs preserve institutional memory beyond individuals.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No adr (architecture decision records) implemented. Teams operate without this capability. | • No ADR (architecture decision records) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of adr (architecture decision records) with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | ADR (architecture decision records) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | ADR (architecture decision records) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | ADR (architecture decision records) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q6: Em que medida Gestão do Conhecimento (learning content & curated paths) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `completions per quarter`

**Context**

- **What it measures:** Curated learning paths tied to role and career ladder.
- **Why it matters:** Structured learning reduces ramp time and improves retention.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No learning content & curated paths implemented. Teams operate without this capability. | • No learning content & curated paths deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of learning content & curated paths with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | learning content & curated paths adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | learning content & curated paths standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | learning content & curated paths is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C4: Automação de Revisão de Código (Code Review Automation)

**7 questions in this capability.**

### P1-C4-Q1: Em que medida Automação de Revisão de Código (AI reviewer bot on every PR) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs AI-reviewed`

**Context**

- **What it measures:** A bot posts AI-generated review comments on every PR.
- **Why it matters:** AI reviewers catch issues before humans look at the code.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No ai reviewer bot on every pr implemented. Teams operate without this capability. | • No AI reviewer bot on every PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of ai reviewer bot on every pr with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | AI reviewer bot on every PR adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | AI reviewer bot on every PR standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | AI reviewer bot on every PR is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q2: Em que medida Automação de Revisão de Código (static linting and style auto-fix) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `lint violations per kLOC`

**Context**

- **What it measures:** Linters and formatters run automatically on every commit.
- **Why it matters:** Automated style removes bikeshedding from reviews.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No static linting and style auto-fix implemented. Teams operate without this capability. | • No static linting and style auto-fix deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of static linting and style auto-fix with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | static linting and style auto-fix adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | static linting and style auto-fix standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | static linting and style auto-fix is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q3: Em que medida Automação de Revisão de Código (automated security review) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `critical findings per PR`

**Context**

- **What it measures:** SAST comments inline on the PR diff.
- **Why it matters:** Inline findings are fixed 10x faster than backlog items.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No automated security review implemented. Teams operate without this capability. | • No automated security review deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of automated security review with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | automated security review adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | automated security review standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | automated security review is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q4: Em que medida Automação de Revisão de Código (required-reviewer rules) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs meeting review rule`

**Context**

- **What it measures:** CODEOWNERS enforces domain-expert review per path.
- **Why it matters:** Right reviewer + right code = better catches.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No required-reviewer rules implemented. Teams operate without this capability. | • No required-reviewer rules deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of required-reviewer rules with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | required-reviewer rules adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | required-reviewer rules standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | required-reviewer rules is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q5: Em que medida Automação de Revisão de Código (review SLA tracking) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median PR cycle time`

**Context**

- **What it measures:** PR cycle time is measured and targeted.
- **Why it matters:** Fast review cycles keep developers in flow.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No review sla tracking implemented. Teams operate without this capability. | • No review SLA tracking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of review sla tracking with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | review SLA tracking adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | review SLA tracking standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | review SLA tracking is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q6: Em que medida Automação de Revisão de Código (change size enforcement) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, data-ai
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median PR size (LoC)`

**Context**

- **What it measures:** Pre-commit hooks encourage small PRs.
- **Why it matters:** Small PRs get better reviews and merge faster.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No change size enforcement implemented. Teams operate without this capability. | • No change size enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of change size enforcement with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | change size enforcement adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | change size enforcement standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | change size enforcement is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q7: Em que medida Automação de Revisão de Código (reviewer load balancing) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `review load balance index`

**Context**

- **What it measures:** Reviewer assignment balances load across the team.
- **Why it matters:** Balanced review load prevents burnout of top reviewers.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No reviewer load balancing implemented. Teams operate without this capability. | • No reviewer load balancing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of reviewer load balancing with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | reviewer load balancing adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | reviewer load balancing standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | reviewer load balancing is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C5: Onboarding e Treinamento de Desenvolvedores (Developer Onboarding & Training)

**7 questions in this capability.**

### P1-C5-Q1: Em que medida Onboarding e Treinamento de Desenvolvedores (codespaces/dev containers for instant env) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `time-to-first-commit (hours)`

**Context**

- **What it measures:** Cloud dev envs are ready in minutes.
- **Why it matters:** Fast env setup unblocks new hires on day one.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No codespaces/dev containers for instant env implemented. Teams operate without this capability. | • No codespaces/dev containers for instant env deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of codespaces/dev containers for instant env with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | codespaces/dev containers for instant env adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | codespaces/dev containers for instant env standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | codespaces/dev containers for instant env is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q2: Em que medida Onboarding e Treinamento de Desenvolvedores (structured onboarding playbook) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% new hires completing onboarding`

**Context**

- **What it measures:** A documented 30/60/90-day onboarding plan per role.
- **Why it matters:** Structured onboarding reduces ramp time by 30-50%.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No structured onboarding playbook implemented. Teams operate without this capability. | • No structured onboarding playbook deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of structured onboarding playbook with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | structured onboarding playbook adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | structured onboarding playbook standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | structured onboarding playbook is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q3: Em que medida Onboarding e Treinamento de Desenvolvedores (mentor pairing program) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `mentor:mentee ratio`

**Context**

- **What it measures:** Every new hire gets a senior mentor for 90 days.
- **Why it matters:** Mentoring shortens ramp and boosts retention.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No mentor pairing program implemented. Teams operate without this capability. | • No mentor pairing program deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of mentor pairing program with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | mentor pairing program adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | mentor pairing program standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | mentor pairing program is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q4: Em que medida Onboarding e Treinamento de Desenvolvedores (hands-on curriculum & kata) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `katas completed per hire`

**Context**

- **What it measures:** Role-specific coding kata produce demonstrable skill.
- **Why it matters:** Deliberate practice builds skill faster than reading.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No hands-on curriculum & kata implemented. Teams operate without this capability. | • No hands-on curriculum & kata deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of hands-on curriculum & kata with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | hands-on curriculum & kata adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | hands-on curriculum & kata standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | hands-on curriculum & kata is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q5: Em que medida Onboarding e Treinamento de Desenvolvedores (shadow on-call rotation) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `new hires who shadowed on-call`

**Context**

- **What it measures:** New hires shadow on-call to learn operational context.
- **Why it matters:** Operational context is the fastest way to understand the system.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No shadow on-call rotation implemented. Teams operate without this capability. | • No shadow on-call rotation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of shadow on-call rotation with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | shadow on-call rotation adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | shadow on-call rotation standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | shadow on-call rotation is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q6: Em que medida Onboarding e Treinamento de Desenvolvedores (onboarding feedback loop) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `NPS from new hires`

**Context**

- **What it measures:** New hires rate onboarding; results drive improvements.
- **Why it matters:** Feedback loops turn onboarding into a continuously improving product.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No onboarding feedback loop implemented. Teams operate without this capability. | • No onboarding feedback loop deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of onboarding feedback loop with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | onboarding feedback loop adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | onboarding feedback loop standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | onboarding feedback loop is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q7: Em que medida Onboarding e Treinamento de Desenvolvedores (ramp-time measurement) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `median ramp-time to first deploy`

**Context**

- **What it measures:** Time-to-first-deploy is measured and improved for new hires.
- **Why it matters:** Measuring ramp turns onboarding improvements into ROI.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No ramp-time measurement implemented. Teams operate without this capability. | • No ramp-time measurement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of ramp-time measurement with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | ramp-time measurement adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | ramp-time measurement standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | ramp-time measurement is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C6: Inner Source e Colaboração (Inner Source & Collaboration)

**6 questions in this capability.**

### P1-C6-Q1: Em que medida Inner Source e Colaboração (internal repos with open contribution) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos open to all devs`

**Context**

- **What it measures:** Repos inside the org welcome PRs from other teams.
- **Why it matters:** Inner source breaks silos and increases reuse.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No internal repos with open contribution implemented. Teams operate without this capability. | • No internal repos with open contribution deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of internal repos with open contribution with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | internal repos with open contribution adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | internal repos with open contribution standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | internal repos with open contribution is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q2: Em que medida Inner Source e Colaboração (CONTRIBUTING.md standards) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos with CONTRIBUTING`

**Context**

- **What it measures:** Every repo documents how to contribute and review.
- **Why it matters:** Clear contribution norms lower friction for cross-team work.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No contributing.md standards implemented. Teams operate without this capability. | • No CONTRIBUTING.md standards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of contributing.md standards with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | CONTRIBUTING.md standards adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | CONTRIBUTING.md standards standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | CONTRIBUTING.md standards is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q3: Em que medida Inner Source e Colaboração (inner-source discovery portal) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `cross-team PRs per month`

**Context**

- **What it measures:** A portal indexes inner-source projects seeking contributions.
- **Why it matters:** Discovery drives participation.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No inner-source discovery portal implemented. Teams operate without this capability. | • No inner-source discovery portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of inner-source discovery portal with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | inner-source discovery portal adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | inner-source discovery portal standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | inner-source discovery portal is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q4: Em que medida Inner Source e Colaboração (good-first-issue labeling) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `GFI issues closed per month`

**Context**

- **What it measures:** Starter issues help newcomers contribute confidently.
- **Why it matters:** Labeling lowers the bar for first-time contributors.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No good-first-issue labeling implemented. Teams operate without this capability. | • No good-first-issue labeling deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of good-first-issue labeling with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | good-first-issue labeling adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | good-first-issue labeling standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | good-first-issue labeling is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q5: Em que medida Inner Source e Colaboração (cross-team design reviews) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `reviews per quarter`

**Context**

- **What it measures:** Design docs are reviewed by multiple teams.
- **Why it matters:** Cross-team review catches assumptions and shares patterns.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No cross-team design reviews implemented. Teams operate without this capability. | • No cross-team design reviews deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of cross-team design reviews with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | cross-team design reviews adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | cross-team design reviews standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | cross-team design reviews is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q6: Em que medida Inner Source e Colaboração (community of practice) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, engineering-leader
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `CoP active members`

**Context**

- **What it measures:** Guilds and CoPs build horizontal expertise.
- **Why it matters:** CoPs accelerate learning and de-risk hiring gaps.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No community of practice implemented. Teams operate without this capability. | • No community of practice deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of community of practice with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | community of practice adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | community of practice standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | community of practice is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C7: Automação de Documentação (Documentation Automation)

**5 questions in this capability.**

### P1-C7-Q1: Em que medida Automação de Documentação (docs-as-code in Git) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% services with docs in repo`

**Context**

- **What it measures:** Docs live with code and are reviewed in PRs.
- **Why it matters:** Docs-as-code prevents docs from rotting away from source.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No docs-as-code in git implemented. Teams operate without this capability. | • No docs-as-code in Git deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of docs-as-code in git with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | docs-as-code in Git adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | docs-as-code in Git standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | docs-as-code in Git is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q2: Em que medida Automação de Documentação (auto-generated API reference) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% APIs with generated docs`

**Context**

- **What it measures:** API reference is generated from OpenAPI or source.
- **Why it matters:** Generated docs are always up to date.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No auto-generated api reference implemented. Teams operate without this capability. | • No auto-generated API reference deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of auto-generated api reference with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | auto-generated API reference adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | auto-generated API reference standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | auto-generated API reference is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q3: Em que medida Automação de Documentação (AI-assisted doc drafting) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% PRs with AI doc suggestions`

**Context**

- **What it measures:** AI suggests README and doc updates from code diffs.
- **Why it matters:** AI drafts raise the floor on documentation quality.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No ai-assisted doc drafting implemented. Teams operate without this capability. | • No AI-assisted doc drafting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of ai-assisted doc drafting with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | AI-assisted doc drafting adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | AI-assisted doc drafting standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | AI-assisted doc drafting is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q4: Em que medida Automação de Documentação (doc quality linting) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Architect, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `broken-link count`

**Context**

- **What it measures:** Link checks and style linters run in CI.
- **Why it matters:** Automated checks keep docs trustworthy.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No doc quality linting implemented. Teams operate without this capability. | • No doc quality linting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of doc quality linting with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | doc quality linting adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | doc quality linting standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | doc quality linting is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q5: Em que medida Automação de Documentação (docs analytics) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `top unanswered queries`

**Context**

- **What it measures:** Search analytics reveal what users cannot find.
- **Why it matters:** Analytics turn docs into a data-driven product.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No docs analytics implemented. Teams operate without this capability. | • No docs analytics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of docs analytics with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | docs analytics adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | docs analytics standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | docs analytics is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C8: Medição de Produtividade do Desenvolvedor (Developer Productivity Measurement)

**6 questions in this capability.**

### P1-C8-Q1: Em que medida Medição de Produtividade do Desenvolvedor (DORA four key metrics) foi adotado entre as equipes?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `deploys/day, lead time, CFR, MTTR`

**Context**

- **What it measures:** Deployment frequency, lead time, change fail rate, MTTR are tracked.
- **Why it matters:** DORA metrics correlate with business outcomes.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No dora four key metrics implemented. Teams operate without this capability. | • No DORA four key metrics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of dora four key metrics with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | DORA four key metrics adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | DORA four key metrics standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | DORA four key metrics is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q2: Em que medida Medição de Produtividade do Desenvolvedor (developer experience surveys) foi adotado entre as equipes?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `DX survey NPS`

**Context**

- **What it measures:** Quarterly surveys measure developer satisfaction.
- **Why it matters:** DX surveys surface friction that metrics miss.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No developer experience surveys implemented. Teams operate without this capability. | • No developer experience surveys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of developer experience surveys with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | developer experience surveys adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | developer experience surveys standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | developer experience surveys is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q3: Em que medida Medição de Produtividade do Desenvolvedor (build/test feedback loop time) foi adotado entre as equipes?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `p95 CI duration`

**Context**

- **What it measures:** CI provides signal within 10 minutes for typical PRs.
- **Why it matters:** Fast feedback keeps developers in flow.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No build/test feedback loop time implemented. Teams operate without this capability. | • No build/test feedback loop time deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of build/test feedback loop time with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | build/test feedback loop time adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | build/test feedback loop time standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | build/test feedback loop time is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q4: Em que medida Medição de Produtividade do Desenvolvedor (SPACE framework adoption) foi adotado entre as equipes?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `SPACE dimensions tracked`

**Context**

- **What it measures:** Teams track Satisfaction, Performance, Activity, Communication, Efficiency.
- **Why it matters:** SPACE balances quantitative and qualitative signals.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No space framework adoption implemented. Teams operate without this capability. | • No SPACE framework adoption deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of space framework adoption with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | SPACE framework adoption adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | SPACE framework adoption standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | SPACE framework adoption is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q5: Em que medida Medição de Produtividade do Desenvolvedor (flow vs friction dashboards) foi adotado entre as equipes?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% teams viewing dashboard monthly`

**Context**

- **What it measures:** Leaders and teams see productivity data side by side.
- **Why it matters:** Shared data aligns improvements across teams.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No flow vs friction dashboards implemented. Teams operate without this capability. | • No flow vs friction dashboards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of flow vs friction dashboards with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | flow vs friction dashboards adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | flow vs friction dashboards standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | flow vs friction dashboards is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q6: Em que medida Medição de Produtividade do Desenvolvedor (quarterly productivity OKRs) foi adotado entre as equipes?

**Metadata**

- **Target audience:** engineering-leader, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% teams hitting DX OKRs`

**Context**

- **What it measures:** DX improvements are tracked as OKRs.
- **Why it matters:** OKRs make productivity a first-class investment.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No quarterly productivity okrs implemented. Teams operate without this capability. | • No quarterly productivity OKRs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of quarterly productivity okrs with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | quarterly productivity OKRs adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | quarterly productivity OKRs standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | quarterly productivity OKRs is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C9: Automação de Ambientes e Espaços de Trabalho (Environment & Workspace Automation)

**5 questions in this capability.**

### P1-C9-Q1: Em que medida Automação de Ambientes e Espaços de Trabalho (reproducible local envs (devcontainers)) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% repos with devcontainer`

**Context**

- **What it measures:** Every repo ships a devcontainer or Nix shell.
- **Why it matters:** Reproducible envs eliminate 'works on my machine' failures.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No reproducible local envs (devcontainers) implemented. Teams operate without this capability. | • No reproducible local envs (devcontainers) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of reproducible local envs (devcontainers) with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | reproducible local envs (devcontainers) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | reproducible local envs (devcontainers) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | reproducible local envs (devcontainers) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q2: Em que medida Automação de Ambientes e Espaços de Trabalho (cloud workspaces (Codespaces/Gitpod)) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% devs using cloud workspace`

**Context**

- **What it measures:** Cloud workspaces are the default dev env.
- **Why it matters:** Cloud workspaces make env setup instant and consistent.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No cloud workspaces (codespaces/gitpod) implemented. Teams operate without this capability. | • No cloud workspaces (Codespaces/Gitpod) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of cloud workspaces (codespaces/gitpod) with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | cloud workspaces (Codespaces/Gitpod) adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | cloud workspaces (Codespaces/Gitpod) standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | cloud workspaces (Codespaces/Gitpod) is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q3: Em que medida Automação de Ambientes e Espaços de Trabalho (tool and SDK version pinning) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `tools pinned per repo`

**Context**

- **What it measures:** Language and tool versions are pinned and lockfiles committed.
- **Why it matters:** Pinned versions keep builds reproducible across machines.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No tool and sdk version pinning implemented. Teams operate without this capability. | • No tool and SDK version pinning deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of tool and sdk version pinning with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | tool and SDK version pinning adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | tool and SDK version pinning standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | tool and SDK version pinning is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q4: Em que medida Automação de Ambientes e Espaços de Trabalho (on-demand test data) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer, qa-test
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `time to get fresh test data`

**Context**

- **What it measures:** Developers can reset or provision realistic test data on demand.
- **Why it matters:** Fresh data unblocks testing and debugging.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No on-demand test data implemented. Teams operate without this capability. | • No on-demand test data deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of on-demand test data with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | on-demand test data adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | on-demand test data standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | on-demand test data is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q5: Em que medida Automação de Ambientes e Espaços de Trabalho (workspace telemetry & health) foi adotado entre as equipes?

**Metadata**

- **Target audience:** Developer, Platform Engineer, Architect
- **Weight:** 1.0
- **Professional Edition:** No
- **Primary KPI:** `% workspaces healthy`

**Context**

- **What it measures:** Workspace telemetry reveals setup failures and tool crashes.
- **Why it matters:** Telemetry lets platform teams fix friction proactively.

**Response format**

5-level Likert scale (L0–L4). Select **one** level that best describes your organization today. Add textual evidence and/or attachments (PDF, DOCX, XLSX, PNG, JPEG, up to 10 MB).

**Levels and expected evidence**

| Level | Label | Description | Suggested evidence |
|---|---|---|---|
| **L0** | Initial | No workspace telemetry & health implemented. Teams operate without this capability. | • No workspace telemetry & health deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Developing | Pilot implementation of workspace telemetry & health with <10% team coverage and ad-hoc use. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Defined | workspace telemetry & health adopted by 25-50% of teams with basic guidelines and training. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Managed | workspace telemetry & health standardized across >75% of teams with measured results and governance. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Optimizing | workspace telemetry & health is optimized, automated, and continuously improved with data-driven insights. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## How this section is scored

- Each question receives a numeric value from the selected level: L0=0, L1=1, L2=2, L3=3, L4=4.
- The capability score is the weighted average of its questions (default weight = 1.0; questions with weight 1.5 or 2.0 count more).
- The **P1** pillar score is the average of the 9 capabilities.
- The result is displayed on a 0–4 scale and converted to maturity % (level / 4 × 100).

## Quick glossary

- **Pillar:** strategic maturity dimension.
- **Capability:** functional subdomain within a pillar.
- **Question:** concrete assessment item, standard ID `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0–L4):** point on the maturity Likert scale.
- **KPI:** key indicator that objectively validates the declared level.
- **Evidence:** qualitative (text) or quantitative (attachment) proof that supports the answer.
