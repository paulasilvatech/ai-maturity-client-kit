# `coleta/`: Collect answers via Microsoft Forms or a multi-respondent Excel

🌐 English · [Português (Brasil)](README.pt-br.md)

This folder has everything the client needs to collect answers from **3 or more people** via Microsoft Forms (or a shared Excel/SharePoint spreadsheet). The `/importar-respostas-excel` skill consumes the output and generates an aggregated `respostas.json` (mean per question).

## Files

| File | What it is |
|---|---|
| **[INSTRUCOES-FORMS.md](INSTRUCOES-FORMS.md)** | Step-by-step guide for the 3 paths: full manual Forms, lean pilot Forms, direct Excel/SharePoint |
| **[perguntas-para-forms.en.md](perguntas-para-forms.en.md)** | The 158 questions formatted for copy/paste into Microsoft Forms (structure by pillar/capability), with English labels. Canonical PT-BR bank: [perguntas-para-forms.md](perguntas-para-forms.md) |
| **[template-export-forms.xlsx](template-export-forms.xlsx)** | Excel template in the exact Forms export format: 158 question columns + 158 evidence columns + 3 mocked respondents for testing |

## When to use each file

- **Creating a manual Microsoft Forms?** → read `INSTRUCOES-FORMS.md` (Path A) + open `perguntas-para-forms.en.md` (or the canonical `perguntas-para-forms.md`) side by side for copy/paste
- **Using Excel/SharePoint directly (faster)?** → read `INSTRUCOES-FORMS.md` (Path C) + use `template-export-forms.xlsx` as the base
- **Want to test the `/importar-respostas-excel` skill now?** → rename `template-export-forms.xlsx` → `respostas-forms.xlsx`, move it to the kit root, and run the skill (it detects the file automatically)

## Next step

After collecting (Forms or Excel), you will have a `respostas-forms.xlsx` file. Move it to the root of `kit-cliente/` and run in Copilot Chat:

```
/importar-respostas-excel
```

Or simply:

```
@ai-maturity-assistant
```

The concierge detects the file and guides you.
