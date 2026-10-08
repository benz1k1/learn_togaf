# CLAUDE.md

Learn TOGAF — single-user study app for three frameworks and five exams: TOGAF 10 Foundation
(OGEA-101) and Practitioner (OGEA-102), ArchiMate 3 Part 1 (OGA-031) and Part 2 (OGA-032), and
the SABSA Chartered Foundation (SCF). FastAPI + server-rendered htmx pages, SQLite, no build
step. `learn_togaf.md` is the plan and the source of truth for the app; `learn_sabsa_archimate.md`
is the plan for the ArchiMate and SABSA tracks and the braid that interleaves all three. Read the
section a change touches before changing it.

## Commands

```bash
cd api && uv sync                      # venv at api/.venv; uv only, never pip or poetry
python start.py                        # granian --reload on http://127.0.0.1:5014
python start.py --load-content         # rebuild the content cache from content/ first
python start.py --reset-progress       # wipe learner state only (attempts, cards, notes, plan)
python start.py --stop
python sources.py init-key | encrypt | login | fetch [--root togaf|archimate] | pdf | index | figures   # §1.4
python generate.py lessons <unit> | glossary | adm | questions <exam code> <unit> | verify      # §1.5
python draw_archimate.py [--check|--force] [id …]   # content/archimate/*.yaml → pages/static/archimate/*.svg
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
content/               blueprint.yaml (exams + units), curriculum.yaml (the 16-week braid), units/, lessons/<unit>/<nn>_<slug>.md,
                       adm/{phases,techniques,artefacts,crosswalk}.yaml, glossary.yaml, questions/<exam code>/*.yaml,
                       archimate/<id>.yaml (ArchiMate views, drawn by draw_archimate.py), review/,
                       examples/<nn>_<slug>.md (worked deliverables, ArchiMate MODEL views and SABSA profiles for Northgate Bank)
resources/sources/     the learner's private copy of the publications (gitignored except manifest.yaml, figures/important.yaml)
```

- Controllers: `async def name(request: Request, ..., connection: sqlite3.Connection = Depends(get_db))`;
  render with `templates.TemplateResponse(request, "x.html", base_context(request, connection, ...))`;
  redirect after a form POST with `RedirectResponse(url, status_code=303)`; htmx requests
  (`HX-Request` header) get a fragment, not a page.
- JSON columns (`refs`, `tags`, `inputs`, …) are stored with `orjson.dumps(...).decode()` and read
  with `orjson.loads`; templates use `| from_json`.
- Timestamps are ISO-8601 UTC strings (`datetime.now(UTC).isoformat(timespec="seconds")`).
- **Exams are data** (learn_sabsa_archimate.md §4.1): `blueprint.exams` is keyed by exam code
  (`OGEA-101`, `OGEA-102`, `OGA-031`, `OGA-032`, `SCF`), each with `track` (TOGAF | ARCHIMATE |
  SABSA) and `scoring` (`single` = one correct option, 1/0; `gradient` = four answers 5/3/1/0).
  Units name their exam; the crosswalk units X1–X3 name a track and no exam. A unit serves every
  exam of its track (A1–A9 carry both the OGA-031 bank and the OGA-032 scenarios). Question set
  files live in `questions/<exam code>/`; `question.exam`, `question.scoring`, `learning_unit.track`
  and `attempt.exam` carry the code, never the words FOUNDATION/PRACTITIONER. Mocks are
  `mode=MOCK&exam=<code>`; readiness is one tile per exam; exam dates are `exam_date:<code>`.
- **The braid**: `content/curriculum.yaml` places every lesson in one of 16 weeks (`lessons:`
  explicit ids win, `units:` sweeps the rest); the plan page follows it and `test_content.py`
  fails on an unplaced lesson. Weekly draw-it / justify-it exercises are `exercise:<week>:<kind>`
  settings.
- **ArchiMate views are static SVGs**, never rendered at runtime: `content/archimate/<id>.yaml`
  → `python draw_archimate.py` → `pages/static/archimate/<id>.svg`. An artefact's view is named
  by its code (`STAKEHOLDER_MAP_MATRIX.svg`) and appears as the "ArchiMate view" tab in the
  artefact's Example panel; a worked example of `kind: MODEL` names it in `figure:`.
  `draw_archimate.py --check` (run by `test_three_frameworks.py`) fails on a stale SVG.
- Question rows: `question` + `question_option` (single 1/0; gradient 5/3/1/0) +
  `lesson_question` (one lesson per question, from the question's `lesson:` or derived from refs;
  a tie warns at load and fails `test_content.py`). Check-yourself draws only a lesson's own
  mapped questions and never re-asks one answered in any lesson check. Mocks draw
  `status = 'reviewed'` only; drills may include drafts and show a badge.
- Stable content ids: lesson `F4/01_slug`, question `F4-017`, phase `A`, term `artifact`,
  technique `GAP_ANALYSIS`, artefact `STAKEHOLDER_MAP_MATRIX`, figure `ADM:fig-6-1` or
  `ARCHIMATE:fig-54`, ArchiMate view `STAKEHOLDER_MAP_MATRIX` / `northgate_migration`.
- Source documents: the six TOGAF documents, `GUIDE:<slug>`, `ARCHIMATE` (crawled with
  `fetch --root archimate`, same Open Group session — the plan's note that no login is needed
  was wrong), and PDF-only `WP:w117|w14c|w172` (`pdf/wp/`), `SABSA` (`pdf/sabsa.pdf`),
  `SABSA:bluebook` (`pdf/sabsa/`). Refs to a document not yet in the store are form-valid but
  unresolved; keep such content `status: draft`.
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
