"""Turn the whole guide into a printable PDF book (cover, clickable contents, bookmarks, page numbers).

    pip install -r requirements-pdf.txt
    python -m playwright install chromium          # plus an emoji font, e.g. fonts-noto-color-emoji
    python scripts/build_pdf.py                    # writes MANUAL.pdf (US Letter)
    python scripts/build_pdf.py --paper a4 --out MANUAL-A4.pdf

How it works: each chapter is rendered from Markdown to HTML, links between chapters become jumps inside
the book, and headless Chromium prints the result (with bookmarks from the headings).
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import tempfile
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).parent))
from guide import SITE, SUBTITLE, TITLE, chapters  # noqa: E402

CSS = (Path(__file__).parent / "pdf" / "book.css").read_text(encoding="utf-8")
PAPER = {"letter": ("8.5in", "11in"), "a4": ("210mm", "297mm")}
EXTENSIONS = ["tables", "sane_lists", "attr_list", "pymdownx.superfences", "pymdownx.tasklist", "pymdownx.highlight"]
EXT_CONFIG = {"pymdownx.highlight": {"use_pygments": False}}


def render(text: str) -> str:
    return markdown.markdown(text, extensions=EXTENSIONS, extension_configs=EXT_CONFIG)


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


def build_html() -> str:
    chaps = chapters()
    stems = {c.stem for c in chaps}
    contents = "".join(f'<li><a href="#{anchor(c.stem)}">{html.escape(c.h1)}</a></li>' for c in chaps)
    sections = "".join(
        f'<section class="chapter" id="{anchor(c.stem)}">{fix_links(render(c.text), stems)}</section>' for c in chaps
    )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title><style>{CSS}</style></head><body>
<div class="cover"><div class="icon">🚀</div><h1>{TITLE}</h1><p>{SUBTITLE}, starting from square one.</p><small>{SITE}</small></div>
<div class="contents"><h1>Contents</h1><ol>{contents}</ol></div>
{sections}</body></html>"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", choices=PAPER, default="letter")
    parser.add_argument("--out", default="MANUAL.pdf")
    args = parser.parse_args()
    width, height = PAPER[args.paper]

    from playwright.sync_api import sync_playwright

    with tempfile.TemporaryDirectory() as tmp:
        page_file = Path(tmp) / "book.html"
        page_file.write_text(build_html(), encoding="utf-8")
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
                    '<div style="font:8px sans-serif;color:#6b7280;width:100%;text-align:center">'
                    f"{TITLE} · <span class='pageNumber'></span></div>"
                ),
                margin={"top": "0.35in", "bottom": "0.45in"},
            )
            browser.close()
    print(f"Wrote {args.out} ({Path(args.out).stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
