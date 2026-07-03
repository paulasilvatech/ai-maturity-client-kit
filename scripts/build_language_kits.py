#!/usr/bin/env python3
"""Build per-language ZIP packages for the AI Maturity client kit.

Packaging rule:
- Copilot customization files under .github/ stay in English in every package.
- Client-facing documentation in each package must match the selected language.
- Shared scripts, templates, JSON schemas, workbooks, and renderers are reused.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMON_EXCLUDED_PARTS = {
    ".git",
    ".mypy_cache",
    "__pycache__",
    "dist",
    "build",
    "saida",
}

COMMON_EXCLUDED_NAMES = {
    ".DS_Store",
    "Thumbs.db",
}

GENERATED_OR_CLIENT_INPUTS = {
    "respostas.json",
    "implementation-guide-inputs.json",
    "respostas-forms.xlsx",
    "respostas-survey-devs.xlsx",
    "respostas-survey-learning.xlsx",
    "survey-devs/respostas-devs.json",
    "survey-learning/respostas-learning.json",
}

COPILOT_CUSTOMIZATION_ROOTS = [
    ".github/copilot-instructions.md",
    ".github/agents",
    ".github/prompts",
    ".github/skills",
]

SHARED_RUNTIME_ROOTS = [
    "framework.json",
    "respostas.json.example",
    "Makefile",
    "scripts",
    "relatorios/templates",
    "relatorios/scripts",
    "relatorios/i18n",
    "relatorios/sample_payload.json",
    "coleta/template-export-forms.xlsx",
    "survey-devs/scripts",
    "survey-devs/respostas-mock-devs.json",
    "survey-devs/template-export-forms-devs.xlsx",
    "survey-learning/scripts",
    "survey-learning/respostas-mock-learning.json",
    "survey-learning/template-export-forms-learning.xlsx",
    "wizard/scripts",
    "wizard/implementation-guide-inputs.template.json",
    "referencia/pontuacao-e-calculo.xlsx",
]

SHARED_CLIENT_ASSETS = [
    # Question banks referenced by every language package. The canonical IDs
    # remain unchanged so Microsoft Forms exports keep parsing correctly.
    "coleta/perguntas-para-forms.md",
    "coleta/perguntas-para-forms.en.md",
    "coleta/perguntas-para-forms.es.md",
    "survey-devs/perguntas-para-forms-devs.md",
    "survey-devs/perguntas-para-forms-devs.en.md",
    "survey-devs/perguntas-para-forms-devs.es.md",
    "survey-learning/perguntas-para-forms-learning.md",
    "survey-learning/perguntas-para-forms-learning.en.md",
    "survey-learning/perguntas-para-forms-learning.es.md",
    # Source docs and references used by translated guides and fallback flows.
    "coleta/INSTRUCOES-FORMS.md",
    "survey-devs/INSTRUCOES-FORMS-DEVS.md",
    "survey-devs/README.md",
    "survey-devs/RUBRICA-MATURIDADE.md",
    "survey-learning/INSTRUCOES-FORMS-LEARNING.md",
    "survey-learning/README.md",
    "wizard/README.md",
    # Canonical step-by-step guide (referenced by the Copilot primitives in
    # every package; EN/ES ship a translated variant once available).
    "GUIA-PASSO-A-PASSO.md",
    # Reference documentation shipped with every package (scoring model,
    # pillar deep dives, and the referencia/ index).
    "referencia/README.md",
    "referencia/pontuacao-e-calculo.md",
    "referencia/P1-produtividade-do-desenvolvedor.md",
    "referencia/P2-ciclo-de-vida-devops.md",
    "referencia/P3-plataforma-de-aplicações.md",
    # Stylesheet referenced by every shipped HTML tool (forms, wizard,
    # calculator all link referencia/branding/tokens-paulasilva-ms.css) and
    # the branding sources the report skills read in every package.
    "referencia/branding/tokens-paulasilva-ms.css",
    "referencia/branding/IDENTITY.md",
    "referencia/branding/VOICE.md",
    # Visual helpers referenced by the quickstarts.
    "formularios",
    "wizard/implementation-guide-wizard.html",
    "referencia/calculadora-pontuacao.html",
]

# Reference example outputs (referencia/exemplo-saida/). Kept as module-level
# constants so validate_packaging_sources() covers the complete manifest.
REFERENCE_EXAMPLE_JSON = [
    "referencia/exemplo-saida/scores.json",
    "referencia/exemplo-saida/gaps.json",
    "referencia/exemplo-saida/recomendacoes.json",
    "referencia/exemplo-saida/payload.json",
    "referencia/exemplo-saida/maturidade-developer-survey-EXEMPLO.json",
    "referencia/exemplo-saida/implementation-guide-inputs-EXEMPLO.json",
]

REFERENCE_EXAMPLE_PT_FILES = [
    "referencia/exemplo-saida/pontuacao-preenchida-2026-05-08.xlsx",
    "referencia/exemplo-saida/README.md",
    "referencia/exemplo-saida/insights-developer-survey-EXEMPLO.md",
    "referencia/exemplo-saida/plano-capacitacao-EXEMPLO.md",
]

REFERENCE_EXAMPLE_PDF_NAMES = [
    "score_justification.pdf",
    "roadmap_part_pillar_p1.pdf",
    "roadmap_part_pillar_p2.pdf",
    "roadmap_part_pillar_p3.pdf",
    "roadmap_part4.pdf",
]

REFERENCE_EXAMPLE_TREES = [
    "referencia/exemplo-saida/en",
    "referencia/exemplo-saida/es",
]

# Paths that Copilot primitives may legitimately reference even though they
# are absent from the ZIPs: gitignored client inputs and generated outputs.
PRIMITIVE_REFERENCE_ALLOWLIST_PREFIXES = (
    "saida/",
    "dist/",
    "docs/",
    # Reference examples are split per language (PT root, en/, es/), while the
    # primitives cite the PT paths as illustrations in every package.
    "referencia/exemplo-saida/",
)

PRIMITIVE_REFERENCE_ALLOWLIST = {
    "respostas.json",
    "implementation-guide-inputs.json",
    "respostas-forms.xlsx",
    "respostas-survey-devs.xlsx",
    "respostas-survey-learning.xlsx",
    "survey-devs/respostas-devs.json",
    "survey-learning/respostas-learning.json",
    # TODO: dead reference inside ai-maturity-reports/SKILL.md ("Sync with
    # global skill" section, maintainer-machine path). Remove this entry once
    # that section is deleted from the skill.
    ".github/skills/paulasilva-ms",
}

LANGUAGE_DOCS = {
    "pt": [],
    "en": [
        ("kit-en/README.md", "README.md"),
        ("kit-en/STEP-BY-STEP.md", "STEP-BY-STEP.md"),
        ("kit-en/FORMS-INSTRUCTIONS.md", "FORMS-INSTRUCTIONS.md"),
    ],
    "es": [
        ("kit-es/README.md", "README.md"),
        ("kit-es/PASO-A-PASO.md", "PASO-A-PASO.md"),
        ("kit-es/INSTRUCCIONES-FORMS.md", "INSTRUCCIONES-FORMS.md"),
    ],
}

LANGUAGE_NOTES = {
        "pt": """# Notas de idioma do pacote PT-BR

- Documentacao de cliente: Portugues (Brasil).
- Arquivos de customizacao do Copilot em `.github/`: mantidos em ingles
    por design, para economizar contexto e melhorar compatibilidade.
- Arquivos JSON, scripts, templates e workbooks sao recursos executaveis
    ou estruturados compartilhados.
""",
        "en": """# Language Notes for the English Package

- Client-facing documentation: English.
- Copilot customization files in `.github/`: intentionally kept in English
    across every language package.
- Shared JSON files, scripts, templates, and workbooks are executable or
    structured assets reused by all languages.
- Canonical Portuguese question banks are included under `coleta/`,
    `survey-devs/`, and `survey-learning/` so Microsoft Forms can be built
    without missing files. Translate respondent-facing text as needed, but
    keep question IDs unchanged.
- Canonical question IDs and some internal field names remain in Portuguese
    where required by the scoring framework and production platform mapping.
""",
        "es": """# Notas de idioma del paquete Espanol

- Documentacion orientada al cliente: Espanol.
- Archivos de customizacion de Copilot en `.github/`: se mantienen en ingles
    intencionalmente en todos los paquetes.
- JSONs, scripts, templates y workbooks compartidos son activos ejecutables
    o estructurados reutilizados por todos los idiomas.
- Los bancos canonicos de preguntas en Portugues se incluyen en `coleta/`,
    `survey-devs/` y `survey-learning/` para crear Microsoft Forms sin
    archivos faltantes. Traduce el texto visible para respondentes segun sea
    necesario, manteniendo los IDs sin cambios.
- IDs canonicos de preguntas y algunos nombres internos permanecen en Portugues
    cuando el framework de scoring y el mapeo de plataforma lo requieren.
""",
}

ARCHIVE_NAMES = {
    "pt": "ai-maturity-kit-pt.zip",
    "en": "ai-maturity-kit-en.zip",
    "es": "ai-maturity-kit-es.zip",
}


def normalized(path: Path) -> str:
    return path.as_posix()


def is_common_excluded(rel: str) -> bool:
    parts = set(Path(rel).parts)
    if parts & COMMON_EXCLUDED_PARTS:
        return True
    if Path(rel).name in COMMON_EXCLUDED_NAMES:
        return True
    if rel.startswith(".github/workflows/"):
        return True
    if rel.startswith("docs/downloads/"):
        return True
    if rel in GENERATED_OR_CLIENT_INPUTS:
        return True
    return False


def should_include_runtime_file(rel: str) -> bool:
    if is_common_excluded(rel):
        return False
    path = Path(rel)
    if path.suffix.lower() == ".md":
        return rel.startswith(".github/")
    if path.suffix.lower() in {".html", ".htm"}:
        return rel.startswith("relatorios/templates/")
    return True


def add_file(
    zf: zipfile.ZipFile,
    source_rel: str,
    dest_rel: str | None = None,
) -> None:
    source = ROOT / source_rel
    if not source.exists() or not source.is_file():
        raise FileNotFoundError(
            f"Packaging source file missing: {source_rel} — the ZIP would ship "
            f"incomplete. Restore the file or remove it from the manifest in "
            f"scripts/build_language_kits.py."
        )
    arcname = dest_rel or source_rel
    if arcname in zf.NameToInfo:
        return
    zf.write(source, arcname)


def iter_source_files(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    return sorted(path for path in source.rglob("*") if path.is_file())


def should_add_tree_file(rel: str, runtime_filter: bool) -> bool:
    if runtime_filter and not should_include_runtime_file(rel):
        return False
    return not is_common_excluded(rel)


def destination_for(
    file_path: Path,
    source: Path,
    dest_rel: str | None,
) -> str:
    if not dest_rel:
        return normalized(file_path.relative_to(ROOT))
    if source.is_file():
        return dest_rel
    return normalized(Path(dest_rel) / file_path.relative_to(source))


def add_tree(
    zf: zipfile.ZipFile,
    source_rel: str,
    dest_rel: str | None = None,
    *,
    runtime_filter: bool = False,
) -> None:
    source = ROOT / source_rel
    if not source.exists():
        raise FileNotFoundError(
            f"Packaging source tree missing: {source_rel} — the ZIP would ship "
            f"incomplete. Restore the tree or remove it from the manifest in "
            f"scripts/build_language_kits.py."
        )

    for file_path in iter_source_files(source):
        rel = normalized(file_path.relative_to(ROOT))
        if not should_add_tree_file(rel, runtime_filter):
            continue
        dest = destination_for(file_path, source, dest_rel)
        if dest in zf.NameToInfo:
            continue
        zf.write(file_path, dest)


def add_copilot_customizations(zf: zipfile.ZipFile) -> None:
    for root in COPILOT_CUSTOMIZATION_ROOTS:
        add_tree(zf, root)


def add_shared_runtime(zf: zipfile.ZipFile) -> None:
    for root in SHARED_RUNTIME_ROOTS:
        add_tree(zf, root, runtime_filter=True)


LANGUAGE_SUFFIXES = (".en.md", ".es.md")

# Markdown assets that are language-invariant by design: no EN/ES variant is
# expected, so no missing-variant warning should be emitted for them.
LANGUAGE_INVARIANT_ASSETS = {
    "referencia/branding/IDENTITY.md",
    "referencia/branding/VOICE.md",
}


def language_variant_of(source_rel: str, lang: str) -> str:
    """Return the sibling variant path <name>.<lang>.md for a canonical doc."""
    return f"{source_rel[: -len('.md')]}.{lang}.md"


def resolve_client_asset(source_rel: str, lang: str) -> tuple[str, str | None]:
    """Pick the source to ship for a client asset in a given language package.

    For EN/ES packages, a Markdown doc with a sibling <name>.<lang>.md variant
    ships THAT variant under the canonical name. Docs whose variants are
    already explicit manifest entries (the question banks ship in all three
    languages side by side) are left untouched. Returns
    (source_to_package, missing_variant) where missing_variant is the variant
    path that does not exist yet (PT original is shipped as fallback).
    """
    if lang == "pt" or not source_rel.endswith(".md"):
        return source_rel, None
    if source_rel.endswith(LANGUAGE_SUFFIXES) or source_rel in LANGUAGE_INVARIANT_ASSETS:
        return source_rel, None
    variant = language_variant_of(source_rel, lang)
    if variant in SHARED_CLIENT_ASSETS:
        return source_rel, None
    if (ROOT / variant).exists():
        return variant, None
    return source_rel, variant


def add_shared_client_assets(zf: zipfile.ZipFile, lang: str) -> list[str]:
    """Add client assets, preferring language variants. Returns missing ones."""
    missing_variants: list[str] = []
    for root in SHARED_CLIENT_ASSETS:
        source, missing = resolve_client_asset(root, lang)
        if missing:
            missing_variants.append(missing)
        if source == root:
            add_tree(zf, root, runtime_filter=False)
        else:
            add_file(zf, source, dest_rel=root)
    return missing_variants


def reference_example_manifest() -> list[str]:
    """Every reference-example path the packages ship, for validation."""
    paths = list(REFERENCE_EXAMPLE_JSON)
    paths += REFERENCE_EXAMPLE_PT_FILES
    paths += REFERENCE_EXAMPLE_TREES
    for pdf_dir in ("referencia/exemplo-saida",
                    "referencia/exemplo-saida/en",
                    "referencia/exemplo-saida/es"):
        paths += [f"{pdf_dir}/{name}" for name in REFERENCE_EXAMPLE_PDF_NAMES]
    return paths


def validate_packaging_sources() -> None:
    required = (
        COPILOT_CUSTOMIZATION_ROOTS
        + SHARED_RUNTIME_ROOTS
        + SHARED_CLIENT_ASSETS
        + [source for docs in LANGUAGE_DOCS.values() for source, _ in docs]
        + reference_example_manifest()
    )
    missing = [path for path in required if not (ROOT / path).exists()]
    if missing:
        joined = "\n  - ".join(missing)
        raise FileNotFoundError(f"Missing packaging source files:\n  - {joined}")


def add_reference_examples(zf: zipfile.ZipFile, lang: str) -> None:
    # JSON examples are language-neutral structured outputs.
    for source in REFERENCE_EXAMPLE_JSON:
        add_file(zf, source)

    if lang == "pt":
        example_dir = ROOT / "referencia/exemplo-saida"
        for file_path in sorted(example_dir.glob("*.pdf")):
            add_file(zf, normalized(file_path.relative_to(ROOT)))
        for source in REFERENCE_EXAMPLE_PT_FILES:
            add_file(zf, source)
    elif lang == "en":
        add_tree(zf, "referencia/exemplo-saida/en", runtime_filter=False)
    elif lang == "es":
        add_tree(zf, "referencia/exemplo-saida/es", runtime_filter=False)


def add_pt_documentation(zf: zipfile.ZipFile) -> None:
    excluded_prefixes = (
        ".github/",
        ".git/",
        "docs/",
        "kit-en/",
        "kit-es/",
        "saida/",
        "dist/",
    )
    for file_path in sorted(ROOT.rglob("*.md")):
        rel = normalized(file_path.relative_to(ROOT))
        if rel.startswith(excluded_prefixes) or is_common_excluded(rel):
            continue
        add_file(zf, rel)

    # PT-BR visual guides are intentionally included only in the PT package.
    add_tree(zf, "formularios", runtime_filter=False)
    add_file(zf, "wizard/implementation-guide-wizard.html")
    add_file(zf, "referencia/calculadora-pontuacao.html")


def add_localized_docs(zf: zipfile.ZipFile, lang: str) -> None:
    if lang == "pt":
        add_pt_documentation(zf)
    for source, dest in LANGUAGE_DOCS[lang]:
        add_file(zf, source, dest)
    zf.writestr("PACKAGE-LANGUAGE-NOTES.md", LANGUAGE_NOTES[lang])


def build_archive(lang: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = output_dir / ARCHIVE_NAMES[lang]
    if archive_path.exists():
        archive_path.unlink()

    with zipfile.ZipFile(
        archive_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as zf:
        add_copilot_customizations(zf)
        add_shared_runtime(zf)
        missing_variants = add_shared_client_assets(zf, lang)
        add_reference_examples(zf, lang)
        add_localized_docs(zf, lang)

    if missing_variants:
        print(
            f"WARNING [{lang}]: {len(missing_variants)} language variant(s) "
            f"missing — shipping the PT-BR original instead:",
            file=sys.stderr,
        )
        for variant in missing_variants:
            print(f"  - {variant}", file=sys.stderr)

    validate_primitive_references(archive_path)
    return archive_path


# Repo-relative path references inside .github primitives. A candidate must
# start with a packaged top-level prefix and look like a file path.
PRIMITIVE_PATH_PATTERN = re.compile(
    r"(?<![\w./-])"
    r"((?:\.github|scripts|relatorios|coleta|survey-devs|survey-learning|"
    r"wizard|referencia|formularios|saida|dist|docs|kit-en|kit-es)/"
    r"[\w./À-ɏ-]+)"
)

ROOT_FILE_REFERENCES = re.compile(
    r"(?<![\w./-])(framework\.json|respostas\.json(?:\.example)?|"
    r"implementation-guide-inputs\.json|Makefile|"
    r"respostas-(?:forms|survey-devs|survey-learning)\.xlsx|"
    r"README\.md|GUIA-PASSO-A-PASSO\.md)(?![\w/-])"
)


def is_allowlisted_reference(ref: str) -> bool:
    if ref in PRIMITIVE_REFERENCE_ALLOWLIST:
        return True
    # `ref` arrives without a trailing slash, so re-append one to also match
    # bare directory references such as "saida" against "saida/".
    return f"{ref}/".startswith(PRIMITIVE_REFERENCE_ALLOWLIST_PREFIXES)


def validate_primitive_references(archive_path: Path) -> None:
    """Assert every repo path referenced by packaged .github primitives
    resolves inside the ZIP (or is an allowlisted client input/output)."""
    with zipfile.ZipFile(archive_path) as zf:
        names = set(zf.namelist())
        dir_prefixes = {f"{Path(name).parent.as_posix()}/" for name in names}
        broken: list[tuple[str, str]] = []
        for name in sorted(names):
            if not name.startswith(".github/") or not name.endswith(".md"):
                continue
            text = zf.read(name).decode("utf-8", errors="replace")
            candidates = set(PRIMITIVE_PATH_PATTERN.findall(text))
            candidates |= set(ROOT_FILE_REFERENCES.findall(text))
            for ref in sorted(candidates):
                ref = ref.rstrip("./")
                if ref in names or f"{ref}/" in dir_prefixes:
                    continue
                if any(n.startswith(f"{ref}/") for n in names):
                    continue
                if is_allowlisted_reference(ref):
                    continue
                broken.append((name, ref))
    if broken:
        lines = "\n".join(f"  - {name}: {ref}" for name, ref in broken)
        raise FileNotFoundError(
            f"Copilot primitives in {archive_path.name} reference paths that "
            f"do not exist inside the ZIP:\n{lines}\n"
            f"Fix the reference or add it to the packaging manifest/allowlist "
            f"in scripts/build_language_kits.py."
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build PT, EN, and ES language kit ZIPs."
    )
    parser.add_argument(
        "--out",
        default="dist",
        help="Output directory for generated ZIP files.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete the output directory before building.",
    )
    args = parser.parse_args()

    output_dir = (ROOT / args.out).resolve()
    if args.clean and output_dir.exists():
        shutil.rmtree(output_dir)

    validate_packaging_sources()
    archives = [build_archive(lang, output_dir) for lang in ("pt", "en", "es")]
    for archive in archives:
        size_mb = archive.stat().st_size / (1024 * 1024)
        try:
            display_path = archive.relative_to(ROOT)
        except ValueError:
            display_path = archive
        print(f"{display_path} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
