# Microsoft Forms Questions — Developer Survey (GitHub + AI)

> 75 questions in 9 sections. Estimated time: **20-25 min**. ANONYMOUS — we do not ask for respondent name or email.


> [!IMPORTANT]
> This localized bank translates instructions and question titles, but keeps answer options canonical when those options feed deterministic scoring. Keep all IDs (`Sx-Qy:`) unchanged in Microsoft Forms.

## How to Create the Form

1. Go to <https://forms.office.com> -> **+ New Form**
2. Suggested title: `Developer Survey — How my team uses GitHub & AI today`
3. Subtitle:
   ```
   Anonymous survey (15-25 min) about your GitHub Copilot practices,
   Copilot Chat modes (Ask/Edit/Agent), AI agents, instruction files,
   AI + Dev best practices and security.
   Your answers will inform the team AI adoption roadmap.
   ```
4. **Settings** (⚙️):
   - ☑ **Anonymous responses** (CRITICAL — keep enabled)
   - ☑ One response per person: **OFF** (we want multiple responses)
   - ☑ Accept responses
5. Add **9 sections** (`+ Add new` -> section icon):
   - **S1 — Respondent profile** (7 questions)
   - **S2 — GitHub Copilot — Adoption and Modes** (9 questions)
   - **S3 — Other Microsoft / GitHub AI tools** (7 questions)
   - **S4 — AI Development Practices** (9 questions)
   - **S5 — Agent Concepts and Structure** (11 questions)
   - **S6 — Markdown / Memory / Instructions** (6 questions)
   - **S7 — Usability and Best Practices** (9 questions)
   - **S8 — Security and Governance** (13 questions)
   - **S9 — Pain Points & Wishlist** (4 questions)

6. For each question below, add the corresponding Forms type:
   - **`choice`** → Choice (Single answer)
   - **`multi`** → Choice (Multiple answers / checkboxes)
   - **`text`** → Long Text

7. **TITLE** of each question must start with the ID + colon. Example:
   ```
   S2-Q1: Do you have an active GitHub Copilot license?
   ```
   > ⚠️ The ID is used by `/importar-survey-devs` for mapping. DO NOT REMOVE it.

8. Share via **+ Send / Collect responses** -> copy link -> send via Slack/Teams/email

9. When responses are ready, **Responses -> Open in Excel** -> rename to `respostas-survey-devs.xlsx` -> move to the kit root

---

## S1 — Respondent profile

_Basic questions about you and your context. Anonymous — we will not ask for name or email._

_7 questions in this section._

### Question `S1-Q1` — _Choice (single answer)_

> **S1-Q1: What is your current role?**

Options:
- Desenvolvedor Backend
- Desenvolvedor Frontend
- Full-Stack
- SRE / Platform Engineer
- Data Engineer / ML Engineer
- Architect
- Tech Lead
- Engineering Manager
- QA / SDET
- DevOps / DevEx
- Other

### Question `S1-Q2` — _Choice (single answer)_

> **S1-Q2: Total time as a developer?**

Options:
- < 2 years
- 2-5 years
- 6-10 years
- 11-15 years
- > 15 years

### Question `S1-Q3` — _Choice (single answer)_

> **S1-Q3: How long have you used AI in development (Copilot, Cursor, Claude Code, etc.)?**

Options:
- Nunca usei
- < 3 months
- 3-12 months
- 1-2 years
- > 2 years

### Question `S1-Q4` — _Choice (multiple answers)_

> **S1-Q4: Main languages you use day to day?**

Options:
- TypeScript / JavaScript
- Python
- C# / .NET
- Java / Kotlin
- Go
- Rust
- C++
- Ruby
- PHP
- Swift
- SQL (primary focus)
- Other

### Question `S1-Q5` — _Choice (single answer)_

> **S1-Q5: How many hours per day do you spend coding on average?**

Options:
- < 2h
- 2-4h
- 4-6h
- 6-8h
- > 8h

### Question `S1-Q6` — _Choice (single answer)_

> **S1-Q6: What is the size of your immediate squad/team?**

Options:
- Sou solo
- 2-4 pessoas
- 5-9 pessoas
- 10-15 pessoas
- > 15 pessoas

### Question `S1-Q7` — _Choice (single answer)_

> **S1-Q7: Work model?**

Options:
- Remoto 100%
- Híbrido (1-2 dias presencial)
- Híbrido (3-4 dias)
- Presencial 100%

---

## S2 — GitHub Copilot — Adoption and Modes

_Focus on GitHub Copilot. Includes current modes (Ask, Edit, Agent), autonomous Coding Agent, and Spaces for shared context._

_9 questions in this section._

### Question `S2-Q1` — _Choice (single answer)_

> **S2-Q1: Do you have an active GitHub Copilot license?**

Options:
- Sim — Copilot Enterprise
- Sim — Copilot Business
- Sim — Copilot Pro+ (individual)
- Sim — Copilot Pro (individual)
- Sim — Copilot Free
- Tenho licença mas não uso
- Não tenho licença

### Question `S2-Q2` — _Choice (single answer)_

> **S2-Q2: How often do you use Copilot?**

Options:
- Diariamente (várias horas)
- Diariamente (esporádico)
- Semanal
- Raramente
- Nunca

### Question `S2-Q3` — _Choice (multiple answers)_

> **S2-Q3: Which Copilot Chat MODES do you use? (select all that apply)**

Options:
- Ask (responder questions)
- Edit (edição multi-arquivo no IDE)
- Agent (autônomo no IDE, executa tasks)
- Copilot Coding Agent (autônomo no GitHub.com — assigna issue, abre PR sozinho)
- Plan / Vision
- Não uso o Chat — só completion inline
- Não conheço esses modos

### Question `S2-Q4` — _Choice (single answer)_

> **S2-Q4: Which MODE do you use MOST day to day?**

Options:
- Ask
- Edit
- Agent (no IDE)
- Coding Agent (autônomo no GitHub)
- Plan / Vision
- Só completion inline
- Não sei a diferença

### Question `S2-Q5` — _Choice (multiple answers)_

> **S2-Q5: Which Copilot features do you use?**

Options:
- Inline code completion
- Chat (questions no IDE)
- Pull Request descriptions automáticas
- Pull Request review (Copilot review)
- Test generation
- Documentation generation
- Issue resolution (Coding Agent assigna issue)
- Slash commands no Chat (/explain, /fix, /tests)
- Copilot Spaces (contexto compartilhado: repos + docs + custom instructions)
- Copilot Coding Agent (tarefas autônomas)
- Copilot CLI (gh copilot)

### Question `S2-Q6` — _Choice (multiple answers)_

> **S2-Q6: Where do you use Copilot?**

Options:
- VS Code
- Visual Studio
- JetBrains (IntelliJ, PyCharm, etc.)
- Neovim
- Xcode
- GitHub.com (web)
- GitHub Mobile
- GitHub Codespaces
- CLI (gh copilot)

### Question `S2-Q7` — _Choice (single answer)_

> **S2-Q7: Perceived productivity gain with Copilot?**

Options:
- Negativo (atrapalha)
- Neutro (sem ganho)
- +10-20%
- +20-40%
- +40-60%
- +60% ou mais
- Não sei medir

### Question `S2-Q8` — _Choice (multiple answers)_

> **S2-Q8: For WHICH TASKS does Copilot help you the most?**

Options:
- Boilerplate / código repetitivo
- Refactoring
- Escrever testes
- Aprender API/lib nova
- Debugging
- Explicar código legado
- Documentação
- SQL / queries complexas
- Regex
- Tradução entre linguagens
- Onboarding em projeto novo

### Question `S2-Q9` — _Long Text (free response)_

> **S2-Q9: In which tasks does Copilot NOT help you, or get in the way?**

---

## S3 — Other Microsoft / GitHub AI tools

_Microsoft Foundry ecosystem and advanced GitHub features._

_7 questions in this section._

### Question `S3-Q1` — _Choice (multiple answers)_

> **S3-Q1: Which other Microsoft / GitHub AI tools do you use today?**

Options:
- Microsoft Foundry (ex-Azure AI Foundry)
- Foundry Agent Service (GA — built on OpenAI Responses API)
- Azure OpenAI Service (direto via API)
- Microsoft 365 Copilot
- GitHub Copilot Spaces
- GitHub Copilot Coding Agent (autônomo)
- GitHub Codespaces
- GitHub Models (playground multi-LLM)
- GitHub Advanced Security (GHAS)
- GitHub Actions com Copilot integration
- Visual Studio com Copilot avançado
- Nenhuma das acima

### Question `S3-Q2` — _Choice (multiple answers)_

> **S3-Q2: WHAT do you use Microsoft Foundry / Azure OpenAI for, if you use it?**

Options:
- PoC / experimentação
- Feature de produto em produção
- Embeddings / RAG
- Foundry Agent Service para agentes autônomos
- Multi-agent orchestration via MCP
- Fine-tuning
- Connectors (Dynamics, SAP, SharePoint, etc.)
- Não uso

### Question `S3-Q3` — _Choice (single answer)_

> **S3-Q3: Do you know GitHub Copilot Coding Agent, the autonomous successor to Workspace that can pick up issues and open PRs?**

Options:
- Uso ativamente em produção
- Já testei mas não uso recorrente
- Conheço mas nunca usei
- Não conheço

### Question `S3-Q4` — _Choice (single answer)_

> **S3-Q4: Do you know Copilot Spaces, the shared-context feature that replaced Knowledge Bases?**

Options:
- Uso e crio Spaces para meu time
- Uso Spaces criados por outros
- Conheço mas não uso
- Não conheço

### Question `S3-Q5` — _Choice (single answer)_

> **S3-Q5: Do you know GitHub Spec Kit (github/spec-kit) for Spec-Driven Development?**

Options:
- Uso
- Conheço mas não uso
- Não conheço

### Question `S3-Q6` — _Choice (single answer)_

> **S3-Q6: Do you know MCP (Model Context Protocol), the standard for agents to consume tools/context?**

Options:
- Uso servidores MCP no meu workflow
- Configurei algum MCP server custom
- Conheço o conceito
- Não conheço

### Question `S3-Q7` — _Choice (single answer)_

> **S3-Q7: Have you used GitHub Models to test different LLMs (gpt-4o, claude, llama, etc.)?**

Options:
- Uso recorrente
- Já testei
- Não conheço

---

## S4 — AI Development Practices

_How you incorporate AI into your workflow: TDD, SDD, AI pair programming, and related practices._

_9 questions in this section._

### Question `S4-Q1` — _Choice (single answer)_

> **S4-Q1: Do you practice TDD with AI, writing tests first with Copilot?**

Options:
- Sempre que possível
- Frequentemente
- Às vezes
- Raramente
- Nunca
- Não sei o que é TDD

### Question `S4-Q2` — _Choice (single answer)_

> **S4-Q2: Do you practice SDD (Spec-Driven Development), writing a spec so AI generates code?**

Options:
- Uso ativamente (com Spec Kit ou similar)
- Já testei em alguns projetos
- Conheço o conceito mas não uso
- Nunca ouvi falar

### Question `S4-Q3` — _Choice (multiple answers)_

> **S4-Q3: At WHICH moments do you consult AI while coding?**

Options:
- Antes de começar (planejar arquitetura)
- Durante (autocomplete + questions)
- Após implementar (review/refactor)
- Quando trava (debugging)
- Para escrever testes
- Para escrever docs
- Para code review do meu próprio PR

### Question `S4-Q4` — _Choice (single answer)_

> **S4-Q4: Do you consider Copilot / an AI agent a pair programmer?**

Options:
- Sim — trato como par
- Às vezes (depende da tarefa)
- Não — só ferramenta de autocompletar
- Não uso de forma estruturada

### Question `S4-Q5` — _Choice (single answer)_

> **S4-Q5: How often do you refactor code with AI help?**

Options:
- Toda semana
- Algumas vezes por mês
- Raramente
- Nunca

### Question `S4-Q6` — _Choice (single answer)_

> **S4-Q6: Who maintains code documentation in your team?**

Options:
- IA gera e o time revisa
- Devs escrevem manualmente, IA ajuda às vezes
- Time mantém manualmente, sem IA
- Documentação está abandonada

### Question `S4-Q7` — _Choice (single answer)_

> **S4-Q7: When you face a difficult bug, what is your first action?**

Options:
- Pergunto ao Copilot Chat / Claude / outro AI
- Procuro nos logs / debugger
- Pergunto a colega humano
- Stack Overflow / documentação
- Depende do bug

### Question `S4-Q8` — _Choice (single answer)_

> **S4-Q8: When onboarding into a new project, do you use AI (with Copilot Spaces or similar) to understand the codebase?**

Options:
- Sempre — primeira coisa que faço
- Frequentemente
- Às vezes
- Não — leio README e código manualmente

### Question `S4-Q9` — _Long Text (free response)_

> **S4-Q9: Describe one concrete AI practice that changed your productivity in the last 6 months:**

---

## S5 — Agent Concepts and Structure

_Checks knowledge and use of structured AI agents, including Microsoft Agentic DevOps personas and agent testing/governance practices._

_11 questions in this section._

### Question `S5-Q1` — _Choice (single answer)_

> **S5-Q1: Do you know what an AI agent is, autonomous versus a reactive assistant?**

Options:
- Sim — explico claramente
- Sim — vagamente
- Não sei a diferença
- Não conheço o termo

### Question `S5-Q2` — _Choice (single answer)_

> **S5-Q2: Do you know the difference between Ask, Edit, Agent, and Coding Agent Copilot modes?**

Options:
- Sim — uso conscientemente
- Mais ou menos
- Não sei a diferença

### Question `S5-Q3` — _Choice (single answer)_

> **S5-Q3: Have you created or used a custom agent (.github/agents/*.agent.md or Claude/Cursor equivalent)?**

Options:
- Já criei
- Já usei mas não criei
- Sei que existem mas nunca usei
- Não sabia que era possível

### Question `S5-Q4` — _Choice (single answer)_

> **S5-Q4: Do you know the concept of a skill (SKILL.md or equivalent reusable instruction block)?**

Options:
- Conheço e uso
- Conheço mas não uso
- Não conheço

### Question `S5-Q5` — _Choice (single answer)_

> **S5-Q5: Have you created prompt files (.prompt.md in .github/prompts/)?**

Options:
- Sim — várias
- Sim — uma ou duas
- Não, mas planejo
- Não conheço

### Question `S5-Q6` — _Choice (single answer)_

> **S5-Q6: Do you know A2A (Agent-to-Agent protocol), agents communicating with each other?**

Options:
- Uso (ex.: Foundry A2A Tool)
- Conheço o conceito
- Não conheço

### Question `S5-Q7` — _Choice (single answer)_

> **S5-Q7: Do you know handoffs between agents, where agent A passes context to agent B?**

Options:
- Uso
- Conheço o conceito
- Não conheço

### Question `S5-Q8` — _Choice (single answer)_

> **S5-Q8: Do you know subagents, where a main agent delegates tasks to specialized subagents?**

Options:
- Uso
- Conheço o conceito
- Não conheço

### Question `S5-Q9` — _Choice (single answer)_

> **S5-Q9: Do you know Microsoft Agentic DevOps personas: System Designer and Agent Operator?**

Options:
- Sim — adoto explicitamente
- Conheço o conceito
- Não conheço

### Question `S5-Q10` — _Choice (single answer)_

> **S5-Q10: Do you TEST your custom agents/prompts/skills before using them on real code?**

Options:
- Sempre — tenho test suite para meus agents
- Frequentemente — manual mas sistemático
- Às vezes — só sanity check
- Raramente / nunca
- Não crio agents/prompts/skills

### Question `S5-Q11` — _Choice (multiple answers)_

> **S5-Q11: Which primitives have you ALREADY CREATED for personal/team use?**

Options:
- Custom prompts (.prompt.md)
- Custom skills (SKILL.md)
- Custom agents (.agent.md)
- Custom MCP server
- Instructions files (copilot-instructions.md / AGENTS.md / CLAUDE.md)
- Spaces compartilhados
- Nenhum dos acima

---

## S6 — Markdown / Memory / Instructions

_About configuration files that teach the agent about your project._

_6 questions in this section._

### Question `S6-Q1` — _Choice (multiple answers)_

> **S6-Q1: Which instruction files do you use today?**

Options:
- .github/copilot-instructions.md
- .github/instructions/*.instructions.md
- AGENTS.md
- CLAUDE.md (raiz do projeto)
- .cursorrules
- Custom instructions em Copilot Spaces
- Nenhum

### Question `S6-Q2` — _Choice (single answer)_

> **S6-Q2: Who maintains the instruction file(s) in your project?**

Options:
- Time inteiro contribui
- 1-2 pessoas dedicadas
- Eu mantenho sozinho
- Ninguém mantém — está desatualizado
- Não temos

### Question `S6-Q3` — _Choice (single answer)_

> **S6-Q3: How often are these files updated?**

Options:
- Toda semana
- Mensalmente
- Trimestralmente
- Quando algo quebra
- Nunca atualizo

### Question `S6-Q4` — _Choice (multiple answers)_

> **S6-Q4: WHAT do you include in instruction files?**

Options:
- Code style / convenções do projeto
- Domain knowledge (regras de negócio)
- Stack / ferramentas
- Forbidden patterns (o que NÃO fazer)
- Examples (good vs bad code)
- Estrutura de pastas / arquitetura
- Comandos comuns (test, build, deploy)
- Não tenho instruções

### Question `S6-Q5` — _Choice (single answer)_

> **S6-Q5: Do you have a shared prompt library with your team (repo or dedicated Copilot Space)?**

Options:
- Sim — Copilot Space compartilhado
- Sim — repo dedicado
- Sim — wiki/Confluence
- Cada um mantém o seu
- Não compartilhamos prompts

### Question `S6-Q6` — _Choice (single answer)_

> **S6-Q6: Do you use persistent agent memory (Foundry Memory, Claude memory, Copilot memory)?**

Options:
- Uso ativamente
- Já testei
- Não conheço

---

## S7 — Usability and Best Practices

_How you and your team learn and improve AI usage._

_9 questions in this section._

### Question `S7-Q1` — _Choice (multiple answers)_

> **S7-Q1: How did you LEARN to use Copilot/AI for development?**

Options:
- Auto-aprendizado (tentativa e erro)
- Workshop interno da empresa
- Documentação oficial
- Vídeos do YouTube
- Curso online (Coursera, Udemy, MS Learn)
- Champion no time
- Eventos / conferências (Microsoft Build, GitHub Universe)
- Comunidades / Discord / Slack

### Question `S7-Q2` — _Choice (single answer)_

> **S7-Q2: Is there an AI/Copilot Champion in your team/company who helps others?**

Options:
- Sim — eu sou
- Sim — outra pessoa
- Não, mas precisava ter
- Não — cada um se vira

### Question `S7-Q3` — _Choice (single answer)_

> **S7-Q3: Is there an internal channel/community to discuss AI usage in engineering?**

Options:
- Sim — ativo (>5 mensagens/semana)
- Sim — pouco ativo
- Não temos canal dedicado
- Não sei

### Question `S7-Q4` — _Choice (multiple answers)_

> **S7-Q4: Does your organization MEASURE developer productivity in a structured way?**

Options:
- DORA metrics (lead time, deployment freq, MTTR, change failure)
- DX index (developer experience)
- SPACE framework
- Métricas de adoção do Copilot (active users)
- Self-report periódico (survey)
- Não medimos formalmente

### Question `S7-Q5` — _Choice (single answer)_

> **S7-Q5: How many prompt iterations do you typically need before you get a good result?**

Options:
- Acerta na 1ª tentativa
- 2-3 iterações
- 4-6 iterações
- 7+ iterações (frequente)

### Question `S7-Q6` — _Choice (single answer)_

> **S7-Q6: Do you trust AI-generated code enough to merge it WITHOUT reviewing line by line?**

Options:
- Nunca — sempre reviso
- Para mudanças triviais (sim)
- Frequentemente (confio)
- Quase sempre

### Question `S7-Q7` — _Choice (single answer)_

> **S7-Q7: How often do you detect hallucinations, where AI invents nonexistent APIs/methods?**

Options:
- Diariamente
- Semanalmente
- Raramente
- Quase nunca

### Question `S7-Q8` — _Choice (single answer)_

> **S7-Q8: Since adopting AI, do you feel you are learning more or less about engineering?**

Options:
- Aprendendo MUITO MAIS (IA acelera)
- Um pouco mais
- Mais ou menos igual
- Aprendendo MENOS (dependência)
- Não sei avaliar

### Question `S7-Q9` — _Choice (single answer)_

> **S7-Q9: Do you share good prompts/usage examples with colleagues in Spaces, Slack, or Confluence?**

Options:
- Frequentemente — em canal compartilhado
- Às vezes — pessoalmente
- Raramente
- Nunca

---

## S8 — Security and Governance

_Security practices for AI usage plus agent governance (scope, red-lines, JIT permissions, audit)._

_13 questions in this section._

### Question `S8-Q1` — _Choice (single answer)_

> **S8-Q1: Does your organization have a DOCUMENTED AI usage policy for engineering?**

Options:
- Sim — política formal e clara
- Sim — mas pouco clara
- Política informal (sem documento)
- Não temos política
- Não sei

### Question `S8-Q2` — _Choice (single answer)_

> **S8-Q2: Do you know WHICH DATA can go to external LLMs (Copilot, ChatGPT)?**

Options:
- Sei claramente o que pode e o que NÃO pode
- Tenho ideia geral
- Vagamente
- Não sei

### Question `S8-Q3` — _Choice (multiple answers)_

> **S8-Q3: Which data types would you NEVER put into external AI prompts?**

Options:
- PII / dados pessoais de clientes
- Secrets / API keys / tokens
- Código de IP estratégico
- Dados financeiros
- Dados de saúde
- Nenhuma restrição (não temos política)

### Question `S8-Q4` — _Choice (multiple answers)_

> **S8-Q4: Which SECURITY tools are active in your repository?**

Options:
- GitHub Advanced Security (GHAS)
- CodeQL scanning
- Secret scanning
- Dependabot / dependency review
- SBOM (Software Bill of Materials)
- Microsoft Defender for DevOps
- Microsoft Defender for Cloud
- Snyk / SonarQube / outro SAST
- Nenhuma

### Question `S8-Q5` — _Choice (single answer)_

> **S8-Q5: Does Code Scanning run on AI-GENERATED code in the PR or IDE?**

Options:
- Sim — gate obrigatório no PR
- Sim — opcional
- Roda mas não bloqueia
- Não roda

### Question `S8-Q6` — _Choice (single answer)_

> **S8-Q6: Does your organization generate SBOMs for critical services?**

Options:
- Sim — automatizado
- Sim — manual quando solicitado
- Não geramos
- Não sei

### Question `S8-Q7` — _Choice (single answer)_

> **S8-Q7: Is there a formal REVIEW process for AI-generated code before merge?**

Options:
- Sim — review obrigatório por outro humano + scanner
- Review humano obrigatório (sem scanner extra)
- Review opcional
- Não temos processo

### Question `S8-Q8` — _Choice (single answer)_

> **S8-Q8: When creating/using a custom agent, do you define explicit SCOPE and RED-LINES?**

Options:
- Sempre — escopo + red-lines documentados
- Frequentemente
- Às vezes
- Raramente / nunca
- Não crio/uso custom agents

### Question `S8-Q9` — _Choice (single answer)_

> **S8-Q9: Does your organization use JIT (Just-In-Time) permissions for agents instead of persistent permissions?**

Options:
- Sim — JIT obrigatório para agents
- Sim — opcional
- Não temos JIT
- Não sei

### Question `S8-Q10` — _Choice (single answer)_

> **S8-Q10: Does your organization have DLP configured to prevent sensitive data in prompts?**

Options:
- Sim — bloqueia ativamente
- Sim — alerta mas não bloqueia
- Não temos
- Não sei

### Question `S8-Q11` — _Choice (single answer)_

> **S8-Q11: Does your organization have AUDIT LOGS for Copilot/AI agents, including autonomous agent decisions?**

Options:
- Sim — logs ativos e revisados
- Logs ativos mas não revisados
- Não temos
- Não sei

### Question `S8-Q12` — _Choice (single answer)_

> **S8-Q12: Have you received formal security training for AI usage?**

Options:
- Sim — treinamento obrigatório anual
- Sim — uma vez (no onboarding)
- Não recebi treinamento
- Não sei

### Question `S8-Q13` — _Choice (single answer)_

> **S8-Q13: How often have you seen Copilot/AI suggest code with an obvious vulnerability?**

Options:
- Diariamente
- Semanalmente
- Mensalmente
- Quase nunca

---

## S9 — Pain Points & Wishlist

_Your ideas and frustrations. Free text — feel free to be candid._

_4 questions in this section._

### Question `S9-Q1` — _Long Text (free response)_

> **S9-Q1: What frustrates you MOST today about using AI in your day-to-day engineering work?**

### Question `S9-Q2` — _Long Text (free response)_

> **S9-Q2: What CHANGE in tooling/process would double your productivity?**

### Question `S9-Q3` — _Long Text (free response)_

> **S9-Q3: Which Microsoft/GitHub feature/tool would you like to exist, or know better?**

### Question `S9-Q4` — _Choice (single answer)_

> **S9-Q4: Would you like to receive the consolidated version of this survey (team-wide aggregated insights)?**

Options:
- Sim — quero ver
- Não, obrigado

---

## Resumo final

- **9 seções** (1 por tema)
- **75 questions** (55 choice + 15 multi + 5 long text)
- **Tempo estimado:** 20-25 min (rascunho rápido em 10 min)
- **Respostas esperadas:** quanto mais devs, melhor — mínimo 5, ideal 15+

## Próximos passos

1. Após coletar respostas, **Responses → Open in Excel** no Microsoft Forms
2. Renomeie o Excel para `respostas-survey-devs.xlsx`
3. Mova para a raiz do `kit-cliente/`
4. No Copilot Chat (modo Agent): `/importar-survey-devs`
5. Depois: `/insights-developer-survey` para gerar relatório consolidado
