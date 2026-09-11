#!/usr/bin/env python3
"""Attach the standard's figures to every lesson that cites their sections (learn_togaf.md §1.4).

For each lesson, the refs in its front matter and body are resolved to sections; every figure
whose section is one of those (or beneath one) is appended in a "Figures from the standard"
block, served from the local store. Idempotent: the block is replaced on every run. Lessons
that already embed a figure by hand keep it; those figures are not repeated.
"""
import re, sys
from pathlib import Path
sys.path.insert(0, "api/src")
from learn_togaf.db import connect
from learn_togaf.sources import index

BLOCK_START, BLOCK_END = "<!-- figures:start -->", "<!-- figures:end -->"
c = connect()
REF_RE = re.compile(r"\b((?:INTRO|ADM|TECH|APPLY|CONTENT|GOV|GUIDE:[a-z0-9\-]+) §[0-9][0-9.]*[0-9])")
total_lessons = with_figs = 0
for path in sorted(Path("content/lessons").glob("*/*.md")):
    text = path.read_text(encoding="utf-8")
    body = re.sub(rf"{BLOCK_START}.*?{BLOCK_END}\n?", "", text, flags=re.S)
    refs = sorted(set(REF_RE.findall(body)))
    section_ids = []
    for ref in refs:
        for row in index.resolve_ref(c, ref):
            section_ids += [r["id"] for r in index.section_with_descendants(c, row["id"])]
    already = set(re.findall(r'/figure/([A-Za-z0-9:\-_]+)', body))
    figures = []
    if section_ids:
        marks = ",".join("?" * len(set(section_ids)))
        for row in c.execute(f"SELECT id, caption, document_code FROM source_figure WHERE section_id IN ({marks}) ORDER BY document_code, id", tuple(set(section_ids))):
            if row["id"] not in already and not row["id"].split(":")[-1].startswith("pdf-"):
                figures.append(row)
    total_lessons += 1
    if not figures:
        path.write_text(body, encoding="utf-8"); continue
    with_figs += 1
    items = "\n".join(
        f'<figure class="max-w-lg"><img src="/figure/{f["id"]}" alt="{f["caption"]}" loading="lazy" class="rounded border border-base-300">'
        f'<figcaption class="text-xs text-base-content/60 mt-1">{f["caption"]} ({f["document_code"]})</figcaption></figure>'
        for f in figures)
    block = f'\n{BLOCK_START}\n## Figures from the standard\n\nThe diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.\n\n<div class="grid gap-4 md:grid-cols-2">\n{items}\n</div>\n{BLOCK_END}\n'
    if "## Check yourself" in body:
        body = body.replace("## Check yourself", block.strip("\n") + "\n\n## Check yourself", 1)
    else:
        body = body.rstrip("\n") + "\n" + block
    path.write_text(body, encoding="utf-8")
    print(f"{path.relative_to('content/lessons')}: {len(figures)} figure(s)")
print(f"{with_figs} of {total_lessons} lessons got figures")
