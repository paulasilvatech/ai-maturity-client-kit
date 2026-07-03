# Copilot hooks

`protect-immutable-paths.json` registers a `preToolUse` hook that runs `check_immutable_paths.py` before every Copilot tool call. When a file-write tool (`create` or `edit`) targets one of the kit's immutable paths, the hook denies the call with an explanatory reason; everything else is deferred to the normal permission flow (the hook never auto-approves).

## What it enforces

Denied write targets (immutable, maintained upstream or mirrored from the platform):

- `framework.json`
- `referencia/`
- `relatorios/templates/`, `relatorios/i18n/`
- `formularios/`
- `coleta/`
- `docs/` (site content is maintainer-owned)

Explicitly allowed write targets: `saida/`, `respostas.json`, `survey-devs/respostas-devs.json`, `survey-learning/respostas-learning.json`, `implementation-guide-inputs.json`.

This turns the "do not modify" prose rules in `copilot-instructions.md` and the skills into deterministic enforcement.

## Which surfaces honor it

- **Copilot cloud (coding) agent on github.com**: reads `.github/hooks/*.json` from the repository.
- **Copilot CLI**: reads `.github/hooks/*.json` from the repository (plus personal hooks in `~/.copilot/hooks/`).
- **VS Code Copilot Chat**: does NOT read this directory. VS Code has a separate agent-scoped hooks preview (`hooks` in `.agent.md`, gated by `chat.useCustomAgentHooks`), so the prose rules remain the guard there.

## Limitations

- Only `create`/`edit` tool calls are intercepted; file writes performed inside `bash`/`powershell` tool commands are not inspected.
- Paths are detected by scanning `toolArgs` values under path-like keys (`path`, `*file*`, `target`, `dest`). Non-path arguments (e.g. edit content strings) are ignored.
- The hook requires `python3` on PATH. Note that `preToolUse` command hooks are fail-closed: if the command itself cannot start, tool calls are denied. The script itself always exits 0, even on malformed input.

## Bypassing for repo maintenance

When maintainers legitimately need Copilot to edit protected files (template sync, docs updates):

1. Set `"disableAllHooks": true` in `protect-immutable-paths.json` for the working session (revert before merging), or
2. Delete or rename the JSON file on your maintenance branch, or
3. Make the edits manually or with a non-Copilot tool; the hook only gates Copilot tool calls.

## Verifying

```bash
python3 -m json.tool .github/hooks/protect-immutable-paths.json
python3 .github/hooks/check_immutable_paths.py --self-test
```

Reference: https://docs.github.com/en/copilot/reference/hooks-reference and https://docs.github.com/en/copilot/concepts/agents/hooks
