"""The sidebar (learn_togaf.md §4, §5.1) — one definition, read by base.html."""

from dataclasses import dataclass

from starlette.requests import Request


@dataclass(frozen=True)
class NavItem:
    label: str
    path: str
    icon: str
    group: str
    active: bool = False


_ITEMS = (
    ("Dashboard", "/", "mdi-view-dashboard-outline", "Study"),
    ("Lessons", "/unit", "mdi-book-open-page-variant-outline", "Study"),
    ("ADM explorer", "/adm", "mdi-sync-circle", "Study"),
    ("Artefacts", "/artefact", "mdi-file-tree-outline", "Study"),
    ("Worked examples", "/example", "mdi-file-document-multiple-outline", "Study"),
    ("Glossary", "/glossary", "mdi-alphabetical-variant", "Study"),
    ("Flashcards", "/review", "mdi-cards-outline", "Drill"),
    ("Practice", "/practice", "mdi-clipboard-check-outline", "Drill"),
    ("Study plan", "/plan", "mdi-calendar-check-outline", "Drill"),
    ("Sources", "/source", "mdi-library-outline", "Author"),
    ("Coverage", "/coverage", "mdi-chart-box-outline", "Author"),
    ("Review queue", "/review-queue", "mdi-clipboard-text-search-outline", "Author"),
    ("Import questions", "/import", "mdi-tray-arrow-down", "Author"),
    ("Export state", "/export", "mdi-content-save-outline", "Author"),
)


def nav_items(request: Request) -> list[NavItem]:
    path = request.url.path
    items = []
    for label, item_path, icon, group in _ITEMS:
        active = (
            path == item_path if item_path == "/" else path == item_path or path.startswith(item_path + "/")
        )
        if item_path == "/unit" and path.startswith("/lesson/"):
            active = True
        if item_path == "/practice" and path.startswith("/attempt/"):
            active = True
        items.append(NavItem(label, item_path, icon, group, active))
    return items
