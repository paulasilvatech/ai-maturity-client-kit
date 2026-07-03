"""paulasilva-ms branding constants and helpers.

Shared by all scripts that generate output (PDFs, reports, JSONs, MD).
Single source of truth for identity strings, palette, and footer markup.

See referencia/branding/IDENTITY.md and referencia/branding/VOICE.md.
"""

# ============================================================
# Identity strings (canonical, never modify)
# ============================================================

AUTHOR = "Paula Silva"
ROLE = "Software Global Black Belt"
ROLE_FULL = "Paula Silva, Software Global Black Belt"
META_BAR = "Paula Silva | Software Global Black Belt"
# Official signature contact per referencia/branding/IDENTITY.md — intentional
# branding for generated markdown/JSON artifacts. NFR-REPORT-011 keeps it OUT
# of the rendered client PDFs/HTML (see render_smoke.py FORBIDDEN_TOKENS).
CONTACT = "paulasilva@microsoft.com"
TAGLINE = "Building the future of software development with AI and Agentic DevOps"

# ============================================================
# Microsoft 4-color palette (logo, accent)
# ============================================================

MS_BLUE = "#00A4EF"
MS_GREEN = "#7FBA00"
MS_YELLOW = "#FFB900"
MS_RED = "#F25022"

PALETTE = {
    "primary": MS_BLUE,
    "positive": MS_GREEN,
    "warn": MS_YELLOW,
    "critical": MS_RED,
}

# ============================================================
# Output helpers
# ============================================================

DESIGN_SYSTEM = "paulasilva-ms Design System v1.7.0"


def md_header() -> str:
    """HTML comment with paulasilva-ms identity (top of generated .md files)."""
    return (
        f"<!-- paulasilva-ms identity: {META_BAR} · {CONTACT} -->\n"
        f"<!-- {DESIGN_SYSTEM} -->\n"
    )


def md_footer() -> str:
    """Markdown footer with Paula Silva attribution (bottom of generated .md files)."""
    return (
        "\n\n---\n\n"
        f"<sub>**{AUTHOR}** | {ROLE} · {CONTACT}</sub>  \n"
        f"<sub>{TAGLINE}</sub>  \n"
        f"<sub>Identidade visual: {DESIGN_SYSTEM} · ver `referencia/branding/`</sub>\n"
    )


def json_metadata() -> dict:
    """Branding metadata to inject into generated JSON files."""
    return {
        "branding": {
            "design_system": DESIGN_SYSTEM,
            "author": AUTHOR,
            "role": ROLE,
            "contact": CONTACT,
            "tagline": TAGLINE,
            "palette": PALETTE,
        }
    }
