"""Keep the site menu, contents tables and Previous/Next links in step with the chapter files.

    python scripts/sync_toc.py

Run it after adding, renaming or retitling a chapter. Chapter order and Parts come from scripts/guide.py.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from guide import BLURBS, GUIDE, PARTS, ROOT, chapters, part_for  # noqa: E402

START, END = "<!-- toc:start -->", "<!-- toc:end -->"


def link_label(c) -> str:
    return f"Chapter {c.num}: {c.title}"


def sync_prev_next(chaps) -> None:
    for i, c in enumerate(chaps):
        parts = []
        if i > 0:
            p = chaps[i - 1]
            parts.append(f"Previous: [Chapter {p.num}]({p.path.name})")
        if i < len(chaps) - 1:
            n = chaps[i + 1]
            parts.append(f"Next: **[{link_label(n)}]({n.path.name})**")
        else:
            parts.append("Back to the start: [Home](index.md)")
        line = " · ".join(parts)
        text = c.text
        new, count = re.subn(r"^(?:Previous:|Next:).*$", line, text, count=1, flags=re.M)
        if count == 0:
            new = text.rstrip("\n") + "\n\n---\n\n" + line + "\n"
        if new != text:
            c.path.write_text(new, encoding="utf-8")


def toc_table(chaps, prefix: str) -> str:
    rows = ["| # | Chapter | You will learn | Time |", "|---|---------|----------------|------|"]
    current = None
    for c in chaps:
        part = part_for(c.num)
        if part is not current:
            current = part
            rows.append(f"| | **{part[1]} {part[2]}** | *{part[3]}* | |")
        learn, time = BLURBS.get(c.num, ("", ""))
        rows.append(f"| {c.num} | [{c.title}]({prefix}{c.path.name}) | {learn} | {time} |")
    return "\n".join(rows)


def sync_table(path: Path, chaps, prefix: str) -> None:
    text = path.read_text(encoding="utf-8")
    block = f"{START}\n{toc_table(chaps, prefix)}\n{END}"
    if START in text:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    else:
        new = re.sub(r"^\| # \| Chapter \|.*?(?=\n\n)", lambda _: block, text, count=1, flags=re.S | re.M)
    path.write_text(new, encoding="utf-8")


def sync_nav(chaps) -> None:
    path = ROOT / "mkdocs.yml"
    text = path.read_text(encoding="utf-8")
    head = text[: text.index("\nnav:")]
    lines = ['nav:', '  - "🏠 Home": index.md', '  - "📄 Download the PDF": download.md']
    current = None
    for c in chaps:
        part = part_for(c.num)
        if part is not current:
            current = part
            lines.append(f'  - "{part[1]} {part[2]}":')
        lines.append(f'      - "{c.num} · {c.title}": {c.path.name}')
    path.write_text(head + "\n" + "\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    chaps = chapters()
    sync_prev_next(chaps)
    sync_table(GUIDE / "index.md", chaps, "")
    sync_table(ROOT / "README.md", chaps, "guide/")
    sync_nav(chaps)
    print(f"Synced {len(chaps)} chapters across {len(PARTS)} parts.")


if __name__ == "__main__":
    main()
