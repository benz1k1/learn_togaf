"""
CSRF for the pages (learn_togaf.md §10): signed double-submit, pure-ASGI middleware.

There is one learner and no login, but the app is still a browser app on a laptop that also
browses the web, and a cross-site form post to ``/import/confirm`` or ``/attempt/1/finish`` is
exactly what CSRF is. So: a random ``lt_session`` cookie is set on first visit, the token is an
HMAC of it under ``security.csrf_secret``, ``base.html`` puts the token on ``<body>`` as an
htmx header and plain forms carry it as a hidden field, and every unsafe method on a page route
must present it. ``/api/*`` is JSON used only by the pages and is checked the same way (the
header is inherited by every htmx call).

Pure ASGI, not ``BaseHTTPMiddleware``: the latter consumes the body to read the form and the
handler then receives an empty one. This reads the body once and replays it.
"""

import hashlib
import hmac
import secrets
from urllib.parse import parse_qs

from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from learn_togaf.config import CSRF_SECRET

SESSION_COOKIE = "lt_session"
CSRF_FORM_FIELD = "csrf_token"
CSRF_HEADER = "x-csrf-token"
UNSAFE_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})


def token_for(session: str) -> str:
    return hmac.new(CSRF_SECRET.encode("utf-8"), session.encode("utf-8"), hashlib.sha256).hexdigest()


def csrf_token(request: Request) -> str:
    session = request.cookies.get(SESSION_COOKIE) or getattr(request.state, "new_session", "")
    return token_for(session) if session else ""


class CsrfMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        request = Request(scope)
        session = request.cookies.get(SESSION_COOKIE) or ""
        new_session = ""
        if not session:
            new_session = secrets.token_urlsafe(32)
            session = new_session
            scope.setdefault("state", {})["new_session"] = new_session

        if request.method in UNSAFE_METHODS and not scope["path"].startswith("/static/"):
            body = b""
            more = True
            while more:
                message = await receive()
                body += message.get("body", b"")
                more = message.get("more_body", False)
            submitted = request.headers.get(CSRF_HEADER, "")
            if not submitted and request.headers.get("content-type", "").startswith(
                "application/x-www-form-urlencoded"
            ):
                submitted = (parse_qs(body.decode("utf-8", errors="replace")).get(CSRF_FORM_FIELD) or [""])[0]
            if not submitted and request.headers.get("content-type", "").startswith("multipart/form-data"):
                # The wizard uploads a file; the token travels in the header htmx adds. A plain
                # multipart form must include the hidden field, which we find without parsing
                # the whole body.
                marker = f'name="{CSRF_FORM_FIELD}"'.encode()
                index = body.find(marker)
                if index >= 0:
                    tail = body[index + len(marker) :].split(b"\r\n\r\n", 1)
                    if len(tail) == 2:
                        submitted = tail[1].split(b"\r\n", 1)[0].decode("utf-8", errors="replace").strip()
            if not new_session and hmac.compare_digest(token_for(session), submitted):
                pass
            else:
                response = PlainTextResponse(
                    "CSRF token missing or invalid. Reload the page and try again.", status_code=403
                )
                await response(scope, receive, send)
                return

            replayed = False

            async def replay() -> Message:
                nonlocal replayed
                if replayed:
                    return {"type": "http.request", "body": b"", "more_body": False}
                replayed = True
                return {"type": "http.request", "body": body, "more_body": False}

            receive = replay

        async def send_with_cookie(message: Message) -> None:
            if new_session and message["type"] == "http.response.start":
                headers = list(message.get("headers", []))
                cookie = f"{SESSION_COOKIE}={new_session}; Path=/; HttpOnly; SameSite=Lax"
                headers.append((b"set-cookie", cookie.encode("latin-1")))
                message["headers"] = headers
            await send(message)

        await self.app(scope, receive, send_with_cookie)
