"""
Pydantic models for every file shape under ``content/`` (learn_togaf.md §2).

The loader and the importers validate with these and nothing else, so a hand-typed set, a
generated draft and a CSV import are all held to the same rules: exactly one correct option on a
Foundation question; points exactly {5, 3, 1, 0} on a Practitioner one; every unit and
objective in the blueprint; every ref in a known-document form; an explanation on every
question. A file that fails validation fails the load with the file and the id.
"""

import hashlib
import re
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator

Exam = Literal["FOUNDATION", "PRACTITIONER"]
Source = Literal["generated", "authored", "imported"]
Status = Literal["draft", "reviewed"]

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
}
_REF_RE = re.compile(
    r"^(?P<doc>[A-Z]+)(?::(?P<guide>[A-Za-z0-9_\-]+))?\s+§(?P<section>[0-9][0-9A-Za-z.\-]*)(?P<rest>.*)$"
)


def validate_ref(ref: str) -> str:
    match = _REF_RE.match(ref.strip())
    if not match or match.group("doc") not in DOCUMENT_CODES:
        raise ValueError(
            f"ref {ref!r} is not in a known-document form: '<DOC> §<section>' with DOC one of "
            f"{', '.join(DOCUMENT_CODES)} (a Series Guide is 'GUIDE:<slug> §<section>')"
        )
    return ref.strip()


def content_hash(*parts: str) -> str:
    normalised = "\n".join(" ".join(part.split()).lower() for part in parts)
    return hashlib.sha256(normalised.encode("utf-8")).hexdigest()[:24]


# ---------------------------------------------------------------- blueprint.yaml (§0)
class ExamFormat(BaseModel):
    code: str
    questions: int
    time_minutes: int
    pass_mark: int
    max_score: int
    open_book: bool = False
    scoring: Literal["single", "gradient"] = "single"


class ObjectiveSpec(BaseModel):
    code: str
    text: str


class UnitSpec(BaseModel):
    code: str
    exam: Exam
    name: str
    weight: int = 0
    objectives: list[ObjectiveSpec] = Field(default_factory=list)


class Blueprint(BaseModel):
    revision: str
    foundation: ExamFormat
    practitioner: ExamFormat
    units: list[UnitSpec]

    @model_validator(mode="after")
    def _weights_sum(self) -> "Blueprint":
        total = sum(unit.weight for unit in self.units if unit.exam == "FOUNDATION")
        if total != self.foundation.questions:
            raise ValueError(
                f"Foundation unit weights sum to {total}, blueprint says {self.foundation.questions}"
            )
        codes = [unit.code for unit in self.units]
        if len(codes) != len(set(codes)):
            raise ValueError("duplicate unit codes in blueprint")
        objectives = [objective.code for unit in self.units for objective in unit.objectives]
        if len(objectives) != len(set(objectives)):
            raise ValueError("duplicate objective codes in blueprint")
        return self

    def unit_codes(self) -> set[str]:
        return {unit.code for unit in self.units}

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


# ---------------------------------------------------------------- adm/*.yaml
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


class AdmArtefact(BaseModel):
    code: str
    name: str
    kind: Literal["CATALOG", "MATRIX", "DIAGRAM", "DELIVERABLE"]
    phase: str
    domain: Literal["BUSINESS", "DATA", "APPLICATION", "TECHNOLOGY", "CROSS"] = "CROSS"
    purpose: str = ""
    refs: list[str] = Field(default_factory=list)

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
    id: str
    unit: str
    objective: str
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
    id: str
    unit: str
    objective: str
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


class QuestionSetFile(BaseModel):
    """A `questions/<exam>/<set>.yaml` file: optional header mapping, then the list."""

    code: str
    exam: Exam
    name: str
    kind: Literal["DRILL", "MOCK", "IMPORTED", "FIGURE"] = "DRILL"
    source: Source = "authored"
    foundation: list[FoundationQuestion] = Field(default_factory=list)
    practitioner: list[PractitionerQuestion] = Field(default_factory=list)

    @model_validator(mode="after")
    def _shape(self) -> "QuestionSetFile":
        if self.exam == "FOUNDATION" and self.practitioner:
            raise ValueError(f"set {self.code}: a FOUNDATION set cannot hold practitioner questions")
        if self.exam == "PRACTITIONER" and self.foundation:
            raise ValueError(f"set {self.code}: a PRACTITIONER set cannot hold foundation questions")
        ids = [question.id for question in self.foundation] + [question.id for question in self.practitioner]
        if len(ids) != len(set(ids)):
            raise ValueError(f"set {self.code}: duplicate question ids")
        return self

    def count(self) -> int:
        return len(self.foundation) + len(self.practitioner)


class ImportantFigure(BaseModel):
    id: str
    why: str
    objectives: list[str] = Field(default_factory=list)
    blank_boxes: list[list[int]] = Field(default_factory=list)  # [x, y, w, h] overlays (§11 q7)
    label: str = ""
