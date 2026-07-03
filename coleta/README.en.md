# `coleta/`: collect responses via Microsoft Forms or multi-respondent Excel

This folder has everything the client needs to collect responses from **3 or more people** via Microsoft Forms (or a shared Excel/SharePoint spreadsheet). The `/import-assessment-responses` skill consumes the output and generates an aggregated `respostas.json` (mean per question).

## Files

| File | What it is |
|---|---|
| **[INSTRUCOES-FORMS.en.md](INSTRUCOES-FORMS.en.md)** | Step-by-step guide for the 3 paths: full manual Forms, lean pilot Forms, direct Excel/SharePoint |
| **[perguntas-para-forms.en.md](perguntas-para-forms.en.md)** | The 158 questions formatted for copy/paste into Microsoft Forms (structured by pillar/capability) |
| **[template-export-forms.xlsx](template-export-forms.xlsx)** | Excel template in the exact Forms export format: 158 question columns + 158 evidence columns + 3 mocked respondents for testing |

## When to use each file

- **Going to create Microsoft Forms manually?** → read `INSTRUCOES-FORMS.en.md` (Path A) + open `perguntas-para-forms.en.md` alongside for copy/paste
- **Going to use Excel/SharePoint directly (faster)?** → read `INSTRUCOES-FORMS.en.md` (Path C) + use `template-export-forms.xlsx` as your base
- **Want to test the `/import-assessment-responses` skill right now?** → rename `template-export-forms.xlsx` → `respostas-forms.xlsx`, move it to the kit root, run the skill (it detects the file automatically)

## Next step

After collecting (Forms or Excel), you will have a `respostas-forms.xlsx` file. Move it to the root of `kit-cliente/` and run in Copilot Chat:

```
/import-assessment-responses
```

Or simply:

```
@ai-maturity-assistant
```

The concierge detects the file and guides you.
