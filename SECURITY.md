# Security policy

## Client data safety

This kit processes client assessment data locally. Real client data must never be committed to this repository:

- `respostas.json`, `respostas.json.backup-*`, `respostas-forms.xlsx`, `respostas-survey-devs.xlsx`, `respostas-survey-learning.xlsx`, `survey-devs/respostas-devs.json`, `survey-learning/respostas-learning.json`, and `implementation-guide-inputs.json` are gitignored on purpose. Keep them that way.
- Only the `*.example` files and the mock data under `referencia/exemplo-saida/` (fictional "Cliente Exemplo S.A." data) belong in git.
- Generated outputs in `saida/` are gitignored as well.

Before pushing, check that no real data slipped through:

```bash
git status --ignored
```

## Reporting a vulnerability

Report vulnerabilities or suspected client-data exposure privately to **paulasilva@microsoft.com**. Do not open a public issue for security reports.
