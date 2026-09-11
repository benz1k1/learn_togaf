"""FastAPI dependencies: one SQLite connection per request (learn_togaf.md §5)."""

import sqlite3
from collections.abc import Iterator

from learn_togaf.db import connect


def get_db() -> Iterator[sqlite3.Connection]:
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()
