# Auditoria Completa do Kit para GitHub Copilot

**Data:** 2026-07-03 · **Branch:** `claude/copilot-kit-audit-0rs8w9` · **Escopo:** todos os primitivos do GitHub Copilot (instructions, agente, prompt, 12 skills, workflows), scripts Python, formulários HTML, empacotamento trilíngue e higiene do repositório.

**Metodologia:** auditoria multi-agente com 25 agentes: 2 agentes de pesquisa nas documentações oficiais (docs.github.com e code.visualstudio.com, estado de 2026), 11 auditores de dimensão, 11 verificadores adversariais (cada achado foi contestado contra os arquivos reais do repositório) e 1 crítico de completude. De 104 achados brutos, 103 foram confirmados na verificação e 1 foi refutado; o crítico de completude adicionou 8 achados. **Total: 111 achados confirmados** (1 crítico, 20 altos, 43 médios, 47 baixos).

---

## 1. Sumário executivo

O kit é funcional e bem projetado no núcleo: o inventário de skills confere com a realidade, o algoritmo de pontuação é consistente entre documentação e código do pipeline, os catálogos i18n têm paridade perfeita de chaves (363 chaves × 3 idiomas), os templates Jinja2 usam autoescape + StrictUndefined, e os scripts de survey são determinísticos e rodam standalone. `framework.json` está íntegro (3 pilares, 28 capabilities, 158 perguntas).

Porém, medido contra os cinco requisitos do dono, o estado atual é este:

| # | Requisito | Estado | Resumo |
|---|---|---|---|
| 1 | Melhores práticas Copilot em todos os primitivos | 🟡 Parcial | Frontmatter das skills é limpo, mas os 9 handoffs do agente apontam para skills inexistentes como agentes (roteamento quebrado), tools usam nomes legados, e faltam `.instructions.md`, `copilot-setup-steps.yml` e hooks |
| 2 | Eficiência de tokens | 🔴 Falha | ~32.300 tokens de primitivos; `copilot-instructions.md` injeta ~3.500 tokens em TODA requisição (60% removível); duplicação 3-5× de algoritmo, thresholds e branding; potencial de corte de ~49% |
| 3 | Modelo certo por tarefa | 🔴 Ausente | Zero pins ou recomendações de modelo em todo o kit (verificado por grep); agente e prompt suportam `model:` e não usam |
| 4 | Executar certo de primeira | 🔴 Falha | As 4 skills numericamente críticas (scores, gaps, estratégias, import Excel) mandam o LLM escrever Python ad-hoc a partir de pseudocódigo; dados do wizard são silenciosamente descartados no PDF (CRÍTICO); coding agent inicia sem dependências; sem CI em PRs |
| 5 | Trilíngue + primitivos em inglês | 🟡 Parcial | Camada de máquina 100% trilíngue (bancos de perguntas, i18n, site, PDFs de exemplo); mas ~26 docs são só PT (7 deles embarcam nos ZIPs EN/ES), 9 de 12 skills têm nome em português e o corpo dos primitivos mistura PT/EN |

**Os 3 problemas que mais importam:**

1. **[CRÍTICO] Dados do wizard são perdidos silenciosamente no PDF do cliente.** O merge grava chaves `*_raw_markdown` que nenhum template lê; o PDF da Parte 4 renderiza pessoas fictícias do sample ("Maria Santos, CTO", "Carlos Rivera") enquanto o script imprime sucesso.
2. **Armadilha de vazamento de dados de cliente:** `respostas.json` e `implementation-guide-inputs.json` (que carrega nome+email) estão trackeados no git apesar de listados no `.gitignore`; o ignore é inerte para arquivos já trackeados, então um `git commit -a` de um consultor publica PII real.
3. **A matemática que vai para o PDF executivo é recalculada pelo LLM a cada execução.** Não existe script determinístico para scores/gaps/recomendações/importação: risco direto de números divergentes entre execuções.

---

## 2. Achado crítico

### C1. Wizard silenciosamente descartado: PDF do cliente renderiza pessoas fictícias

- **Arquivos:** `relatorios/scripts/build_payload_and_render.py:244`, `relatorios/templates/roadmap_part4.html.j2:21,106,130`
- **Evidência:** o merge grava `current_ig[f"{key}_raw_markdown"] = value` a partir de `implementation-guide-inputs.json`, mas nenhum template referencia `raw_markdown` (grep zero hits). O template lê as chaves sem sufixo, que permanecem com os valores do `sample_payload.json` ("Maria Santos, CTO"; "Carlos Rivera" como program manager). O script ainda imprime "✓ Merged implementation-guide-inputs.json (…% completo)".
- **Correção:** fazer o merge escrever nas chaves que o template lê (ou o template preferir `*_raw_markdown` quando presente); falhar ou avisar alto quando campos mesclados não são consumidos; adicionar asserção no smoke test de que texto do wizard aparece no HTML renderizado da Parte 4. **Esforço: M**

---

## 3. Achados altos (20)

### 3.1 Primitivos Copilot

**A1. Os 9 handoffs do agente apontam para skills, não agentes: todo o roteamento está quebrado.**
`.github/agents/ai-maturity-assistant.agent.md` L7-43. Todos os alvos (`calcular-scores`, `gerar-relatorio` etc.) são diretórios de `.github/skills/`; `.github/agents/` contém só 1 arquivo. Pela spec, handoffs apontam para outros agentes; além disso, handoffs não são suportados no cloud agent. **Correção:** remover o bloco `handoffs` e instruir o corpo do agente a invocar as skills por slash command / descrição (skills ativam sozinhas); se quiser botões clicáveis no VS Code, criar wrappers `.agent.md` finos por fluxo. **Esforço: M**

**A2. `tools` do agente usa nomes legados e omite `execute`.**
L4: `tools: ['codebase', 'editFiles', 'search', 'fetch']`. Os aliases portáveis documentados são `execute, read, edit, search, agent, web, todo`. O corpo manda rodar `cp`, `python3`, `pip` (L124, L326-327), impossível sem `execute`. **Correção:** `tools: ['read', 'edit', 'search', 'execute']`. **Esforço: S**

**A3. Falta `.github/workflows/copilot-setup-steps.yml`: o coding agent inicia sem jinja2/weasyprint/openpyxl e sem pango/cairo; a primeira geração de PDF na nuvem falha.**
Não existe nem `requirements.txt`. O local correto é `.github/workflows/copilot-setup-steps.yml` com um job chamado exatamente `copilot-setup-steps` (vale a partir da branch default). **Correção:** adicionar o workflow com setup-python 3.12 + apt libpango + pip install + smoke opcional. **Esforço: S**

**A4. Nenhum pin ou recomendação de modelo em lugar nenhum (requisito 3 totalmente não atendido).**
Grep por `model:` em `.github/` só retorna `disable-model-invocation: false`. Agente e prompt suportam `model:` no frontmatter; skills não podem fixar modelo pela spec, então precisam de guia compensatório. **Correção:** ver matriz de modelos na seção 6. **Esforço: S**

**A5. Núcleo de pontuação sem script determinístico: `calcular-scores`, `gap-analysis`, `recomendar-estrategias` mandam o LLM executar a matemática de pseudocódigo.**
`calcular-scores/SKILL.md` L21-77 + L111 ("Use Python with json stdlib"). Nenhum script no repo escreve `saida/scores.json`, `gaps.json` ou `recomendacoes.json`; os números do PDF executivo são computados pelo LLM a cada rodada. **Correção:** criar `scripts/compute_scores.py`, `compute_gaps.py`, `recommend_strategies.py` validados contra `referencia/exemplo-saida/`; encolher as SKILL.md para invocação + contrato de I/O. **Esforço: M**

**A6. As 3 skills de importação Excel embarcam 50-130 linhas de pseudocódigo Python em vez de script parser.**
Todos os 12 diretórios de skill contêm apenas SKILL.md (verificado). **Correção:** script parametrizado por regex de qid (`P[1-3]-C\d+-Q\d+` / `S\d-Q\d+` / `L\d-Q\d+`) e flag de anonimato; SKILL.md vira invocação + validação. **Esforço: L**

**A7. Importação fixa `"language": "pt-BR"` no metadata: cliente EN/ES recebe PDFs em português na primeira rodada.**
`importar-respostas-excel/SKILL.md` L158; esse campo controla o locale do relatório rio abaixo. **Correção:** preservar idioma existente, aceitar argumento ou perguntar uma vez na importação. **Esforço: S**

**A8. `copilot-instructions.md` injeta ~3.500 tokens em toda requisição; ~60% é móvel.**
Algoritmo completo (L69-126, 3ª cópia), branding (L46-67, triplicado), inventário de 12 skills (L195-231), tabelas S1-S7 e D2-D8, smoke test de contribuidor. Zero arquivos `.instructions.md` por caminho. **Correção:** cortar para ~70 linhas (~1.100 tokens): propósito, tabela de arquivos críticos enxuta, política de idioma, convenções de saída/do-not-modify, idempotência, ponteiros. Economia de ~2.400 tokens por requisição (~69%). **Esforço: M**

**A9. Convenção de idioma codificada contradiz a regra do dono.**
`copilot-instructions.md` L42-43 diz que a estrutura "pode usar inglês" e exemplos "devem ficar em PT-BR": política invertida versus "primitivos SEMPRE em inglês". O agente tem persona, tabelas e rotas em PT-BR estrutural. **Correção:** reescrever a política (primitivos 100% em inglês; apenas blocos de saída ao cliente localizados e rotulados) e traduzir a prosa estrutural do agente. **Esforço: M**

### 3.2 Pipeline e scripts

**A10. Strings PT fixas contaminam relatórios EN/ES.**
`build_payload_and_render.py:48-61,149-224`: rótulos de nível ("Sem resposta", "L1 — Em Desenvolvimento"), `capability_name_pt_br` incondicional e ações recomendadas default em PT entram em qualquer locale, apesar de `level.Lx.name` existir nos 3 catálogos i18n. **Correção:** resolver rótulos via catálogo pelo locale do payload. **Esforço: M**

**A11. `implementation-guide-inputs.json` com PII está trackeado no git (ignore inerte).**
`.gitignore:38` lista o arquivo, mas `git ls-files` mostra que está trackeado desde `4382cd0`. `auto_fill_from_plano.py` sobrescreve esse arquivo raiz com nomes+emails reais. **Correção:** `git rm --cached implementation-guide-inputs.json` + commit; manter só o template e o EXEMPLO. **Esforço: S**

**A12. `respostas.json` trackeado apesar do `.gitignore` (mesma armadilha).**
Byte-idêntico ao `respostas.json.example` (diff exit 0), então trackear não agrega nada; histórico contém apenas dados fake (`@cliente-exemplo.com.br`), então `git rm --cached` é seguro. **Correção:** `git rm --cached respostas.json` e instruir a copiar do `.example`. **Esforço: S**

### 3.3 CI/CD e distribuição

**A13. Nenhum CI valida PRs.**
Só existem `pages.yml` e `release-zips.yml`, ambos push-to-main. Nada roda `make smoke`, `check_language_coverage.py` ou dry-run de empacotamento em PR; `scripts/README.md` pede para o contribuidor rodar manualmente. Ambos os scripts já são CI-ready (exit codes corretos). **Correção:** `ci.yml` em `pull_request` rodando `make smoke-cross validate-docs` (stdlib-only, `permissions: contents: read`). **Esforço: S**

**A14. ZIPs EN/ES embarcam os primitivos Copilot na íntegra, mas excluem os arquivos que eles referenciam.**
Verificado construindo os ZIPs: `ai-maturity-kit-en.zip` inclui `copilot-instructions.md` e todas as skills, mas o único `referencia/*.md` é o README de exemplo; `pontuacao-e-calculo.md`, `P1/P2/P3-*.md` e `GUIA-PASSO-A-PASSO.md` ficam de fora (`add_pt_documentation()` só roda para PT). Num kit EN/ES baixado, o Copilot referencia arquivos inexistentes. **Correção:** adicionar as referências ao `SHARED_CLIENT_ASSETS` + teste de empacotamento que faz grep de caminhos nos primitivos e garante presença no ZIP. **Esforço: M**

**A15. `release-zips.yml` tem filtro `paths` que omite a maior parte do conteúdo empacotado: releases "latest" ficam obsoletas silenciosamente.**
O filtro não inclui `relatorios/`, `coleta/`, `survey-*/`, `wizard/`, `referencia/`, `formularios/`. **Correção:** remover o filtro (build leva segundos) ou cobrir todos os roots do empacotador. **Esforço: S**

### 3.4 Conteúdo e artefatos do cliente

**A16. 26+ docs voltados ao usuário existem só em PT; 7 deles embarcam nos ZIPs EN/ES.**
READMEs de pasta, `RUBRICA-MATURIDADE.md`, instruções de Forms dos 2 surveys, `wizard/README.md`, referência dos 3 pilares etc. Cliente do pacote inglês recebe instruções só em português para 2 dos 3 surveys e para o wizard. **Correção:** priorizar a tradução dos 7 docs de `SHARED_CLIENT_ASSETS`, depois READMEs por pasta; ou política escrita de isenção para docs de contribuidor. **Esforço: L**

**A17. Os 3 formulários HTML dizem "Resposta salva automaticamente" 158 vezes, mas têm zero JavaScript: nada é salvo.**
Único `<script>` é o CDN do Tailwind. Botões de nível, textarea com contador e dropzone de upload são decorativos; um participante que preencher 53 perguntas perde tudo. **Correção:** ou remover os controles fake e banner "somente leitura", ou adicionar persistência localStorage + export JSON (o wizard já implementa esse padrão). **Esforço: M**

**A18. Pesos contradizem entre `framework.json`, o xlsx auditável e o doc do algoritmo: a planilha preenchida não bate com `/calcular-scores`.**
`framework.json`: únicos pesos ≠1.0 são P1-C1-Q3=0.8, P1-C1-Q5=1.1, P1-C2-Q2=0.9. O xlsx usa Peso=1 no exemplo P1 e 1.5/2.0 em P2-C1/P3-C5 (framework diz 1.0); o doc afirma ambos errados em pontos diferentes. `preencher-planilha` manda "manter pesos como estão": dois números diferentes para as mesmas respostas. **Correção:** `framework.json` como fonte única; regenerar xlsx/doc a partir dele, ou `preencher-planilha` sobrescrever a coluna Peso. **Esforço: M**

**A19. Falta guia consolidado de modelos (`.github/MODELS.md`).**
Ver seção 6. **Esforço: S**

**A20. Ausência total de `.github/instructions/*.instructions.md`** (regras de subconjunto infladas no arquivo global sempre carregado + regras de proteção duplicadas em 4 arquivos). Ver A8 e seção 7. **Esforço: M**

---

## 4. Achados médios (43) — agrupados por tema

### Primitivos e consistência
| Achado | Arquivo(s) | Correção resumida |
|---|---|---|
| Caminhos de skill fora do repo fabricados (`../../../../.github/skills/paulasilva-ms/`, `~/.github/skills/ai-maturity-reports/`) | copilot-instructions.md, ai-maturity-reports/SKILL.md | Apontar só para `referencia/branding/*` (existem no repo) |
| Corpo do agente roteia por handoffs não declarados no frontmatter | agent.md | Igualar frontmatter e state machine (ou remover handoffs, ver A1) |
| Agente instruído a rodar shell sem tool de terminal | agent.md | Coberto por A2 |
| Prosa do agente fortemente PT-BR | agent.md | Reescrever em inglês; manter gatilhos PT na description e mock-ups rotulados |
| Prompt sem `model:` | pipeline-completo.prompt.md | `model: Claude Sonnet 4.6` |
| Agente sem `model:` | agent.md | `model:` string única (CLI rejeita forma de array) |
| Nome do prompt em português + sumário final hardcoded PT-BR | pipeline-completo.prompt.md | Renomear (ex.: `run-full-pipeline`) e responder no idioma do cliente |
| 9 de 12 nomes de skill em português (custo de migração: 8-34 arquivos cada) | 9 skills | Renomear em 1 PR atômico com grep de verificação: `calculate-scores`, `generate-reports`, `import-assessment-responses`, `import-developer-survey`, `import-learning-survey`, `training-plan`, `fill-spreadsheet`, `recommend-strategies`, `implementation-wizard` |
| Corpos de skill misturam PT/EN | plano-capacitacao, wizard-implementacao, calcular-scores, recomendar-estrategias | Prosa 100% EN; strings de saída via i18n |
| Deliverables mandatoriamente PT-BR (insights, plano, import log) | 3 skills | Parametrizar pelo `metadata.language` |
| "DO NOT reimplement" seguido de ~300 linhas de reimplementação | insights-developer-survey, plano-capacitacao | Cortar para ~60 linhas: invocação + validação + restrições |
| Zero recursos bundled em 12 skills (schemas/templates inline) | 4+ skills | Mover para `references/` e `scripts/` (tier de recursos da spec) |
| ai-maturity-reports: 80% duplicação + seção de sync de mantenedor com caminhos inexistentes | ai-maturity-reports/SKILL.md | Reduzir a ~40 linhas; sync → doc de manutenção |
| gerar-relatorio com 231 linhas: bloco de chat verbatim, branding duplicado | gerar-relatorio/SKILL.md | Comprimir para spec de formato de 5 linhas |
| Menus ASCII do agente com fatos que driftam (tamanhos de PDF, contagens) | agent.md | Listar arquivos reais gerados em vez de valores fixos |
| wizard-implementacao explica o Modo D duas vezes no mesmo arquivo | wizard-implementacao/SKILL.md | Deduplicar |

### Scripts
| Achado | Arquivo(s) | Correção resumida |
|---|---|---|
| `render_smoke.py` morto: todos os paths apontam para dirs inexistentes | relatorios/scripts/ | Corrigir ROOT/FIXTURES ou deletar |
| Sem validação de entrada: JSON malformado gera traceback bruto | build_payload_and_render.py, render_reports.py | Validar chaves com mensagem acionável ("rode /calcular-scores primeiro") |
| Import Excel dos surveys também é pseudocódigo | importar-survey-devs/learning SKILL.md | Scripts `importar_survey_*.py` espelhando o padrão do gerar_insights |
| `rubric.py` diverge da RUBRICA ("1:1" falso): D2 L3, peso de teste D5 (0.36 vs 15%), divisor D6 (9 vs 8) | survey-devs/scripts/ | Reconciliar código e doc |
| `gerar_insights.py` quebra com input vazio/não pontuável | survey-devs/scripts/ | Guardas + try/except com mensagem de 1 linha |
| Insight rotula dados de A2A como MCP | gerar_insights.py | Computar MCP de S3-Q6 ou renomear métrica |
| Scripts exigem Python 3.11+ (`datetime.UTC`) mas docs prometem 3.10+ | 3 scripts | `datetime.now(timezone.utc)` |
| Auto-fill do wizard parseia markdown com regex frágil (perda verificada de linhas multi-semana do calendário) | auto_fill_from_plano.py | Emitir `plano-capacitacao-<DATE>.json` estruturado e consumir o JSON |
| Rubrica colapsa scores silenciosamente com texto de resposta não canônico PT-BR | rubric.py, calcular_maturidade.py | Cobertura de match por respondente + warning/abort; sinônimos EN/ES |
| `validate_packaging_sources()` não cobre exemplos de referência; `add_file()` pula silenciosamente | build_language_kits.py | Levantar erro ou reportar fontes ausentes |
| Smoke test nunca exercita cálculo de scores nem scripts determinísticos de survey/wizard | smoke_test.py | Estender: gerar scores de verdade e comparar com exemplo-saida |

### i18n e distribuição
| Achado | Arquivo(s) | Correção resumida |
|---|---|---|
| Kits EN/ES são resumos (~13% do volume) rotulados "✅ Translated" | kit-en/, kit-es/ | Tradução integral ou rótulo honesto "condensed" + link ao original |
| 5 ferramentas HTML do cliente só em pt-BR, mas embarcam em todos os ZIPs | formularios/, wizard/, calculadora | Gerar variantes EN/ES dos bancos `.en/.es.md` (estruturas alinhadas) |
| `check_language_coverage.py` valida só 21 paths e passa verde com ~26 docs sem tradução | scripts/ | Estender manifesto ao inventário completo + paridade de chaves i18n |
| `tokens-paulasilva-ms.css` ausente dos 3 ZIPs: link de stylesheet morto em todo HTML do cliente | build_language_kits.py | Adicionar ao SHARED_CLIENT_ASSETS ou inline |
| HTMLs "standalone" dependem do CDN Tailwind Play + Google Fonts (inutilizáveis offline; JS de terceiros em páginas com PII) | 5 HTMLs | Bundle CSS pré-compilado inline + fontes self-hosted |
| Planilha "auditável" cobre só 17 de 158 perguntas (3 de 28 capabilities) | pontuacao-e-calculo.xlsx, preencher-planilha | Gerar 1 aba por capability a partir do framework.json, ou rotular como amostra |
| Sem LICENSE num kit distribuído publicamente (Pages + ZIPs de release) | LICENSE (ausente) | Adicionar (MIT/CC-BY/proprietária) e referenciar nos 3 READMEs |
| Hooks do Copilot suportados (cloud agent + CLI, `.github/hooks/*.json`) e não usados | .github/hooks/ (ausente) | Hook `preToolUse` negando edição de `framework.json`, `referencia/**`, templates (aplica deterministicamente as regras "NEVER modify") |

## 5. Achados baixos (47) — resumo

Contradições internas menores (4 vs 5 templates; 3 vs 4 modos do wizard; semântica de BLOCKED "refused" vs "still compute"; sequência do pipeline escrita 4×), referências a uma árvore `app/` e arquivos de plataforma inexistentes no kit (`scoring.rs`, `ImplementationGuideWizard.tsx`, `QuestionCard.tsx` no rodapé dos formulários), email pessoal hardcoded em todo payload (banido pelo próprio lint NFR-REPORT-011 do kit), fallback silencioso para "Acme Insurance Group" sem `respostas.json`, chave i18n ausente imprime `⟨key⟩` no PDF mas build sai 0, `import re` morto, default de `--out` escrevendo no diretório de exemplos de referência, `install-deps` com `--break-system-packages` (falha em venv/pip<23), datas não determinísticas sem override, avisos de PII só no apêndice do plano, `RUBRIC_VERSION` citado mas inexistente, notas de release com `\n` literal + colisão de tag em re-run, actions pinadas por tag e não por SHA, cleanup do smoke deletando `saida/payload.json` do usuário, comentário do pages.yml contradizendo o trigger, `scripts/README.md` só em PT, README do exemplo EN escrito em português, links cross-language quebrados dentro dos ZIPs, 3 `.DS_Store` + 1 `.pyc` trackeados, ~6.3 MB de PDFs regeneráveis triplicados por idioma, sem `.gitattributes`/CONTRIBUTING/SECURITY, exceção `.gitignore` para `settings.json.example` inexistente, `argument-hint` válido mas VS Code-only, descriptions de skill grandes para o tier sempre-carregado (889/1024 chars), dupla porta de entrada sem ordem em insights-developer-survey, contagem 75 vs ~69 em importar-survey-devs, calculadora com 16 perguntas onde docs dizem 17, chaves default redundantes no frontmatter do agente, e (positivo) `preencher-planilha` com 57 linhas é o modelo de skill a copiar; `AGENTS.md` e `mcp.json` corretamente ausentes por design (documentar como deliberado).

---

## 6. Matriz de modelos recomendados por tarefa (requisito 3)

Pesquisado nas docs oficiais de 2026 (model comparison + custom agents + prompt files). Skills **não podem** fixar modelo pela spec; o pin vale em frontmatter de agente e prompt (forma string única: o Copilot CLI rejeita a forma de array, `github/copilot-cli#2133`).

| Grupo de tarefa | Primitivos | Modelo recomendado | Custo /1M (tier) | Onde aplicar |
|---|---|---|---|---|
| Importação mecânica (Excel→JSON, planilha) | import-assessment-responses, import-developer-survey, import-learning-survey, fill-spreadsheet | **Claude Haiku 4.5** | $1/$5 (0.33×) | `.github/MODELS.md` + guia no orquestrador |
| Computação com script (scores, gaps, estratégias, render) | calculate-scores, gap-analysis, recommend-strategies, generate-reports | **GPT-5 mini** | $0.25/$2 (0.33×) | `.github/MODELS.md` |
| Síntese analítica (relatórios narrativos) | insights-developer-survey, training-plan | **Claude Sonnet 5** (fallback Sonnet 4.6) | $2/$10 | `.github/MODELS.md` |
| Orquestração interativa | agente concierge, prompt do pipeline, implementation-wizard, ai-maturity-reports | **Claude Sonnet 4.6** (default do CLI, compatível com cloud agent) | $3/$15 (9×) | `model:` no frontmatter do agente e do prompt + MODELS.md |

**Implementação recomendada:** criar `.github/MODELS.md` (inglês, ~25 linhas, tratado como primitivo) com essa matriz + forma de invocação (`copilot --model=<slug>` ou `/model`); adicionar UMA linha de ponteiro no `copilot-instructions.md`. **Não** embutir modelos nas descriptions das 12 skills (metadata sempre carregada = custo de token permanente).

---

## 7. Plano de ação priorizado

### Fase 0 — Quick wins de segurança e primeira execução (esforço S, fazer já)
1. `git rm --cached respostas.json implementation-guide-inputs.json .DS_Store referencia/.DS_Store relatorios/.DS_Store scripts/__pycache__/smoke_test.cpython-314.pyc` (A11, A12, higiene).
2. Adicionar `.github/workflows/copilot-setup-steps.yml` (A3).
3. Adicionar `.github/workflows/ci.yml` com `make smoke-cross validate-docs` em PR (A13).
4. Corrigir `tools:` do agente (A2) e adicionar `model:` no agente e no prompt (A4).
5. Criar `.github/MODELS.md` (A19/seção 6).
6. Remover `"language": "pt-BR"` hardcoded da importação (A7).
7. Corrigir filtro `paths` do release-zips.yml (A15).

### Fase 1 — Corretude do produto (esforço M)
8. **Consertar o merge do wizard → template Parte 4 (C1, o crítico) + asserção no smoke.**
9. Localizar rótulos/nomes/ações no `build_payload_and_render.py` via catálogos i18n (A10).
10. Reconciliar pesos framework.json ↔ xlsx ↔ doc (A18).
11. Formulários HTML: persistência localStorage + export, ou modo somente-leitura honesto (A17).
12. Incluir arquivos referenciados + CSS de tokens nos ZIPs EN/ES + teste de empacotamento (A14).
13. Remover handoffs quebrados do agente e rotear por skills (A1).

### Fase 2 — Refatoração de primitivos (esforço M/L)
14. Enxugar `copilot-instructions.md` para ~70 linhas; criar `.github/instructions/{branding,report-templates,contributing}.instructions.md` com `applyTo` (A8, A20).
15. Scripts determinísticos: `compute_scores.py`, `compute_gaps.py`, `recommend_strategies.py`, importadores Excel; SKILL.md viram invocação + contrato (A5, A6). Encolher insights/plano/gerar-relatorio/ai-maturity-reports para ~40-60 linhas.
16. Política de idioma nova: primitivos 100% inglês; renomear as 9 skills PT em 1 PR atômico; traduzir prosa do agente (A9 + médios).
17. Hook `preToolUse` em `.github/hooks/` protegendo arquivos imutáveis.

### Fase 3 — Trilíngue completo (esforço L)
18. Traduzir os 7 docs que embarcam nos ZIPs EN/ES, depois READMEs por pasta (A16).
19. Variantes EN/ES dos 5 HTMLs do cliente a partir dos bancos `.en/.es.md`.
20. Estender `check_language_coverage.py` ao inventário completo + rodar no CI.
21. LICENSE + CONTRIBUTING + .gitattributes.

**Impacto estimado da Fase 2 em tokens:** corpus de primitivos de ~32.300 → ~16.500 tokens (-49%); contexto injetado por requisição de ~3.500 → ~1.100 tokens (-69%).

---

## 8. Pontos fortes confirmados (não mexer)

- Paridade perfeita dos catálogos i18n (363 chaves × 3), templates com `autoescape=True` + `StrictUndefined`, zero `|safe`.
- Bancos de perguntas 100% trilíngues e estruturalmente idênticos (28/75/32 perguntas em PT/EN/ES).
- Scripts de survey determinísticos (2 execuções byte-idênticas fora timestamp), com `--help`, caminhos relativos ao kit e anonimato preservado no fluxo dev.
- Algoritmo de pontuação consistente entre instructions, doc de referência, skills e pipeline (cortes 0.5/1.5/2.5/3.5, thresholds 25/40, prioridades 2.4/1.6/0.9).
- `framework.json` íntegro; exemplos trabalhados do agente batem exatamente com `referencia/exemplo-saida/`.
- Permissões mínimas nos workflows; sem secrets/PII reais commitados hoje; histórico limpo.
- `preencher-planilha/SKILL.md` (57 linhas) é o padrão-ouro de skill enxuta do próprio kit.

---

## Apêndice — Fontes oficiais consultadas

- Custom instructions (repo-wide, path-specific, AGENTS.md): docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions; code.visualstudio.com/docs/agent-customization/custom-instructions
- Custom agents (`.agent.md`, frontmatter, handoffs, tools aliases, limites): docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents; code.visualstudio.com/docs/agent-customization/custom-agents
- Prompt files (`.prompt.md`, campo `agent`, `model`): code.visualstudio.com/docs/agent-customization/prompt-files
- Agent Skills (`SKILL.md`, limites de name/description, recursos bundled, sem pin de modelo): docs.github.com + agentskills.io (spec adotada pelo Copilot)
- Coding agent setup (`copilot-setup-steps.yml`) e hooks: docs.github.com/en/copilot (customize-cloud-agent)
- Modelos e multiplicadores: docs.github.com/en/copilot/reference/ai-models/model-comparison

*Relatório gerado por auditoria multi-agente com verificação adversarial. Achados: 111 confirmados de 112 propostos.*
