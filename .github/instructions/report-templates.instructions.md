---
description: Rules for the production-mirror report templates and i18n string catalogs
applyTo: "relatorios/templates/**,relatorios/i18n/**"
---

# Report templates and i18n catalogs

These files mirror the production platform's report service. Treat them as read-only mirrors: visual and structural parity with the platform is the point.

- Do not restyle or restructure the templates or `_print.css`. The set is: 3 page templates + 1 shared partial (`_components.html.j2`) + `_print.css`, rendering the 5 PDFs (`roadmap_part_pillar.html.j2` renders once per pillar).
- i18n edits must preserve exact key parity across `pt-br.json`, `en.json`, and `es.json`: adding a key means adding it to all three catalogs with the same key path.
- Rendering must keep Jinja2 `autoescape=True` and `StrictUndefined`; never add `|safe` filters or disable escaping.
- If a change seems genuinely needed here, it belongs upstream in the platform repository first; sync the mirror afterwards.
