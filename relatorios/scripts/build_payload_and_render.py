#!/usr/bin/env python3
"""Build payload from kit data and render the 5 PDF reports.

Strategy: use sample_payload.json as the BASE STRUCTURE (provides all the
nested fields the Jinja2 templates expect — scoring_rationale, h1_initiatives,
technology_resources_per_pillar, success_metrics_per_pillar, risks_per_pillar,
horizons narrative, three_horizons technologies, branding, etc.) and OVERWRITE
only the fields we have real client data for:
  - organization (from respostas.json)
  - assessment.id / assessment.completed_date / generated_date
  - scores.overall.weighted_avg / level_label / gap
  - scores.pillars[].weighted_avg / level_label / gap
  - capabilities[].current_score / current_level_label / gap (matched by id)
  - gap_analysis[] (rebuilt from gaps.json, structure mirrors sample)
  - implementation_guide_inputs (from implementation-guide-inputs.json;
    when client data exists, the fictional sample people are ALWAYS dropped)

Fields we DON'T have client data for (h1_initiatives, scoring_rationale,
risks, technology recommendations, etc.) keep the rich sample placeholders —
client can edit saida/payload.json and re-render to personalize them.

All human-visible labels (maturity levels, priorities, default gap actions)
are resolved from relatorios/i18n/<locale>.json so EN/ES reports contain no
Portuguese leakage.

Usage:
    python3 build_payload_and_render.py
    python3 build_payload_and_render.py --kit /path/to/kit-cliente
    python3 build_payload_and_render.py --no-render    # only build payload
    python3 build_payload_and_render.py --html-only    # skip PDF conversion (no weasyprint needed)
    python3 build_payload_and_render.py --allow-sample # demo run with fictional Acme data
    python3 build_payload_and_render.py --date 2026-05-08  # reproducible generated_date
"""
from __future__ import annotations

import argparse
import copy
import datetime
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

# Local imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
import branding  # noqa: E402

DEFAULT_TARGET = 3.0
LOCALES = ("en", "es", "pt-br")

# Priority code -> token the templates expect. priority_badge() renders
# t('priority.' ~ value|lower), so these must match the i18n keys
# priority.critical / priority.high / priority.medium / priority.low.
PRIORITY_TOKEN_BY_CODE = {"P0": "CRITICAL", "P1": "HIGH", "P2": "MEDIUM", "P3": "LOW"}

# The 9 wizard fields that roadmap_part4.html.j2 actually reads
# (via `{% set wiz = implementation_guide_inputs %}`).
WIZARD_KEYS = (
    "executive_steering_committee",
    "tpo",
    "raci_matrix",
    "communication_plan",
    "training_plan",
    "adkar_notes",
    "quick_wins_w1_4",
    "quick_wins_w5_8",
    "quick_wins_w9_12",
)


class PipelineError(Exception):
    """User-facing pipeline error: printed as a single actionable line."""


def fail(msg: str) -> None:
    raise PipelineError(msg)


def load_json(path: Path, hint: str = ""):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"{path}: arquivo não encontrado.{' ' + hint if hint else ''}")
    except json.JSONDecodeError as exc:
        fail(f"{path}: JSON inválido (linha {exc.lineno}): {exc.msg}")


# ─── i18n-aware labels ────────────────────────────────────────────

def load_strings(kit: Path, locale: str) -> dict:
    return load_json(kit / f"relatorios/i18n/{locale}.json",
                     hint="Catálogo i18n do kit ausente ou movido.")


def catalog_string(strings: dict, key: str, locale: str) -> str:
    value = strings.get(key)
    if not isinstance(value, str):
        fail(f"relatorios/i18n/{locale}.json: chave i18n ausente '{key}' "
             f"— atualize o catálogo (as 3 línguas devem ter as mesmas chaves).")
    return value


def level_from_score(score: float) -> int:
    if score < 0.5:
        return 0
    if score < 1.5:
        return 1
    if score < 2.5:
        return 2
    if score < 3.5:
        return 3
    return 4


def label_from_score(score: float | None, strings: dict, locale: str) -> str:
    """Localized maturity label, e.g. 'L2 (AI-Enhanced)' / 'L2 (Aprimorado por IA)'."""
    if score is None:
        return catalog_string(strings, "level.no_response", locale)
    lvl = level_from_score(score)
    return f"L{lvl} ({catalog_string(strings, f'level.L{lvl}.name', locale)})"


def priority_code_from_ps(ps: float) -> str:
    if ps >= 2.4:
        return "P0"
    if ps >= 1.6:
        return "P1"
    if ps >= 0.9:
        return "P2"
    return "P3"


def pe_level_from_score(score: float) -> str:
    """PE Readiness verdict. Values are CSS-coupled tokens (the template derives
    .pe-readiness__verdict-pill--low/--medium/--high from them), matching
    sample_payload.json, so they stay in English for every locale."""
    if score >= 3.0:
        return "HIGH"
    if score >= 2.0:
        return "MEDIUM"
    return "LOW"


# ─── Input validation ─────────────────────────────────────────────

def _require_field(data, dotted: str, path: Path, skill: str) -> None:
    cur = data
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            fail(f"{path}: campo obrigatório ausente '{dotted}' — rode {skill} primeiro.")
        cur = cur[part]


def validate_scores(scores: dict, path: Path) -> None:
    skill = "a skill /calcular-scores (ou /pipeline-completo)"
    _require_field(scores, "overall.score", path, skill)
    if not isinstance(scores.get("pillars"), list):
        fail(f"{path}: campo obrigatório ausente 'pillars' (lista) — rode {skill} primeiro.")
    for i, pillar in enumerate(scores["pillars"]):
        for field in ("id", "score"):
            if field not in pillar:
                fail(f"{path}: pillars[{i}] sem campo '{field}' — rode {skill} primeiro.")
    for i, cap in enumerate(scores.get("capabilities", [])):
        if "id" not in cap:
            fail(f"{path}: capabilities[{i}] sem campo 'id' — rode {skill} primeiro.")


def validate_gaps(gaps: dict, path: Path) -> None:
    skill = "a skill /gap-analysis (ou /pipeline-completo)"
    if not isinstance(gaps.get("gaps"), list):
        fail(f"{path}: campo obrigatório ausente 'gaps' (lista) — rode {skill} primeiro.")
    required = ("capability_id", "capability_name_pt_br", "pillar_id",
                "current_score", "target_level", "gap_size", "priority")
    for i, gap in enumerate(gaps["gaps"]):
        for field in required:
            if field not in gap:
                fail(f"{path}: gaps[{i}] sem campo '{field}' — rode {skill} primeiro.")


def validate_recomendacoes(recs: dict, path: Path) -> None:
    if not isinstance(recs.get("ranked_strategies"), list):
        fail(f"{path}: campo obrigatório ausente 'ranked_strategies' (lista) "
             f"— rode a skill /recomendar-estrategias primeiro.")


def validate_wizard_file(ig: dict, path: Path) -> None:
    if not isinstance(ig.get("implementation_guide_inputs"), dict):
        fail(f"{path}: campo obrigatório ausente 'implementation_guide_inputs' (objeto) "
             f"— gere o arquivo com wizard/implementation-guide-wizard.html ou "
             f"wizard/scripts/auto_fill_from_plano.py.")


# ─── Payload build ────────────────────────────────────────────────

def build_payload(kit: Path, *, allow_sample: bool, locale_override: str | None,
                  generated_date: str) -> dict:
    """Merge sample_payload.json (structure) with client data (overrides)."""
    sample = load_json(kit / "relatorios/sample_payload.json",
                       hint="O kit precisa de relatorios/sample_payload.json como estrutura base.")
    payload = copy.deepcopy(sample)
    _merge_branding(payload)

    scores_path = kit / "saida/scores.json"
    if not scores_path.exists():
        if not allow_sample:
            fail("saida/scores.json não encontrado — rode /pipeline-completo (ou /calcular-scores) "
                 "primeiro, ou use --allow-sample para gerar relatórios de DEMONSTRAÇÃO "
                 "com dados fictícios (Acme Insurance Group).")
        _print_sample_banner("saida/scores.json ausente: TODOS os dados são fictícios (sample Acme).")
        if locale_override:
            payload["locale"] = locale_override
        payload["assessment"]["generated_date"] = generated_date
        _attach_cross_survey(payload, kit)
        return payload

    respostas, scores, gaps = _load_client_pipeline_data(kit, allow_sample)
    meta = respostas.get("metadata", {})

    _apply_locale(payload, meta, locale_override)
    strings = load_strings(kit, payload["locale"])
    cap_names = _load_capability_names(kit)

    _apply_organization(payload, meta)
    _apply_assessment(payload, scores, meta, generated_date)
    _apply_overall_scores(payload, scores, strings)
    _apply_pillar_scores(payload, scores, strings)
    _apply_pe_readiness(payload, scores)
    _apply_capability_scores(payload, scores, respostas, strings, cap_names)
    _apply_gap_analysis(payload, gaps, strings, cap_names)
    _merge_implementation_guide_inputs(payload, kit / "implementation-guide-inputs.json")
    _attach_cross_survey(payload, kit)

    return payload


def _print_sample_banner(detail: str) -> None:
    line = "!" * 72
    print(line)
    print("!!  ATENÇÃO: DADOS DE EXEMPLO EM USO (--allow-sample)")
    print(f"!!  {detail}")
    print("!!  NÃO entregue estes relatórios a um cliente real.")
    print(line)
    print()


def _merge_branding(payload: dict) -> None:
    """Inject only the branding keys the templates consume.

    Templates read branding.platform_name (kept from sample_payload.json) and
    the palette primary color. Personal signature strings (author, contact)
    intentionally stay OUT of the payload: NFR-REPORT-011 bans them from
    client deliverables; they live centralized in branding.py for the
    markdown/JSON artifacts that do sign outputs.
    """
    payload.setdefault("branding", {}).update({
        "primary_color": branding.MS_BLUE,
        "design_system": branding.DESIGN_SYSTEM,
    })


def _load_client_pipeline_data(kit: Path, allow_sample: bool) -> tuple[dict, dict, dict]:
    respostas_path = kit / "respostas.json"
    scores_path = kit / "saida/scores.json"
    gaps_path = kit / "saida/gaps.json"
    recomendacoes_path = kit / "saida/recomendacoes.json"

    if not respostas_path.exists():
        if not allow_sample:
            fail("respostas.json não encontrado — sem ele o relatório sairia com o nome da "
                 "organização fictícia 'Acme Insurance Group'. Copie/gere respostas.json na raiz "
                 "do kit, ou use --allow-sample para aceitar os metadados de exemplo.")
        _print_sample_banner("respostas.json ausente: nome da organização e metadados "
                             "virão do sample (Acme Insurance Group).")
        respostas: dict = {}
    else:
        respostas = load_json(respostas_path)

    scores = load_json(scores_path)
    validate_scores(scores, scores_path)

    if gaps_path.exists():
        gaps = load_json(gaps_path)
        validate_gaps(gaps, gaps_path)
    else:
        gaps = {"gaps": [], "summary": {}}

    # recomendacoes.json is not merged into the payload (yet), but if present
    # it must be well-formed — catching a broken pipeline before rendering.
    if recomendacoes_path.exists():
        validate_recomendacoes(load_json(recomendacoes_path), recomendacoes_path)

    return respostas, scores, gaps


def _apply_locale(payload: dict, meta: dict, locale_override: str | None) -> None:
    if locale_override:
        payload["locale"] = locale_override
        return
    locale = meta.get("language", "pt-br").lower().replace("_", "-")
    if locale not in LOCALES:
        locale = "pt-br"
    payload["locale"] = locale


def _apply_organization(payload: dict, meta: dict) -> None:
    org = payload["organization"]
    org["name"] = meta.get("organization") or org["name"]
    if meta.get("respondent_role"):
        org["primary_contact_role"] = meta["respondent_role"]


def _apply_assessment(payload: dict, scores: dict, meta: dict, generated_date: str) -> None:
    assess = payload["assessment"]
    assess["id"] = scores.get("metadata", {}).get("respondent", assess.get("id", "—"))
    assess["completed_date"] = meta.get("assessment_date", assess["completed_date"])
    assess["generated_date"] = generated_date
    assess["framework_version"] = scores.get("metadata", {}).get(
        "framework_version", assess["framework_version"]
    )


def _apply_overall_scores(payload: dict, scores: dict, strings: dict) -> None:
    locale = payload["locale"]
    overall_score = scores["overall"]["score"]
    payload["scores"]["overall"]["weighted_avg"] = round(overall_score, 2)
    payload["scores"]["overall"]["level_label"] = label_from_score(overall_score, strings, locale)
    target_overall = payload["scores"]["overall"].get("target", 3.0)
    payload["scores"]["overall"]["gap"] = max(0, round(target_overall - overall_score, 2))


def _apply_pillar_scores(payload: dict, scores: dict, strings: dict) -> None:
    locale = payload["locale"]
    sample_pillars_by_id = {p["id"]: p for p in payload["scores"]["pillars"]}
    for p_client in scores.get("pillars", []):
        pid = p_client["id"]
        sample_p = sample_pillars_by_id.get(pid)
        if not sample_p:
            continue
        sample_p["weighted_avg"] = round(p_client["score"], 2)
        sample_p["level_label"] = label_from_score(p_client["score"], strings, locale)
        target = sample_p.get("target", 3.0)
        sample_p["gap"] = max(0, round(target - p_client["score"], 2))


def _apply_pe_readiness(payload: dict, scores: dict) -> None:
    pe_score = scores["overall"].get("pe_score")
    if pe_score is not None:
        payload["scores"]["pe_readiness"]["weighted_score"] = round(pe_score, 2)
        payload["scores"]["pe_readiness"]["level"] = pe_level_from_score(pe_score)


def _load_capability_names(kit: Path) -> dict:
    """Capability id -> localized names from framework.json (the single source
    of truth for capability naming: 'name' is EN, 'name_pt_br' is PT-BR).
    sample_payload.json's capability names diverge from the framework, so
    client scores must NOT be displayed under the sample names."""
    path = kit / "framework.json"
    if not path.exists():
        return {}
    fw = load_json(path)
    names: dict = {}
    for pillar in fw.get("pillars", []):
        for cap in pillar.get("capabilities", []):
            names[cap.get("id")] = {
                "name": cap.get("name"),
                "name_pt_br": cap.get("name_pt_br"),
            }
    return names


def _capability_display_name(cap_names: dict, cid: str, locale: str,
                             fallback: str | None = None) -> str | None:
    entry = cap_names.get(cid) or {}
    if locale == "pt-br":
        return entry.get("name_pt_br") or fallback or entry.get("name")
    # framework.json carries EN + PT-BR names only; ES reports use the EN name
    # (better than leaking Portuguese into an otherwise-Spanish report).
    return entry.get("name") or fallback or entry.get("name_pt_br")


def _apply_capability_scores(payload: dict, scores: dict, respostas: dict, strings: dict,
                             cap_names: dict) -> None:
    target_overrides = respostas.get("target_overrides", {})
    sample_caps_by_id = {c.get("id") or c.get("code"): c for c in payload["capabilities"]}
    for c_client in scores.get("capabilities", []):
        sample_c = sample_caps_by_id.get(c_client["id"])
        if sample_c:
            _apply_single_capability_score(sample_c, c_client, target_overrides,
                                           strings, payload["locale"], cap_names)


def _apply_single_capability_score(sample_c: dict, c_client: dict, target_overrides: dict,
                                   strings: dict, locale: str, cap_names: dict) -> None:
    cid = c_client["id"]
    display_name = _capability_display_name(cap_names, cid, locale)
    if display_name:
        sample_c["name"] = display_name
    score = c_client.get("score")
    sample_c["current_score"] = round(score, 2) if score is not None else 0.0
    sample_c["current_level_label"] = label_from_score(score, strings, locale)
    target = target_overrides.get(cid, DEFAULT_TARGET)
    sample_c["target_score"] = round(float(target), 2)
    sample_c["target_level_label"] = label_from_score(float(target), strings, locale)
    if score is None:
        sample_c["gap"] = 0
        sample_c["gap_priority"] = PRIORITY_TOKEN_BY_CODE["P3"]
        return
    sample_c["gap"] = max(0, round(target - score, 2))
    ps = c_client.get("weight", 1.0) * (target - score)
    sample_c["gap_priority"] = PRIORITY_TOKEN_BY_CODE[priority_code_from_ps(ps)]


def _apply_gap_analysis(payload: dict, gaps: dict, strings: dict, cap_names: dict) -> None:
    new_gap_analysis = [
        _gap_payload_entry(payload, gap, strings, cap_names)
        for gap in gaps.get("gaps", [])
    ]
    if new_gap_analysis:
        payload["gap_analysis"] = new_gap_analysis


def _gap_payload_entry(payload: dict, gap: dict, strings: dict, cap_names: dict) -> dict:
    locale = payload["locale"]
    existing = next(
        (item for item in payload["gap_analysis"]
         if item.get("capability_code") == gap["capability_id"]),
        None,
    )
    recommended_actions = (
        existing.get("recommended_actions", {})
        if existing
        else {
            "h1": catalog_string(strings, "gap.default_action.h1", locale),
            "h2": catalog_string(strings, "gap.default_action.h2", locale),
            "h3": catalog_string(strings, "gap.default_action.h3", locale),
        }
    )
    # gaps.json carries 'P0 — Crítico' style labels; keep only the code and map
    # it to the token the templates localize via t('priority.*').
    priority_code = str(gap["priority"]).split(" ")[0]
    return {
        "pillar_id": gap["pillar_id"],
        "capability_code": gap["capability_id"],
        "capability_name": _capability_display_name(
            cap_names, gap["capability_id"], locale,
            fallback=gap["capability_name_pt_br"],
        ),
        "current": round(gap["current_score"], 2),
        "target": round(gap["target_level"], 2),
        "gap": round(gap["gap_size"], 2),
        "priority": PRIORITY_TOKEN_BY_CODE.get(priority_code, priority_code),
        "recommended_actions": recommended_actions,
    }


# ─── Wizard (implementation-guide-inputs.json) merge ──────────────

def _merge_implementation_guide_inputs(payload: dict, ig_path: Path) -> None:
    """Merge client wizard data into the EXACT keys roadmap_part4.html.j2 reads.

    The wizard (HTML and auto_fill_from_plano.py) exports free-form markdown
    strings; the template expects structured values (lists of dicts, dict,
    lists of strings). Convert each field accordingly. Whenever client scores
    exist, the fictional sample people (Maria Santos, Carlos Rivera, ...) are
    dropped: fields without client data render the template placeholders.
    """
    merged_inputs: dict = {}

    if not ig_path.exists():
        payload["implementation_guide_inputs"] = merged_inputs
        print("ℹ️ implementation-guide-inputs.json não encontrado — a Parte 4 usará placeholders.")
        print("   Preencha com wizard/implementation-guide-wizard.html para personalizar.\n")
        return

    ig = load_json(ig_path)
    validate_wizard_file(ig, ig_path)
    wizard_inputs = ig["implementation_guide_inputs"]

    merged, placeholders, unconsumable, ignored = [], [], [], []
    for key, value in wizard_inputs.items():
        if key not in WIZARD_KEYS:
            ignored.append(key)
            continue
        converted, status = _convert_wizard_value(key, value)
        if status is None:
            placeholders.append(key)
        elif status:
            merged_inputs[key] = converted
            merged.append(key)
        else:
            unconsumable.append(key)

    payload["implementation_guide_inputs"] = merged_inputs

    pct = ig.get("metadata", {}).get("completion_pct", 0)
    print(f"✓ Merged implementation-guide-inputs.json ({pct}% completo)")
    if merged:
        print(f"  Campos aplicados ao relatório: {', '.join(merged)}")
    if placeholders:
        print(f"  Campos vazios/pendentes (placeholder no PDF): {', '.join(placeholders)}")
    if ignored:
        print(f"  Campos desconhecidos ignorados: {', '.join(ignored)}")

    if unconsumable:
        line = "!" * 72
        print(line, file=sys.stderr)
        print("!!  AVISO: campos do wizard NÃO puderam ser aproveitados no relatório:",
              file=sys.stderr)
        for key in unconsumable:
            print(f"!!    - {key}", file=sys.stderr)
        print("!!  Reformate-os (tabelas RACI/comunicação/treinamento em markdown table)",
              file=sys.stderr)
        print("!!  ou edite saida/payload.json manualmente e re-renderize.", file=sys.stderr)
        print(line, file=sys.stderr)

    if not merged and unconsumable:
        fail("implementation-guide-inputs.json contém dados, mas NENHUM campo pôde ser "
             "aproveitado no relatório — corrija o formato dos campos listados acima.")
    print()


def _is_placeholder_text(text: str) -> bool:
    """auto_fill_from_plano.py marks unfilled fields with '(preencher ...)'."""
    s = text.strip()
    return not s or s.lower().startswith("(preencher")


def _strip_bullet(line: str) -> str:
    for prefix in ("- ", "* ", "• "):
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    head, sep, rest = line.partition(". ")
    if sep and head.isdigit():
        return rest.strip()
    return line


def _content_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def _split_name_role(line: str) -> tuple[str, str]:
    for sep in (" — ", " – ", " - "):
        if sep in line:
            name, role = line.split(sep, 1)
            return name.strip(), role.strip()
    if "," in line:
        name, role = line.split(",", 1)
        return name.strip(), role.strip()
    return line.strip(), ""


def _parse_md_table(text: str) -> list[list[str]]:
    """Return table rows (header first) from markdown pipe-table lines."""
    rows = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") for c in cells):
            continue  # separator row |---|---|
        rows.append(cells)
    return rows


def _map_table_rows(header: list[str], data: list[list[str]], fields: list[str],
                    synonyms: dict[str, tuple[str, ...]]) -> list[dict]:
    """Map table columns to template fields: header-name match first,
    then remaining columns positionally (data is preserved, never dropped
    silently — the consultant can fix labels in saida/payload.json)."""
    norm = [h.lower().strip() for h in header]
    col_for: dict[str, int] = {}
    used: set[int] = set()
    for field in fields:
        for i, h in enumerate(norm):
            if i in used:
                continue
            if h == field or any(s in h for s in synonyms.get(field, ())):
                col_for[field] = i
                used.add(i)
                break
    remaining = [i for i in range(len(header)) if i not in used]
    for field in fields:
        if field not in col_for and remaining:
            col_for[field] = remaining.pop(0)
    rows = []
    for cells in data:
        row = {}
        for field in fields:
            idx = col_for.get(field)
            row[field] = cells[idx] if idx is not None and idx < len(cells) else ""
        rows.append(row)
    return rows


_TABLE_FIELDS = {
    "raci_matrix": (
        ["activity", "r", "a", "c", "i"],
        {"activity": ("ativid", "activity"), "r": ("respons",), "a": ("account", "aprov"),
         "c": ("consult",), "i": ("inform",)},
    ),
    "communication_plan": (
        ["audience", "channel", "frequency", "owner"],
        {"audience": ("audi", "públic", "public"), "channel": ("canal", "channel"),
         "frequency": ("freq",), "owner": ("owner", "respons", "champion", "dono")},
    ),
    "training_plan": (
        ["audience", "format", "cadence"],
        {"audience": ("audi", "públic", "public"), "format": ("format",),
         "cadence": ("cad", "freq")},
    ),
}


def _convert_table_string(key: str, value: str):
    rows = _parse_md_table(value)
    if len(rows) < 2:
        return None, False  # real text, but no markdown table to consume
    fields, synonyms = _TABLE_FIELDS[key]
    mapped = _map_table_rows(rows[0], rows[1:], fields, synonyms)
    return (mapped, True) if mapped else (None, False)


def _convert_steering_string(value: str):
    members = []
    for line in _content_lines(value):
        if line.endswith(":"):
            continue  # section header line
        name, role = _split_name_role(_strip_bullet(line))
        if name:
            members.append({"name": name, "role": role})
    return (members, True) if members else (None, False)


def _convert_tpo_string(value: str):
    lines = _content_lines(value)
    if not lines:
        return None, False
    first = lines[0]
    for label in ("program manager:", "programa manager:", "gerente do programa:"):
        if first.lower().startswith(label):
            first = first[len(label):].strip()
            break
    members: list[str] = []
    for line in lines[1:]:
        line = _strip_bullet(line)
        for label in ("membros:", "members:", "miembros:"):
            if line.lower().startswith(label):
                line = line[len(label):].strip()
                break
        if not line:
            continue
        if "," in line and len(line.split(",")) > 1:
            members.extend(part.strip() for part in line.split(",") if part.strip())
        else:
            members.append(line)
    if not first:
        return None, False
    tpo = {"program_manager": first}
    if members:
        tpo["members"] = members
    return tpo, True


def _convert_wizard_string(key: str, value: str):
    if key == "adkar_notes":
        return value.strip(), True
    if key.startswith("quick_wins_"):
        items = [_strip_bullet(line) for line in _content_lines(value)]
        items = [item for item in items if item]
        return (items, True) if items else (None, False)
    if key == "executive_steering_committee":
        return _convert_steering_string(value)
    if key == "tpo":
        return _convert_tpo_string(value)
    if key in _TABLE_FIELDS:
        return _convert_table_string(key, value)
    return None, False


def _convert_wizard_structured(key: str, value):
    """Pass through already-structured values (sample_payload.json shape)."""
    if key == "adkar_notes":
        return (None, False)  # non-string adkar is not renderable
    if key == "tpo":
        if isinstance(value, dict) and str(value.get("program_manager", "")).strip():
            return value, True
        return None, False
    if key.startswith("quick_wins_"):
        if isinstance(value, list) and all(isinstance(v, str) for v in value):
            items = [v.strip() for v in value if v.strip()]
            return (items, True) if items else (None, None)
        return None, False
    if isinstance(value, list):
        if not value:
            return None, None
        if all(isinstance(v, dict) for v in value):
            return value, True
    return None, False


def _convert_wizard_value(key: str, value):
    """Returns (converted_value, status): status True = consumable,
    False = present but not consumable, None = empty/placeholder."""
    if value is None:
        return None, None
    if isinstance(value, str):
        if _is_placeholder_text(value):
            return None, None
        return _convert_wizard_string(key, value)
    return _convert_wizard_structured(key, value)


# ─── Cross-survey artifacts ───────────────────────────────────────

def _attach_cross_survey(payload: dict, kit: Path) -> None:
    """Detect optional survey artifacts and attach them to ``payload``."""
    cross = collect_cross_survey_data(kit)
    if not cross:
        return
    payload["cross_survey_data"] = cross
    bits = []
    if "developer_survey_maturity" in cross:
        n = cross["developer_survey_maturity"].get("respondents") or "?"
        bits.append(f"survey-devs maturity (n={n})")
    if "developer_survey_insights" in cross:
        bits.append("survey-devs insights")
    if "learning_plan" in cross:
        bits.append("learning plan")
    print(f"✓ cross_survey_data attached: {', '.join(bits)}")


def collect_cross_survey_data(kit: Path) -> dict | None:
    """Detect optional outputs from the two complementary surveys and
    expose them as ``payload.cross_survey_data`` for downstream consumption.

    The score justification template renders this field when available, and
    surfacing it in ``payload.json`` keeps the data inspectable for audits.
    """
    out_dir = kit / "saida"
    if not out_dir.exists():
        return None

    cross: dict = {"available": False}

    maturity = _collect_developer_maturity(kit, out_dir)
    if maturity:
        cross["developer_survey_maturity"] = maturity
        cross["available"] = True

    insights = _latest_artifact(kit, out_dir, "insights-developer-survey-*.md")
    if insights:
        cross["developer_survey_insights"] = insights
        cross["available"] = True

    learning_plan = _latest_artifact(kit, out_dir, "plano-capacitacao-*.md")
    if learning_plan:
        cross["learning_plan"] = learning_plan
        cross["available"] = True

    return cross if cross["available"] else None


def _latest_artifact(kit: Path, out_dir: Path, pattern: str) -> dict | None:
    candidates = sorted(out_dir.glob(pattern), reverse=True)
    if not candidates:
        return None
    return {"source_file": str(candidates[0].relative_to(kit))}


def _collect_developer_maturity(kit: Path, out_dir: Path) -> dict | None:
    candidates = sorted(out_dir.glob("maturidade-developer-survey-*.json"), reverse=True)
    if not candidates:
        return None
    try:
        mat = json.loads(candidates[0].read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None

    meta = mat.get("metadata", {}) or {}
    team_overall = mat.get("team_overall", {}) or {}
    return {
        "source_file": str(candidates[0].relative_to(kit)),
        "respondents": meta.get("n_respondents") or meta.get("total_respondents"),
        "overall_score": team_overall.get("score"),
        "overall_label": team_overall.get("label"),
        "dimensions": _developer_maturity_dimensions(mat.get("dimensions") or {}),
    }


def _developer_maturity_dimensions(raw_dims: dict) -> list[dict]:
    dims = []
    for did, entry in raw_dims.items():
        if not isinstance(entry, dict):
            continue
        score = entry.get("team_score", entry.get("score"))
        if score is None:
            continue
        score_float = float(score)
        label = entry.get("label")
        if not label:
            lvl = level_from_score(score_float)
            label = f"L{lvl}"
        dims.append({
            "dimension": did,
            "name": entry.get("name"),
            "score": round(score_float, 2),
            "label": label,
            "respondents": entry.get("respondents_with_score"),
        })
    return dims


# ─── Rendering ────────────────────────────────────────────────────

def check_render_dependencies(html_only: bool) -> None:
    if importlib.util.find_spec("jinja2") is None:
        fail("dependência ausente: jinja2. Instale com: python3 -m pip install jinja2 "
             "(ou: make install-deps)")
    if not html_only and importlib.util.find_spec("weasyprint") is None:
        fail("dependência ausente: weasyprint (necessária para PDF). Instale com: "
             "python3 -m pip install weasyprint (ou: make install-deps), "
             "ou use --html-only para gerar apenas os HTMLs.")


def render_reports(payload_path: Path, out_dir: Path, kit: Path, html_only: bool) -> int:
    """Invoke render_reports.py to produce the 5 reports."""
    script = kit / "relatorios/scripts/render_reports.py"
    cmd = [sys.executable, str(script), "--payload", str(payload_path), "--out", str(out_dir)]
    if html_only:
        cmd.append("--html-only")
    what = "5 HTMLs" if html_only else "5 PDFs"
    print(f"\n→ Renderizando {what} com {payload_path.name}...")
    result = subprocess.run(cmd)
    return result.returncode


def _parse_generated_date(raw: str | None) -> str:
    if not raw:
        return datetime.date.today().isoformat()
    try:
        return datetime.date.fromisoformat(raw).isoformat()
    except ValueError:
        fail(f"--date/REPORT_DATE inválido: '{raw}' — use o formato YYYY-MM-DD (ex.: 2026-05-08).")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Monta saida/payload.json a partir dos dados do kit e renderiza os 5 relatórios."
    )
    ap.add_argument("--kit", default=str(Path(__file__).resolve().parent.parent.parent),
                    help="Path to kit-cliente/")
    ap.add_argument("--out", default=None, help="Output dir (default: <kit>/saida/)")
    ap.add_argument("--no-render", action="store_true",
                    help="Only build payload, skip rendering")
    ap.add_argument("--html-only", action="store_true",
                    help="Render HTML only, skip PDF conversion (no weasyprint needed)")
    ap.add_argument("--allow-sample", action="store_true",
                    help="Allow rendering with fictional sample (Acme) data when client inputs are missing")
    ap.add_argument("--locale", choices=LOCALES, default=None,
                    help="Override report locale (default: respostas.json metadata.language)")
    ap.add_argument("--date", default=os.environ.get("REPORT_DATE"),
                    help="Override generated_date (YYYY-MM-DD) for reproducible output; "
                         "also honored via the REPORT_DATE env var")
    args = ap.parse_args()

    try:
        kit = Path(args.kit).resolve()
        out_dir = Path(args.out).resolve() if args.out else kit / "saida"
        generated_date = _parse_generated_date(args.date)

        if not args.no_render:
            check_render_dependencies(args.html_only)

        out_dir.mkdir(parents=True, exist_ok=True)
        print(f"Kit:     {kit}")
        print(f"Out:     {out_dir}")
        print()

        payload = build_payload(kit, allow_sample=args.allow_sample,
                                locale_override=args.locale,
                                generated_date=generated_date)
    except PipelineError as exc:
        print(f"✗ {exc}", file=sys.stderr)
        return 1

    payload_path = out_dir / "payload.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Payload merged: {payload_path} ({payload_path.stat().st_size:,} bytes)")
    print(f"  Locale:  {payload.get('locale')}")
    print(f"  Org:     {payload['organization']['name']}")
    print(f"  Overall: {payload['scores']['overall']['weighted_avg']} "
          f"({payload['scores']['overall']['level_label']})")

    if args.no_render:
        return 0

    return render_reports(payload_path, out_dir, kit, html_only=args.html_only)


if __name__ == "__main__":
    sys.exit(main())
