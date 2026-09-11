"""
Digital Edition HTML → heading tree (learn_togaf.md §1.4).

Pure functions over HTML text: no network, no database, so the crawl can be replayed against
fixture pages in the test-suite. Every ``h1``–``h4`` that carries an anchor (an ``id`` on the
heading, an ``<a id|name>`` inside it, or an empty ``<a id|name>`` immediately before it)
opens a :class:`ParsedSection` with id ``"<DOC>:<anchor>"``. A heading without an anchor is
not a section of its own — its text is folded into the enclosing section as a bold line.

``ParsedSection.text`` is the section's *own* text, up to the next heading of any level, with
lists as ``-``/``1.`` lines and tables as Markdown tables. The spec's inclusive reading — the
text down to the next heading of the same or a higher level — is the section plus its
descendants, which :func:`learn_togaf.sources.index.section_with_descendants` assembles, so a
chapter is stored once and never duplicated inside its own sub-sections.

Figures: every ``<img>`` inside a ``<figure>``, and every ``<img>`` with a "Figure N-M:"
caption nearby (figcaption, alt/title, or the adjacent text block), becomes a
:class:`ParsedFigure` with id ``"<DOC>:fig-N-M"`` and the section it sits in.
"""

import re
from dataclasses import dataclass, field
from urllib.parse import urljoin

from selectolax.parser import HTMLParser, Node

HEADING_TAGS = ("h1", "h2", "h3", "h4")
_HEADING_LEVEL = {tag: index + 1 for index, tag in enumerate(HEADING_TAGS)}
BLOCK_TAGS = {"p", "ul", "ol", "table", "pre", "blockquote", "dl", "figure"}
SKIP_TAGS = {"script", "style", "noscript", "nav", "header", "footer", "template"}

HEADING_NUMBER_RE = re.compile(r"^\s*(?P<number>\d+(?:\.\d+)*)\.?\s+(?P<title>\S.*)$")
FIGURE_CAPTION_RE = re.compile(
    r"Figure\s+(?P<chapter>\d+)[-–](?P<n>\d+)\s*[:.]?\s*(?P<title>.*)", re.IGNORECASE
)
_WS_RE = re.compile(r"\s+")


@dataclass
class ParsedSection:
    id: str
    document_code: str
    anchor: str
    level: int
    number: str | None
    title: str
    heading_path: str
    anchor_url: str
    ordinal: int
    blocks: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n\n".join(block for block in self.blocks if block).strip()

    @property
    def ref(self) -> str | None:
        """The citable ``"<DOC> §<number>"`` form, or None for an unnumbered heading."""
        return f"{self.document_code} §{self.number}" if self.number else None


@dataclass
class ParsedFigure:
    id: str
    document_code: str
    src: str
    caption: str
    section_id: str | None
    number: str | None


@dataclass
class ParsedPage:
    document_code: str
    url: str
    title: str
    sections: list[ParsedSection] = field(default_factory=list)
    figures: list[ParsedFigure] = field(default_factory=list)


def collapse(text: str) -> str:
    return _WS_RE.sub(" ", text).strip()


def split_heading(text: str) -> tuple[str | None, str]:
    """ "3.3 Inputs" → ("3.3", "Inputs"); "Preface" → (None, "Preface")."""
    match = HEADING_NUMBER_RE.match(text)
    if not match:
        return None, collapse(text)
    return match.group("number"), collapse(match.group("title"))


def figure_number(caption: str) -> str | None:
    match = FIGURE_CAPTION_RE.search(caption)
    return f"{match.group('chapter')}-{match.group('n')}" if match else None


def _heading_anchor(node: Node) -> str | None:
    own = node.attributes.get("id") or node.attributes.get("name")
    if own:
        return own
    for link in node.css("a"):
        anchor = link.attributes.get("id") or link.attributes.get("name")
        if anchor:
            return anchor
    previous = node.prev
    while previous is not None and previous.tag == "-text" and not previous.text().strip():
        previous = previous.prev
    if previous is not None and previous.tag == "a" and not collapse(previous.text(deep=True)):
        return previous.attributes.get("id") or previous.attributes.get("name")
    return None


def _inline_text(node: Node, skip: set[str]) -> str:
    parts: list[str] = []
    for child in node.iter(include_text=True):
        if child.tag == "-text":
            parts.append(child.text())
        elif child.tag in skip or child.tag in SKIP_TAGS:
            continue
        else:
            parts.append(child.text(deep=True, separator=" "))
    return collapse(" ".join(parts))


def _render_list(node: Node, ordered: bool, indent: int = 0) -> list[str]:
    lines: list[str] = []
    counter = 0
    for item in node.iter():
        if item.tag != "li":
            continue
        counter += 1
        marker = f"{counter}." if ordered else "-"
        lines.append(f"{'  ' * indent}{marker} {_inline_text(item, {'ul', 'ol'})}")
        for nested in item.iter():
            if nested.tag in ("ul", "ol"):
                lines.extend(_render_list(nested, nested.tag == "ol", indent + 1))
    return lines


def _render_table(node: Node) -> str:
    rows: list[list[str]] = []
    for row in node.css("tr"):
        cells = [
            collapse(cell.text(deep=True, separator=" ")).replace("|", "\\|")
            for cell in row.iter()
            if cell.tag in ("th", "td")
        ]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return "\n".join(lines)


def _render_definition_list(node: Node) -> str:
    lines: list[str] = []
    for child in node.iter():
        if child.tag == "dt":
            lines.append(f"**{collapse(child.text(deep=True, separator=' '))}**")
        elif child.tag == "dd":
            lines.append(f": {collapse(child.text(deep=True, separator=' '))}")
    return "\n".join(lines)


def _sibling_text(node: Node | None) -> str:
    while node is not None and node.tag == "-text" and not node.text().strip():
        node = node.next
    if node is None:
        return ""
    return collapse(node.text(deep=True, separator=" ")) if node.tag != "-text" else collapse(node.text())


def _previous_sibling_text(node: Node | None) -> str:
    while node is not None and node.tag == "-text" and not node.text().strip():
        node = node.prev
    if node is None:
        return ""
    return collapse(node.text(deep=True, separator=" ")) if node.tag != "-text" else collapse(node.text())


class _Walker:
    def __init__(self, document_code: str, url: str) -> None:
        self.document_code = document_code
        self.url = url
        self.page = ParsedPage(document_code=document_code, url=url, title="")
        self.stack: list[tuple[int, str]] = []
        self.current: ParsedSection | None = None
        self.ordinal = 0
        self.seen_figures: set[str] = set()

    # ------------------------------------------------------------------ headings
    def _open_section(self, node: Node, anchor: str) -> None:
        level = _HEADING_LEVEL[node.tag]
        heading_text = collapse(node.text(deep=True, separator=" "))
        number, title = split_heading(heading_text)
        while self.stack and self.stack[-1][0] >= level:
            self.stack.pop()
        self.stack.append((level, heading_text))
        # The path is built from the numbered headings only ("ADM › 3. Phase A › 3.3 Inputs"):
        # an unnumbered ancestor such as the document title is not a level of the tree.
        path = [text for _, text in self.stack[:-1] if split_heading(text)[0]] + [heading_text]
        self.ordinal += 1
        self.current = ParsedSection(
            id=f"{self.document_code}:{anchor}",
            document_code=self.document_code,
            anchor=anchor,
            level=level,
            number=number,
            title=title,
            heading_path=" › ".join([self.document_code, *path]),
            anchor_url=f"{self.url}#{anchor}",
            ordinal=self.ordinal,
        )
        self.page.sections.append(self.current)

    def _append(self, block: str) -> None:
        if block and self.current is not None:
            self.current.blocks.append(block)

    # ------------------------------------------------------------------ figures
    def _register_image(self, img: Node, enclosing_figure: Node | None) -> None:
        src = img.attributes.get("src") or ""
        if not src:
            return
        caption = ""
        if enclosing_figure is not None:
            figcaption = enclosing_figure.css_first("figcaption")
            if figcaption is not None:
                caption = collapse(figcaption.text(deep=True, separator=" "))
        candidates = [
            caption,
            collapse(img.attributes.get("alt") or ""),
            collapse(img.attributes.get("title") or ""),
            _sibling_text(img.next),
            _sibling_text(img.parent.next if img.parent is not None else None),
            _previous_sibling_text(img.parent.prev if img.parent is not None else None),
        ]
        numbered = next((text for text in candidates if text and figure_number(text)), "")
        if numbered:
            caption = numbered
        elif enclosing_figure is None:
            return  # a decorative image: no figure context and no "Figure N-M" caption
        elif not caption:
            caption = collapse(img.attributes.get("alt") or "") or src.rsplit("/", 1)[-1]
        number = figure_number(caption)
        slug = number or re.sub(r"[^a-z0-9]+", "-", src.rsplit("/", 1)[-1].rsplit(".", 1)[0].lower()).strip(
            "-"
        )
        figure_id = f"{self.document_code}:fig-{slug}"
        suffix = 2
        while figure_id in self.seen_figures:
            figure_id = f"{self.document_code}:fig-{slug}-{suffix}"
            suffix += 1
        self.seen_figures.add(figure_id)
        self.page.figures.append(
            ParsedFigure(
                id=figure_id,
                document_code=self.document_code,
                src=urljoin(self.url, src),
                caption=caption,
                section_id=self.current.id if self.current else None,
                number=number,
            )
        )
        self._append(f"[{caption}]")

    # ------------------------------------------------------------------ blocks
    def _render_block(self, node: Node) -> None:
        tag = node.tag
        if tag == "figure":
            for img in node.css("img"):
                self._register_image(img, node)
            return
        for img in node.css("img"):
            self._register_image(img, None)
        if tag == "p":
            text = _inline_text(node, set())
            if self.page.figures and text == self.page.figures[-1].caption:
                return  # the caption paragraph was already recorded with the figure
            self._append(text)
        elif tag in ("ul", "ol"):
            self._append("\n".join(_render_list(node, tag == "ol")))
        elif tag == "table":
            self._append(_render_table(node))
        elif tag == "pre":
            self._append(f"```\n{node.text(deep=True).strip()}\n```")
        elif tag == "blockquote":
            self._append("> " + collapse(node.text(deep=True, separator=" ")))
        elif tag == "dl":
            self._append(_render_definition_list(node))

    def walk(self, node: Node) -> None:
        for child in node.iter(include_text=True):
            tag = child.tag
            if tag in SKIP_TAGS:
                continue
            if tag == "-text":
                text = collapse(child.text())
                if text:
                    self._append(text)
            elif tag in _HEADING_LEVEL:
                anchor = _heading_anchor(child)
                if anchor:
                    self._open_section(child, anchor)
                else:
                    self._append(f"**{collapse(child.text(deep=True, separator=' '))}**")
            elif tag in BLOCK_TAGS:
                self._render_block(child)
            elif tag == "img":
                self._register_image(child, None)
            elif tag == "a" and not collapse(child.text(deep=True)):
                continue  # an empty anchor element; the heading it belongs to picks it up
            else:
                self.walk(child)


def parse_page(html: str, document_code: str, url: str) -> ParsedPage:
    """Walk one saved page into its sections and figures."""
    tree = HTMLParser(html)
    walker = _Walker(document_code, url)
    title_node = tree.css_first("title")
    body = tree.body if tree.body is not None else tree.root
    if body is not None:
        walker.walk(body)
    walker.page.title = (
        collapse(title_node.text())
        if title_node is not None
        else (walker.page.sections[0].title if walker.page.sections else "")
    )
    return walker.page


def page_links(html: str, url: str) -> list[str]:
    """Every ``href`` on the page resolved against its URL, fragments stripped, in order."""
    links: list[str] = []
    for link in HTMLParser(html).css("a[href]"):
        href = (link.attributes.get("href") or "").strip()
        if not href or href.startswith(("mailto:", "javascript:")):
            continue
        resolved = urljoin(url, href).split("#", 1)[0]
        if resolved and resolved not in links:
            links.append(resolved)
    return links
