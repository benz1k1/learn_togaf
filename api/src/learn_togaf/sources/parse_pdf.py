"""
Licensed PDFs (learn_togaf.md §1.4): the outline (bookmarks) mapped onto the same section
numbers the HTML headings carry, so a ``source_section`` knows its ``pdf_page`` as well as its
anchor; the page images at native resolution for the figure store; and, for a PDF-only
document (a guide with no HTML edition), sections built from the outline with the page text.
"""

import hashlib
from dataclasses import dataclass, field
from pathlib import Path

import pymupdf

from learn_togaf.sources.parse_html import ParsedSection, collapse, split_heading


@dataclass
class OutlineEntry:
    level: int
    title: str
    number: str | None
    page: int  # 1-based


@dataclass
class PdfInfo:
    path: Path
    title: str
    page_count: int
    hash: str
    outline: list[OutlineEntry] = field(default_factory=list)


@dataclass
class PdfImage:
    page: int  # 1-based
    index: int  # 1-based within the page
    data: bytes
    ext: str
    width: int
    height: int


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_outline(document: pymupdf.Document) -> list[OutlineEntry]:
    entries: list[OutlineEntry] = []
    for level, title, page in document.get_toc(simple=True):
        number, _ = split_heading(title)
        entries.append(OutlineEntry(level=level, title=collapse(title), number=number, page=page))
    return entries


def register_pdf(path: Path) -> PdfInfo:
    with pymupdf.open(path) as document:
        outline = read_outline(document)
        title = collapse(document.metadata.get("title") or "")
        if not title and outline:
            title = outline[0].title
        if not title:
            title = path.stem
        return PdfInfo(
            path=path, title=title, page_count=document.page_count, hash=file_hash(path), outline=outline
        )


def outline_pages(info: PdfInfo) -> dict[str, int]:
    """Section number → first page, from the bookmarks. A number that appears twice keeps its
    first occurrence (front matter sometimes repeats chapter titles)."""
    pages: dict[str, int] = {}
    for entry in info.outline:
        if entry.number and entry.number not in pages:
            pages[entry.number] = entry.page
    return pages


def page_images(path: Path) -> list[PdfImage]:
    images: list[PdfImage] = []
    with pymupdf.open(path) as document:
        for page_number, page in enumerate(document, start=1):
            for index, image in enumerate(page.get_images(full=True), start=1):
                extracted = document.extract_image(image[0])
                images.append(
                    PdfImage(
                        page=page_number,
                        index=index,
                        data=extracted["image"],
                        ext=extracted["ext"],
                        width=int(extracted["width"]),
                        height=int(extracted["height"]),
                    )
                )
    return images


def sections_from_outline(path: Path, document_code: str, info: PdfInfo) -> list[ParsedSection]:
    """Sections for a PDF-only document: one per bookmark, text = its pages up to the next
    bookmark. Ids use the section number when there is one, else a slug of the title."""
    sections: list[ParsedSection] = []
    stack: list[tuple[int, str]] = []
    with pymupdf.open(path) as document:
        for ordinal, entry in enumerate(info.outline, start=1):
            next_page = info.outline[ordinal].page if ordinal < len(info.outline) else document.page_count + 1
            text = "\n\n".join(
                document[page - 1].get_text().strip()
                for page in range(entry.page, max(entry.page, next_page))
            )
            while stack and stack[-1][0] >= entry.level:
                stack.pop()
            stack.append((entry.level, entry.title))
            path_titles = [title for _, title in stack[:-1] if split_heading(title)[0]] + [entry.title]
            anchor = entry.number or "".join(ch if ch.isalnum() else "-" for ch in entry.title.lower()).strip(
                "-"
            )
            sections.append(
                ParsedSection(
                    id=f"{document_code}:{anchor}",
                    document_code=document_code,
                    anchor=anchor,
                    level=min(entry.level, 4),
                    number=entry.number,
                    title=split_heading(entry.title)[1],
                    heading_path=" › ".join([document_code, *path_titles]),
                    anchor_url="",
                    ordinal=ordinal,
                    blocks=[text],
                )
            )
    return sections


def image_size(path: Path) -> tuple[int, int]:
    """Width and height of an image file (PNG/JPEG/GIF/SVG…) through pymupdf, no PIL."""
    if path.suffix.lower() == ".svg":
        with pymupdf.open(path) as document:
            rect = document[0].rect
            return int(rect.width), int(rect.height)
    pixmap = pymupdf.Pixmap(str(path))
    return pixmap.width, pixmap.height
