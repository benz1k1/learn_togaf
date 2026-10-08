"""
SQLite access (learn_togaf.md §3, §5): one connection per request, WAL, foreign keys on,
``schema.sql`` applied at start-up. Rows come back as ``sqlite3.Row`` so controllers index by
column name; JSON columns are decoded by the service that owns them.
"""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from learn_togaf.config import DB_PATH

_SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def connect(path: Path = DB_PATH) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=30, isolation_level=None, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 30000")
    return connection


# Columns added after a table first shipped. ``CREATE TABLE IF NOT EXISTS`` leaves an existing
# table alone, so each is added here when missing; the content loader then rebuilds the rows.
_ADDED_COLUMNS: tuple[tuple[str, str, str], ...] = (
    ("learning_unit", "track", "TEXT NOT NULL DEFAULT 'TOGAF'"),
    ("learning_unit", "scoring", "TEXT NOT NULL DEFAULT ''"),
    ("question", "track", "TEXT NOT NULL DEFAULT 'TOGAF'"),
    ("question", "scoring", "TEXT NOT NULL DEFAULT 'single'"),
    ("adm_phase", "crosswalk", "TEXT NOT NULL DEFAULT ''"),
    ("adm_artefact", "archimate", "TEXT NOT NULL DEFAULT ''"),
    ("example_document", "track", "TEXT NOT NULL DEFAULT 'TOGAF'"),
    ("example_document", "figure", "TEXT NOT NULL DEFAULT ''"),
    ("example_document", "viewpoint", "TEXT NOT NULL DEFAULT ''"),
    ("example_document", "artefacts", "TEXT NOT NULL DEFAULT '[]'"),
)


def apply_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(_SCHEMA_PATH.read_text(encoding="utf-8"))
    for table, column, definition in _ADDED_COLUMNS:
        present = {row["name"] for row in connection.execute(f"PRAGMA table_info({table})")}
        if column not in present:
            connection.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


@contextmanager
def transaction(connection: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    """An explicit transaction on an autocommit connection: every write path uses this so a
    half-applied content load or import never lands."""
    connection.execute("BEGIN IMMEDIATE")
    try:
        yield connection
    except BaseException:
        connection.execute("ROLLBACK")
        raise
    else:
        connection.execute("COMMIT")


@contextmanager
def open_db() -> Iterator[sqlite3.Connection]:
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()
