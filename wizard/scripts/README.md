# `wizard/scripts/`

🌐 English · [Português (Brasil)](README.pt-br.md)

📖 **Navigation:** [🏠 Index](../../README.md) · [« Wizard](../README.md)

Scripts that support the Implementation Guide Wizard.

## Contents

| File | Purpose |
|---|---|
| [`auto_fill_from_plano.py`](auto_fill_from_plano.py) | Wizard **mode D**: reads `saida/plano-capacitacao-<DATE>.md` (Learning Survey output) and generates `implementation-guide-inputs.json` at the root, automatically filling in **6 of the 9 fields** (Champions, training_plan, calendar, ADKAR-knowledge, quick wins). |

## Usage

```bash
python3 wizard/scripts/auto_fill_from_plano.py
```

It automatically picks the latest `plano-capacitacao-*.md` in `saida/`. Output: `implementation-guide-inputs.json` at the root (67 % complete; you still need to fill in TPO and RACI Matrix manually).

> [!TIP]
> Only run it if you have already generated the capacitation plan via `/plano-capacitacao`. Otherwise, use mode A (HTML wizard), B (edit the JSON template), or C (guided chat), all described in [`../README.md`](../README.md).
