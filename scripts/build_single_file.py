"""Stitch the whole guide into one Markdown file: great for offline reading, or for
handing to an AI as context.

    python scripts/build_single_file.py            # writes MANUAL.md
    python scripts/build_single_file.py out.md     # custom output path
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from guide import SITE, TITLE, chapters  # noqa: E402


def to_site_url(target: str) -> str:
    """Links between files don't survive concatenation, so point them at the website."""
    path, _, frag = target.partition("#")
    if path.endswith(".md"):
        path = "" if path == "index.md" else path.removesuffix(".md") + "/"
    return SITE + path + (f"#{frag}" if frag else "")


def main(out: Path) -> None:
    chaps = chapters()
    toc = [f"# {TITLE}", "", "## Table of Contents", ""] + [f"- {c.h1}" for c in chaps]
    body: list[str] = []
    for c in chaps:
        text = re.sub(
            r"\]\((?!https?://|#)([^)\s]+)\)", lambda m: f"]({to_site_url(m.group(1))})", c.text
        )
        text = re.sub(r"^# ", "## ", text, count=1, flags=re.M)
        body += ["", "---", "", text]
    out.write_text("\n".join(toc + body) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("MANUAL.md"))
