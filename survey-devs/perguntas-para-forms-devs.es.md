# Preguntas para Microsoft Forms — Developer Survey (GitHub + IA)

> 75 preguntas en 9 secciones. Tiempo estimado: **20-25 min**. ANÓNIMO — no pedimos nombre ni email del respondente.




   ```text
   Survey anónimo (15-25 min) sobre tus prácticas con GitHub Copilot,
   modos de Copilot Chat (Ask/Edit/Agent), agentes IA, instruction files,
   mejores prácticas de IA + Dev y seguridad.
   Tus respuestas alimentarán el roadmap de adopción de IA del equipo.
   ```

4. **Settings** (⚙️):
   - ☑ **Anonymous responses** (CRÍTICO — dejar marcado)
   - ☑ One response per person: **DESMARCADO** (queremos múltiples respuestas)
   - ☑ Accept responses
5. Agrega **9 secciones** (`+ Add new` -> icono de sección):
   - **S1 — Perfil del respondente** (7 preguntas)
   - **S2 — GitHub Copilot — Adopción y Modos** (9 preguntas)
   - **S3 — Otras herramientas Microsoft / GitHub AI** (7 preguntas)
   - **S4 — Prácticas de Desarrollo con IA** (9 preguntas)
   - **S5 — Conceptos y Estructura de Agentes** (11 preguntas)
   - **S6 — Markdown / Memory / Instructions** (6 preguntas)
   - **S7 — Usabilidad y Best Practices** (9 preguntas)
   - **S8 — Seguridad y Gobernanza** (13 preguntas)
   - **S9 — Pain Points & Wishlist** (4 preguntas)

6. Para cada pregunta abajo, agrega en Forms el tipo correspondiente:
   - **`choice`** → Choice (Single answer)
   - **`multi`** → Choice (Multiple answers / checkboxes)
   - **`text`** → Long Text

7. **TÍTULO** de cada pregunta debe comenzar con el ID + dos puntos. Ejemplo:

   ```text
   S2-Q1: Tienes una licencia activa de GitHub Copilot?
   ```

   > ⚠️ El ID es usado por `/importar-survey-devs` para mapear de vuelta. NO LO REMUEVAS.

8. Comparte vía **+ Send / Collect responses** -> copiar link -> enviar por Slack/Teams/email

9. Cuando tengas respuestas, **Responses -> Open in Excel** -> renombra a `respostas-survey-devs.xlsx` -> mueve a la raíz del kit

---

## S1 — Perfil del respondente

_Preguntas básicas sobre ti y tu contexto. Anónimo — no pediremos nombre ni email._

_7 preguntas en esta sección._

### Pregunta `S1-Q1` — _Choice (single answer)_

> **S1-Q1: Cuál es tu cargo actual?**

Opciones:

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
- Otro

### Pregunta `S1-Q2` — _Choice (single answer)_

> **S1-Q2: Tiempo total como desarrollador?**

Opciones:

- < 2 años
- 2-5 años
- 6-10 años
- 11-15 años
- > 15 años

### Pregunta `S1-Q3` — _Choice (single answer)_

> **S1-Q3: Hace cuánto usas IA en desarrollo (Copilot, Cursor, Claude Code, etc.)?**

Opciones:

- Nunca usé
- < 3 meses
- 3-12 meses
- 1-2 años
- > 2 años

### Pregunta `S1-Q4` — _Choice (multiple answers)_

> **S1-Q4: Lenguajes principales que usas en el día a día?**

Opciones:

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
- SQL (foco principal)
- Otra

### Pregunta `S1-Q5` — _Choice (single answer)_

> **S1-Q5: Cuántas horas al día pasas codificando en promedio?**

Opciones:

- < 2h
- 2-4h
- 4-6h
- 6-8h
- > 8h

### Pregunta `S1-Q6` — _Choice (single answer)_

> **S1-Q6: Cuál es el tamaño de tu squad/equipo inmediato?**

Opciones:

- Sou solo
- 2-4 pessoas
- 5-9 pessoas
- 10-15 pessoas
- > 15 pessoas

### Pregunta `S1-Q7` — _Choice (single answer)_

> **S1-Q7: Modelo de trabajo?**

Opciones:

- Remoto 100%
- Híbrido (1-2 dias presencial)
- Híbrido (3-4 dias)
- Presencial 100%

---

## S2 — GitHub Copilot — Adopción y Modos

_Foco en GitHub Copilot. Incluye los modos actuales (Ask, Edit, Agent), Coding Agent autónomo y Spaces para contexto compartido._

_9 preguntas en esta sección._

### Pregunta `S2-Q1` — _Choice (single answer)_

> **S2-Q1: Tienes una licencia activa de GitHub Copilot?**

Opciones:

- Sim — Copilot Enterprise
- Sim — Copilot Business
- Sim — Copilot Pro+ (individual)
- Sim — Copilot Pro (individual)
- Sim — Copilot Free
- Tenho licença mas não uso
- Não tenho licença

### Pregunta `S2-Q2` — _Choice (single answer)_

> **S2-Q2: Frecuencia de uso de Copilot?**

Opciones:

- Diariamente (várias horas)
- Diariamente (esporádico)
- Semanal
- Raramente
- Nunca

### Pregunta `S2-Q3` — _Choice (multiple answers)_

> **S2-Q3: Qué MODOS de Copilot Chat usas? (selecciona todos los que apliquen)**

Opciones:

- Ask (responder preguntas)
- Edit (edição multi-arquivo no IDE)
- Agent (autônomo no IDE, executa tasks)
- Copilot Coding Agent (autônomo no GitHub.com — assigna issue, abre PR sozinho)
- Plan / Vision
- Não uso o Chat — só completion inline
- Não conheço esses modos

### Pregunta `S2-Q4` — _Choice (single answer)_

> **S2-Q4: Qué MODO usas MÁS en el día a día?**

Opciones:

- Ask
- Edit
- Agent (no IDE)
- Coding Agent (autônomo no GitHub)
- Plan / Vision
- Só completion inline
- Não sei a diferença

### Pregunta `S2-Q5` — _Choice (multiple answers)_

> **S2-Q5: Qué features de Copilot usas?**

Opciones:

- Inline code completion
- Chat (preguntas no IDE)
- Pull Request descriptions automáticas
- Pull Request review (Copilot review)
- Test generation
- Documentation generation
- Issue resolution (Coding Agent assigna issue)
- Slash commands no Chat (/explain, /fix, /tests)
- Copilot Spaces (contexto compartilhado: repos + docs + custom instructions)
- Copilot Coding Agent (tarefas autônomas)
- Copilot CLI (gh copilot)

### Pregunta `S2-Q6` — _Choice (multiple answers)_

> **S2-Q6: Dónde usas Copilot?**

Opciones:

- VS Code
- Visual Studio
- JetBrains (IntelliJ, PyCharm, etc.)
- Neovim
- Xcode
- GitHub.com (web)
- GitHub Mobile
- GitHub Codespaces
- CLI (gh copilot)

### Pregunta `S2-Q7` — _Choice (single answer)_

> **S2-Q7: Ganancia de productividad percibida con Copilot?**

Opciones:

- Negativo (atrapalha)
- Neutro (sem ganho)
- +10-20%
- +20-40%
- +40-60%
- +60% ou mais
- Não sei medir

### Pregunta `S2-Q8` — _Choice (multiple answers)_

> **S2-Q8: Para QUÉ TAREAS te ayuda más Copilot?**

Opciones:

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

### Pregunta `S2-Q9` — _Long Text (respuesta libre)_

> **S2-Q9: En qué tareas Copilot NO te ayuda, o te estorba?**

---

## S3 — Otras herramientas Microsoft / GitHub AI

_Ecosistema Microsoft Foundry y features avanzadas de GitHub._

_7 preguntas en esta sección._

### Pregunta `S3-Q1` — _Choice (multiple answers)_

> **S3-Q1: Qué otras herramientas Microsoft / GitHub AI usas hoy?**

Opciones:

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

### Pregunta `S3-Q2` — _Choice (multiple answers)_

> **S3-Q2: Para QUÉ usas Microsoft Foundry / Azure OpenAI, si lo usas?**

Opciones:

- PoC / experimentação
- Feature de produto em produção
- Embeddings / RAG
- Foundry Agent Service para agentes autônomos
- Multi-agent orchestration via MCP
- Fine-tuning
- Connectors (Dynamics, SAP, SharePoint, etc.)
- Não uso

### Pregunta `S3-Q3` — _Choice (single answer)_

> **S3-Q3: Conoces GitHub Copilot Coding Agent, el sucesor autónomo de Workspace que toma issues y abre PRs?**

Opciones:

- Uso ativamente em produção
- Já testei mas não uso recorrente
- Conheço mas nunca usei
- Não conheço

### Pregunta `S3-Q4` — _Choice (single answer)_

> **S3-Q4: Conoces Copilot Spaces, la funcionalidad de contexto compartido que reemplazó Knowledge Bases?**

Opciones:

- Uso e crio Spaces para meu time
- Uso Spaces criados por outros
- Conheço mas não uso
- Não conheço

### Pregunta `S3-Q5` — _Choice (single answer)_

> **S3-Q5: Conoces GitHub Spec Kit (github/spec-kit) para Spec-Driven Development?**

Opciones:

- Uso
- Conheço mas não uso
- Não conheço

### Pregunta `S3-Q6` — _Choice (single answer)_

> **S3-Q6: Conoces MCP (Model Context Protocol), el estándar para que agentes consuman tools/contexto?**

Opciones:

- Uso servidores MCP no meu workflow
- Configurei algum MCP server custom
- Conheço o conceito
- Não conheço

### Pregunta `S3-Q7` — _Choice (single answer)_

> **S3-Q7: Has usado GitHub Models para probar diferentes LLMs (gpt-4o, claude, llama, etc.)?**

Opciones:

- Uso recorrente
- Já testei
- Não conheço

---

## S4 — Prácticas de Desarrollo con IA

_Cómo incorporas IA en tu flujo: TDD, SDD, pair programming con IA y prácticas relacionadas._

_9 preguntas en esta sección._

### Pregunta `S4-Q1` — _Choice (single answer)_

> **S4-Q1: Practicas TDD con IA, escribiendo tests primero con Copilot?**

Opciones:

- Sempre que possível
- Frequentemente
- Às vezes
- Raramente
- Nunca
- Não sei o que é TDD

### Pregunta `S4-Q2` — _Choice (single answer)_

> **S4-Q2: Practicas SDD (Spec-Driven Development), escribiendo una spec para que IA genere código?**

Opciones:

- Uso ativamente (com Spec Kit ou similar)
- Já testei em alguns projetos
- Conheço o conceito mas não uso
- Nunca ouvi falar

### Pregunta `S4-Q3` — _Choice (multiple answers)_

> **S4-Q3: En QUÉ momentos consultas IA durante el coding?**

Opciones:

- Antes de começar (planejar arquitetura)
- Durante (autocomplete + preguntas)
- Após implementar (review/refactor)
- Quando trava (debugging)
- Para escrever testes
- Para escrever docs
- Para code review do meu próprio PR

### Pregunta `S4-Q4` — _Choice (single answer)_

> **S4-Q4: Consideras Copilot / un agente IA como pair programmer?**

Opciones:

- Sim — trato como par
- Às vezes (depende da tarefa)
- Não — só ferramenta de autocompletar
- Não uso de forma estruturada

### Pregunta `S4-Q5` — _Choice (single answer)_

> **S4-Q5: Con qué frecuencia refactorizas código con ayuda de IA?**

Opciones:

- Toda semana
- Algumas vezes por mês
- Raramente
- Nunca

### Pregunta `S4-Q6` — _Choice (single answer)_

> **S4-Q6: Quién mantiene la documentación del código en tu equipo?**

Opciones:

- IA gera e o time revisa
- Devs escrevem manualmente, IA ajuda às vezes
- Time mantém manualmente, sem IA
- Documentação está abandonada

### Pregunta `S4-Q7` — _Choice (single answer)_

> **S4-Q7: Cuando tienes un bug difícil, cuál es tu primera acción?**

Opciones:

- Pergunto ao Copilot Chat / Claude / outro AI
- Procuro nos logs / debugger
- Pergunto a colega humano
- Stack Overflow / documentação
- Depende do bug

### Pregunta `S4-Q8` — _Choice (single answer)_

> **S4-Q8: Al hacer onboarding en un proyecto nuevo, usas IA (con Copilot Spaces o similar) para entender la base de código?**

Opciones:

- Sempre — primeira coisa que faço
- Frequentemente
- Às vezes
- Não — leio README e código manualmente

### Pregunta `S4-Q9` — _Long Text (respuesta libre)_

> **S4-Q9: Describe una práctica concreta con IA que cambió tu productividad en los últimos 6 meses:**

---

## S5 — Conceptos y Estructura de Agentes

_Verifica conocimiento y uso de agentes de IA estructurados, incluyendo personas Agentic DevOps de Microsoft y prácticas de prueba/gobernanza de agentes._

_11 preguntas en esta sección._

### Pregunta `S5-Q1` — _Choice (single answer)_

> **S5-Q1: Sabes qué es un AI agent, autónomo versus asistente reactivo?**

Opciones:

- Sim — explico claramente
- Sim — vagamente
- Não sei a diferença
- Não conheço o termo

### Pregunta `S5-Q2` — _Choice (single answer)_

> **S5-Q2: Sabes la diferencia entre Ask, Edit, Agent y Coding Agent (modos de Copilot)?**

Opciones:

- Sim — uso conscientemente
- Mais ou menos
- Não sei a diferença

### Pregunta `S5-Q3` — _Choice (single answer)_

> **S5-Q3: Ya creaste o usaste un custom agent (.github/agents/*.agent.md o equivalente Claude/Cursor)?**

Opciones:

- Já criei
- Já usei mas não criei
- Sei que existem mas nunca usei
- Não sabia que era possível

### Pregunta `S5-Q4` — _Choice (single answer)_

> **S5-Q4: Conoces el concepto de skill (SKILL.md o equivalente, bloque reutilizable de instrucciones)?**

Opciones:

- Conheço e uso
- Conheço mas não uso
- Não conheço

### Pregunta `S5-Q5` — _Choice (single answer)_

> **S5-Q5: Ya creaste prompt files (.prompt.md en .github/prompts/)?**

Opciones:

- Sim — várias
- Sim — uma ou duas
- Não, mas planejo
- Não conheço

### Pregunta `S5-Q6` — _Choice (single answer)_

> **S5-Q6: Conoces A2A (Agent-to-Agent protocol), agentes comunicándose entre sí?**

Opciones:

- Uso (ex.: Foundry A2A Tool)
- Conheço o conceito
- Não conheço

### Pregunta `S5-Q7` — _Choice (single answer)_

> **S5-Q7: Conoces handoffs entre agentes, cuando el agente A pasa contexto al agente B?**

Opciones:

- Uso
- Conheço o conceito
- Não conheço

### Pregunta `S5-Q8` — _Choice (single answer)_

> **S5-Q8: Conoces subagentes, cuando un agente principal delega tareas a subagentes especializados?**

Opciones:

- Uso
- Conheço o conceito
- Não conheço

### Pregunta `S5-Q9` — _Choice (single answer)_

> **S5-Q9: Conoces las personas Microsoft Agentic DevOps: System Designer y Agent Operator?**

Opciones:

- Sim — adoto explicitamente
- Conheço o conceito
- Não conheço

### Pregunta `S5-Q10` — _Choice (single answer)_

> **S5-Q10: TESTEAS tus custom agents/prompts/skills antes de usarlos en código real?**

Opciones:

- Sempre — tenho test suite para meus agents
- Frequentemente — manual mas sistemático
- Às vezes — só sanity check
- Raramente / nunca
- Não crio agents/prompts/skills

### Pregunta `S5-Q11` — _Choice (multiple answers)_

> **S5-Q11: Qué primitivos YA CREASTE para uso personal/equipo?**

Opciones:

- Custom prompts (.prompt.md)
- Custom skills (SKILL.md)
- Custom agents (.agent.md)
- Custom MCP server
- Instructions files (copilot-instructions.md / AGENTS.md / CLAUDE.md)
- Spaces compartilhados
- Nenhum dos acima

---

## S6 — Markdown / Memory / Instructions

_Sobre archivos de configuración que enseñan al agente sobre tu proyecto._

_6 preguntas en esta sección._

### Pregunta `S6-Q1` — _Choice (multiple answers)_

> **S6-Q1: Qué archivos de instrucciones usas hoy?**

Opciones:

- .github/copilot-instructions.md
- .github/instructions/*.instructions.md
- AGENTS.md
- CLAUDE.md (raiz do projeto)
- .cursorrules
- Custom instructions em Copilot Spaces
- Nenhum

### Pregunta `S6-Q2` — _Choice (single answer)_

> **S6-Q2: Quién mantiene los archivos de instrucciones en tu proyecto?**

Opciones:

- Time inteiro contribui
- 1-2 pessoas dedicadas
- Eu mantenho sozinho
- Ninguém mantém — está desatualizado
- Não temos

### Pregunta `S6-Q3` — _Choice (single answer)_

> **S6-Q3: Frecuencia de actualización de esos archivos?**

Opciones:

- Toda semana
- Mensalmente
- Trimestralmente
- Quando algo quebra
- Nunca atualizo

### Pregunta `S6-Q4` — _Choice (multiple answers)_

> **S6-Q4: QUÉ incluyes en los archivos de instrucciones?**

Opciones:

- Code style / convenções do projeto
- Domain knowledge (regras de negócio)
- Stack / ferramentas
- Forbidden patterns (o que NÃO fazer)
- Examples (good vs bad code)
- Estrutura de pastas / arquitetura
- Comandos comuns (test, build, deploy)
- Não tenho instruções

### Pregunta `S6-Q5` — _Choice (single answer)_

> **S6-Q5: Tienes una prompt library compartida con tu equipo (repo o Copilot Space dedicado)?**

Opciones:

- Sim — Copilot Space compartilhado
- Sim — repo dedicado
- Sim — wiki/Confluence
- Cada um mantém o seu
- Não compartilhamos prompts

### Pregunta `S6-Q6` — _Choice (single answer)_

> **S6-Q6: Usas memoria persistente del agente (Foundry Memory, Claude memory, Copilot memory)?**

Opciones:

- Uso ativamente
- Já testei
- Não conheço

---

## S7 — Usabilidad y Best Practices

_Cómo tú y tu equipo aprenden y mejoran el uso de IA._

_9 preguntas en esta sección._

### Pregunta `S7-Q1` — _Choice (multiple answers)_

> **S7-Q1: Cómo APRENDISTE a usar Copilot/IA en desarrollo?**

Opciones:

- Auto-aprendizado (tentativa e erro)
- Workshop interno da empresa
- Documentação oficial
- Vídeos do YouTube
- Curso online (Coursera, Udemy, MS Learn)
- Champion no time
- Eventos / conferências (Microsoft Build, GitHub Universe)
- Comunidades / Discord / Slack

### Pregunta `S7-Q2` — _Choice (single answer)_

> **S7-Q2: Existe un AI/Copilot Champion en tu equipo/empresa que ayuda a otros?**

Opciones:

- Sim — eu sou
- Sim — outra pessoa
- Não, mas precisava ter
- Não — cada um se vira

### Pregunta `S7-Q3` — _Choice (single answer)_

> **S7-Q3: Hay un canal/comunidad interna para discutir uso de IA en ingeniería?**

Opciones:

- Sim — ativo (>5 mensagens/semana)
- Sim — pouco ativo
- Não temos canal dedicado
- Não sei

### Pregunta `S7-Q4` — _Choice (multiple answers)_

> **S7-Q4: Tu organización MIDE productividad del dev de forma estructurada?**

Opciones:

- DORA metrics (lead time, deployment freq, MTTR, change failure)
- DX index (developer experience)
- SPACE framework
- Métricas de adoção do Copilot (active users)
- Self-report periódico (survey)
- Não medimos formalmente

### Pregunta `S7-Q5` — _Choice (single answer)_

> **S7-Q5: Cuántas iteraciones típicas de prompt necesitas antes de tener un buen resultado?**

Opciones:

- Acerta na 1ª tentativa
- 2-3 iterações
- 4-6 iterações
- 7+ iterações (frequente)

### Pregunta `S7-Q6` — _Choice (single answer)_

> **S7-Q6: Confías en el código generado por IA lo suficiente para mergearlo SIN revisar línea por línea?**

Opciones:

- Nunca — sempre reviso
- Para mudanças triviais (sim)
- Frequentemente (confio)
- Quase sempre

### Pregunta `S7-Q7` — _Choice (single answer)_

> **S7-Q7: Con qué frecuencia detectas hallucinations, cuando la IA inventa APIs/métodos inexistentes?**

Opciones:

- Diariamente
- Semanalmente
- Raramente
- Quase nunca

### Pregunta `S7-Q8` — _Choice (single answer)_

> **S7-Q8: Desde que adoptaste IA, sientes que aprendes más o menos sobre ingeniería?**

Opciones:

- Aprendendo MUITO MAIS (IA acelera)
- Um pouco mais
- Mais ou menos igual
- Aprendendo MENOS (dependência)
- Não sei avaliar

### Pregunta `S7-Q9` — _Choice (single answer)_

> **S7-Q9: Compartes buenos prompts/ejemplos de uso con colegas en Spaces, Slack o Confluence?**

Opciones:

- Frequentemente — em canal compartilhado
- Às vezes — pessoalmente
- Raramente
- Nunca

---

## S8 — Seguridad y Gobernanza

_Prácticas de seguridad en el uso de IA y gobernanza de agentes (alcance, red-lines, permisos JIT, auditoría)._

_13 preguntas en esta sección._

### Pregunta `S8-Q1` — _Choice (single answer)_

> **S8-Q1: Tu organización tiene una POLÍTICA DOCUMENTADA de uso de IA en ingeniería?**

Opciones:

- Sim — política formal e clara
- Sim — mas pouco clara
- Política informal (sem documento)
- Não temos política
- Não sei

### Pregunta `S8-Q2` — _Choice (single answer)_

> **S8-Q2: Sabes QUÉ DATOS pueden ir a LLMs externas (Copilot, ChatGPT)?**

Opciones:

- Sei claramente o que pode e o que NÃO pode
- Tenho ideia geral
- Vagamente
- Não sei

### Pregunta `S8-Q3` — _Choice (multiple answers)_

> **S8-Q3: Qué tipos de datos JAMÁS colocas en prompts de IA externa?**

Opciones:

- PII / dados pessoais de clientes
- Secrets / API keys / tokens
- Código de IP estratégico
- Dados financeiros
- Dados de saúde
- Nenhuma restrição (não temos política)

### Pregunta `S8-Q4` — _Choice (multiple answers)_

> **S8-Q4: Qué herramientas de SEGURIDAD están activas en tu repo?**

Opciones:

- GitHub Advanced Security (GHAS)
- CodeQL scanning
- Secret scanning
- Dependabot / dependency review
- SBOM (Software Bill of Materials)
- Microsoft Defender for DevOps
- Microsoft Defender for Cloud
- Snyk / SonarQube / outro SAST
- Nenhuma

### Pregunta `S8-Q5` — _Choice (single answer)_

> **S8-Q5: Code Scanning corre sobre código GENERADO por IA en el PR o IDE?**

Opciones:

- Sim — gate obrigatório no PR
- Sim — opcional
- Roda mas não bloqueia
- Não roda

### Pregunta `S8-Q6` — _Choice (single answer)_

> **S8-Q6: Tu organización genera SBOM de servicios críticos?**

Opciones:

- Sim — automatizado
- Sim — manual quando solicitado
- Não geramos
- Não sei

### Pregunta `S8-Q7` — _Choice (single answer)_

> **S8-Q7: Existe un proceso formal de REVIEW para código generado por IA antes del merge?**

Opciones:

- Sim — review obrigatório por outro humano + scanner
- Review humano obrigatório (sem scanner extra)
- Review opcional
- Não temos processo

### Pregunta `S8-Q8` — _Choice (single answer)_

> **S8-Q8: Cuando creas/usas un custom agent, defines ALCANCE y RED-LINES explícitos?**

Opciones:

- Sempre — escopo + red-lines documentados
- Frequentemente
- Às vezes
- Raramente / nunca
- Não crio/uso custom agents

### Pregunta `S8-Q9` — _Choice (single answer)_

> **S8-Q9: Tu organización usa permisos JIT (Just-In-Time) para agentes versus permisos persistentes?**

Opciones:

- Sim — JIT obrigatório para agents
- Sim — opcional
- Não temos JIT
- Não sei

### Pregunta `S8-Q10` — _Choice (single answer)_

> **S8-Q10: Tu organización tiene DLP configurado para evitar datos sensibles en prompts?**

Opciones:

- Sim — bloqueia ativamente
- Sim — alerta mas não bloqueia
- Não temos
- Não sei

### Pregunta `S8-Q11` — _Choice (single answer)_

> **S8-Q11: Tu organización tiene AUDIT LOGS de uso de Copilot/agentes IA, incluyendo decisiones autónomas de agents?**

Opciones:

- Sim — logs ativos e revisados
- Logs ativos mas não revisados
- Não temos
- Não sei

### Pregunta `S8-Q12` — _Choice (single answer)_

> **S8-Q12: Ya recibiste entrenamiento formal de seguridad en el uso de IA?**

Opciones:

- Sim — treinamento obrigatório anual
- Sim — uma vez (no onboarding)
- Não recebi treinamento
- Não sei

### Pregunta `S8-Q13` — _Choice (single answer)_

> **S8-Q13: Con qué frecuencia viste a Copilot/IA sugerir código con vulnerabilidad obvia?**

Opciones:

- Diariamente
- Semanalmente
- Mensalmente
- Quase nunca

---

## S9 — Pain Points & Wishlist

_Tus ideas y frustraciones. Texto libre — responde con libertad._

_4 preguntas en esta sección._

### Pregunta `S9-Q1` — _Long Text (respuesta libre)_

> **S9-Q1: QUÉ MÁS te frustra hoy en el uso de IA en tu día a día de ingeniería?**

### Pregunta `S9-Q2` — _Long Text (respuesta libre)_

> **S9-Q2: Qué CAMBIO en herramienta/proceso duplicaría tu productividad?**

### Pregunta `S9-Q3` — _Long Text (respuesta libre)_

> **S9-Q3: Qué feature/herramienta Microsoft/GitHub te gustaría que existiera o conocer mejor?**

### Pregunta `S9-Q4` — _Choice (single answer)_

> **S9-Q4: Te gustaría recibir la versión consolidada de este survey (insights agregados de todo el equipo)?**

Opciones:

- Sim — quero ver
- Não, obrigado

---

## Resumo final

- **9 seções** (1 por tema)
- **75 preguntas** (55 choice + 15 multi + 5 long text)
- **Tempo estimado:** 20-25 min (rascunho rápido em 10 min)
- **Respostas esperadas:** quanto mais devs, melhor — mínimo 5, ideal 15+

## Próximos passos

1. Após coletar respostas, **Responses → Open in Excel** no Microsoft Forms
2. Renomeie o Excel para `respostas-survey-devs.xlsx`
3. Mova para a raiz do `kit-cliente/`
4. No Copilot Chat (modo Agent): `/importar-survey-devs`
5. Depois: `/insights-developer-survey` para gerar relatório consolidado
