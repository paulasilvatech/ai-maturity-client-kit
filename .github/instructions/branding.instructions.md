---
description: Branding and voice rules (paulasilva-ms design system) for HTML and CSS artifacts generated in this kit
applyTo: "**/*.html,**/*.css"
---

# Branding for generated HTML and CSS

Canon: `referencia/branding/IDENTITY.md` (identity strings, logo SVG markup) and `referencia/branding/VOICE.md` (voice rules). This file is the working summary.

Scope exception: these rules do NOT apply to `relatorios/templates/*.html.j2` or `relatorios/templates/_print.css`. Those mirror the production platform and must not be restyled (see `report-templates.instructions.md`).

## Visual identity

- Load `referencia/branding/tokens-paulasilva-ms.css` (relative path); do not redefine tokens inline.
- Use the Microsoft 4-color palette tokens: `--c-blue-500` (#00A4EF), `--c-green-500` (#7FBA00), `--c-yellow-500` (#FFB900), `--c-red-500` (#F25022), plus their 50/100/700 variants.
- Fonts: Inter (sans) and JetBrains Mono (mono), via the `--font-sans` / `--font-mono` tokens.
- Add the `<div class="deck-brand">` chrome bar with the 22px logo SVG from `IDENTITY.md`.
- Signature: `Paula Silva | Software Global Black Belt`. Contact: `paulasilva@microsoft.com`, the single channel (no social links).

## Voice

- No em-dashes and no en-dashes. Use comma, colon, or semicolon; write ranges with a hyphen or "to"/"a".
- No banned vocabulary (see `VOICE.md`: revolutionary, world-class, "leverage" as a verb, and similar).
- Oxford comma; single space after a period; pedagogical without condescension.
- Exemption: platform-inherited data labels keep their original form (e.g. "L2 — Definido" coming from scoring JSONs). Never rewrite data values to satisfy voice rules.
