#!/usr/bin/env python3
"""Copilot preToolUse hook: deny file writes to the kit's immutable paths.

Invoked by GitHub Copilot (cloud agent / CLI) before every tool call, per
.github/hooks/protect-immutable-paths.json. Reads the hook payload from
stdin (JSON with toolName, toolArgs, cwd) and prints a JSON decision to
stdout: {"permissionDecision": "deny", ...} when a file-write tool targets
a protected path, or {} to defer to the normal permission flow.

Protected (deny writes):  framework.json, referencia/, relatorios/templates/,
                          relatorios/i18n/, formularios/, coleta/, docs/
Always allowed (writes):  saida/, respostas.json, survey-devs/respostas-devs.json,
                          survey-learning/respostas-learning.json,
                          implementation-guide-inputs.json

Usage:
    echo '<payload-json>' | python3 check_immutable_paths.py
    python3 check_immutable_paths.py --self-test
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path, PurePosixPath

# check_immutable_paths.py -> .github/hooks/ -> .github/ -> kit root
KIT_ROOT = Path(__file__).resolve().parent.parent.parent

# Tool names that write or modify files (per the Copilot hooks reference).
WRITE_TOOLS = {"create", "edit"}

# Paths a Copilot session may always write (relative to the kit root).
ALLOWED_FILES = {
    "respostas.json",
    "survey-devs/respostas-devs.json",
    "survey-learning/respostas-learning.json",
    "implementation-guide-inputs.json",
}
ALLOWED_DIRS = ("saida",)

# Immutable paths: maintained upstream or mirrored from the platform.
PROTECTED_FILES = {"framework.json"}
PROTECTED_DIRS = (
    "referencia",
    "relatorios/templates",
    "relatorios/i18n",
    "formularios",
    "coleta",
    "docs",
)


def candidate_paths(args_obj):
    """Collect string values under path-like keys from the toolArgs object."""
    found = []

    def looks_like_path_key(key):
        k = key.lower()
        return "path" in k or "file" in k or k in {"target", "dest", "destination"}

    def walk(node, key=None):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, k)
        elif isinstance(node, list):
            for item in node:
                walk(item, key)
        elif isinstance(node, str) and key is not None and looks_like_path_key(key):
            found.append(node)

    walk(args_obj)
    return found


def normalize(raw, cwd):
    """Resolve a raw path to a kit-root-relative POSIX string, or None if outside."""
    p = PurePosixPath(raw.replace("\\", "/"))
    base = Path(cwd) if cwd else KIT_ROOT
    absolute = Path(p) if p.is_absolute() else base / str(p)
    try:
        rel = Path(absolute).resolve().relative_to(KIT_ROOT)
    except ValueError:
        return None
    return rel.as_posix()


def decide(payload):
    """Return the hook output object for one preToolUse payload."""
    tool = str(payload.get("toolName", "")).lower()
    if tool not in WRITE_TOOLS:
        return {}
    cwd = payload.get("cwd") or str(KIT_ROOT)
    for raw in candidate_paths(payload.get("toolArgs") or {}):
        rel = normalize(raw, cwd)
        if rel is None:
            continue
        if rel in ALLOWED_FILES or any(
            rel == d or rel.startswith(d + "/") for d in ALLOWED_DIRS
        ):
            continue
        if rel in PROTECTED_FILES or any(
            rel == d or rel.startswith(d + "/") for d in PROTECTED_DIRS
        ):
            return {
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"'{rel}' is an immutable kit path (reference data, templates, "
                    "forms, or docs site). Write outputs to saida/ or the response "
                    "JSON files instead; see .github/hooks/README.md."
                ),
            }
    return {}


def self_test():
    root = str(KIT_ROOT)
    cases = [
        ({"toolName": "edit", "cwd": root,
          "toolArgs": {"path": "framework.json"}}, "deny"),
        ({"toolName": "create", "cwd": root,
          "toolArgs": {"filePath": "relatorios/templates/base.html"}}, "deny"),
        ({"toolName": "edit", "cwd": root,
          "toolArgs": {"path": root + "/referencia/pontuacao-e-calculo.md"}}, "deny"),
        ({"toolName": "edit", "cwd": root,
          "toolArgs": {"path": "docs/content.json"}}, "deny"),
        ({"toolName": "create", "cwd": root,
          "toolArgs": {"path": "saida/scores.json"}}, "defer"),
        ({"toolName": "edit", "cwd": root,
          "toolArgs": {"path": "respostas.json"}}, "defer"),
        ({"toolName": "edit", "cwd": root,
          "toolArgs": {"path": "survey-devs/respostas-devs.json"}}, "defer"),
        ({"toolName": "view", "cwd": root,
          "toolArgs": {"path": "framework.json"}}, "defer"),
        ({"toolName": "edit", "cwd": root,
          "toolArgs": {"path": "scripts/smoke_test.py"}}, "defer"),
        ({"toolName": "edit", "cwd": root,
          "toolArgs": {"old_string": "see referencia/x.md",
                       "path": "README.md"}}, "defer"),
    ]
    failures = 0
    for payload, expected in cases:
        out = decide(payload)
        got = "deny" if out.get("permissionDecision") == "deny" else "defer"
        status = "ok" if got == expected else "FAIL"
        if got != expected:
            failures += 1
        print(f"[{status}] {payload['toolName']} {payload['toolArgs']} -> {got}")
    if failures:
        print(f"self-test failed: {failures} case(s)")
        return 1
    print(f"self-test passed: {len(cases)} cases")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Copilot preToolUse hook denying writes to immutable kit paths "
                    "(reads the hook payload JSON from stdin)."
    )
    ap.add_argument("--self-test", action="store_true",
                    help="Run built-in allow/deny cases and exit")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    # Never exit non-zero on malformed input: preToolUse hooks are fail-closed,
    # and a crashing hook would block every tool call in the session.
    try:
        payload = json.load(sys.stdin)
        output = decide(payload)
    except Exception:
        output = {}
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
