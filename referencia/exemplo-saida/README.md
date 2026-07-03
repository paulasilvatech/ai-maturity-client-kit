# Exemplos de outputs finais — AI Maturity Assessment Kit

> Esta pasta contém **PDFs reais gerados a partir de `respostas.json.example`** (perfil "Cliente Exemplo S.A.", 46 respostas mockadas). São o **preview exato** do que o cliente vai gerar ao rodar `/run-full-pipeline` com seus próprios dados.

## 📊 Os 5 PDFs principais — Cliente Exemplo S.A. (PT-BR)

| Arquivo | Tamanho | Conteúdo |
|---|---|---|
| **[score_justification.pdf](score_justification.pdf)** | 337 KB (27 págs.) | Justificativa de score: overall **1.99 (L2)**, breakdown por pillar, PE Readiness com path recommendation |
| **[roadmap_part_pillar_p1.pdf](roadmap_part_pillar_p1.pdf)** | 369 KB (16 págs.) | Pillar P1 deep-dive, 9 capabilities de Produtividade (média **2.69, L3**) |
| **[roadmap_part_pillar_p2.pdf](roadmap_part_pillar_p2.pdf)** | 371 KB (17 págs.) | Pillar P2 deep-dive, 10 capabilities de DevOps (média **1.52, L2**) |
| **[roadmap_part_pillar_p3.pdf](roadmap_part_pillar_p3.pdf)** | 373 KB (17 págs.) | Pillar P3 deep-dive, 9 capabilities de Plataforma (média **1.92, L2**) |
| **[roadmap_part4.pdf](roadmap_part4.pdf)** | 338 KB (19 págs.) | Implementation Guide consolidado (Three Horizons + comitês + RACI + comms + treinamento + ADKAR + quick wins) |

**Total:** 5 PDFs · 96 páginas · branding limpo (sem valores monetários, sem Microsoft confidential, conforme NFR-REPORT-011).

## 🌐 Versões EN e ES (mesmo cliente, outro locale)

- A subpasta [`en/`](en/) tem os mesmos 5 PDFs renderizados em inglês.
- A subpasta [`es/`](es/) tem os mesmos 5 PDFs renderizados em espanhol.

Ambas foram geradas com os mesmos inputs, trocando apenas o locale (`--locale en` / `--locale es`). Veja os READMEs de cada subpasta para o comando exato.

## 📦 Arquivos auxiliares (intermediários do pipeline)

### Outputs do assessment principal

| Arquivo | Origem | Para que serve |
|---|---|---|
| **[scores.json](scores.json)** | `/calculate-scores` | Scores brutos: overall, 3 pillars, 28 capabilities |
| **[gaps.json](gaps.json)** | `/gap-analysis` | 10 gaps ordenados por prioridade (3 P0, 0 P1, 1 P2, 6 P3) |
| **[recomendacoes.json](recomendacoes.json)** | `/recommend-strategies` | 6 estratégias rankeadas + tecnologias |
| **[payload.json](payload.json)** | `/generate-reports` | Payload completo enviado ao Jinja2 (debug + customização) |
| **[pontuacao-preenchida-2026-05-08.xlsx](pontuacao-preenchida-2026-05-08.xlsx)** | `/fill-spreadsheet` | Planilha auditável com SUMPRODUCT |
| **[import-log-2026-05-08.md](import-log-2026-05-08.md)** | `/import-assessment-responses` | Log da importação (ilustrativo) |

### ⭐ Outputs do Developer Survey (anônimo)

| Arquivo | Origem | Para que serve |
|---|---|---|
| **[insights-developer-survey-EXEMPLO.md](insights-developer-survey-EXEMPLO.md)** | `/insights-developer-survey` | Relatório completo PT-BR de insights (12 seções). Gerado a partir dos 5 mocks do `survey-devs/respostas-mock-devs.json` |
| **[maturidade-developer-survey-EXEMPLO.json](maturidade-developer-survey-EXEMPLO.json)** | `/insights-developer-survey` | Maturidade calculada por rubrica determinística v1.1, L0-L4 nas 7 dimensões D2-D8, com `match_coverage` no metadata |

### ⭐ Outputs do Learning & Growth Survey (identificado)

| Arquivo | Origem | Para que serve |
|---|---|---|
| **[plano-capacitacao-EXEMPLO.md](plano-capacitacao-EXEMPLO.md)** | `/training-plan` | Plano de capacitação com top 10 tópicos (inscritos pré-validados por nome+email), Champions Network, mentor pairs, calendário 90 dias. Seções com PII trazem aviso de distribuição restrita |
| **[plano-capacitacao-EXEMPLO.json](plano-capacitacao-EXEMPLO.json)** | `/training-plan` | Dados estruturados do plano (tópicos, cohorts, champions, mentores, calendário, barreiras), fonte primária do wizard Mode D |
| **[implementation-guide-inputs-EXEMPLO.json](implementation-guide-inputs-EXEMPLO.json)** | `/implementation-wizard` Mode D | Auto-fill que extrai 6 dos 9 inputs do wizard direto do plano de capacitação |

## 🧬 Como esses PDFs foram gerados (algoritmo do `generate-reports`)

```
respostas.json.example          (input do cliente — 46 respostas mockadas)
    ↓
/calculate-scores  →  saida/scores.json
    ↓
/gap-analysis     →  saida/gaps.json
    ↓
/recommend-strategies  →  saida/recomendacoes.json
    ↓
/generate-reports invoca relatorios/scripts/build_payload_and_render.py:
  ├─ Carrega relatorios/sample_payload.json (estrutura completa, ~28 caps com narrativa rica)
  ├─ SOBRESCREVE só campos que temos dados:
  │   • organization                    ← respostas::metadata
  │   • scores.overall.weighted_avg     ← scores.json
  │   • scores.pillars[].weighted_avg   ← scores.json
  │   • capabilities[].current_score    ← scores.json (matched by id)
  │   • gap_analysis[]                  ← gaps.json (rebuilt structure)
  │   • implementation_guide_inputs     ← implementation-guide-inputs.json
  │     (dados do wizard convertidos para as chaves que o template lê;
  │      as pessoas fictícias do sample são SEMPRE descartadas)
  ├─ MANTÉM placeholders profissionais do sample para campos sem dados:
  │   • capabilities[].scoring_rationale, h1_initiatives, evidence_collected
  │   • technology_resources_per_pillar
  │   • risks_per_pillar, success_metrics_per_pillar, next_steps_per_pillar
  │   • horizons (narrative)
  └─ Renderiza via render_reports.py:
      Jinja2 + i18n (pt-br/en/es) + WeasyPrint → 5 PDFs
```

## 🎯 Resultados do Cliente Exemplo S.A.

### Maturidade global

- **Overall:** **1.99** (L2 — Definido)
- **Threshold:** OK (46/158 respondidas — perfil enxuto realista)
- **Cobertura por pillar:** P1 = 13/53 · P2 = 18/59 · P3 = 15/46

### Por pillar

| Pillar | Score | Rótulo | Forte/Fraco |
|---|---|---|---|
| **P1** Produtividade | **2.69** | L3 — Gerenciado | 💪 Copilot bem adotado |
| **P2** DevOps | **1.52** | L2 — Definido | ⚠️ DevSecOps fraco |
| **P3** Plataforma | **1.92** | L2 — Definido | ⚠️ Aplicações Agênticas fracas |

### Top 3 gaps P0 (críticos)

1. **P3-C5** Aplicações Agênticas — gap 3.17 → priority 3.17 → estratégia **S6**
2. **P2-C4** DevSecOps — gap 2.75 → priority 3.30 → estratégia **S7**
3. **P2-C10** Supply Chain Security — gap 2.33 → priority 2.57 → estratégia **S7**

### Top 3 estratégias recomendadas

1. **S7** Security & Governance — priority cumulativa **5.87** (2 capabilities P0)
2. **S6** Agentic Activation — priority cumulativa **3.92** (2 capabilities P0)
3. **S5** GitHub Copilot Acceleration — priority cumulativa **3.01** (4 capabilities)

### Estratégias sem gaps relevantes

- S1 GitHub Migration · S3 App Modernization · S4 AI Applications

## 🧪 Como regerar cada arquivo desta pasta

Todos os comandos rodam a partir da raiz do kit. Os exemplos usam a data pinada `2026-05-08` para que a saída seja byte-idêntica à desta pasta.

### 1. Preparar os inputs de exemplo

```bash
cp respostas.json.example respostas.json
cp referencia/exemplo-saida/scores.json saida/scores.json
cp referencia/exemplo-saida/gaps.json saida/gaps.json
cp referencia/exemplo-saida/recomendacoes.json saida/recomendacoes.json
cp referencia/exemplo-saida/implementation-guide-inputs-EXEMPLO.json implementation-guide-inputs.json
```

(Ou gere `saida/*.json` do zero com `make recommend`, o resultado é idêntico.)

### 2. payload.json e os 5 PDFs PT-BR

```bash
# Só o payload + HTMLs (não precisa de weasyprint):
python3 relatorios/scripts/build_payload_and_render.py --html-only --date 2026-05-08

# PDFs completos (precisa de weasyprint; make install-deps):
export SOURCE_DATE_EPOCH=1778257208   # pina os timestamps de fonte embutidos no PDF
python3 relatorios/scripts/build_payload_and_render.py --date 2026-05-08
# ou, com a data de hoje: make pipeline
```

### 3. PDFs EN e ES

```bash
python3 relatorios/scripts/build_payload_and_render.py --date 2026-05-08 --locale en --out referencia/exemplo-saida/en
python3 relatorios/scripts/build_payload_and_render.py --date 2026-05-08 --locale es --out referencia/exemplo-saida/es
```

### 4. Outputs dos surveys complementares

```bash
# Developer Survey (insights + maturidade em um comando):
python3 survey-devs/scripts/gerar_insights.py \
  --input survey-devs/respostas-mock-devs.json --now 2026-05-08T16:20:08Z
# gera saida/insights-developer-survey-2026-05-08.md
#      saida/maturidade-developer-survey-2026-05-08.json

# Learning & Growth Survey (plano .md + .json):
python3 survey-learning/scripts/gerar_plano_capacitacao.py \
  --input survey-learning/respostas-mock-learning.json --now 2026-05-08T16:20:08Z
# gera saida/plano-capacitacao-2026-05-08.{md,json}
```

Renomeie os arquivos datados para o sufixo `-EXEMPLO` ao copiá-los para esta pasta.

## ⚠️ Limitações conhecidas (e como contornar)

Algumas seções dos PDFs **mantém placeholders do sample_payload.json** para campos onde não temos dados estruturados do cliente. Especificamente:

- Por capability: `scoring_rationale`, `h1_initiatives`, `evidence_collected`, `h2_key_enabler`, narrativa de horizons
- `technology_resources_per_pillar` detalhado (tabelas H1/H2/H3 por pillar)
- `risks_per_pillar` / `success_metrics_per_pillar` / `next_steps_per_pillar`
- Campos do wizard sem resposta (ex.: `training_plan` neste exemplo) rendem o placeholder neutro do template. As pessoas fictícias do sample (Maria Santos, Carlos Rivera etc.) nunca aparecem quando existem dados do cliente.

### Como personalizar

**Para Implementation Guide (Parte 4):**
```
/implementation-wizard   # 9 steps preenchem tudo da Parte 4
/generate-reports        # re-renderiza com dados reais
```

**Para narrativa per capability (scoring_rationale, h1_initiatives etc.):**
```bash
# Editar manualmente saida/payload.json (substituir placeholders Acme)
code saida/payload.json

# Re-renderizar (pula a etapa de merge)
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
```

---

**Renderizador:** WeasyPrint 69.0 + Jinja2 · **Templates:** `relatorios/templates/` · **Data pinada:** 2026-05-08 (`--date` / `--now`)
