# Learn TOGAF

A single-user study app for the TOGAF® Standard, 10th Edition exams (Foundation OGEA-101 and
Practitioner OGEA-102). FastAPI + htmx pages, SQLite, no build step. `learn_togaf.md` is the plan.

## First run

```bash
cd api && uv sync && cd ..
python sources.py init-key                 # only if ~/learn_togaf.yaml does not exist yet
python sources.py encrypt --set opengroup.password   # paste your Open Group password; writes the token into the env YAML
python start.py --load-content             # http://127.0.0.1:5014
```

Configuration is `resources/env/dev/.env.yaml` (nested YAML). The Fernet key that unwraps the
secrets in it lives outside the repo in `~/learn_togaf.yaml`, so the env file can be shared:
the username is plain text, the password is a token that is useless without the key.

## Building the content from the standard

```bash
python sources.py login      # your own Open Group account, once; stores the session locally
python sources.py fetch      # crawls the Digital Edition into resources/sources/ (gitignored)
python sources.py index      # sections, PDF pages, objective → section mapping
python sources.py figures    # every diagram, with caption and section
python generate.py lessons F4 && python generate.py verify      # drafts land in content/review/
```

Drafts are reviewed on `/review-queue`; mocks draw reviewed items only. Coverage against the
§6 targets is on `/coverage`, and `api/tests/test_bank_targets.py` fails until they are met.

## Tests

```bash
python start.py                            # in one terminal
cd api && LEARN_TOGAF_ENV=dev uv run pytest -q -k "not bank_targets"
```
