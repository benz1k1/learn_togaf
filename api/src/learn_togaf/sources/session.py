"""
The learner's Open Group session (learn_togaf.md §1.4).

``login`` opens the publication URL in Playwright, fills the SSO form when its fields are found,
waits for the learner to finish whatever the identity provider asks for, and saves the browser
storage state to ``resources/sources/session.json``. ``fetch`` and ``figures`` reuse the cookies
from that file in an ``httpx`` client — the browser is only ever used to log in.
"""

import sys
from pathlib import Path

import httpx
import orjson
from loguru import logger
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

from learn_togaf.config import SOURCES_BROWSER_EXECUTABLE, SOURCES_DIR, SOURCES_USER_AGENT

SESSION_FILE = SOURCES_DIR / "session.json"
LOGIN_HOST = "identity.opengroup.org"
# The Open Group SSO is a WSO2 identity server: the VISIBLE username box is #usernameUserInput
# (a hidden #username sits beside it and must not be matched first), the password is #password
# and the submit button is #sign-in-button. Generic names follow for a changed form.
USERNAME_SELECTORS = (
    "#usernameUserInput",
    "input[name='email']",
    "input[type='email']",
    "input[name='username']:visible",
)
PASSWORD_SELECTORS = ("#password", "input[name='password']", "input[type='password']")
SUBMIT_SELECTORS = ("#sign-in-button", "button[type='submit']", "input[type='submit']")


class LoginRequired(RuntimeError):
    """A fetch was redirected to the identity provider: the saved session is missing or stale."""


def _storage_state() -> dict:
    if not SESSION_FILE.is_file():
        raise LoginRequired(f"No saved session at {SESSION_FILE}. Run: python sources.py login")
    return orjson.loads(SESSION_FILE.read_bytes())


def session_cookies() -> httpx.Cookies:
    cookies = httpx.Cookies()
    for cookie in _storage_state().get("cookies", []):
        cookies.set(
            cookie["name"], cookie["value"], domain=cookie.get("domain", ""), path=cookie.get("path", "/")
        )
    return cookies


def http_client() -> httpx.Client:
    """One polite client for the crawl: the saved cookies, the configured User-Agent, redirects
    followed so a bounce to the identity provider is visible on ``response.url``."""
    return httpx.Client(
        cookies=session_cookies(),
        headers={"User-Agent": SOURCES_USER_AGENT},
        follow_redirects=True,
        timeout=60.0,
    )


def is_login_redirect(response: httpx.Response) -> bool:
    """True only when the response ENDS on the identity provider (its login form).

    A hop through it that comes back to the requested page is the SSO renewing the publication
    site's own session cookie from the identity cookies — a successful silent re-login, not a
    failure — and the crawl carries the renewed cookie in its jar from then on."""
    return response.url.host == LOGIN_HOST


def login(login_url: str, credentials: tuple[str, str] | None, headless: bool) -> Path:
    """Open the login page, fill the form if it is there, wait for the learner, save the state."""
    with sync_playwright() as playwright:
        try:
            launch_options: dict = {"headless": headless}
            if SOURCES_BROWSER_EXECUTABLE:
                launch_options["executable_path"] = SOURCES_BROWSER_EXECUTABLE
            browser = playwright.chromium.launch(**launch_options)
        except PlaywrightError as exc:
            raise SystemExit(
                "Playwright could not start Chromium. Install the browser once with:\n"
                "    cd api && .venv/bin/python -m playwright install chromium\n"
                f"({exc.__class__.__name__}: {str(exc).splitlines()[0]})"
            ) from exc
        context = browser.new_context(user_agent=SOURCES_USER_AGENT)
        page = context.new_page()
        page.goto(login_url, wait_until="domcontentloaded")
        if credentials is not None:
            username, password = credentials
            user_field = next((page.locator(s) for s in USERNAME_SELECTORS if page.locator(s).count()), None)
            password_field = next(
                (page.locator(s) for s in PASSWORD_SELECTORS if page.locator(s).count()), None
            )
            if user_field is not None and password_field is not None:
                user_field.first.fill(username)
                password_field.first.fill(password)
                submit = next((page.locator(s) for s in SUBMIT_SELECTORS if page.locator(s).count()), None)
                if submit is not None:
                    submit.first.click()
                else:
                    password_field.first.press("Enter")
                logger.info(
                    "submitted the Open Group SSO form; waiting for the bounce back to the publication"
                )
                try:
                    page.wait_for_url(lambda url: LOGIN_HOST not in url, timeout=45_000)
                except PlaywrightError:
                    raise SystemExit(
                        f"login did not leave {LOGIN_HOST} within 45 s — wrong credentials, or the identity "
                        f"provider asked for a step the form cannot answer (run without --headless to see it). "
                        f"Page now: {page.url}"
                    ) from None
            else:
                logger.info("SSO form fields not found on the page; complete the login by hand")
        print(
            "Complete the login in the browser window, then press Enter here to save the session.",
            file=sys.stderr,
        )
        if headless:
            page.wait_for_timeout(5000)
        else:
            input()
        SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
        context.storage_state(path=str(SESSION_FILE))
        browser.close()
    SESSION_FILE.chmod(0o600)
    logger.info(f"session saved to {SESSION_FILE}")
    return SESSION_FILE
