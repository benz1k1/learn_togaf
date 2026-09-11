"""
Shared fixtures for the live-server suite (learn_togaf.md §8): every test drives the app already
running on 127.0.0.1:5014 over httpx. Never TestClient.

``csrf(client)`` fetches ``/`` so the ``lt_session`` cookie is set and derives the token exactly
as ``pages/security.token_for`` does; ``post(client, path, data)`` sends a form POST with it.
Other feature suites import these helpers.
"""

import hashlib
import hmac
import os
import sqlite3
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import httpx
import pytest

os.environ.setdefault("LEARN_TOGAF_ENV", "dev")
_SRC = str(Path(__file__).resolve().parents[1] / "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

from learn_togaf.config import CSRF_SECRET  # noqa: E402
from learn_togaf.db import connect  # noqa: E402

BASE_URL = "http://127.0.0.1:5014"
SESSION_COOKIE = "lt_session"
CSRF_HEADER = "X-CSRF-Token"


@pytest.fixture(scope="session")
def client() -> httpx.Client:
    with httpx.Client(base_url=BASE_URL, timeout=30, follow_redirects=False) as session:
        try:
            response = session.get("/")
        except httpx.ConnectError:
            pytest.fail(f"No server on {BASE_URL}. Start it: python start.py")
        if response.status_code != 200:
            pytest.fail(f"GET / returned {response.status_code}; the server is not healthy")
        yield session


def csrf(client: httpx.Client) -> str:
    """The token the CSRF middleware expects: HMAC-SHA256 of the session cookie under the configured secret."""
    if SESSION_COOKIE not in client.cookies:
        client.get("/")
    session = client.cookies.get(SESSION_COOKIE)
    if not session:
        pytest.fail("GET / did not set the lt_session cookie")
    return hmac.new(CSRF_SECRET.encode("utf-8"), session.encode("utf-8"), hashlib.sha256).hexdigest()


@pytest.fixture(scope="session")
def db() -> Iterator[sqlite3.Connection]:
    """The same SQLite file the server uses; tests read from it and only write learner state
    they created themselves (or time-travel an attempt's clock)."""
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()


def post(
    client: httpx.Client, path: str, data: dict[str, Any] | None = None, htmx: bool = False, **kwargs: Any
) -> httpx.Response:
    """Form POST with the CSRF header (the way htmx sends it). Extra kwargs go to httpx (files=, json=, headers=)."""
    headers = {CSRF_HEADER: csrf(client), **kwargs.pop("headers", {})}
    if htmx:
        headers["HX-Request"] = "true"
    return client.post(path, data=data, headers=headers, **kwargs)


def get(client: httpx.Client, path: str, htmx: bool = False) -> httpx.Response:
    headers = {"HX-Request": "true"} if htmx else {}
    return client.get(path, headers=headers)
