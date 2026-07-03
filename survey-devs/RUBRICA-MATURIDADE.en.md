# AI Maturity Rubric: Developer Survey

> **Deterministic model** that maps survey answers to L0-L4 levels across **7 dimensions**, mirroring the main maturity assessment's scale. Scored per team (no individual scores in the report, preserving anonymity).

**Rubric version:** 1.1 · **Date:** 2026-07-03 · Constant `RUBRIC_VERSION` in [`scripts/rubric.py`](scripts/rubric.py)
**Implementation:** [`scripts/rubric.py`](scripts/rubric.py) · **Runner:** [`scripts/calcular_maturidade.py`](scripts/calcular_maturidade.py)

---

## 🎯 Principles

1. **Deterministic**: the same answer always produces the same level. No LLM, no randomness.
2. **Auditable**: every rule is documented in this file, and the code replicates it 1:1.
3. **Conservative**: when in doubt, go down a level (avoids inflating declared maturity).
4. **Anonymous**: computed per respondent individually, but **only aggregates** appear in the report (average, distribution).
5. **Mirror of the main assessment**: uses the same L0-L4 scale (Initial → Optimizing) for direct comparison.

## 🧭 Scale (same as the main assessment)

| Range | Label | Description |
|---|---|---|
| `< 0.5` | **L0: Initial** | No practice, no knowledge, no tooling |
| `[0.5, 1.5)` | **L1: Developing** | Occasional adoption, basic knowledge |
| `[1.5, 2.5)` | **L2: Defined** | Regular use, knows key concepts |
| `[2.5, 3.5)` | **L3: Managed** | Broad adoption, knows advanced concepts, measures impact |
| `≥ 3.5` | **L4: Optimizing** | Full mastery, creates primitives, continuous optimization |

## 📊 The 7 dimensions

| ID | Dimension | Comes from | What it measures |
|---|---|---|---|
| **D2** | **Copilot Adoption** | S2 (9 q) | Frequency + breadth of modes + features + measured gain |
| **D3** | **MS/GH Tooling Breadth** | S3 (7 q) | How many advanced tools (Foundry, Spaces, Coding Agent, MCP, Spec Kit) are used |
| **D4** | **AI Dev Practices** | S4 (9 q) | TDD with AI, SDD, pair programming, debugging, onboarding |
| **D5** | **Agent Concepts Mastery** | S5 (11 q) | Knowledge of 9 key concepts + creation of primitives + testing |
| **D6** | **Instructions Maturity** | S6 (6 q) | Use of instructions files, maintenance, shared prompt library |
| **D7** | **Best Practices** | S7 (9 q) | Champion, DORA/DX metrics, community, sharing |
| **D8** | **Security & Governance** | S8 (13 q) | Policy, GHAS, scanners, SBOM, JIT, red-lines, audit, training |

> **Excluded from the score:** S1 (profile: only categorizes) and S9 (free text: becomes quotes).

## ⚖️ Detailed rules per dimension

> Quoted answer options below are the canonical PT-BR strings from the question bank, which is what the rubric matches (see the match-coverage guardrail); the localized question banks ([EN](perguntas-para-forms-devs.en.md), [ES](perguntas-para-forms-devs.es.md)) translate question titles but keep options canonical.

### D2: Copilot Adoption

| Key answer | Signals |
|---|---|
| `S2-Q1: Não tenho licença` OR `Tenho mas não uso` | **Hard L0** |
| `S2-Q2: Nunca` | **Hard L0** |
| `S2-Q2: Raramente` | L1 |
| `S2-Q2: Diariamente` + `S2-Q5: 2+ features` + `S2-Q3: 1+ mode` | **L2** |
| The above + `S2-Q3: uses Agent or Coding Agent` + `S2-Q5: 4+ features` + positive gain | **L3** |
| The above + `S2-Q3: Coding Agent` + `S2-Q5: Spaces` + `S2-Q7: gain >40%` + `S2-Q5: 5+ features` | **L4** |

Notes (conservative):
- "Positive gain" = an explicit answer of `+10%` or more on S2-Q7. An unanswered gain or "Não sei medir" does NOT grant L3.
- Each level requires the previous level's base (L3 and L4 require daily use).

### D3: MS/GH Tooling Breadth

Point-by-point score: `n_tools (S3-Q1) + advanced_signals (S3-Q3, Q4, Q6, Q2)`

- `n_tools` = how many tools checked in S3-Q1 (excluding "Nenhuma")
- `advanced_signals` = +1 for each:
  - Coding Agent: "Uso ativamente"
  - Spaces: "Uso e crio"
  - MCP: "Uso servidores" or "Configurei custom"
  - Foundry used for "MCP", "multi-agent", or "agentes autônomos"

**Mapping:**
- `score ≥ 8` → **L4** (5+ tools + 3+ advanced signals)
- `score 5-7` → **L3**
- `score 3-4` → **L2**
- `score 1-2` → **L1**
- `score 0` → **L0**

### D4: AI Dev Practices

Weighted sum (max ~10 points), mapped to 0-4:

| Question | Signal | Points |
|---|---|---|
| `S4-Q1` TDD with AI | "Sempre" | +2 |
|  | "Frequentemente" | +1.5 |
|  | "Não sei TDD" | -1 |
| `S4-Q2` SDD | "Uso ativamente" | +2 |
|  | "Já testei" | +1 |
|  | "Nunca ouvi falar" | -0.5 |
| `S4-Q3` Moments consulting AI (multi) | n_momentos × 0.4 (cap 2.0) | up to +2 |
| `S4-Q4` Pair programmer mindset | "Trato como par" | +1.5 |
|  | "Às vezes" | +0.5 |
| `S4-Q5` Refactoring | "Toda semana" | +1 |
| `S4-Q7` Debugging with AI first | "Pergunto Copilot" | +0.5 |
| `S4-Q8` Onboarding with AI | "Sempre" | +1 |

**Mapping:** `score / 10 × 4` → rounded.

### D5: Agent Concepts Mastery

3 components:

**(a) Coverage of 9 concepts** (60% of the weight): for each one, +1.0 if "uses/explains", else 0:
- S5-Q1 AI agent
- S5-Q2 Copilot modes
- S5-Q3 Custom agents
- S5-Q4 Skills
- S5-Q5 Prompt files
- S5-Q6 A2A
- S5-Q7 Handoffs
- S5-Q8 Subagents
- S5-Q9 Agentic DevOps personas

**(b) Primitives created (S5-Q11 multi)** (25% of the weight): n_primitivos × 0.25 (cap 1.0)

**(c) Agent testing (S5-Q10)** (15% of the weight):
- "Sempre" (test suite) → +1.0
- "Frequentemente" → +0.5
- "Não crio agents" → 0 (neutral)

**Formula:** `(coverage × 0.6 × 4) + min(n_primitivos × 0.25, 1.0) + (test_bonus × 0.6)`. Capped at 4.0.

> The three components add up to exactly 4.0 (2.4 + 1.0 + 0.6), so L4 is attainable.

**Minimum coverage:** if `<5` questions answered → returns `None` (not scored).

### D6: Instructions Maturity

| Question | Signal | Points |
|---|---|---|
| `S6-Q1` Files (multi) | "Nenhum" or empty | **Hard L0** |
|  | 4+ types | +2 |
|  | 2-3 types | +1.5 |
|  | 1 type | +1 |
| `S6-Q2` Maintainer | "Time inteiro contribui" | +2 |
|  | "1-2 dedicadas" | +1.5 |
|  | "Eu mantenho sozinho" | +1 |
|  | "Ninguém mantém" / "Não temos" | -1 |
| `S6-Q3` Update freq | "Toda semana" | +1 |
|  | "Mensalmente" | +0.7 |
|  | "Trimestralmente" | +0.4 |
|  | "Nunca" | -0.5 |
| `S6-Q4` Content (multi) | n_tipos × 0.3 (cap 2.0) | up to +2 |
| `S6-Q5` Library shared | "Copilot Space" / "repo dedicado" | +1 |
|  | "wiki/Confluence" | +0.5 |
|  | "Não compartilhamos" | -0.5 |

**Mapping:** `score / 8 × 4` (8 is the real attainable maximum: 2 + 2 + 1 + 2 + 1).

### D7: Best Practices

| Question | Signal | Points |
|---|---|---|
| `S7-Q1` Learning sources (multi) | n_fontes × 0.3 (cap 1.5) | up to +1.5 |
| `S7-Q2` Champion | "eu sou" / "outra pessoa" | +1.5 |
|  | "Cada um se vira" | -0.5 |
| `S7-Q3` Internal channel | ">5 mensagens/sem" | +1 |
|  | "pouco ativo" | +0.5 |
| `S7-Q4` Metrics (multi) | DORA/DX/SPACE/Copilot count × 0.5 (cap 2.0) | up to +2 |
|  | "Não medimos" | -1 |
| `S7-Q5` Iterations | "1ª tentativa" / "2-3" | +1 |
|  | "7+" | -0.5 |
| `S7-Q9` Shares prompts | "Frequentemente" | +1 |
|  | "Nunca" | -0.5 |

**Mapping:** `score / 8 × 4`.

### D8: Security & Governance (CRITICAL, conservative)

The largest number of rules + penalties for red flags:

| Question | Signal | Points |
|---|---|---|
| `S8-Q1` Policy + `S8-Q4` (Sec tools) | ("Não temos política" OR "Não sei") + "Nenhuma ferramenta" | **Hard L0** |
| `S8-Q1` | "formal e clara" | +2 |
|  | "pouco clara" | +1 |
|  | "informal" | +0.5 |
| `S8-Q2` Knows sensitive data | "Sei claramente" | +1 |
| `S8-Q3` Forbidden (multi) | n_tipos × 0.2 (cap 1.0) | up to +1 |
|  | "Nenhuma restrição" | -1 |
| `S8-Q4` Sec tools (multi) | n_tools × 0.3 (cap 2.0) | up to +2 |
| `S8-Q5` Code scan on the PR | "gate obrigatório" | +1 |
| `S8-Q6` SBOM | "automatizado" | +0.5 |
| `S8-Q7` Formal AI review | "obrigatório humano + scanner" | +1 |
| `S8-Q8` Agent red-lines | "Sempre" | +1 |
| `S8-Q9` JIT permissions | "JIT obrigatório" | +1 |
| `S8-Q10` DLP | "bloqueia" | +0.5 |
| `S8-Q11` Audit | "ativos e revisados" | +0.5 |
| `S8-Q12` Training | "obrigatório anual" | +0.5 |

**Mapping:** `score / 12 × 4`.

## 🧮 Respondent overall score

```
overall = mean(D2..D8)  # only dimensions with score != None
```

## 🛡️ Match-coverage guardrail

Rule matching is case-insensitive substring matching over the canonical PT-BR options (with EN/ES synonyms for the highest-signal options, e.g. license, frequency, policy). If a client translates or changes the options in Forms, the rules stop recognizing the answers and scores silently deflate.

To protect against this, `calcular_maturidade.py` measures per respondent the **match coverage**: % of answered scoreable questions whose text matches some known canonical option (`rubric.match_coverage`). Behavior based on the team average:

| Average coverage | Behavior |
|---|---|
| ≥ 70% | Proceeds normally |
| 40% to 70% | Proceeds with a **highlighted warning** (scores may be underestimated) |
| < 40% | **Aborts** with an actionable error; use `--force` to proceed anyway |

The measured coverage (average/minimum) goes to `metadata.match_coverage` in the output JSON.

## 🧮 Team aggregation

```
team_score(D) = mean(D across all respondents)  # ignores None
team_overall  = mean(overall across all respondents)
distribution(D) = % of respondents at each L0-L4
```

## 📤 Output

`saida/maturidade-developer-survey-<DATE>.json`:

```jsonc
{
  "metadata": {
    "computed_at": "2026-07-03T12:00:00+00:00",
    "source": "survey-devs/respostas-devs.json",
    "n_respondents": 12,
    "rubric_version": "1.1 (deterministic)",
    "match_coverage": {"avg_pct": 100.0, "min_pct": 100.0, "n_measured": 12},
    "anonymous": true,
    "scope": "team aggregate (no individual scores in output)"
  },
  "team_overall": {
    "score": 2.22,
    "label": "L2 — Definido",
    "respondents_with_overall": 12
  },
  "dimensions": {
    "D2": {
      "name": "Copilot Adoption",
      "team_score": 0.80,
      "label": "L1 — Em Desenvolvimento",
      "respondents_with_score": 12,
      "distribution_count": {"L0": 5, "L1": 5, "L2": 2, "L3": 0, "L4": 0},
      "distribution_pct": {"L0": 41.7, "L1": 41.7, "L2": 16.7, "L3": 0, "L4": 0}
    },
    "D3": {...}, "D4": {...}, "D5": {...},
    "D6": {...}, "D7": {...}, "D8": {...}
  },
  "ranking": {
    "top": [["D7", "Best Practices", 2.91], ...],
    "bottom": [["D2", "Copilot Adoption", 0.80], ...]
  }
}
```

## 🔄 How to run

### Via skill in Copilot Chat

```
/insights-developer-survey   # invokes the script automatically
```

### Via CLI

```bash
python3 survey-devs/scripts/calcular_maturidade.py
# Output:
#   - saida/maturidade-developer-survey-DATE.json
#   - summary on stdout (overall + per-dimension table + ranking)
```

## 🔗 Cross-reference with the main assessment

Individual maturity (from the survey) **feeds and validates** the organizational assessment's capabilities:

| Survey dimension | Assessment capability | What to validate |
|---|---|---|
| **D2** Copilot Adoption | `P1-C1` AI Coding Assistants | Declared score vs. real adoption declared by devs |
| **D3** MS/GH Tooling | `P3-C3` AI Applications + `P3-C5` Agentic Apps | Technical sophistication in AI |
| **D4** AI Dev Practices | `P1-C2` DevEx + `P1-C8` Productivity Metrics | Structured practices |
| **D5** Agent Concepts | `P3-C5` Agentic Apps | Advanced knowledge |
| **D6** Instructions | `P1-C7` Automated documentation | Maintenance of AI context |
| **D7** Best Practices | `P1-C5` Onboarding + `P1-C8` Metrics | Adoption culture |
| **D8** Security & Governance | `P2-C4` DevSecOps + `P2-C10` Supply Chain | Real governance |

> 💡 **Classic pattern:** leadership rates P1-C1 as L3, but survey D2 shows L1 (60% of devs rarely use it) → **dissonance** between strategy and practice. The `/insights-developer-survey` skill highlights this in section 12 of the report.

## 📝 Changelog

### v1.1 (2026-07-03) · code vs. document reconciliation

An audit found divergences between `rubric.py` and this document (which is the contract). Decisions made, one per divergence:

1. **D2, L3 gate** · the code granted L3 for weekly use + Agent + (3+ modes OR 4+ features) without requiring positive gain (an unanswered gain passed). **Decision: code fixed to follow the document** (daily use + Agent or Coding Agent + 4+ features + explicit positive gain), which is the conservative rule. L4 now also requires the L3 base (daily use), as the table's "The above +" always indicated.
2. **D5, testing weight** · the code gave the testing component a maximum weight of 0.36 (9%), contradicting the declared "15% of the weight", and made L4 unattainable (maximum 3.76). **Decision: code fixed to 0.6** (15% of 4.0); the three components now add up to exactly 4.0.
3. **D6, mapping divisor** · code and document used `/9`, but the real maximum of points is 8 (2+2+1+2+1), making L4 unattainable (maximum 3.56). **Decision: both fixed to `/8`.**
4. **Rules that existed in the code but were absent from the document** · documented with no behavior change: the D8 hard-L0 includes "Não sei" (not knowing whether a policy exists is, conservatively, equivalent to not having one); D6 "Trimestralmente" +0.4, "Eu mantenho sozinho" +1, and "wiki/Confluence" +0.5.
5. **New additions** · a `RUBRIC_VERSION` constant in `rubric.py` (exported to the JSON metadata); EN/ES synonyms for the highest-signal options; the match-coverage guardrail (section above).

## 📊 Rubric calibration and review

This is **version 1.1**. A quarterly review is recommended based on:

- Cases where a score seems under/overestimated (calibrate weights)
- Ecosystem changes (e.g. Copilot launches a new mode → add it to S2-Q3 + update D2)
- Respondent feedback ("that question was ambiguous")

**How to propose a change:**
1. Edit `scripts/rubric.py` with the updated rule
2. Document the why in this file
3. Increment `RUBRIC_VERSION` and re-run with previous data to compare

## 🔐 Anonymity policy in scoring

The rubric computes a score PER respondent individually, but the output JSON and the report:

- ✅ Show **aggregated team scores** (average, % distribution)
- ✅ Show **distribution per level** (% of devs at each L0-L4)
- ❌ Do NOT show scores per respondent_id
- ❌ Do NOT show role/profile alongside a score (aggregation by role only if ≥3 devs share the same role)

This preserves the survey's anonymity pact while enabling insights useful to the team.
