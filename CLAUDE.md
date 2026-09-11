# CLAUDE.md

Learn TOGAF — single-user study app for the TOGAF 10 Foundation (OGEA-101) and Practitioner
(OGEA-102) exams. FastAPI + server-rendered htmx pages, SQLite, no build step. `learn_togaf.md`
is the plan and the source of truth; read the section a change touches before changing it.

## Commands

```bash
cd api && uv sync                      # venv at api/.venv; uv only, never pip or poetry
python start.py                        # uvicorn --reload on http://127.0.0.1:5014
python start.py --load-content         # rebuild the content cache from content/ first
python start.py --stop
python sources.py init-key | encrypt | login | fetch | pdf | index | figures   # §1.4
python generate.py lessons <unit> | glossary | adm | questions foundation <unit> | verify      # §1.5
cd api && uv run ruff check --fix . && uv run ruff format . && uv run mypy src/
cd api && LEARN_TOGAF_ENV=dev uv run pytest -q      # needs the server running on 5014
```

## Configuration

`LEARN_TOGAF_ENV=dev` → `resources/env/dev/.env.yaml` (nested YAML, not dotenv);
`LEARN_TOGAF_ENV_YAML=/abs/path` overrides. Required keys are read through `config._require()`;
no code defaults, no `os.getenv(...) or "<literal>"`.

**Secrets.** The Fernet key is NOT in the repo: `fernet.key_file` names `~/learn_togaf.yaml`
(`fernet_key: "<key>"`, mode 600). `opengroup.password` and `anthropic.api_key` in the env YAML
are Fernet tokens made with `python sources.py encrypt`; `opengroup.username` is plain text.
They are decrypted lazily by `config.opengroup_credentials()` / `config.anthropic_api_key()`,
never at app start-up, so the app runs before a password has been pasted in.

## Layout and the contract every module follows

```
api/src/learn_togaf/
  config.py            _require() over the env YAML; paths, port, csrf secret, sources/anthropic settings
  db.py                connect() (sqlite3.Row, WAL, FK on), apply_schema(), transaction(conn)
  deps.py              get_db() — one connection per request:  connection: sqlite3.Connection = Depends(get_db)
  schema.sql           §3 tables. Content cache tables are rebuilt by the loader; learner state is never touched by it.
  content/models.py    Pydantic models for every file shape (§2). Importers and generators validate with THESE.
  content/loader.py    load_all(conn, content_dir); parse_question_set(raw, path, blueprint); insert_question_set(conn, set, ...)
  pages/urls.py        the route table — every page and /api route, one list, registered by name
  pages/controller/    one module per page; plain async functions named in urls.py (names are fixed, keep them)
  pages/templates/     base.html (extends), _*.html fragments, error.html
  pages/templating.py  `templates` + filters: markdown, fmt_dt, fmt_date, attr_json, from_json, duration
  pages/context.py     base_context(request, conn, **extra) — ALWAYS build template context with this; get_setting/set_setting
  pages/security.py    CsrfMiddleware (pure ASGI). Every unsafe method needs the token: htmx gets it from <body hx-headers>;
                       plain <form method="post"> must {% include "_csrf.html" %}.
  service/             one module per feature, plain functions taking the connection first; no HTTP, no templates
  importers/           one module per format → list of normalised question dicts in the §2 file shape
  sources/, generate/  the CLIs' packages (§1.4, §1.5)
content/               blueprint.yaml, units/, lessons/<unit>/<nn>_<slug>.md, adm/*.yaml, glossary.yaml, questions/<exam>/*.yaml, review/
resources/sources/     the learner's private copy of the publications (gitignored except manifest.yaml, figures/important.yaml)
```

- Controllers: `async def name(request: Request, ..., connection: sqlite3.Connection = Depends(get_db))`;
  render with `templates.TemplateResponse(request, "x.html", base_context(request, connection, ...))`;
  redirect after a form POST with `RedirectResponse(url, status_code=303)`; htmx requests
  (`HX-Request` header) get a fragment, not a page.
- JSON columns (`refs`, `tags`, `inputs`, …) are stored with `orjson.dumps(...).decode()` and read
  with `orjson.loads`; templates use `| from_json`.
- Timestamps are ISO-8601 UTC strings (`datetime.now(UTC).isoformat(timespec="seconds")`).
- Question rows: `question` + `question_option` (Foundation points 1/0; Practitioner 5/3/1/0).
  Mocks draw `status = 'reviewed'` only; drills may include drafts and show a badge.
- Stable content ids: lesson `F4/01_slug`, question `F4-017`, phase `A`, term `artifact`,
  technique `GAP_ANALYSIS`, artefact `STAKEHOLDER_MAP_MATRIX`, figure `ADM:fig-6-1`.
- Vendored static under `pages/static/` (htmx 2, Alpine 3, Tailwind play build, daisyUI 4, MDI,
  Chart.js). No CDN. Theme `data-theme="pastel"`.

## Conventions (workspace-wide, applied unchanged)

uv only; Pydantic v2 for every file shape and request; `orjson`, `polars`, `ruff`; imports at
module scope, stdlib → third party → local; loguru with **f-strings only** (`%s` args are
silently dropped); global exception handler, `try/except` only at I/O boundaries; REST paths
singular; no fallback logic — fail fast; tests drive a **running** server over httpx (never
`TestClient`), `pytest.fail()` never `pytest.skip()`; don't overwrite manual edits.

## Testing

`api/tests/` — live-server pytest over `httpx` against `http://127.0.0.1:5014` (`LEARN_TOGAF_ENV=dev`).
Each test file owns one feature slice. Content validity (`test_content.py`) asserts every file
under `content/` loads and the §6 coverage floors — expected to FAIL until the bank reaches
target; that is the gate, not a bug.
