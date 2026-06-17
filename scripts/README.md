# `scripts/` — Utilitários do kit

📖 **Navegação:** [🏠 Índice](../README.md)

Scripts auxiliares de manutenção e validação do kit (não invocados pelo cliente final no fluxo normal — são para contribuidores).

## Conteúdo

| Arquivo | Propósito |
| --- | --- |
| [`smoke_test.py`](smoke_test.py) | Teste end-to-end automatizado: copia `respostas.json.example` → roda `build_payload_and_render.py --no-render` → valida shape do `payload.json` → restaura workspace. Stdlib puro (sem pytest). |
| [`build_language_kits.py`](build_language_kits.py) | Gera os ZIPs públicos PT-BR, EN e ES e valida que os assets referenciados pelos pacotes existem. |
| [`check_language_coverage.py`](check_language_coverage.py) | Reporta cobertura multilíngue obrigatória e lacunas consultivas, como bancos de perguntas EN/ES ainda pendentes de revisão humana. |

## Como usar

```bash
make smoke          # assessment only
make smoke-cross    # + cross-survey enrichment (developer + learning surveys)
make validate-docs  # content.json + package source validation
make build-kits     # dist/ai-maturity-kit-{pt,en,es}.zip

# ou direto:
python3 scripts/smoke_test.py
python3 scripts/smoke_test.py --with-cross-survey
python3 scripts/check_language_coverage.py
python3 scripts/build_language_kits.py --out dist --clean
```

> [!TIP]
> Rode `make smoke` antes de abrir PR que toca o pipeline (`relatorios/scripts/*.py` ou qualquer SKILL.md em `.github/skills/`).
