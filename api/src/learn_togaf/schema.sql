-- Learn TOGAF — SQLite schema (learn_togaf.md §3).
-- Two kinds of table, kept apart: content cache (rebuilt from files, never edited here) and
-- learner state (the only thing worth backing up). Applied at start-up; every statement is
-- idempotent.

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------- source index (§1.4)
CREATE TABLE IF NOT EXISTS source_document (
    code TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    kind TEXT NOT NULL,                      -- STANDARD | GUIDE | CONFORMANCE
    html_url TEXT,
    pdf_path TEXT,
    fetched_at TEXT,
    content_hash TEXT
);
CREATE TABLE IF NOT EXISTS source_section (
    id TEXT PRIMARY KEY,                     -- "<doc>:<anchor-or-ordinal>", e.g. "ADM:6.3"
    document_code TEXT NOT NULL REFERENCES source_document(code) ON DELETE CASCADE,
    heading_path TEXT NOT NULL,              -- "ADM › 6. Phase A › 6.3 Inputs"
    anchor_url TEXT,
    pdf_page INTEGER,
    ordinal INTEGER NOT NULL,
    text TEXT NOT NULL,
    content_hash TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS source_section_doc_idx ON source_section(document_code, ordinal);
CREATE TABLE IF NOT EXISTS source_figure (
    id TEXT PRIMARY KEY,                     -- "<doc>:fig-6-1"
    document_code TEXT NOT NULL REFERENCES source_document(code) ON DELETE CASCADE,
    section_id TEXT REFERENCES source_section(id) ON DELETE SET NULL,
    caption TEXT NOT NULL,
    file_path TEXT NOT NULL,
    width INTEGER,
    height INTEGER,
    important INTEGER NOT NULL DEFAULT 0,
    content_hash TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS objective_source (
    objective_code TEXT NOT NULL,
    section_id TEXT NOT NULL,
    PRIMARY KEY (objective_code, section_id)
);

-- ---------------------------------------------------------------- content cache (§2)
CREATE TABLE IF NOT EXISTS learning_unit (
    code TEXT PRIMARY KEY,                   -- F1..F8, P1..P9, G_*
    exam TEXT NOT NULL,                      -- FOUNDATION | PRACTITIONER
    name TEXT NOT NULL,
    ordinal INTEGER NOT NULL,
    weight INTEGER NOT NULL,                 -- questions in the blueprint (Foundation) or scenarios (Practitioner)
    summary_md TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS objective (
    code TEXT PRIMARY KEY,                   -- "4.3"
    unit_code TEXT NOT NULL REFERENCES learning_unit(code) ON DELETE CASCADE,
    text TEXT NOT NULL,
    ordinal INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS lesson (
    id TEXT PRIMARY KEY,                     -- "<unit>/<nn>_<slug>"
    unit_code TEXT NOT NULL REFERENCES learning_unit(code) ON DELETE CASCADE,
    slug TEXT NOT NULL,
    title TEXT NOT NULL,
    body_md TEXT NOT NULL,
    reading_minutes INTEGER NOT NULL,
    ordinal INTEGER NOT NULL,
    refs TEXT NOT NULL,                      -- JSON array of section refs
    source TEXT NOT NULL,                    -- generated | authored
    status TEXT NOT NULL,                    -- draft | reviewed
    content_hash TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS lesson_objective (
    lesson_id TEXT NOT NULL REFERENCES lesson(id) ON DELETE CASCADE,
    objective_code TEXT NOT NULL,
    PRIMARY KEY (lesson_id, objective_code)
);
CREATE TABLE IF NOT EXISTS glossary_term (
    id TEXT PRIMARY KEY,                     -- slug
    term TEXT NOT NULL,
    definition TEXT NOT NULL,
    document TEXT NOT NULL,
    section TEXT NOT NULL,
    confusable_with TEXT NOT NULL,           -- JSON array of term ids
    objectives TEXT NOT NULL,                -- JSON array of objective codes
    source TEXT NOT NULL,
    status TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS adm_phase (
    code TEXT PRIMARY KEY,                   -- PRELIM, A..H, REQ
    name TEXT NOT NULL,
    objective TEXT NOT NULL,                 -- JSON array
    approach TEXT NOT NULL,
    inputs TEXT NOT NULL,                    -- JSON array
    steps TEXT NOT NULL,                     -- JSON array
    outputs TEXT NOT NULL,                   -- JSON array
    artefacts TEXT NOT NULL,                 -- JSON array of artefact codes
    deliverables TEXT NOT NULL,              -- JSON array
    refs TEXT NOT NULL,                      -- JSON array
    traps TEXT NOT NULL,                     -- JSON array
    ordinal INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS adm_technique (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    purpose TEXT NOT NULL,
    phases TEXT NOT NULL,                    -- JSON array of phase codes
    artefacts TEXT NOT NULL,                 -- JSON array
    traps TEXT NOT NULL,                     -- JSON array
    refs TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS adm_artefact (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    kind TEXT NOT NULL,                      -- CATALOG | MATRIX | DIAGRAM | DELIVERABLE
    phase_code TEXT NOT NULL,
    domain TEXT NOT NULL,                    -- BUSINESS | DATA | APPLICATION | TECHNOLOGY | CROSS
    purpose TEXT NOT NULL,
    refs TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS question_set (
    code TEXT PRIMARY KEY,
    exam TEXT NOT NULL,
    name TEXT NOT NULL,
    source TEXT NOT NULL,                    -- generated | authored | imported
    kind TEXT NOT NULL,                      -- DRILL | MOCK | IMPORTED | FIGURE
    question_count INTEGER NOT NULL DEFAULT 0,
    file_name TEXT,
    imported_at TEXT
);
CREATE TABLE IF NOT EXISTS question (
    id TEXT PRIMARY KEY,
    exam TEXT NOT NULL,                      -- FOUNDATION | PRACTITIONER
    unit_code TEXT NOT NULL,
    objective_code TEXT NOT NULL,
    set_code TEXT NOT NULL REFERENCES question_set(code) ON DELETE CASCADE,
    source TEXT NOT NULL,
    status TEXT NOT NULL,                    -- draft | reviewed
    figure_id TEXT,
    stem_or_scenario TEXT NOT NULL,
    question_text TEXT NOT NULL DEFAULT '',
    explanation TEXT NOT NULL DEFAULT '',
    open_book_hint TEXT NOT NULL DEFAULT '',
    refs TEXT NOT NULL,                      -- JSON array
    difficulty INTEGER NOT NULL DEFAULT 2,
    tags TEXT NOT NULL,                      -- JSON array
    content_hash TEXT NOT NULL,
    verified_at TEXT,
    reviewed_at TEXT,
    unit_unverified INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS question_unit_idx ON question(exam, unit_code, objective_code, status);
CREATE INDEX IF NOT EXISTS question_hash_idx ON question(content_hash);
CREATE TABLE IF NOT EXISTS question_option (
    question_id TEXT NOT NULL REFERENCES question(id) ON DELETE CASCADE,
    key TEXT NOT NULL,
    text TEXT NOT NULL,
    points INTEGER NOT NULL,                 -- Foundation 1/0, Practitioner 5/3/1/0
    why TEXT NOT NULL DEFAULT '',
    ordinal INTEGER NOT NULL,
    PRIMARY KEY (question_id, key)
);

-- ---------------------------------------------------------------- learner state (§3)
CREATE TABLE IF NOT EXISTS attempt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam TEXT NOT NULL,
    mode TEXT NOT NULL,                      -- DRILL | MOCK
    set_code TEXT,
    seed INTEGER NOT NULL,
    question_ids TEXT NOT NULL,              -- JSON array, in order
    started_at TEXT NOT NULL,
    finished_at TEXT,
    time_limit_s INTEGER,
    score INTEGER,
    max_score INTEGER,
    passed INTEGER,
    filters TEXT NOT NULL DEFAULT '{}'       -- JSON: units/objectives/sources chosen for a drill
);
CREATE TABLE IF NOT EXISTS attempt_answer (
    attempt_id INTEGER NOT NULL REFERENCES attempt(id) ON DELETE CASCADE,
    question_id TEXT NOT NULL,
    chosen_key TEXT,
    points INTEGER,
    answered_at TEXT,
    flagged INTEGER NOT NULL DEFAULT 0,
    seconds INTEGER,
    changed_from_correct INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (attempt_id, question_id)
);
CREATE TABLE IF NOT EXISTS card_review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_kind TEXT NOT NULL,                 -- TERM | PHASE_IO | TECHNIQUE | ARTEFACT | FIGURE | QUESTION
    card_ref TEXT NOT NULL,                  -- stable content id
    due_at TEXT NOT NULL,
    interval_days REAL NOT NULL DEFAULT 0,
    ease REAL NOT NULL DEFAULT 2.5,
    reps INTEGER NOT NULL DEFAULT 0,
    lapses INTEGER NOT NULL DEFAULT 0,
    last_grade INTEGER,
    last_reviewed_at TEXT,
    UNIQUE (card_kind, card_ref)
);
CREATE INDEX IF NOT EXISTS card_review_due_idx ON card_review(due_at);
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ref_kind TEXT NOT NULL,                  -- LESSON | TERM | PHASE | QUESTION
    ref_id TEXT NOT NULL,
    body_md TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE (ref_kind, ref_id)
);
CREATE TABLE IF NOT EXISTS study_session (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    lessons_read INTEGER NOT NULL DEFAULT 0,
    cards_reviewed INTEGER NOT NULL DEFAULT 0,
    questions_answered INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS lesson_progress (
    lesson_id TEXT PRIMARY KEY,
    state TEXT NOT NULL,                     -- READ | CHECKED | MASTERED
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS setting (
    key TEXT PRIMARY KEY,                    -- exam_date, daily_card_cap, plan_json, import_mapping:<source>
    value TEXT NOT NULL
);
