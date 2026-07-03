"""Rubrica determinística de maturidade IA — Developer Survey v2.0.

Mapeia respostas individuais para níveis L0-L4 em 7 dimensões. Resultado
agregado vira score do time (média ponderada) + distribuição (% devs por L).

Princípios:
- Determinística: mesma resposta → mesmo nível, sempre
- Auditável: cada regra documentada
- Conservadora: na dúvida, desce o nível (evita inflar maturidade)
- Anonimato: aplica por respondente individual, mas só agregados saem no relatório

Cada função `score_DX(responses)` retorna float em [0.0, 4.0] ou None se cobertura insuficiente.
"""
from typing import Optional

# Single source of truth for the rubric version. Exported to the metadata of
# every writer (calcular_maturidade.py, gerar_insights.py). Bump it whenever a
# scoring rule changes and document the change in RUBRICA-MATURIDADE.md.
RUBRIC_VERSION = "1.1"


# =========================================================
# Helpers
# =========================================================

def _ans(responses: dict, qid: str) -> Optional[str]:
    """Returns answer string for qid, or None if not answered."""
    r = responses.get(qid)
    if r is None or r.get("value") is None:
        return None
    val = str(r["value"]).strip()
    return val if val else None


def _multi(responses: dict, qid: str) -> list[str]:
    """Returns list of selected options for multi-choice answers."""
    val = _ans(responses, qid)
    if not val:
        return []
    return [opt.strip() for opt in val.split(";") if opt.strip()]


def _matches(answer: Optional[str], *patterns: str) -> bool:
    """Case-insensitive substring match — answer contains ANY of patterns."""
    if not answer:
        return False
    a = answer.lower()
    return any(p.lower() in a for p in patterns)


def _multi_count(items: list[str], *patterns: str) -> int:
    """Count how many items match any of the patterns."""
    return sum(1 for item in items if _matches(item, *patterns))


# =========================================================
# D2 — Copilot Adoption Maturity
# =========================================================
# Sinais: licença + frequência + breadth de modos + features + ganho percebido

def score_D2(responses: dict) -> Optional[float]:
    """Copilot Adoption Maturity (L0-L4)."""
    license_ans = _ans(responses, "S2-Q1")
    if license_ans is None:
        return None

    # Hard L0: no license, or has one but never uses it.
    # EN/ES synonyms cover clients that translated the answer options in Forms.
    if _matches(license_ans, "Não tenho licença", "don't have a license", "do not have a license",
                "no tengo licencia") or \
       _matches(license_ans, "Tenho licença mas não uso", "have a license but", "tengo licencia pero"):
        return 0.0

    freq = _ans(responses, "S2-Q2")
    if _matches(freq, "Nunca", "Never"):
        return 0.0
    if _matches(freq, "Raramente", "Rarely", "Rara vez"):
        return 1.0

    modes = _multi(responses, "S2-Q3")
    n_modes = sum(1 for m in modes if not _matches(m, "Não conheço", "Não uso"))
    uses_agent = any(_matches(m, "Agent (autônomo no IDE", "Coding Agent") for m in modes)
    uses_coding_agent = any(_matches(m, "Coding Agent (autônomo no GitHub") for m in modes)

    features = _multi(responses, "S2-Q5")
    n_features = len(features)
    uses_spaces = any(_matches(f, "Spaces") for f in features)
    uses_pr_review = any(_matches(f, "PR review") for f in features)

    gain = _ans(responses, "S2-Q7")
    high_gain = _matches(gain, "+40", "+60") if gain else False
    positive_gain = _matches(gain, "+10", "+20", "+40", "+60") if gain else False
    daily = _matches(freq, "Diariamente", "Daily", "Diario") if freq else False

    # Ladder documented in RUBRICA-MATURIDADE.md (each level builds on the one
    # below it; an unanswered gain question does NOT grant L3 -- conservative).
    # L4: L3 base + Coding Agent + Spaces + measured gain >40% + 5+ features
    if daily and uses_coding_agent and uses_spaces and high_gain and n_features >= 5:
        return 4.0

    # L3: daily use + Agent or Coding Agent + 4+ features + explicit positive gain
    if daily and (uses_agent or uses_coding_agent) and n_features >= 4 and positive_gain:
        return 3.0

    # L2: daily use + 1+ chat mode + 2+ features
    if daily and n_modes >= 1 and n_features >= 2:
        return 2.0

    # L1: has license and weekly+ use but no breadth
    return 1.0


# =========================================================
# D3 — MS/GH Tooling Breadth
# =========================================================
# Conta quantas ferramentas avançadas USA (Foundry, Spaces, Coding Agent, MCP, Spec Kit, etc.)

ADVANCED_MS_GH_TOOLS = [
    "Microsoft Foundry",
    "Foundry Agent Service",
    "Azure OpenAI",
    "Microsoft 365 Copilot",
    "GitHub Copilot Spaces",
    "GitHub Copilot Coding Agent",
    "GitHub Codespaces",
    "GitHub Models",
    "GitHub Advanced Security",
    "GitHub Actions com Copilot",
    "Visual Studio com Copilot",
]


def score_D3(responses: dict) -> Optional[float]:
    """MS/GitHub Tooling Breadth (L0-L4)."""
    tools = _multi(responses, "S3-Q1")
    if not tools:
        return None
    if any(_matches(t, "Nenhuma das acima") for t in tools):
        return 0.0

    # Count MS/GH tools used (excluding "nenhuma")
    n_tools = sum(1 for t in tools if not _matches(t, "Nenhuma"))

    # Bonus signals: knows specific advanced concepts
    coding_agent_use = _ans(responses, "S3-Q3")
    spaces_use = _ans(responses, "S3-Q4")
    mcp_use = _ans(responses, "S3-Q6")
    foundry_use = _multi(responses, "S3-Q2")

    advanced_count = 0
    if _matches(coding_agent_use, "Uso ativamente"):
        advanced_count += 1
    if _matches(spaces_use, "Uso e crio Spaces"):
        advanced_count += 1
    if _matches(mcp_use, "Uso servidores MCP", "Configurei algum MCP"):
        advanced_count += 1
    if any(_matches(f, "MCP", "Multi-agent", "agentes autônomos") for f in foundry_use):
        advanced_count += 1

    # Mapping: tools count + advanced signals → L
    score = n_tools + advanced_count

    if score >= 8: return 4.0  # 5+ tools + 3+ advanced signals
    if score >= 5: return 3.0  # ~4 tools + some advanced
    if score >= 3: return 2.0  # ~3 tools, basic adoption
    if score >= 1: return 1.0  # 1-2 tools
    return 0.0


# =========================================================
# D4 — AI Dev Practices Maturity
# =========================================================
# TDD com IA + SDD + pair programming + IA em todas as fases do dev

def score_D4(responses: dict) -> Optional[float]:
    """AI Dev Practices Maturity (L0-L4)."""
    tdd = _ans(responses, "S4-Q1")
    sdd = _ans(responses, "S4-Q2")
    moments = _multi(responses, "S4-Q3")
    pair = _ans(responses, "S4-Q4")
    refactor = _ans(responses, "S4-Q5")
    debug = _ans(responses, "S4-Q7")
    onboarding = _ans(responses, "S4-Q8")

    if all(x is None for x in [tdd, sdd, pair, refactor]):
        return None

    score = 0

    # TDD com IA
    if _matches(tdd, "Sempre que possível"): score += 2
    elif _matches(tdd, "Frequentemente"): score += 1.5
    elif _matches(tdd, "Às vezes"): score += 1
    elif _matches(tdd, "Não sei o que é TDD"): score -= 1

    # SDD
    if _matches(sdd, "Uso ativamente"): score += 2
    elif _matches(sdd, "Já testei"): score += 1
    elif _matches(sdd, "Nunca ouvi falar"): score -= 0.5

    # Breadth de momentos (max 7 momentos)
    n_moments = len(moments)
    score += min(n_moments * 0.4, 2.0)  # cap 2.0

    # Pair programmer mindset
    if _matches(pair, "Sim — trato como par"): score += 1.5
    elif _matches(pair, "Às vezes"): score += 0.5

    # Refactoring
    if _matches(refactor, "Toda semana"): score += 1
    elif _matches(refactor, "Algumas vezes"): score += 0.5

    # Debugging com IA primeiro
    if _matches(debug, "Pergunto ao Copilot"): score += 0.5

    # Onboarding com IA
    if _matches(onboarding, "Sempre"): score += 1
    elif _matches(onboarding, "Frequentemente"): score += 0.5

    # Cap and map (range 0-10 → 0-4)
    score = max(0, min(score, 10))
    return round(score / 10 * 4, 2)


# =========================================================
# D5 — Agent Concepts Mastery
# =========================================================
# Conhecimento de 11 conceitos + criou primitives + testa agents

def score_D5(responses: dict) -> Optional[float]:
    """Agent Concepts Mastery (L0-L4)."""
    # 8 conceitos chave (Q1-Q8 do S5 + Q9 personas + Q10 testar)
    concept_questions = [
        ("S5-Q1", ["Sim — explico claramente"]),         # AI agent
        ("S5-Q2", ["Sim — uso conscientemente"]),        # Modos
        ("S5-Q3", ["Já criei", "Já usei"]),              # Custom agents
        ("S5-Q4", ["Conheço e uso", "Conheço mas não uso"]),  # Skills
        ("S5-Q5", ["Sim — várias", "Sim — uma ou duas"]),     # Prompt files
        ("S5-Q6", ["Uso", "Conheço o conceito"]),        # A2A
        ("S5-Q7", ["Uso", "Conheço o conceito"]),        # Handoffs
        ("S5-Q8", ["Uso", "Conheço o conceito"]),        # Subagentes
        ("S5-Q9", ["Sim — adoto", "Conheço o conceito"]),     # Personas Agentic DevOps
    ]

    answered = 0
    knowledge_score = 0
    for qid, deep_keywords in concept_questions:
        ans = _ans(responses, qid)
        if ans is None:
            continue
        answered += 1
        # Strong knowledge (use/explain) = 1.0
        if any(_matches(ans, k) for k in deep_keywords):
            knowledge_score += 1.0

    if answered < 5:
        return None  # insufficient coverage

    # Coverage ratio
    coverage = knowledge_score / len(concept_questions)  # 0-1

    # Bonus: created primitives (S5-Q11 multi)
    primitives = _multi(responses, "S5-Q11")
    n_primitives = sum(1 for p in primitives if not _matches(p, "Nenhum dos acima"))

    # Bonus: tests agents (S5-Q10)
    tests = _ans(responses, "S5-Q10")
    test_bonus = 0
    if _matches(tests, "Sempre — tenho test suite"): test_bonus = 1.0
    elif _matches(tests, "Frequentemente"): test_bonus = 0.5
    elif _matches(tests, "Não crio agents"): test_bonus = 0  # neutral

    # Combined score: 60% coverage (max 2.4) + 25% primitives (max 1.0)
    # + 15% testing (max 0.6). Weights sum to exactly 4.0 so L4 is attainable.
    raw = (coverage * 0.6 * 4) + min(n_primitives * 0.25, 1.0) + (test_bonus * 0.6)

    return round(min(raw, 4.0), 2)


# =========================================================
# D6 — Instructions Files Maturity
# =========================================================

def score_D6(responses: dict) -> Optional[float]:
    """Instructions / Memory Maturity (L0-L4)."""
    files = _multi(responses, "S6-Q1")
    maintainer = _ans(responses, "S6-Q2")
    freq = _ans(responses, "S6-Q3")
    content = _multi(responses, "S6-Q4")
    library = _ans(responses, "S6-Q5")

    if not files and maintainer is None:
        return None

    # Hard L0: nenhum arquivo de instrução
    if any(_matches(f, "Nenhum") for f in files) or len(files) == 0:
        return 0.0

    score = 0

    # Files breadth
    n_files = sum(1 for f in files if not _matches(f, "Nenhum"))
    if n_files >= 4: score += 2
    elif n_files >= 2: score += 1.5
    elif n_files >= 1: score += 1

    # Maintainer
    if _matches(maintainer, "Time inteiro contribui"): score += 2
    elif _matches(maintainer, "1-2 pessoas dedicadas"): score += 1.5
    elif _matches(maintainer, "Eu mantenho sozinho"): score += 1
    elif _matches(maintainer, "Ninguém mantém"): score -= 1
    elif _matches(maintainer, "Não temos"): score -= 1

    # Update frequency
    if _matches(freq, "Toda semana"): score += 1
    elif _matches(freq, "Mensalmente"): score += 0.7
    elif _matches(freq, "Trimestralmente"): score += 0.4
    elif _matches(freq, "Nunca atualizo"): score -= 0.5

    # Content richness (max ~7 types)
    n_content = sum(1 for c in content if not _matches(c, "Não tenho"))
    score += min(n_content * 0.3, 2.0)

    # Prompt library shared
    if _matches(library, "Copilot Space compartilhado", "repo dedicado"): score += 1
    elif _matches(library, "wiki/Confluence"): score += 0.5
    elif _matches(library, "Não compartilhamos"): score -= 0.5

    # Map to 0-4. True attainable max is 8 (2 files + 2 maintainer + 1 freq
    # + 2 content + 1 library), so divide by 8 to keep L4 reachable.
    score = max(0, min(score, 8))
    return round(score / 8 * 4, 2)


# =========================================================
# D7 — Best Practices
# =========================================================

def score_D7(responses: dict) -> Optional[float]:
    """Usabilidade e Best Practices (L0-L4)."""
    learning = _multi(responses, "S7-Q1")
    champion = _ans(responses, "S7-Q2")
    channel = _ans(responses, "S7-Q3")
    metrics = _multi(responses, "S7-Q4")
    iterations = _ans(responses, "S7-Q5")
    sharing = _ans(responses, "S7-Q9")

    if not learning and champion is None:
        return None

    score = 0

    # Learning sources breadth
    n_sources = len(learning)
    score += min(n_sources * 0.3, 1.5)

    # Champion
    if _matches(champion, "Sim — eu sou", "Sim — outra pessoa"): score += 1.5
    elif _matches(champion, "Não, mas precisava"): score += 0
    elif _matches(champion, "Não — cada um se vira"): score -= 0.5

    # Internal channel
    if _matches(channel, "ativo (>5"): score += 1
    elif _matches(channel, "pouco ativo"): score += 0.5

    # Metrics measurement
    rich_metrics = sum(1 for m in metrics if any(
        _matches(m, k) for k in ["DORA", "DX", "SPACE", "Copilot"]
    ))
    score += min(rich_metrics * 0.5, 2.0)
    if any(_matches(m, "Não medimos") for m in metrics): score -= 1

    # Iteration efficiency (proxy for skill)
    if _matches(iterations, "Acerta na 1ª", "2-3 iterações"): score += 1
    elif _matches(iterations, "7+"): score -= 0.5

    # Sharing prompts
    if _matches(sharing, "Frequentemente"): score += 1
    elif _matches(sharing, "Às vezes"): score += 0.5
    elif _matches(sharing, "Nunca"): score -= 0.5

    # Map to 0-4 (raw range ~-2 to 8)
    score = max(0, min(score, 8))
    return round(score / 8 * 4, 2)


# =========================================================
# D8 — Security & Governance Maturity
# =========================================================
# Crítico: red flags pesam negativamente

def score_D8(responses: dict) -> Optional[float]:
    """Security & Governance Maturity (L0-L4) — critical, conservative scoring."""
    policy = _ans(responses, "S8-Q1")
    knows_data = _ans(responses, "S8-Q2")
    forbidden = _multi(responses, "S8-Q3")
    sec_tools = _multi(responses, "S8-Q4")
    scan_in_pr = _ans(responses, "S8-Q5")
    sbom = _ans(responses, "S8-Q6")
    review = _ans(responses, "S8-Q7")
    red_lines = _ans(responses, "S8-Q8")
    jit = _ans(responses, "S8-Q9")
    dlp = _ans(responses, "S8-Q10")
    audit = _ans(responses, "S8-Q11")
    training = _ans(responses, "S8-Q12")

    if policy is None and not sec_tools:
        return None

    # Hard L0: no policy (or does not know whether one exists) + no tools.
    # EN/ES synonyms cover clients that translated the answer options in Forms.
    if (_matches(policy, "Não temos política", "don't have a policy", "do not have a policy",
                 "no tenemos pol") or _matches(policy, "Não sei", "I don't know", "no lo sé")) and \
       (any(_matches(t, "Nenhuma", "None") for t in sec_tools) or not sec_tools):
        return 0.0

    score = 0

    # Policy
    if _matches(policy, "política formal e clara", "formal and clear", "formal y clara"): score += 2
    elif _matches(policy, "pouco clara"): score += 1
    elif _matches(policy, "informal"): score += 0.5

    # Knows what data can/cannot
    if _matches(knows_data, "Sei claramente"): score += 1
    elif _matches(knows_data, "Tenho ideia geral"): score += 0.5

    # Forbidden data list (good if multiple)
    n_forbidden = sum(1 for f in forbidden if not _matches(f, "Nenhuma restrição"))
    score += min(n_forbidden * 0.2, 1.0)
    if any(_matches(f, "Nenhuma restrição") for f in forbidden): score -= 1

    # Security tools breadth
    n_tools = sum(1 for t in sec_tools if not _matches(t, "Nenhuma"))
    score += min(n_tools * 0.3, 2.0)

    # Code scanning gate
    if _matches(scan_in_pr, "gate obrigatório"): score += 1
    elif _matches(scan_in_pr, "Sim — opcional"): score += 0.5

    # SBOM
    if _matches(sbom, "automatizado"): score += 0.5

    # Review process
    if _matches(review, "obrigatório por outro humano + scanner"): score += 1
    elif _matches(review, "Review humano obrigatório"): score += 0.5

    # Red-lines for agents (critical for advanced)
    if _matches(red_lines, "Sempre"): score += 1
    elif _matches(red_lines, "Frequentemente"): score += 0.5

    # JIT permissions
    if _matches(jit, "JIT obrigatório"): score += 1
    elif _matches(jit, "Sim — opcional"): score += 0.5

    # DLP
    if _matches(dlp, "bloqueia ativamente"): score += 0.5
    elif _matches(dlp, "alerta"): score += 0.25

    # Audit
    if _matches(audit, "logs ativos e revisados"): score += 0.5
    elif _matches(audit, "ativos mas não revisados"): score += 0.25

    # Training
    if _matches(training, "obrigatório anual"): score += 0.5
    elif _matches(training, "uma vez"): score += 0.25

    # Map to 0-4 (raw range ~0-12)
    score = max(0, min(score, 12))
    return round(score / 12 * 4, 2)


# =========================================================
# Public API
# =========================================================

DIMENSIONS = [
    ("D2", "Copilot Adoption", score_D2,
     "Adoção e profundidade de uso do GitHub Copilot — frequência, modos (Ask/Edit/Agent/Coding Agent), features, ganho mensurado"),
    ("D3", "MS/GH Tooling Breadth", score_D3,
     "Amplitude de uso do ecossistema Microsoft/GitHub — Foundry, Spaces, Coding Agent, MCP, Spec Kit, GHAS"),
    ("D4", "AI Dev Practices", score_D4,
     "Práticas estruturadas com IA — TDD, SDD, pair programming, debugging, onboarding"),
    ("D5", "Agent Concepts Mastery", score_D5,
     "Conhecimento de conceitos avançados — agentes, MCP, A2A, handoffs, subagentes, personas Agentic DevOps + criação de primitives + testes"),
    ("D6", "Instructions Maturity", score_D6,
     "Maturidade de instructions files — copilot-instructions.md, AGENTS.md, CLAUDE.md, manutenção, prompt library compartilhada"),
    ("D7", "Best Practices", score_D7,
     "Cultura e usabilidade — Champions, métricas DORA/DX, comunidade, compartilhamento"),
    ("D8", "Security & Governance", score_D8,
     "Política de IA, GHAS, scanners, SBOM, escopo+red-lines de agents, JIT permissions, audit, treinamento"),
]


def label_for(score: Optional[float]) -> str:
    """Maps score 0-4 to L0-L4 label (same as assessment principal)."""
    if score is None: return "Sem dados"
    if score < 0.5: return "L0 — Inicial"
    if score < 1.5: return "L1 — Em Desenvolvimento"
    if score < 2.5: return "L2 — Definido"
    if score < 3.5: return "L3 — Gerenciado"
    return "L4 — Otimizando"


def score_respondent(responses: dict) -> dict:
    """Compute all 7 dimensions for a single respondent."""
    out = {}
    for did, name, fn, _ in DIMENSIONS:
        s = fn(responses)
        out[did] = {
            "name": name,
            "score": s,
            "label": label_for(s),
        }
    # Overall: average of non-null dimensions
    valid = [d["score"] for d in out.values() if d["score"] is not None]
    overall = round(sum(valid) / len(valid), 2) if valid else None
    out["overall"] = {
        "name": "Maturidade Overall",
        "score": overall,
        "label": label_for(overall),
        "dimensions_scored": len(valid),
    }
    return out


def aggregate_team(respondent_scores: list[dict]) -> dict:
    """Aggregate individual scores into team averages and distribution."""
    n = len(respondent_scores)
    if n == 0:
        return {"error": "No respondents"}

    # Per-dimension team aggregation
    dims = {}
    for did, name, _, desc in DIMENSIONS:
        scores = [r[did]["score"] for r in respondent_scores if r[did]["score"] is not None]
        if not scores:
            dims[did] = {"name": name, "description": desc, "team_score": None, "label": "Sem dados",
                        "respondents_with_score": 0, "distribution": {}}
            continue

        avg = round(sum(scores) / len(scores), 2)
        # Distribution by L0-L4
        dist = {"L0": 0, "L1": 0, "L2": 0, "L3": 0, "L4": 0}
        for s in scores:
            if s < 0.5: dist["L0"] += 1
            elif s < 1.5: dist["L1"] += 1
            elif s < 2.5: dist["L2"] += 1
            elif s < 3.5: dist["L3"] += 1
            else: dist["L4"] += 1
        dist_pct = {k: round(100 * v / len(scores), 1) for k, v in dist.items()}

        dims[did] = {
            "name": name,
            "description": desc,
            "team_score": avg,
            "label": label_for(avg),
            "respondents_with_score": len(scores),
            "distribution_count": dist,
            "distribution_pct": dist_pct,
        }

    # Overall team score (average of all respondent overall scores)
    overalls = [r["overall"]["score"] for r in respondent_scores if r["overall"]["score"] is not None]
    team_overall = round(sum(overalls) / len(overalls), 2) if overalls else None

    return {
        "team_overall_score": team_overall,
        "team_overall_label": label_for(team_overall),
        "n_respondents": n,
        "n_with_overall": len(overalls),
        "dimensions": dims,
    }


# =========================================================
# Match-coverage guardrail
# =========================================================
# Canonical answer options per scored question (plus the EN/ES synonyms the
# scoring functions above also accept). Used by calcular_maturidade.py to
# detect answer text the rubric cannot interpret (e.g. options translated in
# Forms), which would otherwise silently deflate scores to L0/None.

COVERAGE_QUESTIONS: dict = {
    "S2-Q1": ('Sim — Copilot Enterprise',
              'Sim — Copilot Business',
              'Sim — Copilot Pro+ (individual)',
              'Sim — Copilot Pro (individual)',
              'Sim — Copilot Free',
              'Tenho licença mas não uso',
              'Não tenho licença',
              "don't have a license",
              'do not have a license',
              'no tengo licencia',
              'have a license but',
              'tengo licencia pero'),
    "S2-Q2": ('Diariamente (várias horas)',
              'Diariamente (esporádico)',
              'Semanal',
              'Raramente',
              'Nunca',
              'Daily',
              'Weekly',
              'Rarely',
              'Never',
              'Rara vez',
              'Diario'),
    "S2-Q3": ('Ask (responder perguntas)',
              'Edit (edição multi-arquivo no IDE)',
              'Agent (autônomo no IDE, executa tasks)',
              'Copilot Coding Agent (autônomo no GitHub.com — assigna issue, abre PR sozinho)',
              'Plan / Vision',
              'Não uso o Chat — só completion inline',
              'Não conheço esses modos'),
    "S2-Q5": ('Inline code completion',
              'Chat (perguntas no IDE)',
              'Pull Request descriptions automáticas',
              'Pull Request review (Copilot review)',
              'Test generation',
              'Documentation generation',
              'Issue resolution (Coding Agent assigna issue)',
              'Slash commands no Chat (/explain, /fix, /tests)',
              'Copilot Spaces (contexto compartilhado: repos + docs + custom instructions)',
              'Copilot Coding Agent (tarefas autônomas)',
              'Copilot CLI (gh copilot)'),
    "S2-Q7": ('Negativo (atrapalha)',
              'Neutro (sem ganho)',
              '+10-20%',
              '+20-40%',
              '+40-60%',
              '+60% ou mais',
              'Não sei medir'),
    "S3-Q1": ('Microsoft Foundry (ex-Azure AI Foundry)',
              'Foundry Agent Service (GA — built on OpenAI Responses API)',
              'Azure OpenAI Service (direto via API)',
              'Microsoft 365 Copilot',
              'GitHub Copilot Spaces',
              'GitHub Copilot Coding Agent (autônomo)',
              'GitHub Codespaces',
              'GitHub Models (playground multi-LLM)',
              'GitHub Advanced Security (GHAS)',
              'GitHub Actions com Copilot integration',
              'Visual Studio com Copilot avançado',
              'Nenhuma das acima'),
    "S3-Q2": ('PoC / experimentação',
              'Feature de produto em produção',
              'Embeddings / RAG',
              'Foundry Agent Service para agentes autônomos',
              'Multi-agent orchestration via MCP',
              'Fine-tuning',
              'Connectors (Dynamics, SAP, SharePoint, etc.)',
              'Não uso'),
    "S3-Q3": ('Uso ativamente em produção',
              'Já testei mas não uso recorrente',
              'Conheço mas nunca usei',
              'Não conheço'),
    "S3-Q4": ('Uso e crio Spaces para meu time',
              'Uso Spaces criados por outros',
              'Conheço mas não uso',
              'Não conheço'),
    "S3-Q6": ('Uso servidores MCP no meu workflow',
              'Configurei algum MCP server custom',
              'Conheço o conceito',
              'Não conheço'),
    "S4-Q1": ('Sempre que possível',
              'Frequentemente',
              'Às vezes',
              'Raramente',
              'Nunca',
              'Não sei o que é TDD'),
    "S4-Q2": ('Uso ativamente (com Spec Kit ou similar)',
              'Já testei em alguns projetos',
              'Conheço o conceito mas não uso',
              'Nunca ouvi falar'),
    "S4-Q3": ('Antes de começar (planejar arquitetura)',
              'Durante (autocomplete + perguntas)',
              'Após implementar (review/refactor)',
              'Quando trava (debugging)',
              'Para escrever testes',
              'Para escrever docs',
              'Para code review do meu próprio PR'),
    "S4-Q4": ('Sim — trato como par',
              'Às vezes (depende da tarefa)',
              'Não — só ferramenta de autocompletar',
              'Não uso de forma estruturada'),
    "S4-Q5": ('Toda semana',
              'Algumas vezes por mês',
              'Raramente',
              'Nunca'),
    "S4-Q7": ('Pergunto ao Copilot Chat / Claude / outro AI',
              'Procuro nos logs / debugger',
              'Pergunto a colega humano',
              'Stack Overflow / documentação',
              'Depende do bug'),
    "S4-Q8": ('Sempre — primeira coisa que faço',
              'Frequentemente',
              'Às vezes',
              'Não — leio README e código manualmente'),
    "S5-Q1": ('Sim — explico claramente',
              'Sim — vagamente',
              'Não sei a diferença',
              'Não conheço o termo'),
    "S5-Q2": ('Sim — uso conscientemente',
              'Mais ou menos',
              'Não sei a diferença'),
    "S5-Q3": ('Já criei',
              'Já usei mas não criei',
              'Sei que existem mas nunca usei',
              'Não sabia que era possível'),
    "S5-Q4": ('Conheço e uso',
              'Conheço mas não uso',
              'Não conheço'),
    "S5-Q5": ('Sim — várias',
              'Sim — uma ou duas',
              'Não, mas planejo',
              'Não conheço'),
    "S5-Q6": ('Uso (ex.: Foundry A2A Tool)',
              'Conheço o conceito',
              'Não conheço'),
    "S5-Q7": ('Uso',
              'Conheço o conceito',
              'Não conheço'),
    "S5-Q8": ('Uso',
              'Conheço o conceito',
              'Não conheço'),
    "S5-Q9": ('Sim — adoto explicitamente',
              'Conheço o conceito',
              'Não conheço'),
    "S5-Q10": ('Sempre — tenho test suite para meus agents',
              'Frequentemente — manual mas sistemático',
              'Às vezes — só sanity check',
              'Raramente / nunca',
              'Não crio agents/prompts/skills'),
    "S5-Q11": ('Custom prompts (.prompt.md)',
              'Custom skills (SKILL.md)',
              'Custom agents (.agent.md)',
              'Custom MCP server',
              'Instructions files (copilot-instructions.md / AGENTS.md / CLAUDE.md)',
              'Spaces compartilhados',
              'Nenhum dos acima'),
    "S6-Q1": ('.github/copilot-instructions.md',
              '.github/instructions/*.instructions.md',
              'AGENTS.md',
              'CLAUDE.md (raiz do projeto)',
              '.cursorrules',
              'Custom instructions em Copilot Spaces',
              'Nenhum'),
    "S6-Q2": ('Time inteiro contribui',
              '1-2 pessoas dedicadas',
              'Eu mantenho sozinho',
              'Ninguém mantém — está desatualizado',
              'Não temos'),
    "S6-Q3": ('Toda semana',
              'Mensalmente',
              'Trimestralmente',
              'Quando algo quebra',
              'Nunca atualizo'),
    "S6-Q4": ('Code style / convenções do projeto',
              'Domain knowledge (regras de negócio)',
              'Stack / ferramentas',
              'Forbidden patterns (o que NÃO fazer)',
              'Examples (good vs bad code)',
              'Estrutura de pastas / arquitetura',
              'Comandos comuns (test, build, deploy)',
              'Não tenho instruções'),
    "S6-Q5": ('Sim — Copilot Space compartilhado',
              'Sim — repo dedicado',
              'Sim — wiki/Confluence',
              'Cada um mantém o seu',
              'Não compartilhamos prompts'),
    "S7-Q1": ('Auto-aprendizado (tentativa e erro)',
              'Workshop interno da empresa',
              'Documentação oficial',
              'Vídeos do YouTube',
              'Curso online (Coursera, Udemy, MS Learn)',
              'Champion no time',
              'Eventos / conferências (Microsoft Build, GitHub Universe)',
              'Comunidades / Discord / Slack'),
    "S7-Q2": ('Sim — eu sou',
              'Sim — outra pessoa',
              'Não, mas precisava ter',
              'Não — cada um se vira'),
    "S7-Q3": ('Sim — ativo (>5 mensagens/semana)',
              'Sim — pouco ativo',
              'Não temos canal dedicado',
              'Não sei'),
    "S7-Q4": ('DORA metrics (lead time, deployment freq, MTTR, change failure)',
              'DX index (developer experience)',
              'SPACE framework',
              'Métricas de adoção do Copilot (active users)',
              'Self-report periódico (survey)',
              'Não medimos formalmente'),
    "S7-Q5": ('Acerta na 1ª tentativa',
              '2-3 iterações',
              '4-6 iterações',
              '7+ iterações (frequente)'),
    "S7-Q9": ('Frequentemente — em canal compartilhado',
              'Às vezes — pessoalmente',
              'Raramente',
              'Nunca'),
    "S8-Q1": ('Sim — política formal e clara',
              'Sim — mas pouco clara',
              'Política informal (sem documento)',
              'Não temos política',
              'Não sei',
              'formal and clear',
              'formal y clara',
              "don't have a policy",
              'do not have a policy',
              'no tenemos pol',
              "I don't know",
              'no lo sé'),
    "S8-Q2": ('Sei claramente o que pode e o que NÃO pode',
              'Tenho ideia geral',
              'Vagamente',
              'Não sei'),
    "S8-Q3": ('PII / dados pessoais de clientes',
              'Secrets / API keys / tokens',
              'Código de IP estratégico',
              'Dados financeiros',
              'Dados de saúde',
              'Nenhuma restrição (não temos política)'),
    "S8-Q4": ('GitHub Advanced Security (GHAS)',
              'CodeQL scanning',
              'Secret scanning',
              'Dependabot / dependency review',
              'SBOM (Software Bill of Materials)',
              'Microsoft Defender for DevOps',
              'Microsoft Defender for Cloud',
              'Snyk / SonarQube / outro SAST',
              'Nenhuma'),
    "S8-Q5": ('Sim — gate obrigatório no PR',
              'Sim — opcional',
              'Roda mas não bloqueia',
              'Não roda'),
    "S8-Q6": ('Sim — automatizado',
              'Sim — manual quando solicitado',
              'Não geramos',
              'Não sei'),
    "S8-Q7": ('Sim — review obrigatório por outro humano + scanner',
              'Review humano obrigatório (sem scanner extra)',
              'Review opcional',
              'Não temos processo'),
    "S8-Q8": ('Sempre — escopo + red-lines documentados',
              'Frequentemente',
              'Às vezes',
              'Raramente / nunca',
              'Não crio/uso custom agents'),
    "S8-Q9": ('Sim — JIT obrigatório para agents',
              'Sim — opcional',
              'Não temos JIT',
              'Não sei'),
    "S8-Q10": ('Sim — bloqueia ativamente',
              'Sim — alerta mas não bloqueia',
              'Não temos',
              'Não sei'),
    "S8-Q11": ('Sim — logs ativos e revisados',
              'Logs ativos mas não revisados',
              'Não temos',
              'Não sei'),
    "S8-Q12": ('Sim — treinamento obrigatório anual',
              'Sim — uma vez (no onboarding)',
              'Não recebi treinamento',
              'Não sei'),
}


def match_coverage(responses: dict) -> tuple:
    """Return (matched, answered) across the scored questions.

    A question counts as *answered* when it has a non-empty value, and as
    *matched* when at least one selected option contains a known canonical
    option string (case-insensitive substring, same rule the scorers use).
    """
    matched = 0
    answered = 0
    for qid, patterns in COVERAGE_QUESTIONS.items():
        raw = _ans(responses, qid)
        if raw is None:
            continue
        answered += 1
        parts = [p.strip() for p in raw.split(";") if p.strip()] or [raw]
        if any(_matches(part, *patterns) for part in parts):
            matched += 1
    return matched, answered
