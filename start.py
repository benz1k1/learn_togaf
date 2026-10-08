#!/usr/bin/env python3
"""
Start Learn TOGAF locally (learn_togaf.md §5).

    python start.py                    # granian --reload on 5014 (127.0.0.1)
    python start.py --load-content     # rebuild the content cache from content/ first
    python start.py --reset-progress   # wipe the learner's state (attempts, cards, notes, plan), keep content
    python start.py --stop             # stop whatever is on the port
    python start.py --port 5015

Port 5014 is chosen against the workspace map (loylty_program 5012, clowreed 5000, ten_tail
5002, rocket 5006, media_box 5007, MOS 5008).
"""

import argparse
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
API_DIR = REPO_ROOT / "api"
VENV_PYTHON = API_DIR / ".venv" / "bin" / "python"
LOG_DIR = REPO_ROOT / "logs"
DEFAULT_PORT = 5014


def _python() -> str:
    if not VENV_PYTHON.is_file():
        raise SystemExit(f"No venv at {VENV_PYTHON}. Run: cd api && uv sync")
    return str(VENV_PYTHON)


def _environment(profile: str) -> dict[str, str]:
    environment = dict(os.environ)
    environment.setdefault("LEARN_TOGAF_ENV", profile)
    src = str(API_DIR / "src")
    existing = environment.get("PYTHONPATH", "")
    environment["PYTHONPATH"] = f"{src}:{existing}" if existing else src
    return environment


def _pids_on_port(port: int) -> list[int]:
    result = subprocess.run(["lsof", "-t", f"-i:{port}"], capture_output=True, text=True)
    return [int(line) for line in result.stdout.split() if line.strip().isdigit()]


def stop(port: int, wait_seconds: int = 15) -> None:
    for pid in _pids_on_port(port):
        print(f"  killing pid {pid} on port {port}")
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    deadline = time.time() + wait_seconds
    while time.time() < deadline and _pids_on_port(port):
        time.sleep(0.5)
    for pid in _pids_on_port(port):
        os.kill(pid, signal.SIGKILL)


def load_content(environment: dict[str, str]) -> None:
    code = (
        "from learn_togaf.config import CONTENT_DIR\n"
        "from learn_togaf.db import apply_schema, connect\n"
        "from learn_togaf.content.loader import load_all\n"
        "c = connect(); apply_schema(c); print(load_all(c, CONTENT_DIR).summary())\n"
    )
    subprocess.run([_python(), "-c", code], cwd=API_DIR, env=environment, check=True)


LEARNER_STATE_TABLES = (
    "attempt_answer",
    "attempt",
    "card_review",
    "note",
    "study_session",
    "lesson_progress",
    "setting",
)


def reset_progress(environment: dict[str, str]) -> None:
    """Delete every learner-state row (learn_togaf.md §3) and nothing else: the content cache and
    the source index are rebuilt from files, but this is the one thing the learner owns."""
    code = (
        "from learn_togaf.db import apply_schema, connect, transaction\n"
        f"tables = {LEARNER_STATE_TABLES!r}\n"
        "c = connect(); apply_schema(c)\n"
        "with transaction(c):\n"
        "    for t in tables: print(t, c.execute(f'DELETE FROM {t}').rowcount, 'rows deleted')\n"
    )
    subprocess.run([_python(), "-c", code], cwd=API_DIR, env=environment, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--profile", default="dev", help="LEARN_TOGAF_ENV profile (resources/env/<profile>/.env.yaml)")
    parser.add_argument("--load-content", action="store_true")
    parser.add_argument("--reset-progress", action="store_true", help="delete the learner's state, then exit")
    parser.add_argument("--no-reload", action="store_true")
    parser.add_argument("--stop", action="store_true")
    args = parser.parse_args()

    if args.stop:
        stop(args.port)
        return

    environment = _environment(args.profile)
    LOG_DIR.mkdir(exist_ok=True)
    if args.reset_progress:
        reset_progress(environment)
        return
    if args.load_content:
        load_content(environment)
    if _pids_on_port(args.port):
        print(f"port {args.port} is busy; stopping the previous server")
        stop(args.port)
    # Granian (Rust ASGI server). PYTHONPATH already points at api/src via _environment().
    command = [
        _python(), "-m", "granian", "--interface", "asgi", "learn_togaf.main:app",
        "--host", args.host, "--port", str(args.port),
    ]
    if not args.no_reload:
        # Watches every file under src, so Jinja template edits reload too.
        command += ["--reload", "--reload-paths", str(API_DIR / "src")]
    print(f"Learn TOGAF on http://{args.host}:{args.port}")
    try:
        subprocess.run(command, cwd=API_DIR, env=environment, check=False)
    except KeyboardInterrupt:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
