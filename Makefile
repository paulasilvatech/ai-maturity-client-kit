# AI Maturity Assessment kit — convenience targets
#
# All targets are optional shortcuts around the Python entry points so the kit
# remains usable with `python3` directly. There are no compiled artifacts.

PY ?= python3
KIT := $(CURDIR)

.PHONY: help smoke smoke-cross test ci validate-docs build-kits scores gaps \
	recommend import-assessment pipeline workbook install-deps clean-saida

help:
	@echo "AI Maturity Assessment kit"
	@echo ""
	@echo "Pipeline:"
	@echo "  make import-assessment XLSX=file.xlsx  Import a Forms .xlsx export into respostas.json"
	@echo "  make scores          Compute maturity scores (saida/scores.json)"
	@echo "  make gaps            Compute scores + gap analysis (saida/gaps.json)"
	@echo "  make recommend       Compute scores + gaps + strategy ranking (saida/recomendacoes.json)"
	@echo "  make pipeline        Run full pipeline (build payload + render 5 PDFs)"
	@echo "  make workbook        Regenerate the auditable workbook template (referencia/)"
	@echo ""
	@echo "Quality gates:"
	@echo "  make smoke           End-to-end smoke test (scoring + payload + HTML, no PDFs)"
	@echo "  make smoke-cross     Smoke test including cross-survey enrichment"
	@echo "  make test            Developer-survey rubric unit tests (stdlib only)"
	@echo "  make validate-docs   Validate JSON content, language coverage and packaging"
	@echo "  make ci              Everything CI runs: smoke-cross + test + validate-docs"
	@echo ""
	@echo "Packaging & setup:"
	@echo "  make build-kits      Build PT, EN and ES public ZIP packages"
	@echo "  make install-deps    Install Python dependencies (jinja2, weasyprint, openpyxl)"
	@echo "  make clean-saida     Remove generated artifacts in saida/"
	@echo ""
	@echo "All commands operate on respostas.json at the workspace root."

smoke:
	@$(PY) scripts/smoke_test.py

smoke-cross:
	@$(PY) scripts/smoke_test.py --with-cross-survey

test:
	@$(PY) survey-devs/scripts/test_rubric.py

ci: smoke-cross test validate-docs

validate-docs:
	@$(PY) -m json.tool docs/content.json >/dev/null
	@$(PY) scripts/check_language_coverage.py
	@$(PY) scripts/build_language_kits.py --out dist-validate --clean >/dev/null
	@rm -rf dist-validate
	@echo "docs and package sources OK"

build-kits:
	@$(PY) scripts/build_language_kits.py --out dist --clean

scores:
	@$(PY) scripts/compute_scores.py

gaps: scores
	@$(PY) scripts/compute_gaps.py

recommend: gaps
	@$(PY) scripts/recommend_strategies.py

# Usage: make import-assessment XLSX=respostas-forms.xlsx
XLSX ?= respostas-forms.xlsx
import-assessment:
	@$(PY) scripts/import_assessment_responses.py --input "$(XLSX)"

pipeline:
	@$(PY) relatorios/scripts/build_payload_and_render.py

# Regenerates the empty template. For client-filled workbooks, pass --respostas
# and --out saida/... (see .github/skills/fill-spreadsheet/SKILL.md).
workbook:
	@$(PY) scripts/generate_scoring_workbook.py

# Inside a virtualenv, pip installs into the venv; outside one, fall back to
# a user install (with --break-system-packages for PEP 668 system Pythons).
install-deps:
	@if $(PY) -c 'import sys; raise SystemExit(0 if sys.prefix != sys.base_prefix else 1)'; then \
		$(PY) -m pip install jinja2 weasyprint openpyxl; \
	else \
		$(PY) -m pip install --user --break-system-packages jinja2 weasyprint openpyxl; \
	fi

clean-saida:
	@find saida -mindepth 1 ! -name '.gitkeep' -delete
	@echo "saida/ cleaned"
