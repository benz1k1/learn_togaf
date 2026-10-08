"""
Page and /api routes (learn_togaf.md §5.1), registered as a list, not decorators, so the
whole surface is readable in one place. Each controller module exposes plain functions.
"""

from collections.abc import Callable
from typing import Any

from fastapi import FastAPI

from learn_togaf.pages.controller import (
    adm,
    coverage,
    dashboard,
    examples,
    glossary,
    importer,
    lessons,
    notes,
    plan,
    practice,
    review,
    review_queue,
    sources,
)

ROUTES: list[tuple[str, Callable[..., Any], list[str]]] = [
    ("/", dashboard.dashboard, ["GET"]),
    ("/unit", lessons.unit_list, ["GET"]),
    ("/unit/{code}", lessons.unit_page, ["GET"]),
    ("/lesson/{lesson_id:path}", lessons.lesson_page, ["GET"]),
    ("/lesson-check/{lesson_id:path}", lessons.check_yourself, ["GET"]),
    ("/lesson-check/{lesson_id:path}", lessons.check_yourself_answer, ["POST"]),
    ("/lesson-progress/{lesson_id:path}", lessons.mark_progress, ["POST"]),
    ("/adm", adm.adm_page, ["GET"]),
    ("/adm/technique/{code}", adm.technique_page, ["GET"]),
    ("/adm/{phase}", adm.phase_page, ["GET"]),
    ("/adm-panel/{phase}", adm.phase_panel, ["GET"]),
    ("/artefact", adm.artefact_page, ["GET"]),
    ("/artefact/{code}/example", adm.artefact_example, ["GET"]),
    ("/example", examples.example_list, ["GET"]),
    ("/example/{example_id}", examples.example_page, ["GET"]),
    ("/glossary", glossary.glossary_page, ["GET"]),
    ("/glossary/{term_id}", glossary.term_page, ["GET"]),
    ("/review", review.review_page, ["GET"]),
    ("/review/next", review.next_card, ["GET"]),
    ("/review/{card_id}/grade", review.grade_card, ["POST"]),
    ("/review/rebuild", review.rebuild_cards, ["POST"]),
    ("/practice", practice.practice_page, ["GET"]),
    ("/practice", practice.start_attempt, ["POST"]),
    ("/attempt/{attempt_id}", practice.attempt_page, ["GET"]),
    ("/attempt/{attempt_id}/question/{index}", practice.question_fragment, ["GET"]),
    ("/attempt/{attempt_id}/answer", practice.answer, ["POST"]),
    ("/attempt/{attempt_id}/flag", practice.flag, ["POST"]),
    ("/attempt/{attempt_id}/finish", practice.finish, ["POST"]),
    ("/attempt/{attempt_id}/review", practice.review_attempt, ["GET"]),
    ("/attempt/{attempt_id}/timer", practice.timer_fragment, ["GET"]),
    ("/open-book", practice.open_book, ["GET"]),
    ("/import", importer.import_page, ["GET"]),
    ("/import/preview", importer.preview, ["POST"]),
    ("/import/confirm", importer.confirm, ["POST"]),
    ("/import/remove/{set_code}", importer.remove_set, ["POST"]),
    ("/import/state", importer.import_state, ["POST"]),
    ("/export", notes.export_page, ["GET"]),
    ("/export/state.json", notes.export_state, ["GET"]),
    ("/note", notes.save_note, ["POST"]),
    ("/plan", plan.plan_page, ["GET"]),
    ("/plan", plan.save_plan, ["POST"]),
    ("/plan/exercise/{week}/{kind}", plan.toggle_exercise, ["POST"]),
    ("/coverage", coverage.coverage_page, ["GET"]),
    ("/source", sources.source_index, ["GET"]),
    ("/source/{section_id:path}", sources.section_page, ["GET"]),
    ("/figure/{figure_id:path}", sources.figure_file, ["GET"]),
    ("/review-queue", review_queue.queue_page, ["GET"]),
    ("/review-queue/{draft_id:path}/accept", review_queue.accept_draft, ["POST"]),
    ("/review-queue/{draft_id:path}/reject", review_queue.reject_draft, ["POST"]),
    ("/api/attempt/{attempt_id}/timer", practice.timer_json, ["GET"]),
    ("/api/review/due", review.due_json, ["GET"]),
    ("/api/content/reload", dashboard.reload_content, ["POST"]),
]


def register_page_routes(app: FastAPI) -> None:
    for path, endpoint, methods in ROUTES:
        app.add_api_route(path, endpoint, methods=methods, include_in_schema=path.startswith("/api/"))
