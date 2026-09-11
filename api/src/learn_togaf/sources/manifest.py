"""
``resources/sources/manifest.yaml`` (learn_togaf.md §1.4): the checked-in inventory of the
source store — documents → pages → {url, title, hash, fetched_at, etag}, the registered PDFs
and the HTML-vs-PDF figure counts. Hashes and URLs only; no text of the standard is ever
written here, which is why the file may be committed while the rest of the store is not.
"""

from pathlib import Path

import yaml
from pydantic import BaseModel, Field

MANIFEST_VERSION = 1
LICENCE_NOTE = (
    "Personal copy of The Open Group publications fetched by the account holder for their own "
    "study (learn_togaf.md §1.3). This manifest holds URLs, titles and hashes only."
)


class PageEntry(BaseModel):
    url: str
    title: str = ""
    hash: str = ""
    fetched_at: str = ""
    etag: str = ""


class PdfEntry(BaseModel):
    path: str
    title: str = ""
    page_count: int = 0
    hash: str = ""
    registered_at: str = ""


class DocumentEntry(BaseModel):
    code: str
    kind: str = "STANDARD"  # STANDARD | GUIDE
    title: str = ""
    html_url: str = ""
    pages: dict[str, PageEntry] = Field(default_factory=dict)
    pdf: PdfEntry | None = None
    figure_counts: dict[str, int] = Field(default_factory=dict)  # {"html": n, "pdf": n}


class Manifest(BaseModel):
    version: int = MANIFEST_VERSION
    licence: str = LICENCE_NOTE
    fetched_at: str = ""
    documents: dict[str, DocumentEntry] = Field(default_factory=dict)

    def document(self, segment: str, code: str, kind: str) -> DocumentEntry:
        entry = self.documents.get(segment)
        if entry is None:
            entry = DocumentEntry(code=code, kind=kind)
            self.documents[segment] = entry
        return entry


def manifest_path(sources_dir: Path) -> Path:
    return sources_dir / "manifest.yaml"


def load_manifest(sources_dir: Path) -> Manifest:
    path = manifest_path(sources_dir)
    if not path.is_file():
        return Manifest()
    with open(path, encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    return Manifest.model_validate(raw)


def save_manifest(sources_dir: Path, manifest: Manifest) -> None:
    sources_dir.mkdir(parents=True, exist_ok=True)
    data = manifest.model_dump(exclude_none=True)
    with open(manifest_path(sources_dir), "w", encoding="utf-8") as handle:
        handle.write(
            "# Written by `python sources.py fetch|pdf|figures`. URLs, titles and hashes only — no text.\n"
        )
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True, width=120)
