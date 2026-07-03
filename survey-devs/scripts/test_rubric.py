#!/usr/bin/env python3
"""Permanent rubric tests for the Developer Survey (stdlib unittest, no deps).

Asserts every documented threshold in survey-devs/RUBRICA-MATURIDADE.md v1.1
against scripts/rubric.py, plus:

- regression: calcular_maturidade.py on respostas-mock-devs.json returns the
  pinned per-dimension team scores;
- match-coverage guardrail triggers on a synthetic English-answers respondent;
- RUBRIC_VERSION consistency between rubric.py, RUBRICA-MATURIDADE.md and the
  metadata written by both writers (calcular_maturidade.py, gerar_insights.py);
- the insights report derives the MCP metric from S3-Q6 (not the A2A question).

Run:
    python3 survey-devs/scripts/test_rubric.py
"""
from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import rubric  # noqa: E402
import calcular_maturidade as calc  # noqa: E402

RUBRICA_DOC = SCRIPT_DIR.parent / "RUBRICA-MATURIDADE.md"
MOCK_INPUT = SCRIPT_DIR.parent / "respostas-mock-devs.json"
FIXED_NOW = "2026-07-03T00:00:00Z"

# Pinned regression values: current output of calcular_maturidade.py on
# respostas-mock-devs.json (rubric v1.1). Update ONLY on a deliberate rubric
# change, together with a RUBRIC_VERSION bump and a changelog entry in
# RUBRICA-MATURIDADE.md.
EXPECTED_TEAM_SCORES = {
    "D2": 0.80,
    "D3": 2.40,
    "D4": 2.68,
    "D5": 2.72,
    "D6": 2.60,
    "D7": 2.91,
    "D8": 1.92,
}
EXPECTED_OVERALL = 2.29
EXPECTED_OVERALL_LABEL = "L2 — Definido"


def responses(mapping: dict) -> dict:
    """Build a responses dict in the survey JSON shape from {qid: value}."""
    return {qid: {"value": value} for qid, value in mapping.items()}


class TestScaleLabels(unittest.TestCase):
    """Level cut-points documented in the 'Escala' table."""

    def test_cut_points(self):
        self.assertEqual(rubric.label_for(None), "Sem dados")
        self.assertEqual(rubric.label_for(0.0), "L0 — Inicial")
        self.assertEqual(rubric.label_for(0.49), "L0 — Inicial")
        self.assertEqual(rubric.label_for(0.5), "L1 — Em Desenvolvimento")
        self.assertEqual(rubric.label_for(1.49), "L1 — Em Desenvolvimento")
        self.assertEqual(rubric.label_for(1.5), "L2 — Definido")
        self.assertEqual(rubric.label_for(2.49), "L2 — Definido")
        self.assertEqual(rubric.label_for(2.5), "L3 — Gerenciado")
        self.assertEqual(rubric.label_for(3.49), "L3 — Gerenciado")
        self.assertEqual(rubric.label_for(3.5), "L4 — Otimizando")
        self.assertEqual(rubric.label_for(4.0), "L4 — Otimizando")


class TestD2CopilotAdoption(unittest.TestCase):
    """D2 ladder, including the v1.1 reconciled L3 gate (daily + explicit gain)."""

    DAILY = "Diariamente (várias horas)"
    MODES_BASIC = "Ask (responder perguntas)"
    MODES_AGENT = "Ask (responder perguntas);Agent (autônomo no IDE, executa tasks)"
    MODES_CODING_AGENT = (
        "Ask (responder perguntas);"
        "Copilot Coding Agent (autônomo no GitHub.com — assigna issue, abre PR sozinho)"
    )
    FEATURES_2 = "Inline code completion;Chat (perguntas no IDE)"
    FEATURES_4 = FEATURES_2 + ";Test generation;Documentation generation"
    FEATURES_5_SPACES = (
        FEATURES_4
        + ";Copilot Spaces (contexto compartilhado: repos + docs + custom instructions)"
    )

    def test_unanswered_license_is_not_scored(self):
        self.assertIsNone(rubric.score_D2(responses({})))

    def test_hard_l0_no_license(self):
        self.assertEqual(rubric.score_D2(responses({"S2-Q1": "Não tenho licença"})), 0.0)

    def test_hard_l0_license_unused(self):
        self.assertEqual(rubric.score_D2(responses({"S2-Q1": "Tenho licença mas não uso"})), 0.0)

    def test_hard_l0_never_uses(self):
        r = responses({"S2-Q1": "Sim — Copilot Business", "S2-Q2": "Nunca"})
        self.assertEqual(rubric.score_D2(r), 0.0)

    def test_l1_rarely(self):
        r = responses({"S2-Q1": "Sim — Copilot Business", "S2-Q2": "Raramente"})
        self.assertEqual(rubric.score_D2(r), 1.0)

    def test_l2_daily_one_mode_two_features(self):
        r = responses({
            "S2-Q1": "Sim — Copilot Business",
            "S2-Q2": self.DAILY,
            "S2-Q3": self.MODES_BASIC,
            "S2-Q5": self.FEATURES_2,
        })
        self.assertEqual(rubric.score_D2(r), 2.0)

    def test_l3_requires_daily_agent_4features_positive_gain(self):
        r = responses({
            "S2-Q1": "Sim — Copilot Enterprise",
            "S2-Q2": self.DAILY,
            "S2-Q3": self.MODES_AGENT,
            "S2-Q5": self.FEATURES_4,
            "S2-Q7": "+10-20%",
        })
        self.assertEqual(rubric.score_D2(r), 3.0)

    def test_l3_gate_unanswered_gain_does_not_grant_l3(self):
        # Documented conservative note: unanswered gain caps at L2.
        r = responses({
            "S2-Q1": "Sim — Copilot Enterprise",
            "S2-Q2": self.DAILY,
            "S2-Q3": self.MODES_AGENT,
            "S2-Q5": self.FEATURES_4,
        })
        self.assertEqual(rubric.score_D2(r), 2.0)

    def test_l3_gate_nao_sei_medir_does_not_grant_l3(self):
        r = responses({
            "S2-Q1": "Sim — Copilot Enterprise",
            "S2-Q2": self.DAILY,
            "S2-Q3": self.MODES_AGENT,
            "S2-Q5": self.FEATURES_4,
            "S2-Q7": "Não sei medir",
        })
        self.assertEqual(rubric.score_D2(r), 2.0)

    def test_l3_gate_weekly_use_does_not_grant_l3(self):
        # v1.1 reconciliation: the pre-1.1 code granted L3 to weekly users;
        # the documented rule requires daily use.
        r = responses({
            "S2-Q1": "Sim — Copilot Enterprise",
            "S2-Q2": "Semanal",
            "S2-Q3": self.MODES_AGENT,
            "S2-Q5": self.FEATURES_4,
            "S2-Q7": "+20-40%",
        })
        self.assertEqual(rubric.score_D2(r), 1.0)

    def test_l4_full_ladder(self):
        r = responses({
            "S2-Q1": "Sim — Copilot Enterprise",
            "S2-Q2": "Diariamente (esporádico)",
            "S2-Q3": self.MODES_CODING_AGENT,
            "S2-Q5": self.FEATURES_5_SPACES,
            "S2-Q7": "+40-60%",
        })
        self.assertEqual(rubric.score_D2(r), 4.0)

    def test_l4_requires_daily_base(self):
        r = responses({
            "S2-Q1": "Sim — Copilot Enterprise",
            "S2-Q2": "Semanal",
            "S2-Q3": self.MODES_CODING_AGENT,
            "S2-Q5": self.FEATURES_5_SPACES,
            "S2-Q7": "+60% ou mais",
        })
        self.assertEqual(rubric.score_D2(r), 1.0)


class TestD3ToolingBreadth(unittest.TestCase):
    """D3 point score (n_tools + advanced signals) and level cut-points."""

    TOOLS = [
        "Microsoft Foundry (ex-Azure AI Foundry)",
        "Azure OpenAI Service (direto via API)",
        "GitHub Copilot Spaces",
        "GitHub Codespaces",
        "GitHub Models (playground multi-LLM)",
    ]

    def _score(self, n_tools, extra=None):
        r = {"S3-Q1": {"value": ";".join(self.TOOLS[:n_tools])}}
        r.update(responses(extra or {}))
        return rubric.score_D3(r)

    def test_no_answer_is_not_scored(self):
        self.assertIsNone(rubric.score_D3(responses({})))

    def test_nenhuma_das_acima_is_l0(self):
        self.assertEqual(rubric.score_D3(responses({"S3-Q1": "Nenhuma das acima"})), 0.0)

    def test_score_1_to_2_is_l1(self):
        self.assertEqual(self._score(1), 1.0)
        self.assertEqual(self._score(2), 1.0)

    def test_score_3_to_4_is_l2(self):
        self.assertEqual(self._score(3), 2.0)
        self.assertEqual(self._score(4), 2.0)

    def test_score_5_to_7_is_l3(self):
        self.assertEqual(self._score(5), 3.0)
        self.assertEqual(self._score(4, {"S3-Q3": "Uso ativamente em produção"}), 3.0)  # 4+1=5
        self.assertEqual(self._score(5, {
            "S3-Q3": "Uso ativamente em produção",
            "S3-Q4": "Uso e crio Spaces para meu time",
        }), 3.0)  # 5+2=7

    def test_score_8_plus_is_l4_with_all_advanced_signals(self):
        # 5 tools + 3 advanced signals (Coding Agent, Spaces, MCP) = 8.
        self.assertEqual(self._score(5, {
            "S3-Q3": "Uso ativamente em produção",
            "S3-Q4": "Uso e crio Spaces para meu time",
            "S3-Q6": "Uso servidores MCP no meu workflow",
        }), 4.0)

    def test_foundry_mcp_usage_counts_as_advanced_signal(self):
        # 4 tools + MCP answer + Foundry multi-agent usage = 6 -> L3.
        self.assertEqual(self._score(4, {
            "S3-Q6": "Configurei algum MCP server custom",
            "S3-Q2": "Multi-agent orchestration via MCP",
        }), 3.0)


class TestD4DevPractices(unittest.TestCase):
    """D4 point table (max 10 mapped to 0-4)."""

    # Neutral answer: satisfies the not-all-None guard, contributes 0 points.
    NEUTRAL = {"S4-Q4": "Não — só ferramenta de autocompletar"}

    def _score(self, extra):
        r = dict(self.NEUTRAL)
        r.update(extra)
        return rubric.score_D4(responses(r))

    def test_all_unanswered_is_not_scored(self):
        self.assertIsNone(rubric.score_D4(responses({"S4-Q3": "Para escrever testes"})))

    def test_neutral_baseline_is_zero(self):
        self.assertEqual(self._score({}), 0.0)

    def test_tdd_points(self):
        self.assertEqual(self._score({"S4-Q1": "Sempre que possível"}), 0.8)     # +2
        self.assertEqual(self._score({"S4-Q1": "Frequentemente"}), 0.6)          # +1.5
        self.assertEqual(self._score({"S4-Q1": "Às vezes"}), 0.4)                # +1
        self.assertEqual(self._score({"S4-Q1": "Não sei o que é TDD"}), 0.0)     # -1, clamped

    def test_sdd_points(self):
        self.assertEqual(self._score({"S4-Q2": "Uso ativamente (com Spec Kit ou similar)"}), 0.8)  # +2
        self.assertEqual(self._score({"S4-Q2": "Já testei em alguns projetos"}), 0.4)              # +1
        self.assertEqual(self._score({"S4-Q2": "Nunca ouvi falar"}), 0.0)                          # -0.5, clamped

    def test_moments_breadth_capped_at_2(self):
        three = "Antes de começar (planejar arquitetura);Quando trava (debugging);Para escrever testes"
        self.assertEqual(self._score({"S4-Q3": three}), 0.48)  # 3 x 0.4 = 1.2
        seven = ";".join([
            "Antes de começar (planejar arquitetura)",
            "Durante (autocomplete + perguntas)",
            "Após implementar (review/refactor)",
            "Quando trava (debugging)",
            "Para escrever testes",
            "Para escrever docs",
            "Para code review do meu próprio PR",
        ])
        self.assertEqual(self._score({"S4-Q3": seven}), 0.8)   # capped at 2.0

    def test_pair_refactor_debug_onboarding_points(self):
        self.assertEqual(rubric.score_D4(responses({"S4-Q4": "Sim — trato como par"})), 0.6)       # +1.5
        self.assertEqual(rubric.score_D4(responses({"S4-Q4": "Às vezes (depende da tarefa)"})), 0.2)  # +0.5
        self.assertEqual(self._score({"S4-Q5": "Toda semana"}), 0.4)                               # +1
        self.assertEqual(self._score({"S4-Q5": "Algumas vezes por mês"}), 0.2)                     # +0.5
        self.assertEqual(self._score({"S4-Q7": "Pergunto ao Copilot Chat / Claude / outro AI"}), 0.2)  # +0.5
        self.assertEqual(self._score({"S4-Q8": "Sempre — primeira coisa que faço"}), 0.4)          # +1
        self.assertEqual(self._score({"S4-Q8": "Frequentemente"}), 0.2)                            # +0.5


class TestD5AgentConcepts(unittest.TestCase):
    """D5 weights: 60% coverage (2.4) + 25% primitives (1.0) + 15% testing (0.6)."""

    STRONG = {
        "S5-Q1": "Sim — explico claramente",
        "S5-Q2": "Sim — uso conscientemente",
        "S5-Q3": "Já criei",
        "S5-Q4": "Conheço e uso",
        "S5-Q5": "Sim — várias",
        "S5-Q6": "Uso (ex.: Foundry A2A Tool)",
        "S5-Q7": "Uso",
        "S5-Q8": "Uso",
        "S5-Q9": "Sim — adoto explicitamente",
    }
    # 5 answered questions, none matching the deep-knowledge keywords.
    WEAK5 = {
        "S5-Q1": "Sim — vagamente",
        "S5-Q2": "Mais ou menos",
        "S5-Q3": "Sei que existem mas nunca usei",
        "S5-Q4": "Não conheço",
        "S5-Q5": "Não, mas planejo",
    }
    PRIMITIVES_4 = (
        "Custom prompts (.prompt.md);Custom skills (SKILL.md);"
        "Custom agents (.agent.md);Custom MCP server"
    )

    def test_under_5_answered_is_not_scored(self):
        four = dict(list(self.STRONG.items())[:4])
        self.assertIsNone(rubric.score_D5(responses(four)))

    def test_coverage_weight_is_2_4(self):
        self.assertEqual(rubric.score_D5(responses(self.STRONG)), 2.4)

    def test_primitives_weight_capped_at_1(self):
        r = dict(self.WEAK5)
        r["S5-Q11"] = self.PRIMITIVES_4
        self.assertEqual(rubric.score_D5(responses(r)), 1.0)  # 4 x 0.25, cap 1.0
        r["S5-Q11"] = "Custom prompts (.prompt.md);Custom skills (SKILL.md)"
        self.assertEqual(rubric.score_D5(responses(r)), 0.5)  # 2 x 0.25
        r["S5-Q11"] = "Nenhum dos acima"
        self.assertEqual(rubric.score_D5(responses(r)), 0.0)

    def test_testing_weight_is_0_6(self):
        # v1.1 reconciliation: the testing component is worth 0.6 (15% of 4.0),
        # not the pre-1.1 0.36.
        r = dict(self.WEAK5)
        r["S5-Q10"] = "Sempre — tenho test suite para meus agents"
        self.assertEqual(rubric.score_D5(responses(r)), 0.6)
        r["S5-Q10"] = "Frequentemente — manual mas sistemático"
        self.assertEqual(rubric.score_D5(responses(r)), 0.3)
        r["S5-Q10"] = "Não crio agents/prompts/skills"
        self.assertEqual(rubric.score_D5(responses(r)), 0.0)  # neutral

    def test_components_sum_to_exactly_4(self):
        r = dict(self.STRONG)
        r["S5-Q11"] = self.PRIMITIVES_4
        r["S5-Q10"] = "Sempre — tenho test suite para meus agents"
        self.assertEqual(rubric.score_D5(responses(r)), 4.0)


class TestD6InstructionsMaturity(unittest.TestCase):
    """D6 point table and the v1.1 reconciled divisor 8 (L4 reachable)."""

    FILES_1 = ".github/copilot-instructions.md"
    FILES_2 = FILES_1 + ";AGENTS.md"
    FILES_4 = FILES_2 + ";.github/instructions/*.instructions.md;CLAUDE.md (raiz do projeto)"
    CONTENT_7 = ";".join([
        "Code style / convenções do projeto",
        "Domain knowledge (regras de negócio)",
        "Stack / ferramentas",
        "Forbidden patterns (o que NÃO fazer)",
        "Examples (good vs bad code)",
        "Estrutura de pastas / arquitetura",
        "Comandos comuns (test, build, deploy)",
    ])

    def test_unanswered_is_not_scored(self):
        self.assertIsNone(rubric.score_D6(responses({})))

    def test_hard_l0_no_files(self):
        self.assertEqual(rubric.score_D6(responses({"S6-Q1": "Nenhum"})), 0.0)
        self.assertEqual(rubric.score_D6(responses({"S6-Q2": "Não temos"})), 0.0)

    def test_files_breadth_points(self):
        self.assertEqual(rubric.score_D6(responses({"S6-Q1": self.FILES_1})), 0.5)   # +1 -> 1/8*4
        self.assertEqual(rubric.score_D6(responses({"S6-Q1": self.FILES_2})), 0.75)  # +1.5
        self.assertEqual(rubric.score_D6(responses({"S6-Q1": self.FILES_4})), 1.0)   # +2

    def test_maintainer_points(self):
        base = {"S6-Q1": self.FILES_1}  # +1
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q2": "Time inteiro contribui"})), 1.5)   # +2
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q2": "1-2 pessoas dedicadas"})), 1.25)   # +1.5
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q2": "Eu mantenho sozinho"})), 1.0)      # +1
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q2": "Ninguém mantém — está desatualizado"})), 0.0)  # -1

    def test_update_frequency_points(self):
        base = {"S6-Q1": self.FILES_1}  # +1
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q3": "Toda semana"})), 1.0)       # +1
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q3": "Mensalmente"})), 0.85)      # +0.7
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q3": "Trimestralmente"})), 0.7)   # +0.4
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q3": "Nunca atualizo"})), 0.25)   # -0.5

    def test_content_and_library_points(self):
        base = {"S6-Q1": self.FILES_1}  # +1
        three = "Code style / convenções do projeto;Stack / ferramentas;Examples (good vs bad code)"
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q4": three})), 0.95)  # +0.9
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q4": self.CONTENT_7})), 1.5)  # capped +2
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q5": "Sim — repo dedicado"})), 1.0)      # +1
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q5": "Sim — wiki/Confluence"})), 0.75)   # +0.5
        self.assertEqual(rubric.score_D6(responses({**base, "S6-Q5": "Não compartilhamos prompts"})), 0.25)  # -0.5

    def test_divisor_8_makes_l4_reachable(self):
        # v1.1 reconciliation: max points = 2+2+1+2+1 = 8, divided by 8, so a
        # maxed respondent scores exactly 4.0 (the pre-1.1 /9 capped at 3.56).
        r = responses({
            "S6-Q1": self.FILES_4,                          # +2
            "S6-Q2": "Time inteiro contribui",              # +2
            "S6-Q3": "Toda semana",                         # +1
            "S6-Q4": self.CONTENT_7,                        # +2 (capped)
            "S6-Q5": "Sim — Copilot Space compartilhado",   # +1
        })
        self.assertEqual(rubric.score_D6(r), 4.0)


class TestD7BestPractices(unittest.TestCase):
    """D7 point table, divisor 8."""

    LEARNING_5 = ";".join([
        "Auto-aprendizado (tentativa e erro)",
        "Workshop interno da empresa",
        "Documentação oficial",
        "Champion no time",
        "Comunidades / Discord / Slack",
    ])
    METRICS_4 = ";".join([
        "DORA metrics (lead time, deployment freq, MTTR, change failure)",
        "DX index (developer experience)",
        "SPACE framework",
        "Métricas de adoção do Copilot (active users)",
    ])

    def test_unanswered_is_not_scored(self):
        self.assertIsNone(rubric.score_D7(responses({})))

    def test_champion_points(self):
        one_source = {"S7-Q1": "Documentação oficial"}  # +0.3
        self.assertEqual(rubric.score_D7(responses({**one_source, "S7-Q2": "Sim — eu sou"})), 0.9)         # +1.5
        self.assertEqual(rubric.score_D7(responses({**one_source, "S7-Q2": "Sim — outra pessoa"})), 0.9)   # +1.5
        self.assertEqual(rubric.score_D7(responses({**one_source, "S7-Q2": "Não, mas precisava ter"})), 0.15)  # +0
        self.assertEqual(rubric.score_D7(responses({**one_source, "S7-Q2": "Não — cada um se vira"})), 0.0)    # -0.5, clamped

    def test_channel_metrics_iterations_sharing_points(self):
        base = {"S7-Q2": "Não, mas precisava ter"}  # 0 points, satisfies guard
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q3": "Sim — ativo (>5 mensagens/semana)"})), 0.5)  # +1
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q3": "Sim — pouco ativo"})), 0.25)                 # +0.5
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q4": self.METRICS_4})), 1.0)                       # +2 (4 x 0.5)
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q4": "Não medimos formalmente"})), 0.0)            # -1, clamped
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q5": "2-3 iterações"})), 0.5)                      # +1
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q5": "7+ iterações (frequente)"})), 0.0)           # -0.5, clamped
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q9": "Frequentemente — em canal compartilhado"})), 0.5)  # +1
        self.assertEqual(rubric.score_D7(responses({**base, "S7-Q9": "Nunca"})), 0.0)                              # -0.5, clamped

    def test_divisor_8_makes_l4_reachable(self):
        r = responses({
            "S7-Q1": self.LEARNING_5,                            # +1.5 (capped)
            "S7-Q2": "Sim — eu sou",                             # +1.5
            "S7-Q3": "Sim — ativo (>5 mensagens/semana)",        # +1
            "S7-Q4": self.METRICS_4,                             # +2 (capped)
            "S7-Q5": "Acerta na 1ª tentativa",                   # +1
            "S7-Q9": "Frequentemente — em canal compartilhado",  # +1
        })
        self.assertEqual(rubric.score_D7(r), 4.0)


class TestD8SecurityGovernance(unittest.TestCase):
    """D8 point table, hard L0 (including 'Não sei'), divisor 12."""

    FORBIDDEN_5 = ";".join([
        "PII / dados pessoais de clientes",
        "Secrets / API keys / tokens",
        "Código de IP estratégico",
        "Dados financeiros",
        "Dados de saúde",
    ])
    TOOLS_7 = ";".join([
        "GitHub Advanced Security (GHAS)",
        "CodeQL scanning",
        "Secret scanning",
        "Dependabot / dependency review",
        "SBOM (Software Bill of Materials)",
        "Microsoft Defender for DevOps",
        "Snyk / SonarQube / outro SAST",
    ])

    def test_unanswered_is_not_scored(self):
        self.assertIsNone(rubric.score_D8(responses({})))

    def test_hard_l0_no_policy_and_no_tools(self):
        r = responses({"S8-Q1": "Não temos política", "S8-Q4": "Nenhuma"})
        self.assertEqual(rubric.score_D8(r), 0.0)

    def test_hard_l0_includes_nao_sei(self):
        # Documented in the v1.1 changelog: not knowing whether a policy
        # exists is conservatively equivalent to not having one.
        self.assertEqual(rubric.score_D8(responses({"S8-Q1": "Não sei"})), 0.0)

    def test_policy_points(self):
        self.assertEqual(rubric.score_D8(responses({"S8-Q1": "Sim — política formal e clara"})), 0.67)  # +2
        self.assertEqual(rubric.score_D8(responses({"S8-Q1": "Sim — mas pouco clara"})), 0.33)          # +1
        self.assertEqual(rubric.score_D8(responses({"S8-Q1": "Política informal (sem documento)"})), 0.17)  # +0.5

    def test_forbidden_data_points_and_penalty(self):
        base = {"S8-Q1": "Sim — política formal e clara"}  # +2
        r = responses({**base, "S8-Q3": self.FORBIDDEN_5})
        self.assertEqual(rubric.score_D8(r), 1.0)  # +1.0 (5 x 0.2) -> 3/12*4
        r = responses({**base, "S8-Q3": "Nenhuma restrição (não temos política)"})
        self.assertEqual(rubric.score_D8(r), 0.33)  # -1 -> 1/12*4

    def test_individual_signal_points(self):
        base = {"S8-Q1": "Sim — mas pouco clara"}  # +1 baseline = 0.33
        cases = [
            ("S8-Q2", "Sei claramente o que pode e o que NÃO pode", 1.0),   # +1
            ("S8-Q2", "Tenho ideia geral", 0.5),                            # +0.5
            ("S8-Q5", "Sim — gate obrigatório no PR", 1.0),                 # +1
            ("S8-Q6", "Sim — automatizado", 0.5),                           # +0.5
            ("S8-Q7", "Sim — review obrigatório por outro humano + scanner", 1.0),  # +1
            ("S8-Q8", "Sempre — escopo + red-lines documentados", 1.0),     # +1
            ("S8-Q9", "Sim — JIT obrigatório para agents", 1.0),            # +1
            ("S8-Q10", "Sim — bloqueia ativamente", 0.5),                   # +0.5
            ("S8-Q11", "Sim — logs ativos e revisados", 0.5),               # +0.5
            ("S8-Q12", "Sim — treinamento obrigatório anual", 0.5),         # +0.5
        ]
        for qid, answer, points in cases:
            with self.subTest(qid=qid, answer=answer):
                score = rubric.score_D8(responses({**base, qid: answer}))
                self.assertEqual(score, round((1 + points) / 12 * 4, 2))

    def test_divisor_12_makes_l4_reachable(self):
        r = responses({
            "S8-Q1": "Sim — política formal e clara",                    # +2
            "S8-Q2": "Sei claramente o que pode e o que NÃO pode",       # +1
            "S8-Q3": self.FORBIDDEN_5,                                   # +1 (capped)
            "S8-Q4": self.TOOLS_7,                                       # +2 (capped)
            "S8-Q5": "Sim — gate obrigatório no PR",                     # +1
            "S8-Q6": "Sim — automatizado",                               # +0.5
            "S8-Q7": "Sim — review obrigatório por outro humano + scanner",  # +1
            "S8-Q8": "Sempre — escopo + red-lines documentados",         # +1
            "S8-Q9": "Sim — JIT obrigatório para agents",                # +1
            "S8-Q10": "Sim — bloqueia ativamente",                       # +0.5
            "S8-Q11": "Sim — logs ativos e revisados",                   # +0.5
            "S8-Q12": "Sim — treinamento obrigatório anual",             # +0.5
        })
        self.assertEqual(rubric.score_D8(r), 4.0)


class TestMatchCoverageGuardrail(unittest.TestCase):
    """Guardrail: English (translated) answer options must trigger abort <40%."""

    # Ten scored questions answered in English, none matching the canonical
    # PT-BR options nor the EN/ES synonyms rubric.py accepts.
    ENGLISH_RESPONSES = {
        "S2-Q1": "Yes - Copilot Business",
        "S2-Q2": "Every day (several hours)",
        "S2-Q3": "Ask (answer questions)",
        "S2-Q5": "Unit test creation",
        "S4-Q1": "Whenever possible",
        "S5-Q4": "I know and use it",
        "S6-Q2": "Whole team contributes",
        "S7-Q2": "Yes - I am the champion",
        "S8-Q1": "Yes - formal and documented policy",
        "S8-Q2": "I know exactly what is allowed",
    }

    def test_english_answers_have_zero_match_coverage(self):
        matched, answered = rubric.match_coverage(responses(self.ENGLISH_RESPONSES))
        self.assertEqual(answered, len(self.ENGLISH_RESPONSES))
        self.assertEqual(matched, 0)

    def test_guardrail_aborts_below_40_pct_and_force_overrides(self):
        respondents = [{"responses": responses(self.ENGLISH_RESPONSES)}]
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertFalse(calc.check_coverage_guardrail(respondents, force=False))
            self.assertTrue(calc.check_coverage_guardrail(respondents, force=True))

    def test_canonical_mock_answers_pass_the_guardrail(self):
        data = json.loads(MOCK_INPUT.read_text(encoding="utf-8"))
        respondents = data["respondents"]
        stats = calc.coverage_stats(respondents)
        self.assertGreaterEqual(stats["avg_pct"], calc.COVERAGE_WARN_PCT)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(calc.check_coverage_guardrail(respondents, force=False))


class TestRubricVersionConsistency(unittest.TestCase):
    """RUBRIC_VERSION must agree between rubric.py, the doc and both writers."""

    def test_doc_declares_the_same_version(self):
        doc = RUBRICA_DOC.read_text(encoding="utf-8")
        self.assertIn(f"**Versão da rubrica:** {rubric.RUBRIC_VERSION}", doc)

    def test_shared_metadata_builder_embeds_the_version(self):
        data = json.loads(MOCK_INPUT.read_text(encoding="utf-8"))
        team = rubric.aggregate_team(
            [rubric.score_respondent(r.get("responses", {})) for r in data["respondents"]]
        )
        out = calc.build_maturity_output(data["respondents"], team, MOCK_INPUT,
                                         computed_at=FIXED_NOW)
        self.assertEqual(out["metadata"]["rubric_version"],
                         f"{rubric.RUBRIC_VERSION} (deterministic)")


class TestPipelineRegression(unittest.TestCase):
    """End-to-end pins: both writers on respostas-mock-devs.json."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        out = Path(cls.tmp.name)
        for script in ("calcular_maturidade.py", "gerar_insights.py"):
            proc = subprocess.run(
                [sys.executable, str(SCRIPT_DIR / script),
                 "--input", str(MOCK_INPUT),
                 "--out", str(out / script.replace(".py", "")),
                 "--now", FIXED_NOW],
                capture_output=True, text=True, cwd=str(KIT_ROOT), timeout=120,
            )
            if proc.returncode != 0:
                raise AssertionError(f"{script} failed:\n{proc.stdout}\n{proc.stderr}")
        cls.calc_json = json.loads(
            (out / "calcular_maturidade" / "maturidade-developer-survey-2026-07-03.json")
            .read_text(encoding="utf-8"))
        cls.insights_json = json.loads(
            (out / "gerar_insights" / "maturidade-developer-survey-2026-07-03.json")
            .read_text(encoding="utf-8"))
        cls.insights_md = (
            (out / "gerar_insights" / "insights-developer-survey-2026-07-03.md")
            .read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_pinned_per_dimension_team_scores(self):
        dims = self.calc_json["dimensions"]
        for did, expected in EXPECTED_TEAM_SCORES.items():
            with self.subTest(dimension=did):
                self.assertAlmostEqual(dims[did]["team_score"], expected, places=2)

    def test_pinned_team_overall(self):
        overall = self.calc_json["team_overall"]
        self.assertAlmostEqual(overall["score"], EXPECTED_OVERALL, places=2)
        self.assertEqual(overall["label"], EXPECTED_OVERALL_LABEL)

    def test_both_writers_stamp_the_rubric_version(self):
        expected = f"{rubric.RUBRIC_VERSION} (deterministic)"
        self.assertEqual(self.calc_json["metadata"]["rubric_version"], expected)
        self.assertEqual(self.insights_json["metadata"]["rubric_version"], expected)
        self.assertIn(f"**Versão da rubrica:** {rubric.RUBRIC_VERSION}", self.insights_md)

    def test_both_writers_agree_on_the_maturity_output(self):
        self.assertEqual(self.calc_json["dimensions"], self.insights_json["dimensions"])
        self.assertEqual(self.calc_json["team_overall"], self.insights_json["team_overall"])

    def test_mcp_metric_derives_from_s3_q6_not_a2a(self):
        # Audit fix: MCP awareness must come from the real MCP question
        # (S3-Q6), tolerantly matched; A2A (S5-Q6) stays a separate metric.
        data = json.loads(MOCK_INPUT.read_text(encoding="utf-8"))
        respondents = data["respondents"]
        n = len(respondents)

        def pct_matching(qid, *patterns):
            total = 0
            for r in respondents:
                raw = str(r.get("responses", {}).get(qid, {}).get("value", "") or "")
                parts = [p.strip() for p in raw.split(";") if p.strip()]
                if any(rubric._matches(part, *patterns) for part in parts):
                    total += 1
            return round(100 * total / n, 1)

        pct_mcp = pct_matching("S3-Q6", "Uso servidores MCP", "Configurei algum MCP",
                               "Conheço o conceito")
        pct_a2a = pct_matching("S5-Q6", "Uso (ex", "Conheço o conceito")
        self.assertIn(f"{pct_mcp:.0f}% conhece MCP (S3-Q6)", self.insights_md)
        self.assertIn(f"{pct_a2a:.0f}% conhece A2A (S5-Q6)", self.insights_md)


if __name__ == "__main__":
    unittest.main(verbosity=2)
