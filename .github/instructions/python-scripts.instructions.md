---
description: Conventions for the kit's deterministic Python scripts
applyTo: "scripts/**,survey-devs/scripts/**,survey-learning/scripts/**,wizard/scripts/**,relatorios/scripts/**"
---

# Python script conventions

Observed conventions in this codebase; keep new and edited scripts consistent with them.

- argparse CLI with a working `--help`; constrain values where applicable (e.g. `choices=["pt-br", "en", "es"]` for locales).
- pathlib everywhere, with kit-root-relative defaults derived from `Path(__file__).resolve()`; never hardcode absolute paths.
- Deterministic output: the same inputs produce the same bytes. Expose `--now` / `--date` overrides for timestamps so reruns and CI comparisons are stable.
- Timezone-aware datetimes (`datetime.now(timezone.utc)` or an explicit timezone); never naive `utcnow()`.
- Errors are actionable one-liners naming the file and the fix (e.g. "saida/scores.json not found: run scripts/compute_scores.py first"), not raw tracebacks for expected failure modes.
- stdlib first; third-party libraries only where inherent to the task: `openpyxl` for Excel import, `jinja2`/`weasyprint` for report rendering.
- Code, comments, and docstrings in English. Runtime client-facing strings follow `respostas.json::metadata.language`, default pt-br.
- Outputs go to `saida/`: canonical filenames overwrite, audit artifacts carry a date in the filename.
- Run `make smoke` (and `make smoke-cross` when touching survey scripts) before opening a PR.
