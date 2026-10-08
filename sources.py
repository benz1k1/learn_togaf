#!/usr/bin/env python3
"""
The source store CLI (learn_togaf.md §1.4).

    python sources.py init-key                 # ~/learn_togaf.yaml with a new Fernet key (refuses to overwrite)
    python sources.py encrypt                  # prompt for a plaintext, print the Fernet token
    python sources.py encrypt --set opengroup.password    # …and write it into the env YAML in place
    python sources.py login [--headless]       # Playwright: Open Group SSO → resources/sources/session.json
    python sources.py fetch [--limit N] [--root togaf|archimate]   # crawl into resources/sources/html/
    python sources.py pdf                      # register PDFs placed under resources/sources/pdf/
    python sources.py index                    # HTML + PDF → source_* tables, text/, objective_source, ADM diff
    python sources.py figures                  # every diagram → resources/sources/figures/ + source_figure

Runs under the api venv (api/.venv/bin/python) with PYTHONPATH=api/src and LEARN_TOGAF_ENV
defaulting to dev; re-executes itself under that interpreter when ``learn_togaf`` is not
importable from the current one. Never fetches the PDFs (they are purchases) and never commits
text: the store is gitignored except manifest.yaml and figures/important.yaml.
"""

import argparse
import getpass
import os
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
API_DIR = REPO_ROOT / "api"
VENV_PYTHON = API_DIR / ".venv" / "bin" / "python"


def _reexec_in_venv() -> None:
    os.environ.setdefault("LEARN_TOGAF_ENV", "dev")
    src = str(API_DIR / "src")
    existing = os.environ.get("PYTHONPATH", "")
    if src not in existing.split(os.pathsep):
        os.environ["PYTHONPATH"] = f"{src}{os.pathsep}{existing}" if existing else src
    try:
        import learn_togaf  # noqa: F401
    except ImportError:
        if not VENV_PYTHON.is_file():
            raise SystemExit(f"No venv at {VENV_PYTHON}. Run: cd api && uv sync") from None
        if Path(sys.executable).resolve() == VENV_PYTHON.resolve():
            raise
        os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])


_reexec_in_venv()

import yaml  # noqa: E402
from cryptography.fernet import Fernet  # noqa: E402
from loguru import logger  # noqa: E402

from learn_togaf import config  # noqa: E402
from learn_togaf.content.loader import load_blueprint  # noqa: E402
from learn_togaf.db import apply_schema, connect  # noqa: E402
from learn_togaf.sources import fetch as fetch_module  # noqa: E402
from learn_togaf.sources import figures as figures_module  # noqa: E402
from learn_togaf.sources import index as index_module  # noqa: E402
from learn_togaf.sources import parse_pdf, session  # noqa: E402
from learn_togaf.sources.manifest import PdfEntry, load_manifest, save_manifest  # noqa: E402
from learn_togaf.sources.parse_html import ParsedPage, parse_page  # noqa: E402


# ---------------------------------------------------------------- init-key / encrypt
def cmd_init_key(args: argparse.Namespace) -> None:
    path = config.FERNET_KEY_FILE
    if path.exists():
        raise SystemExit(
            f"{path} already exists; refusing to overwrite a Fernet key (the tokens in the env YAML depend on it)."
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    key = Fernet.generate_key().decode()
    with open(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "w", encoding="utf-8") as handle:
        handle.write(
            f'# Learn TOGAF Fernet key (learn_togaf.md §10). Keep it out of the repo.\nfernet_key: "{key}"\n'
        )
    print(f"wrote {path} (mode 600)")


def _set_env_value(dotted: str, token: str) -> Path:
    """Replace the value of a nested key in the env YAML with a targeted line edit, so comments
    and layout survive (a yaml dump would flatten them)."""
    path = config.ENV_FILE
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    keys = dotted.split(".")
    depth = 0
    for index, line in enumerate(lines):
        stripped = line.lstrip(" ")
        indent = (len(line) - len(stripped)) // 2
        match = re.match(r"^([A-Za-z0-9_\-]+):(.*)$", stripped)
        if not match or indent != depth or match.group(1) != keys[depth]:
            continue
        depth += 1
        if depth == len(keys):
            lines[index] = f'{" " * (indent * 2)}{keys[-1]}: "{token}"\n'
            path.write_text("".join(lines), encoding="utf-8")
            return path
    raise SystemExit(f"key {dotted} not found in {path}")


def cmd_encrypt(args: argparse.Namespace) -> None:
    plain = getpass.getpass("plaintext: ")
    if not plain:
        raise SystemExit("nothing to encrypt")
    token = config.fernet_encrypt(plain)
    print(token)
    if args.set:
        print(f"written to {args.set} in {_set_env_value(args.set, token)}")


# ---------------------------------------------------------------- login / fetch / pdf
def cmd_login(args: argparse.Namespace) -> None:
    credentials: tuple[str, str] | None
    try:
        credentials = config.opengroup_credentials()
    except ValueError as exc:
        logger.warning(f"{exc}; the form will not be pre-filled")
        credentials = None
    session.login(config.SOURCES_LOGIN_URL, credentials, headless=args.headless)


# Crawl roots: the TOGAF Digital Edition (many documents under one site) and the ArchiMate
# specification (one flat document, segment "archimate"). Both use the same saved session.
CRAWL_ROOTS = {
    "togaf": (config.SOURCES_BASE_URL, None),
    "archimate": (config.SOURCES_ARCHIMATE_URL, "archimate"),
}


def cmd_fetch(args: argparse.Namespace) -> None:
    manifest = load_manifest(config.SOURCES_DIR)
    roots = list(CRAWL_ROOTS) if args.root == "all" else [args.root]
    try:
        with session.http_client() as client:
            for name in roots:
                base_url, root_segment = CRAWL_ROOTS[name]
                report = fetch_module.crawl(
                    client,
                    base_url,
                    config.SOURCES_DIR,
                    manifest,
                    config.SOURCES_DELAY_SECONDS,
                    args.limit,
                    root_segment=root_segment,
                )
                save_manifest(config.SOURCES_DIR, manifest)
                print(f"{name}: {report.summary()}")
                for page in report.pages:
                    print(f"  saved {page}")
    except session.LoginRequired as exc:
        save_manifest(config.SOURCES_DIR, manifest)
        raise SystemExit(str(exc)) from exc


def cmd_pdf(args: argparse.Namespace) -> None:
    manifest = load_manifest(config.SOURCES_DIR)
    pdf_dir = config.SOURCES_DIR / "pdf"
    paths = (
        sorted(pdf_dir.glob("*.pdf"))
        + sorted(pdf_dir.glob("guides/*.pdf"))
        + sorted(pdf_dir.glob("wp/*.pdf"))
        + sorted(pdf_dir.glob("sabsa/*.pdf"))
    )
    if not paths:
        raise SystemExit(
            f"no PDFs under {pdf_dir}: place the licensed downloads there as <doc>.pdf (adm.pdf, guides/<slug>.pdf,"
            f" wp/w117.pdf, wp/w14c.pdf, wp/w172.pdf, sabsa.pdf, sabsa/bluebook.pdf)"
        )
    for path in paths:
        segment = f"{path.parent.name}/{path.stem}" if path.parent != pdf_dir else path.stem
        code = index_module.document_code(segment)
        if code is None:
            print(
                f"  {path.name}: not a known document segment ({', '.join(index_module.SEGMENT_CODES)} or guides/<slug>); skipped"
            )
            continue
        info = parse_pdf.register_pdf(path)
        entry = manifest.document(segment, code=code, kind=index_module.document_kind(code))
        entry.pdf = PdfEntry(
            path=str(path.relative_to(config.SOURCES_DIR)),
            title=info.title,
            page_count=info.page_count,
            hash=info.hash,
            registered_at=datetime.now(UTC).isoformat(timespec="seconds"),
        )
        print(f"  {segment}: {info.title!r}, {info.page_count} pages, {len(info.outline)} outline entries")
    save_manifest(config.SOURCES_DIR, manifest)


# ---------------------------------------------------------------- index
def cmd_index(args: argparse.Namespace) -> None:
    manifest = load_manifest(config.SOURCES_DIR)
    connection = connect()
    apply_schema(connection)
    indexed = 0
    for segment, document in manifest.documents.items():
        code = index_module.document_code(segment)
        if code is None:
            continue
        pdf_pages: dict[str, int] = {}
        pdf_path = None
        if document.pdf is not None:
            pdf_path = str(config.SOURCES_DIR / document.pdf.path)
            pdf_pages = parse_pdf.outline_pages(parse_pdf.register_pdf(Path(pdf_path)))
        pages = []
        for page, entry in document.pages.items():
            path = fetch_module.html_path(config.SOURCES_DIR, segment, page)
            if path.is_file():
                pages.append(parse_page(path.read_text(encoding="utf-8", errors="replace"), code, entry.url))
        if pages:
            index_module.index_document(connection, code, pages, pdf_pages, pdf_path)
            indexed += 1
        elif pdf_path is not None:
            info = parse_pdf.register_pdf(Path(pdf_path))
            sections = parse_pdf.sections_from_outline(Path(pdf_path), code, info)
            index_module.index_document(
                connection, code, [ParsedPage(code, "", info.title, sections)], {}, pdf_path
            )
            indexed += 1
    if not indexed:
        raise SystemExit("nothing indexed: run `python sources.py fetch` (and `pdf`) first")
    written = index_module.write_text_files(connection, config.SOURCES_DIR)
    print(f"indexed {indexed} document(s); wrote {written} section files under {config.SOURCES_DIR / 'text'}")

    mapping = index_module.load_objective_mapping(config.SOURCES_DIR / index_module.OBJECTIVE_MAPPING_FILE)
    blueprint = load_blueprint(config.CONTENT_DIR)
    counts = index_module.apply_objective_mapping(connection, mapping, blueprint.objective_codes())
    empty = sorted(code for code, count in counts.items() if count == 0)
    print(
        f"objective_source: {sum(counts.values())} rows for {len(counts)} objectives; {len(empty)} matched nothing: {empty}"
    )
    unmapped = sorted(blueprint.objective_codes() - set(mapping))
    if unmapped:
        print(f"objectives with no entry in objective_sections.yaml: {unmapped}")

    parsed = index_module.parse_adm_phases(connection)
    if parsed:
        with open(config.CONTENT_DIR / "adm" / "phases.yaml", encoding="utf-8") as handle:
            authored = yaml.safe_load(handle) or []
        differences = index_module.diff_adm_phases(parsed, authored)
        path = index_module.write_parsed_phases(config.CONTENT_DIR, parsed)
        print(
            f"ADM phases: parsed {len(parsed)}; {len(differences)} difference(s) against adm/phases.yaml; written to {path}"
        )
        for line in differences:
            print(f"  {line}")
    else:
        print("ADM phases: no ADM phase chapters indexed (nothing to diff)")


# ---------------------------------------------------------------- figures
def cmd_figures(args: argparse.Namespace) -> None:
    manifest = load_manifest(config.SOURCES_DIR)
    connection = connect()
    apply_schema(connection)
    important = figures_module.important_ids(config.SOURCES_DIR)
    figures_dir = config.SOURCES_DIR / "figures"
    per_segment = figures_module.html_figures(config.SOURCES_DIR, manifest, index_module.document_code)
    total = 0
    with session.http_client() as client:
        for segment, figures in per_segment.items():
            try:
                records = figures_module.download_figures(
                    client, figures, figures_dir / segment, config.SOURCES_DELAY_SECONDS
                )
            except session.LoginRequired as exc:
                raise SystemExit(str(exc)) from exc
            total += figures_module.record_figures(connection, records, important)
            manifest.documents[segment].figure_counts["html"] = len(records)
    for segment, document in manifest.documents.items():
        code = index_module.document_code(segment)
        if document.pdf is None or code is None:
            continue
        records = figures_module.pdf_figures(
            config.SOURCES_DIR / document.pdf.path, code, figures_dir / segment
        )
        total += figures_module.record_figures(connection, records, important)
        document.figure_counts["pdf"] = len(records)
    save_manifest(config.SOURCES_DIR, manifest)
    print(f"recorded {total} figures")
    for segment, document in manifest.documents.items():
        if document.figure_counts:
            html_count, pdf_count = (
                document.figure_counts.get("html", 0),
                document.figure_counts.get("pdf", 0),
            )
            flag = "" if html_count == pdf_count else "   <- mismatch"
            print(f"  {segment}: html={html_count} pdf={pdf_count}{flag}")
    missing = sorted(important - {row["id"] for row in connection.execute("SELECT id FROM source_figure")})
    if missing:
        print(f"important.yaml ids with no stored figure: {missing}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init-key", help="create the Fernet key file named by fernet.key_file").set_defaults(
        func=cmd_init_key
    )
    encrypt = sub.add_parser("encrypt", help="encrypt a secret for the env YAML")
    encrypt.add_argument(
        "--set", metavar="DOTTED.KEY", help="also write the token into the env YAML, e.g. opengroup.password"
    )
    encrypt.set_defaults(func=cmd_encrypt)
    login = sub.add_parser("login", help="log in to the Open Group SSO with Playwright and save the session")
    login.add_argument("--headless", action="store_true")
    login.set_defaults(func=cmd_login)
    fetch = sub.add_parser("fetch", help="crawl the Digital Edition and the ArchiMate specification")
    fetch.add_argument("--limit", type=int, help="stop after N requests per root (a partial run)")
    fetch.add_argument("--root", choices=["all", *CRAWL_ROOTS], default="all", help="which site to crawl")
    fetch.set_defaults(func=cmd_fetch)
    sub.add_parser("pdf", help="register the PDFs under resources/sources/pdf/").set_defaults(func=cmd_pdf)
    sub.add_parser("index", help="build the source index").set_defaults(func=cmd_index)
    sub.add_parser("figures", help="download every diagram").set_defaults(func=cmd_figures)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
