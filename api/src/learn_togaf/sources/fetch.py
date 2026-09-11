"""
Crawl the Digital Edition (learn_togaf.md §1.4): from ``sources.base_url``, following only
links under ``pubs.opengroup.org/togaf-standard/**``, one request at a time with the configured
delay, using the cookies ``session.py`` saved. Each page lands in
``resources/sources/html/<doc>/<page>.html``; the manifest records URL, title, hash, ETag and
fetch time. A page whose ETag or hash is unchanged is not rewritten. A redirect to the identity
provider stops the crawl with a message to run ``login``.

``classify_url`` and ``html_path`` are pure so the layout can be tested without the network.
"""

import hashlib
import time
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlsplit

import httpx
from loguru import logger

from learn_togaf.sources.manifest import Manifest, PageEntry
from learn_togaf.sources.parse_html import page_links, parse_page
from learn_togaf.sources.session import LoginRequired, is_login_redirect

PAGE_SUFFIXES = (".html", ".htm", "")
BINARY_SUFFIXES = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".pdf",
    ".css",
    ".js",
    ".zip",
    ".ico",
    ".woff",
    ".woff2",
)


def content_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def classify_url(url: str, base_url: str) -> tuple[str, str] | None:
    """(document segment, page file name) for an in-scope page URL, else None.

    ``…/togaf-standard/adm/chap03.html`` → ``("adm", "chap03.html")``;
    ``…/togaf-standard/guides/business-scenarios/`` → ``("guides/business-scenarios", "index.html")``;
    the publication root itself → ``("root", "index.html")``. Images, PDFs and assets are None.
    """
    if not url.startswith(base_url):
        return None
    rel = urlsplit(url[len(base_url) :]).path
    suffix = Path(rel).suffix.lower()
    if suffix in BINARY_SUFFIXES or (suffix and suffix not in PAGE_SUFFIXES):
        return None
    parts = [part for part in rel.split("/") if part]
    if not parts:
        return "root", "index.html"
    if parts[0] == "guides":
        if len(parts) == 1:
            return "guides", "index.html"
        segment, rest = f"guides/{parts[1]}", parts[2:]
    else:
        segment, rest = parts[0], parts[1:]
    page = "__".join(rest) if rest else "index.html"
    if rel.endswith("/") or not Path(page).suffix:
        page = f"{page}__index.html" if rest else "index.html"
    return segment, page


def html_path(sources_dir: Path, segment: str, page: str) -> Path:
    return sources_dir / "html" / segment / page


@dataclass
class CrawlReport:
    fetched: int = 0
    unchanged: int = 0
    skipped: int = 0
    pages: list[str] = field(default_factory=list)

    def summary(self) -> str:
        return f"fetched={self.fetched} unchanged={self.unchanged} out_of_scope={self.skipped}"


def crawl(
    client: httpx.Client,
    base_url: str,
    sources_dir: Path,
    manifest: Manifest,
    delay_seconds: float,
    limit: int | None = None,
) -> CrawlReport:
    report = CrawlReport()
    queue = [base_url]
    seen = {base_url}
    while queue:
        if limit is not None and report.fetched >= limit:
            logger.info(f"--limit {limit} reached; {len(queue)} URLs left in the queue")
            break
        url = queue.pop(0)
        classified = classify_url(url, base_url)
        if classified is None:
            report.skipped += 1
            continue
        segment, page = classified
        document = manifest.documents.get(segment)
        previous = document.pages.get(page) if document is not None else None
        headers = {"If-None-Match": previous.etag} if previous is not None and previous.etag else {}
        response = client.get(url, headers=headers)
        report.fetched += 1
        time.sleep(delay_seconds)
        if is_login_redirect(response):
            raise LoginRequired(
                f"{url} redirected to the Open Group identity provider: the saved session has expired. "
                f"Run: python sources.py login"
            )
        if response.status_code == 304:
            report.unchanged += 1
            body = html_path(sources_dir, segment, page).read_bytes()
        elif response.status_code >= 400:
            # A dead link on the site itself (the index links a misspelled page). Log it, keep
            # crawling; the manifest simply never carries a page for it.
            logger.warning(f"{url}: HTTP {response.status_code}, skipped")
            report.skipped += 1
            continue
        else:
            body = response.content
        digest = content_hash(body)
        path = html_path(sources_dir, segment, page)
        if previous is not None and previous.hash == digest and path.is_file():
            report.unchanged += 1 if response.status_code != 304 else 0
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            report.pages.append(f"{segment}/{page}")
        html = body.decode("utf-8", errors="replace")
        parsed = parse_page(html, "TMP", url)
        kind = "GUIDE" if segment.startswith("guides/") else "STANDARD"
        entry = manifest.document(segment, code=segment, kind=kind)
        if page == "index.html":
            entry.html_url = url
            entry.title = entry.title or parsed.title
        entry.pages[page] = PageEntry(
            url=url,
            title=parsed.title,
            hash=digest,
            fetched_at=datetime.now(UTC).isoformat(timespec="seconds"),
            etag=response.headers.get("etag", previous.etag if previous else ""),
        )
        for link in page_links(html, url):
            if link.startswith(base_url) and link not in seen:
                seen.add(link)
                queue.append(link)
    manifest.fetched_at = datetime.now(UTC).isoformat(timespec="seconds")
    return report
