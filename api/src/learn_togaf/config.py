"""
Configuration (learn_togaf.md §5, §10).

The env file is nested **YAML**, not dotenv, loaded once at import. Required keys are read
through :func:`_require`, which raises when the key is missing or empty: there is no code
default for any of them and nothing re-reads a configured value from ``os.environ``.

Secrets (``opengroup.password``, ``anthropic.api_key``) are Fernet tokens. The key is NOT in the
env file: ``fernet.key_file`` names a YAML file in the user's home directory holding
``fernet_key``, so the env file can be shared and the key cannot leave the machine by accident.
Secrets are decrypted lazily by the CLI that needs them (``sources.py``, ``generate.py``), never
at app start-up, so the study app runs before a password has been pasted in.
"""

import os
from pathlib import Path
from typing import Any

import yaml
from cryptography.fernet import Fernet, InvalidToken

_REPO_ROOT = Path(__file__).resolve().parents[3]


def _resolve_env_file() -> Path:
    explicit = (os.getenv("LEARN_TOGAF_ENV_YAML") or "").strip()
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        if not path.is_file():
            raise ValueError(f"LEARN_TOGAF_ENV_YAML file not found: {path}")
        return path
    profile = (os.getenv("LEARN_TOGAF_ENV") or "").strip()
    if not profile:
        raise ValueError(
            "Neither LEARN_TOGAF_ENV_YAML nor LEARN_TOGAF_ENV is set. Export LEARN_TOGAF_ENV=dev, "
            "or LEARN_TOGAF_ENV_YAML=/absolute/path/to/.env.yaml."
        )
    path = _REPO_ROOT / "resources" / "env" / profile / ".env.yaml"
    if not path.is_file():
        raise ValueError(
            f"LEARN_TOGAF_ENV={profile} resolves to {path}, which does not exist. "
            f"Copy resources/env/dev/.env.yaml.example to it."
        )
    return path


def _load_yaml(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must be a YAML mapping at the top level")
    return data


def _nested_get(root: Any, *keys: str) -> Any:
    node = root
    for key in keys:
        if not isinstance(node, dict) or key not in node:
            return None
        node = node[key]
    return node


ENV_FILE = _resolve_env_file()
SETTINGS: dict[str, Any] = _load_yaml(ENV_FILE)


def _scalar_str(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return str(value).strip()


def _require(*keys: str) -> str:
    value = _scalar_str(_nested_get(SETTINGS, *keys))
    if not value:
        raise ValueError(f"Missing required config: {'.'.join(keys)}. Set it in {ENV_FILE}.")
    return value


def _opt_str(*keys: str, default: str) -> str:
    return _scalar_str(_nested_get(SETTINGS, *keys)) or default


def _opt_int(*keys: str, default: int) -> int:
    value = _scalar_str(_nested_get(SETTINGS, *keys))
    return int(value) if value else default


def _opt_float(*keys: str, default: float) -> float:
    value = _scalar_str(_nested_get(SETTINGS, *keys))
    return float(value) if value else default


# ------------------------------------------------------------------ Fernet key (home directory)
FERNET_KEY_FILE = Path(_require("fernet", "key_file")).expanduser()


def fernet_key() -> str:
    """The key from ``fernet.key_file``. Read on demand so the app starts without it."""
    if not FERNET_KEY_FILE.is_file():
        raise ValueError(
            f"Fernet key file {FERNET_KEY_FILE} (fernet.key_file in {ENV_FILE}) does not exist. "
            f"Create it with: python sources.py init-key"
        )
    key = _scalar_str(_load_yaml(FERNET_KEY_FILE).get("fernet_key"))
    if not key:
        raise ValueError(f"{FERNET_KEY_FILE} has no fernet_key")
    return key


def fernet_encrypt(plain: str) -> str:
    return Fernet(fernet_key().encode()).encrypt(plain.encode()).decode()


def _require_secret(*keys: str) -> str:
    """A required key whose YAML value is a Fernet token. Plaintext is rejected."""
    token = _require(*keys)
    try:
        return Fernet(fernet_key().encode()).decrypt(token.encode()).decode()
    except InvalidToken as exc:
        raise ValueError(
            f"Config {'.'.join(keys)} is not a valid Fernet token for the key in {FERNET_KEY_FILE}. "
            f"Secrets in the env YAML are encrypted, never plaintext: python sources.py encrypt"
        ) from exc


def opengroup_credentials() -> tuple[str, str]:
    """(username, password) for the learner's Open Group account. Decrypted on demand."""
    return _require("opengroup", "username"), _require_secret("opengroup", "password")


def anthropic_api_key() -> str:
    return _require_secret("anthropic", "api_key")


# ------------------------------------------------------------------ required at start-up
APP_HOST = _require("app", "host")
APP_PORT = int(_require("app", "port"))
APP_BIND = _opt_str("app", "bind", default=APP_HOST)

CONTENT_DIR = Path(_require("paths", "content_dir"))
SOURCES_DIR = Path(_require("paths", "sources_dir"))
DB_PATH = Path(_require("paths", "db_path"))
LOG_DIR = Path(_require("paths", "log_dir"))

CSRF_SECRET = _require("security", "csrf_secret")

SOURCES_BASE_URL = _require("sources", "base_url")
SOURCES_LOGIN_URL = _require("sources", "login_url")
SOURCES_ARCHIMATE_URL = _require("sources", "archimate_url")
SOURCES_DELAY_SECONDS = _opt_float("sources", "delay_seconds", default=1.5)
SOURCES_USER_AGENT = _require("sources", "user_agent")
# Optional: a system Chromium for Playwright instead of a per-venv download (e.g. /usr/bin/chromium).
SOURCES_BROWSER_EXECUTABLE = _opt_str("sources", "browser_executable", default="")

ANTHROPIC_MODEL = _require("anthropic", "model")
ANTHROPIC_EFFORT = _require("anthropic", "effort")
ANTHROPIC_BATCH_SIZE = int(_require("anthropic", "batch_size"))
ANTHROPIC_MAX_TOKENS = int(_require("anthropic", "max_tokens"))

LOG_LEVEL = _opt_str("logging", "level", default="INFO")

# The learner's private copy of the publications is served on the loopback only (§1.3).
LOCAL_ONLY_HOSTS = frozenset({"127.0.0.1", "::1", "localhost"})
