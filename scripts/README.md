# `scripts/`: Kit utilities

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../README.md)

Maintenance and validation helpers for the kit. The client does not run them in the normal flow; they are for contributors.

## Contents

| File | Purpose |
| --- | --- |
| [`smoke_test.py`](smoke_test.py) | Automated end-to-end test: copies `respostas.json.example`, runs `build_payload_and_render.py --no-render`, validates the `payload.json` shape, and restores the workspace. Pure stdlib (no pytest). |
| [`build_language_kits.py`](build_language_kits.py) | Builds the public PT-BR, EN, and ES ZIPs and validates that every asset referenced by the packages exists. The PT ZIP ships the `X.pt-br.md` / `X.pt-br.html` copies under their base names; no ZIP contains `*.pt-br.*` names. |
| [`check_language_coverage.py`](check_language_coverage.py) | Reports multilingual coverage: required package files, translated doc pairs (`X.md` and `X.pt-br.md`, fails when the EN base is missing), and advisory gaps in the localized question banks. |

## Usage

```bash
make smoke          # assessment only
make smoke-cross    # + cross-survey enrichment (developer + learning surveys)
make validate-docs  # content.json + language coverage + package sources
make build-kits     # dist/ai-maturity-kit-{pt,en,es}.zip

# or directly:
python3 scripts/smoke_test.py
python3 scripts/smoke_test.py --with-cross-survey
python3 scripts/check_language_coverage.py
python3 scripts/build_language_kits.py --out dist --clean
```

> [!TIP]
> Run `make smoke` before opening a PR that touches the pipeline (`relatorios/scripts/*.py` or any SKILL.md under `.github/skills/`).
