# `coleta/`: recolectar respuestas vía Microsoft Forms o Excel multi-respondiente

Esta carpeta tiene todo para que el cliente recolecte respuestas de **3 o más personas** vía Microsoft Forms (o una hoja de cálculo Excel/SharePoint compartida). La skill `/import-assessment-responses` consume el output y genera un `respostas.json` agregado (media por pregunta).

## Archivos

| Archivo | Qué es |
|---|---|
| **[INSTRUCOES-FORMS.es.md](INSTRUCOES-FORMS.es.md)** | Guía paso a paso de los 3 caminos: Forms manual completo, Forms reducido piloto, Excel/SharePoint directo |
| **[perguntas-para-forms.es.md](perguntas-para-forms.es.md)** | Las 158 preguntas formateadas para copy/paste en Microsoft Forms (estructura por pilar/capability) |
| **[template-export-forms.xlsx](template-export-forms.xlsx)** | Excel template en el formato exacto del export de Forms: 158 columnas de pregunta + 158 de evidencia + 3 respondientes mockeados para prueba |

## Cuándo usar cada archivo

- **¿Vas a crear el Microsoft Forms manual?** → lee `INSTRUCOES-FORMS.es.md` (Camino A) + abre `perguntas-para-forms.es.md` al lado para copy/paste
- **¿Vas a usar Excel/SharePoint directo (más rápido)?** → lee `INSTRUCOES-FORMS.es.md` (Camino C) + usa `template-export-forms.xlsx` como base
- **¿Quieres probar la skill `/import-assessment-responses` ahora?** → renombra `template-export-forms.xlsx` → `respostas-forms.xlsx`, muévelo a la raíz del kit, ejecuta la skill (lo detecta automáticamente)

## Próximo paso

Después de recolectar (Forms o Excel), tendrás un archivo `respostas-forms.xlsx`. Muévelo a la raíz de `kit-cliente/` y ejecuta en Copilot Chat:

```
/import-assessment-responses
```

O simplemente:

```
@ai-maturity-assistant
```

El concierge detecta el archivo y te guía.
