"""
Pydantic models for every file shape under ``content/`` (learn_togaf.md §2, learn_sabsa_archimate.md §4).

The loader and the importers validate with these and nothing else, so a hand-typed set, a
generated draft and a CSV import are all held to the same rules: exactly one correct option on a
single-answer question; points exactly {5, 3, 1, 0} on a gradient one; every unit and
objective in the blueprint; every ref in a known-document form; an explanation on every
question. A file that fails validation fails the load with the file and the id.

Exams are data (learn_sabsa_archimate.md §4.1): ``blueprint.exams`` is keyed by exam code and
each entry says which ``track`` it belongs to and whether its ``scoring`` is ``single`` (one
correct option, 1/0) or ``gradient`` (four answers, 5/3/1/0). Every unit names its exam code;
a crosswalk unit names none and carries a track instead. Question sets, attempts and readiness
all key on the exam code, so a new exam is a blueprint entry, not a code change.
"""

import hashlib
import re
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator

Source = Literal["generated", "authored", "imported"]
Status = Literal["draft", "reviewed"]
Scoring = Literal["single", "gradient"]
Track = Literal["TOGAF", "ARCHIMATE", "SABSA", "CROSSWALK"]
TRACKS: tuple[str, ...] = ("TOGAF", "ARCHIMATE", "SABSA", "CROSSWALK")

# Points the best answer of a question earns, by the exam's scoring.
MAX_POINTS: dict[str, int] = {"single": 1, "gradient": 5}

# Document codes a ref may name (§1.1–1.2). A ref is "<CODE> §<section>" or "<CODE> §<section> <title>".
DOCUMENT_CODES = {
    "INTRO": "Introduction and Core Concepts",
    "ADM": "Architecture Development Method",
    "TECH": "ADM Techniques",
    "APPLY": "Applying the ADM",
    "CONTENT": "Architecture Content",
    "GOV": "EA Capability and Governance",
    "GUIDE": "TOGAF Series Guide",
    "CONF": "Conformance Requirements",
    "ARCHIMATE": "ArchiMate 3.2 Specification",
    "WP": "The Open Group White Paper (WP:w117, WP:w14c, WP:w172)",
    "SABSA": "SABSA White Paper (SABSA:bluebook for the Blue Book)",
}
# Which track a document belongs to, for the glossary chips and the coverage grouping.
DOCUMENT_TRACKS: dict[str, str] = {
    "ARCHIMATE": "ARCHIMATE",
    "SABSA": "SABSA",
    "WP": "CROSSWALK",
}
_REF_RE = re.compile(
    r"^(?P<doc>[A-Z]+)(?::(?P<guide>[A-Za-z0-9_\-]+))?\s+§(?P<section>[0-9A-Z][0-9A-Za-z.\-]*)(?P<rest>.*)$"
)


def validate_ref(ref: str) -> str:
    match = _REF_RE.match(ref.strip())
    if not match or match.group("doc") not in DOCUMENT_CODES:
        raise ValueError(
            f"ref {ref!r} is not in a known-document form: '<DOC> §<section>' with DOC one of "
            f"{', '.join(DOCUMENT_CODES)} (a Series Guide is 'GUIDE:<slug> §<section>', a white paper 'WP:<id> §<section>')"
        )
    return ref.strip()


def document_track(document: str) -> str:
    """``"ARCHIMATE"`` → ARCHIMATE, ``"WP:w117"`` → CROSSWALK, anything else → TOGAF."""
    return DOCUMENT_TRACKS.get(document.split(":")[0], "TOGAF")


def content_hash(*parts: str) -> str:
    normalised = "\n".join(" ".join(part.split()).lower() for part in parts)
    return hashlib.sha256(normalised.encode("utf-8")).hexdigest()[:24]


# ---------------------------------------------------------------- blueprint.yaml (§0, SABSA/ArchiMate §4.1)
class ExamFormat(BaseModel):
    code: str = ""  # filled from the ``exams`` key by the Blueprint validator
    track: Track
    name: str
    questions: int
    time_minutes: int
    pass_mark: int
    max_score: int
    open_book: bool = False
    scoring: Scoring = "single"
    revision: str = ""  # which conformance document / datasheet the figures were checked against

    @property
    def max_points(self) -> int:
        return MAX_POINTS[self.scoring]

    @property
    def label(self) -> str:
        return f"{self.name} ({self.code})"


class ObjectiveSpec(BaseModel):
    code: str
    text: str


class UnitSpec(BaseModel):
    code: str
    exam: str | None = None  # an exam code from blueprint.exams; None for a crosswalk unit
    track: Track | None = None  # derived from the exam when omitted; required when exam is None
    name: str
    weight: int = 0
    objectives: list[ObjectiveSpec] = Field(default_factory=list)

    @model_validator(mode="after")
    def _track_or_exam(self) -> "UnitSpec":
        if self.exam is None and self.track is None:
            raise ValueError(f"unit {self.code}: a unit without an exam must name its track")
        if self.exam is None and self.weight:
            raise ValueError(f"unit {self.code}: a unit without an exam cannot carry a weight")
        return self


class Blueprint(BaseModel):
    revision: str
    exams: dict[str, ExamFormat]
    units: list[UnitSpec]

    @model_validator(mode="after")
    def _consistent(self) -> "Blueprint":
        if not self.exams:
            raise ValueError("blueprint.exams is empty")
        for code, exam in self.exams.items():
            exam.code = code
        for unit in self.units:
            if unit.exam is not None:
                if unit.exam not in self.exams:
                    raise ValueError(f"unit {unit.code}: exam {unit.exam!r} is not in blueprint.exams")
                exam_track = self.exams[unit.exam].track
                if unit.track is None:
                    unit.track = exam_track
                elif unit.track != exam_track:
                    raise ValueError(
                        f"unit {unit.code}: track {unit.track} disagrees with exam {unit.exam} ({exam_track})"
                    )
        for code, exam in self.exams.items():
            if exam.scoring != "single":
                continue
            weighted = [unit for unit in self.units if unit.exam == code]
            if not weighted:
                continue
            total = sum(unit.weight for unit in weighted)
            if total != exam.questions:
                raise ValueError(f"{code} unit weights sum to {total}, blueprint says {exam.questions}")
        codes = [unit.code for unit in self.units]
        if len(codes) != len(set(codes)):
            raise ValueError("duplicate unit codes in blueprint")
        objectives = [objective.code for unit in self.units for objective in unit.objectives]
        if len(objectives) != len(set(objectives)):
            raise ValueError("duplicate objective codes in blueprint")
        return self

    def exam(self, code: str) -> ExamFormat:
        if code not in self.exams:
            raise ValueError(f"{code!r} is not an exam code in blueprint.yaml ({', '.join(self.exams)})")
        return self.exams[code]

    def exams_by_track(self) -> dict[str, list[ExamFormat]]:
        grouped: dict[str, list[ExamFormat]] = {}
        for exam in self.exams.values():
            grouped.setdefault(exam.track, []).append(exam)
        return grouped

    def unit_codes(self) -> set[str]:
        return {unit.code for unit in self.units}

    def unit(self, code: str) -> UnitSpec:
        for unit in self.units:
            if unit.code == code:
                return unit
        raise ValueError(f"{code!r} is not a unit code in blueprint.yaml")

    def objective_codes(self) -> set[str]:
        return {objective.code for unit in self.units for objective in unit.objectives}

    def objective_unit(self) -> dict[str, str]:
        return {objective.code: unit.code for unit in self.units for objective in unit.objectives}


# ---------------------------------------------------------------- lessons (§2)
class LessonFrontMatter(BaseModel):
    title: str
    unit: str
    objectives: list[str] = Field(min_length=1)
    refs: list[str] = Field(default_factory=list)
    reading_minutes: int = 5
    source: Source = "authored"
    status: Status = "draft"
    model: str | None = None
    generated_at: str | None = None

    @field_validator("refs")
    @classmethod
    def _refs(cls, refs: list[str]) -> list[str]:
        return [validate_ref(ref) for ref in refs]


class Lesson(BaseModel):
    id: str
    unit: str
    slug: str
    ordinal: int
    front: LessonFrontMatter
    body_md: str

    def hash(self) -> str:
        return content_hash(self.front.title, self.body_md)


# ---------------------------------------------------------------- curriculum.yaml (SABSA/ArchiMate §4.6)
class CurriculumExercises(BaseModel):
    draw: str = ""
    justify: str = ""


class CurriculumWeek(BaseModel):
    """One braided week: a theme, the lessons in study order, the draw-it / justify-it exercises.

    ``lessons`` are explicit lesson ids; ``units`` places every not-yet-placed lesson of those
    units, in ordinal order, after the explicit ones. A mock week may name neither."""

    week: int
    theme: str
    lessons: list[str] = Field(default_factory=list)
    units: list[str] = Field(default_factory=list)
    exercises: CurriculumExercises = Field(default_factory=CurriculumExercises)


# ---------------------------------------------------------------- examples/ (§2, §4.3)
ExampleKind = Literal["DELIVERABLE", "ASSESSMENT", "SCENARIO", "MODEL", "PROFILE"]
ExamplePhase = Literal["PRELIM", "A", "B", "C", "D", "E", "F", "G", "H", "REQ"]


class ExampleFrontMatter(BaseModel):
    """A worked example document for the one fictional enterprise every example shares.

    ``track`` says which framework's deliverable it is: a TOGAF deliverable, an ArchiMate
    ``MODEL`` (a view of the case enterprise, drawn in the notation) or a SABSA ``PROFILE`` /
    deliverable (a Matrix cell filled in for the case). ``figure`` names the static SVG a MODEL
    embeds, under ``pages/static/archimate/``; ``viewpoint`` names the ArchiMate viewpoint."""

    title: str
    deliverable: str
    phase: ExamplePhase
    kind: ExampleKind = "DELIVERABLE"
    track: Track = "TOGAF"
    summary: str
    refs: list[str] = Field(min_length=1)
    figure: str | None = None
    viewpoint: str | None = None
    artefacts: list[str] = Field(default_factory=list)  # TOGAF artefact codes this example realises
    source: Source = "authored"
    status: Status = "draft"

    @field_validator("refs")
    @classmethod
    def _refs(cls, refs: list[str]) -> list[str]:
        return [validate_ref(ref) for ref in refs]

    @model_validator(mode="after")
    def _model_has_figure(self) -> "ExampleFrontMatter":
        if self.kind == "MODEL" and not self.figure:
            raise ValueError("a MODEL example must name the figure it draws (figure: <name>.svg)")
        if self.kind == "MODEL" and self.track != "ARCHIMATE":
            raise ValueError("a MODEL example is an ArchiMate view; set track: ARCHIMATE")
        return self


class ExampleDocument(BaseModel):
    id: str
    ordinal: int
    front: ExampleFrontMatter
    body_md: str

    def hash(self) -> str:
        return content_hash(self.front.title, self.body_md)


# ---------------------------------------------------------------- glossary.yaml
class GlossaryTerm(BaseModel):
    id: str
    term: str
    definition: str
    document: str
    section: str
    confusable_with: list[str] = Field(default_factory=list)
    objectives: list[str] = Field(default_factory=list)
    source: Source = "authored"
    status: Status = "draft"

    @field_validator("document")
    @classmethod
    def _document(cls, document: str) -> str:
        code = document.split(":")[0]
        if code not in DOCUMENT_CODES:
            raise ValueError(f"glossary document {document!r} is not a known document code")
        return document

    @property
    def track(self) -> str:
        return document_track(self.document)


# ---------------------------------------------------------------- adm/*.yaml
class CrosswalkArchimate(BaseModel):
    """How an ADM phase is drawn in ArchiMate (the specification's TOGAF appendix, W14C)."""

    viewpoints: list[str] = Field(default_factory=list)
    elements: list[str] = Field(default_factory=list)
    ref: str
    lessons: list[str] = Field(default_factory=list)
    note: str = ""

    @field_validator("ref")
    @classmethod
    def _ref(cls, ref: str) -> str:
        return validate_ref(ref)


class CrosswalkSabsa(BaseModel):
    """Where an ADM phase lands in the SABSA Matrix (W117, G152)."""

    layers: list[str] = Field(default_factory=list)
    cells: list[str] = Field(default_factory=list)
    artefacts: list[str] = Field(default_factory=list)
    ref: str
    lessons: list[str] = Field(default_factory=list)
    note: str = ""

    @field_validator("ref")
    @classmethod
    def _ref(cls, ref: str) -> str:
        return validate_ref(ref)


class Crosswalk(BaseModel):
    phase: str
    archimate: CrosswalkArchimate
    sabsa: CrosswalkSabsa


class AdmPhase(BaseModel):
    code: str
    name: str
    objective: list[str]
    approach: str = ""
    inputs: list[str] = Field(default_factory=list)
    steps: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    artefacts: list[str] = Field(default_factory=list)
    deliverables: list[str] = Field(default_factory=list)
    refs: list[str] = Field(default_factory=list)
    traps: list[str] = Field(default_factory=list)
    crosswalk: Crosswalk | None = None  # attached by the loader from adm/crosswalk.yaml

    @field_validator("refs")
    @classmethod
    def _refs(cls, refs: list[str]) -> list[str]:
        return [validate_ref(ref) for ref in refs]


class AdmTechnique(BaseModel):
    code: str
    name: str
    purpose: str
    phases: list[str] = Field(default_factory=list)
    artefacts: list[str] = Field(default_factory=list)
    traps: list[str] = Field(default_factory=list)
    refs: list[str] = Field(default_factory=list)

    @field_validator("refs")
    @classmethod
    def _refs(cls, refs: list[str]) -> list[str]:
        return [validate_ref(ref) for ref in refs]


class ArchimateMapping(BaseModel):
    """How a TOGAF artefact is expressed in ArchiMate (W14C, the spec's TOGAF appendix): the
    viewpoint that carries it, the elements and relationships it is drawn with, and the ref."""

    viewpoint: str
    elements: list[str] = Field(min_length=1)
    relationships: list[str] = Field(default_factory=list)
    ref: str
    note: str = ""

    @field_validator("ref")
    @classmethod
    def _ref(cls, ref: str) -> str:
        return validate_ref(ref)


class AdmArtefact(BaseModel):
    code: str
    name: str
    kind: Literal["CATALOG", "MATRIX", "DIAGRAM", "DELIVERABLE"]
    phase: str
    domain: Literal["BUSINESS", "DATA", "APPLICATION", "TECHNOLOGY", "CROSS"] = "CROSS"
    purpose: str = ""
    refs: list[str] = Field(default_factory=list)
    archimate: ArchimateMapping | None = None

    @field_validator("refs")
    @classmethod
    def _refs(cls, refs: list[str]) -> list[str]:
        return [validate_ref(ref) for ref in refs]


# ---------------------------------------------------------------- questions (§2)
class FoundationOption(BaseModel):
    key: str
    text: str
    correct: bool = False
    why: str = ""


class FoundationQuestion(BaseModel):
    """The single-answer shape (``scoring: single``): four options, exactly one correct, 1/0."""

    id: str
    unit: str
    objective: str
    lesson: str | None = (
        None  # lesson id whose check-yourself shows it; None → derived from refs by the loader
    )
    stem: str
    options: list[FoundationOption] = Field(min_length=4, max_length=4)
    explanation: str = Field(min_length=1)
    refs: list[str] = Field(default_factory=list)
    figure: str | None = None
    difficulty: int = Field(default=2, ge=1, le=3)
    tags: list[str] = Field(default_factory=list)
    source: Source = "authored"
    status: Status = "draft"
    model: str | None = None
    generated_at: str | None = None

    @field_validator("refs")
    @classmethod
    def _refs(cls, refs: list[str]) -> list[str]:
        return [validate_ref(ref) for ref in refs]

    @model_validator(mode="after")
    def _one_correct(self) -> "FoundationQuestion":
        correct = [option.key for option in self.options if option.correct]
        if len(correct) != 1:
            raise ValueError(f"question {self.id}: exactly one correct option required, got {correct}")
        keys = [option.key for option in self.options]
        if sorted(keys) != ["A", "B", "C", "D"]:
            raise ValueError(f"question {self.id}: option keys must be A, B, C, D, got {keys}")
        return self

    def hash(self) -> str:
        return content_hash(self.stem, *(option.text for option in self.options))


class PractitionerAnswer(BaseModel):
    key: str
    points: int
    text: str
    why: str = Field(min_length=1)


class PractitionerQuestion(BaseModel):
    """The gradient shape (``scoring: gradient``): a scenario, a question, four answers scored 5/3/1/0."""

    id: str
    unit: str
    objective: str
    lesson: str | None = (
        None  # lesson id whose check-yourself shows it; None → derived from refs by the loader
    )
    scenario: str = Field(min_length=1)
    question: str = Field(min_length=1)
    answers: list[PractitionerAnswer] = Field(min_length=4, max_length=4)
    refs: list[str] = Field(default_factory=list)
    open_book_hint: str = ""
    figure: str | None = None
    difficulty: int = Field(default=2, ge=1, le=3)
    tags: list[str] = Field(default_factory=list)
    source: Source = "authored"
    status: Status = "draft"
    model: str | None = None
    generated_at: str | None = None

    @field_validator("refs")
    @classmethod
    def _refs(cls, refs: list[str]) -> list[str]:
        return [validate_ref(ref) for ref in refs]

    @model_validator(mode="after")
    def _gradient(self) -> "PractitionerQuestion":
        points = sorted(answer.points for answer in self.answers)
        if points != [0, 1, 3, 5]:
            raise ValueError(f"question {self.id}: answer points must be exactly 5, 3, 1, 0, got {points}")
        keys = [answer.key for answer in self.answers]
        if sorted(keys) != ["A", "B", "C", "D"]:
            raise ValueError(f"question {self.id}: answer keys must be A, B, C, D, got {keys}")
        return self

    def hash(self) -> str:
        return content_hash(self.scenario, self.question, *(answer.text for answer in self.answers))


Question = FoundationQuestion | PractitionerQuestion


class QuestionSetFile(BaseModel):
    """A `questions/<exam code>/<set>.yaml` file: optional header mapping, then the list.

    ``exam`` is an exam code; ``track`` and ``scoring`` are copied from the blueprint by
    ``parse_question_set`` so the shape check and the cache insert need no second lookup."""

    code: str
    exam: str
    track: Track
    scoring: Scoring
    name: str
    kind: Literal["DRILL", "MOCK", "IMPORTED", "FIGURE"] = "DRILL"
    source: Source = "authored"
    single: list[FoundationQuestion] = Field(default_factory=list)
    gradient: list[PractitionerQuestion] = Field(default_factory=list)

    @model_validator(mode="after")
    def _shape(self) -> "QuestionSetFile":
        if self.scoring == "single" and self.gradient:
            raise ValueError(f"set {self.code}: {self.exam} is single-answer; it cannot hold gradient questions")
        if self.scoring == "gradient" and self.single:
            raise ValueError(f"set {self.code}: {self.exam} is gradient-scored; it cannot hold single-answer questions")
        ids = [question.id for question in self.questions()]
        if len(ids) != len(set(ids)):
            raise ValueError(f"set {self.code}: duplicate question ids")
        return self

    def questions(self) -> list[Question]:
        return [*self.single, *self.gradient]

    def count(self) -> int:
        return len(self.single) + len(self.gradient)


class ImportantFigure(BaseModel):
    id: str
    why: str
    objectives: list[str] = Field(default_factory=list)
    blank_boxes: list[list[int]] = Field(default_factory=list)  # [x, y, w, h] overlays (§11 q7)
    label: str = ""
