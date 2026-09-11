#!/usr/bin/env python3
"""
The generation pipeline CLI (learn_togaf.md §1.5) — drafts into content/review/ from the source index.

    python generate.py lessons <unit>                       # one lesson per objective of the unit
    python generate.py glossary                             # the Definitions sections → glossary draft
    python generate.py adm                                  # parsed phase lists + model-filled traps
    python generate.py questions foundation <unit> [--batch]
    python generate.py questions practitioner <unit> [--batch]
    python generate.py figure-questions [--batch]
    python generate.py verify [--batch]                     # independent judge over content/review/

Every subcommand takes --dry-run (print the prompts and input section ids, no API call) and
--limit N. Nothing is generated for an objective with no objective_source row — run
`python sources.py index` after mapping it in resources/sources/objective_sections.yaml.
Runs under api/.venv with PYTHONPATH=api/src and LEARN_TOGAF_ENV defaulting to dev.
"""

import argparse
import os
import sys
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

from learn_togaf import config  # noqa: E402
from learn_togaf.db import apply_schema, connect  # noqa: E402
from learn_togaf.generate import adm, figure_questions, glossary, lessons, questions, verify  # noqa: E402


def _connection():
    connection = connect()
    apply_schema(connection)
    return connection


def cmd_lessons(args: argparse.Namespace) -> None:
    for path in lessons.run(_connection(), config.CONTENT_DIR, args.unit, args.dry_run, args.limit):
        print(f"wrote {path}")


def cmd_glossary(args: argparse.Namespace) -> None:
    path = glossary.run(_connection(), config.CONTENT_DIR, args.dry_run, args.limit)
    if path:
        print(f"wrote {path}")


def cmd_adm(args: argparse.Namespace) -> None:
    for path in adm.run(_connection(), config.CONTENT_DIR, args.dry_run, args.limit):
        print(f"wrote {path}")


def cmd_questions(args: argparse.Namespace) -> None:
    path = questions.run(
        _connection(),
        config.CONTENT_DIR,
        args.exam,
        args.unit,
        args.dry_run,
        args.limit,
        args.batch,
        args.count,
    )
    if path:
        print(f"wrote {path}")


def cmd_figure_questions(args: argparse.Namespace) -> None:
    path = figure_questions.run(_connection(), config.CONTENT_DIR, args.dry_run, args.limit, args.batch)
    if path:
        print(f"wrote {path}")


def cmd_verify(args: argparse.Namespace) -> None:
    print(verify.run(_connection(), config.CONTENT_DIR, args.dry_run, args.limit, args.batch))


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--dry-run", action="store_true", help="print the prompts and section ids; no API call"
    )
    common.add_argument("--limit", type=int, help="only the first N objectives / items")
    sub = parser.add_subparsers(dest="command", required=True)

    lessons_parser = sub.add_parser("lessons", parents=[common], help="draft lessons for a unit")
    lessons_parser.add_argument("unit")
    lessons_parser.set_defaults(func=cmd_lessons)
    sub.add_parser("glossary", parents=[common], help="draft the glossary").set_defaults(func=cmd_glossary)
    sub.add_parser("adm", parents=[common], help="draft the ADM traps and cross-references").set_defaults(
        func=cmd_adm
    )
    questions_parser = sub.add_parser("questions", parents=[common], help="draft a question set for a unit")
    questions_parser.add_argument("exam", choices=["foundation", "practitioner"])
    questions_parser.add_argument("unit")
    questions_parser.add_argument("--batch", action="store_true", help="use the Message Batches API")
    questions_parser.add_argument(
        "--count", type=int, default=questions.DEFAULT_PER_OBJECTIVE, help="questions per objective"
    )
    questions_parser.set_defaults(func=cmd_questions)
    figures_parser = sub.add_parser(
        "figure-questions", parents=[common], help="draft figure questions for mapped figures"
    )
    figures_parser.add_argument("--batch", action="store_true")
    figures_parser.set_defaults(func=cmd_figure_questions)
    verify_parser = sub.add_parser("verify", parents=[common], help="judge every draft under content/review/")
    verify_parser.add_argument("--batch", action="store_true")
    verify_parser.set_defaults(func=cmd_verify)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
