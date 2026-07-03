# Contributing

Thank you for helping maintain the AI Maturity Assessment kit. This document covers the contributor workflow; client usage is documented in [README.md](README.md) and [GUIA-PASSO-A-PASSO.md](GUIA-PASSO-A-PASSO.md).

## Setup

Python 3.11+ with `jinja2`, `openpyxl`, and (for PDF rendering) `weasyprint`:

```bash
make install-deps
```

The smoke tests and packaging validation run without WeasyPrint; only the final PDF rendering needs it.

## Validating changes

| Command | What it does |
| --- | --- |
| `make smoke` | End-to-end smoke test of the assessment pipeline (stages `respostas.json.example`, builds the payload without rendering PDFs, validates its shape, restores the workspace). |
| `make smoke-cross` | Same, plus the cross-survey enrichment path (developer + learning surveys). |
| `make validate-docs` | Validates `docs/content.json` syntax, runs the language coverage report, and dry-runs the ZIP packager against all referenced sources. |

CI (`.github/workflows/ci.yml`) runs all of the above on every pull request and on pushes to `develop` and `main`. Run `make smoke-cross` locally before opening a PR that touches the pipeline (`relatorios/scripts/*.py`, `scripts/*.py`, or any `SKILL.md` under `.github/skills/`).

## Packaging

`make build-kits` (or `python3 scripts/build_language_kits.py --out dist --clean`) builds the three public ZIPs: `dist/ai-maturity-kit-{pt,en,es}.zip`. The packager validates that every referenced source file exists and fails otherwise.

## Release flow

- `main` is the release branch; `develop` is the integration branch.
- Work lands on `develop` via pull request; CI must pass.
- Merging `develop` into `main` triggers two deployments automatically:
  - `pages.yml` rebuilds the ZIPs into `docs/downloads/` and publishes the GitHub Pages site.
  - `release-zips.yml` rebuilds the ZIPs and refreshes the rolling `kits-latest` GitHub release.
- `copilot-setup-steps.yml` only takes effect from the default branch; changes to it must reach `main` before the Copilot coding agent picks them up.

## Language policy

- **Primitives are English:** code, code comments, commit messages, workflows, scripts, and contributor docs (this file, SECURITY.md, hooks).
- **Client-facing documentation is trilingual:** PT-BR is the canonical source; EN and ES counterparts are sibling variants (`<name>.en.md` / `<name>.es.md`) that the packager ships under the canonical filename in the EN/ES ZIPs. `scripts/check_language_coverage.py` enforces coverage in CI.
- **Client outputs are localized:** generated reports follow `respostas.json::metadata.language` (pt-br / en / es).
- No em-dashes in client-facing content (see `referencia/branding/VOICE.md`).

## Data safety

Never commit real client data. `respostas.json`, the survey response files, and `implementation-guide-inputs.json` are gitignored on purpose; see [SECURITY.md](SECURITY.md).

## PR checklist

- [ ] `make smoke-cross` passes locally.
- [ ] `make validate-docs` passes locally.
- [ ] No real client data staged (`git status --ignored`).
- [ ] New or changed client-facing docs keep PT/EN/ES parity (or the gap is called out in the PR description).
- [ ] Primitives (code, workflows, contributor docs) are in English.
- [ ] Report templates (`relatorios/templates/`) and i18n catalogs (`relatorios/i18n/`) were not edited in place; see "Maintainer sync" below.

## Maintainer sync (templates from the global skill)

The report templates, print CSS, i18n catalogs, and `sample_payload.json` in this kit are mirrored from the maintainer's global skill `~/.github/skills/ai-maturity-reports/`. Do not edit them in place; update the global skill and sync into the kit:

```bash
SKILL=~/.github/skills/ai-maturity-reports
KIT=$(pwd)  # in kit-cliente/

cp $SKILL/assets/templates/*.html.j2 $KIT/relatorios/templates/
cp $SKILL/assets/templates/_print.css $KIT/relatorios/templates/_print.css
cp $SKILL/assets/i18n/*.json $KIT/relatorios/i18n/
cp $SKILL/assets/fixtures/sample_payload.json $KIT/relatorios/sample_payload.json

# Re-apply paulasilva-ms branding to _print.css :root tokens
# (see referencia/branding/IDENTITY.md for the exact MS palette)
```

After syncing, re-render the example PDFs to validate:

```bash
cp respostas.json.example respostas.json
python3 survey-devs/scripts/calcular_maturidade.py
# (run other skills to populate saida/)
python3 relatorios/scripts/build_payload_and_render.py
# Copy outputs to referencia/exemplo-saida/
```

These paths exist only on the maintainer's machine; clients and most contributors never need this section.
