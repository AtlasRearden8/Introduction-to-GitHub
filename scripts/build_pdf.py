"""Turn the whole guide into a PDF book (cover, part dividers, clickable contents, bookmarks, page numbers).

    pip install -r requirements-pdf.txt
    python -m playwright install chromium          # plus an emoji font, e.g. fonts-noto-color-emoji
    python scripts/build_pdf.py                    # MANUAL.pdf: black-and-purple edition, US Letter
    python scripts/build_pdf.py --paper a4 --out MANUAL-A4.pdf
    python scripts/build_pdf.py --theme print --out MANUAL-print.pdf    # white pages, light on toner, still purple

How it works: each chapter is rendered from Markdown to HTML, links between chapters become jumps inside
the book, and headless Chromium prints the result (with bookmarks from the headings).
"""

from __future__ import annotations

import argparse
import base64
import html
import os
import re
import sys
import tempfile
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).parent))
from guide import (  # noqa: E402
    AUTHOR, BOOK_SUBTITLE, BOOK_TAGLINE, BOOK_TITLE, PARTS, SITE, YEAR, chapters, part_for,
)

FONT_DIR = Path(__file__).parent / "pdf" / "fonts"
FONT_FACES = [  # (family, weight, file)
    ("Plus Jakarta Sans", 400, "pjs-400.woff2"), ("Plus Jakarta Sans", 500, "pjs-500.woff2"),
    ("Plus Jakarta Sans", 600, "pjs-600.woff2"), ("Plus Jakarta Sans", 700, "pjs-700.woff2"),
    ("Plus Jakarta Sans", 800, "pjs-800.woff2"),
    ("Fraunces", 600, "fraunces-600.woff2"), ("Fraunces", 700, "fraunces-700.woff2"),
    ("Fraunces", 800, "fraunces-800.woff2"),
    ("JetBrains Mono", 400, "jbm-400.woff2"), ("JetBrains Mono", 700, "jbm-700.woff2"),
]
PAPER_COLOR = {"dark": "#0b0712", "print": "#ffffff"}


def font_css() -> str:
    """Fonts are embedded, so the book looks identical on every computer."""
    rules = []
    for family, weight, name in FONT_FACES:
        data = base64.b64encode((FONT_DIR / name).read_bytes()).decode()
        rules.append(
            f'@font-face{{font-family:"{family}";font-weight:{weight};font-style:normal;'
            f'src:url(data:font/woff2;base64,{data}) format("woff2");}}'
        )
    return "".join(rules)


def book_css(theme: str) -> str:
    css = (Path(__file__).parent / "pdf" / "book.css").read_text(encoding="utf-8")
    return font_css() + css.replace("PAPER", PAPER_COLOR[theme])


PAPER = {"letter": ("8.5in", "11in"), "a4": ("210mm", "297mm")}
EXTENSIONS = ["tables", "sane_lists", "attr_list", "md_in_html", "pymdownx.superfences", "pymdownx.tasklist", "pymdownx.highlight"]
EXT_CONFIG = {"pymdownx.highlight": {"use_pygments": False}}


def render(text: str) -> str:
    return markdown.markdown(text, extensions=EXTENSIONS, extension_configs=EXT_CONFIG)


SECTION_CLASS = {"Try it": "try", "Stuck?": "stuck", "Checkpoint": "check"}
CAUTION = ("Careful", "Golden rule", "Danger")
EMOJI_TAIL = re.compile(r"\s*([^\w\s.,!?&:;'\"()/-]+)\s*$")


def decorate(body: str) -> str:
    """Turn plain Markdown HTML into the designed book: chapter opener card, section bands, callout types."""

    def opener(m: re.Match) -> str:
        num, title = m.group(1), m.group(2)
        icon = ""
        tail = EMOJI_TAIL.search(title)
        if tail:
            icon, title = tail.group(1), title[: tail.start()]
        goals = re.search(r"<p>(?:[^<]{0,4})<strong>Goals:</strong>\s*(.*?)</p>", body, re.S)
        lede = f'<p class="goals">{goals.group(1)}</p>' if goals else ""
        return (
            f'<header class="opener"><div class="icon">{icon}</div><div class="eyebrow">Chapter {num}</div>'
            f"<h1>{title}</h1>{lede}</header>"
        )

    body = re.sub(r"<h1>Chapter (\d+): (.*?)</h1>", opener, body, count=1)
    body = re.sub(r"<p>(?:[^<]{0,4})<strong>Goals:</strong>.*?</p>\s*(<hr\s*/?>)?", "", body, count=1, flags=re.S)

    def band(m: re.Match) -> str:
        emoji, label = m.group(1), m.group(2)
        return f'<h2 class="band {SECTION_CLASS[label]}">{emoji} {label}'

    body = re.sub(r"<h2>(\S+) (Try it|Stuck\?|Checkpoint)", band, body)

    def callout(m: re.Match) -> str:
        prefix, label = m.group(1), m.group(2)
        kind = "warn" if ("⚠" in prefix or label.startswith(CAUTION)) else "note"
        return f'<blockquote class="{kind}"><p>{prefix}<strong>{label}'

    body = re.sub(r"<blockquote>\s*<p>([^<]{0,6})<strong>([^<]*)", callout, body)
    return body


def anchor(stem: str) -> str:
    return f"ch-{stem}"


def fix_links(body: str, stems: set[str]) -> str:
    """chapter.md links → jumps inside the book; index.md/download.md → the website."""

    def repl(m: re.Match) -> str:
        target = m.group(1)
        path, _, _ = target.partition("#")
        stem = path.removesuffix(".md")
        if path.endswith(".md") and stem in stems:
            return f'href="#{anchor(stem)}"'
        if path.endswith(".md"):
            return f'href="{SITE}{"" if stem == "index" else stem + "/"}"'
        return m.group(0)

    return re.sub(r'href="((?!https?://|#|mailto:)[^"]+)"', repl, body)


def part_divider(part, index: int) -> str:
    start, emoji, name, blurb = part
    return (
        f'<div class="part"><div class="pn">{index:02d}</div><div class="eyebrow">Part {index}</div>'
        f"<h1>{emoji} {html.escape(name)}</h1><p>{html.escape(blurb)}</p></div>"
    )


def front_matter(kdp: bool) -> str:
    """The first pages: a designed cover for the screen editions, a plain title page and copyright page for KDP."""
    if not kdp:
        return (
            '<div class="cover"><div class="emojis">🌱 🛠️ 🤝 🧯 🚀</div><div class="kicker">A beginner\'s guide</div>'
            f"<h1>{html.escape(BOOK_TITLE)}</h1><p>{html.escape(BOOK_SUBTITLE)}.</p>"
            f'<div class="by">by {html.escape(AUTHOR)}</div><small>{SITE}</small></div>'
        )
    return (
        '<div class="titlepage"><div class="kicker">A beginner\'s guide</div>'
        f"<h1>{html.escape(BOOK_TITLE)}</h1><p class=\"sub\">{html.escape(BOOK_SUBTITLE)}</p>"
        f'<div class="rule"></div><div class="by">{html.escape(AUTHOR)}</div></div>'
        '<div class="copyright">'
        f"<p><strong>{html.escape(BOOK_TITLE)}</strong><br>{html.escape(BOOK_SUBTITLE)}</p>"
        f"<p>Copyright © {YEAR} {html.escape(AUTHOR)}. All rights reserved.</p>"
        "<p>No part of this book may be reproduced, stored in a retrieval system, or transmitted in any form or by any "
        "means without the prior written permission of the author, except for brief quotations in a review.</p>"
        "<p>GitHub, GitHub Desktop, and the Octocat are trademarks of GitHub, Inc. Other product names are trademarks "
        "of their respective owners. This book is an independent guide. It is not affiliated with, endorsed by, or "
        "sponsored by GitHub, Inc.</p>"
        "<p>Every effort has been made to keep the instructions accurate. GitHub changes its screens and menus from time to "
        "time, so what you see may look slightly different. The official documentation at docs.github.com is the final "
        "word on exact screens.</p>"
        "<p>First edition, 2026.</p>"
        f"<p>Online edition: {SITE}</p></div>"
    )


def build_html(theme: str = "dark", kdp: bool = False, placeholders: bool = True) -> str:
    chaps = chapters()
    stems = {c.stem for c in chaps}
    starts = {p[0]: (i + 1, p) for i, p in enumerate(PARTS)}

    toc, sections = [], []
    for c in chaps:
        if c.num in starts:
            idx, part = starts[c.num]
            toc.append(f'</ol><h2 class="toc-part">Part {idx} · {part[1]} {html.escape(part[2])}</h2><ol>')
            sections.append(part_divider(part, idx))
        toc.append(
            f'<li><a href="#{anchor(c.stem)}"><span class="n">{c.num:02d}</span>'
            f'<span class="t">{html.escape(c.title)}</span></a></li>'
        )
        body = fix_links(decorate(render(c.text)), stems)
        if not placeholders:
            body = re.sub(r'<p class="shot">.*?</p>', "", body, flags=re.S)
            body = re.sub(r"<blockquote[^>]*>\s*<p>[^<]{0,6}<strong>Screenshots\.</strong>.*?</blockquote>", "", body, flags=re.S)
        sections.append(f'<section class="chapter" id="{anchor(c.stem)}">{body}</section>')

    contents = "".join(toc)
    cls = theme + (" kdp" if kdp else "")
    return f"""<!doctype html><html lang="en" class="{cls}"><head><meta charset="utf-8"><title>{html.escape(BOOK_TITLE)}</title><style>{book_css(theme)}</style></head><body>
{front_matter(kdp)}
<div class="contents"><div class="eyebrow">Inside</div><h1>Contents</h1><ol>{contents}</ol></div>
{"".join(sections)}</body></html>""".replace("<ol></ol>", "")


def finish_kdp(path: str) -> None:
    """Final touches for print-on-demand: no page number on the title and copyright pages, and an even page count
    (printers want an even number of pages, so one blank page is added at the end if needed)."""
    import pymupdf

    doc = pymupdf.open(path)
    for i in (0, 1):
        page = doc[i]
        r = page.rect
        page.draw_rect(pymupdf.Rect(0, r.height - 50, r.width, r.height), color=None, fill=(1, 1, 1))
    if doc.page_count % 2:
        w, h = doc[-1].rect.width, doc[-1].rect.height
        doc.new_page(width=w, height=h)
        print("Added one blank page so the page count is even.")
    tmp = path + ".tmp"
    doc.save(tmp)
    doc.close()
    os.replace(tmp, path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", choices=PAPER, default="letter")
    parser.add_argument("--theme", choices=("dark", "print"), default="dark")
    parser.add_argument("--out", default="MANUAL.pdf")
    parser.add_argument("--kdp", action="store_true", help="interior for print-on-demand (title and copyright pages, plain backgrounds, even page count)")
    parser.add_argument("--no-placeholders", action="store_true", help="leave out the dashed Screenshot boxes")
    args = parser.parse_args()
    width, height = PAPER[args.paper]
    footer_color = {"dark": "#8f84ad", "print": "#8a809f"}[args.theme]

    from playwright.sync_api import sync_playwright

    with tempfile.TemporaryDirectory() as tmp:
        page_file = Path(tmp) / "book.html"
        page_file.write_text(build_html("print" if args.kdp else args.theme, args.kdp, not args.no_placeholders), encoding="utf-8")
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
            page = browser.new_page()
            page.goto(page_file.as_uri())
            page.pdf(
                path=args.out,
                width=width,
                height=height,
                print_background=True,
                outline=True,
                tagged=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=(
                    f'<div style="font:8px sans-serif;color:{footer_color};width:100%;padding:0 0.95in;'
                    'display:flex;justify-content:space-between">'
                    f"<span>{BOOK_TITLE}</span><span class='pageNumber'></span></div>"
                ),
                prefer_css_page_size=True,
            )
            browser.close()
    if args.kdp:
        finish_kdp(args.out)
    print(f"Wrote {args.out} ({Path(args.out).stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
