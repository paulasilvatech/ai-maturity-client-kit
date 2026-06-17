# AI Maturity Assessment kit — convenience targets
#
# All targets are optional shortcuts around the Python entry points so the kit
# remains usable with `python3` directly. There are no compiled artifacts.

PY ?= python3
KIT := $(CURDIR)

.PHONY: help smoke smoke-cross validate-docs build-kits install-deps pipeline clean-saida

help:
	@echo "AI Maturity Assessment kit"
	@echo ""
	@echo "Targets:"
	@echo "  make smoke         End-to-end smoke test (assessment only, no PDFs)"
	@echo "  make smoke-cross   Smoke test including cross-survey enrichment"
	@echo "  make validate-docs Validate JSON content and package source references"
	@echo "  make build-kits    Build PT, EN and ES public ZIP packages"
	@echo "  make pipeline      Run full pipeline (build payload + render 5 PDFs)"
	@echo "  make install-deps  Install Python dependencies (jinja2, weasyprint, openpyxl)"
	@echo "  make clean-saida   Remove generated artifacts in saida/"
	@echo ""
	@echo "All commands operate on respostas.json at the workspace root."

smoke:
	@$(PY) scripts/smoke_test.py

smoke-cross:
	@$(PY) scripts/smoke_test.py --with-cross-survey

validate-docs:
	@$(PY) -m json.tool docs/content.json >/dev/null
	@$(PY) scripts/build_language_kits.py --out dist-validate --clean >/dev/null
	@rm -rf dist-validate
	@echo "docs and package sources OK"

build-kits:
	@$(PY) scripts/build_language_kits.py --out dist --clean

pipeline:
	@$(PY) relatorios/scripts/build_payload_and_render.py

install-deps:
	@$(PY) -m pip install --user --break-system-packages jinja2 weasyprint openpyxl

clean-saida:
	@find saida -mindepth 1 ! -name '.gitkeep' -delete
	@echo "saida/ cleaned"
