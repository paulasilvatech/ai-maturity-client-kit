# `referencia/exemplo-saida/es/`

📖 **Navegación:** [🏠 Índice](../../../README.md) · [« Ejemplo de salida](../README.md)

Versión en **español** de los 5 PDFs de referencia generados a partir de `respostas.json.example` (Cliente Exemplo S.A., locale forzado a `es`).

## Contenido

| Archivo | Descripción |
|---|---|
| `score_justification.pdf` | Justificación de puntuación (overall 1.99, L2) |
| `roadmap_part_pillar_p1.pdf` | Deep-dive del pilar Productividad del Desarrollador |
| `roadmap_part_pillar_p2.pdf` | Deep-dive del pilar Ciclo de Vida DevOps |
| `roadmap_part_pillar_p3.pdf` | Deep-dive del pilar Plataforma de Aplicaciones |
| `roadmap_part4.pdf` | Guía de Implementación (consolidada) |

## Cuándo usar

- Mostrar al cliente final cómo **se verán los PDFs en español** (si define `language: "es"` en `respostas.json::metadata`)
- Validar visualmente que las plantillas manejan bien los textos en español

> [!NOTE]
> Los PDFs en PT-BR (default) están en el directorio padre: [`../`](../).

## Cómo regenerar

Desde la raíz del kit, con los inputs de ejemplo preparados (ver [`../README.md`](../README.md), paso 1):

```bash
export SOURCE_DATE_EPOCH=1778257208   # fija los timestamps de fuentes embebidas (PDFs byte-estables)
python3 relatorios/scripts/build_payload_and_render.py \
  --date 2026-05-08 --locale es --out referencia/exemplo-saida/es
```

`--locale es` construye un payload con etiquetas en español desde `relatorios/i18n/es.json` y renderiza los 5 PDFs. Para generar informes reales en español, define `metadata.language` como `"es"` en `respostas.json` y ejecuta `/generate-reports`.
