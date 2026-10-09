"""Shared helpers: the chapter list, in reading order, read from the guide/ folder."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "guide"
TITLE = "Introduction to GitHub"
SUBTITLE = "A complete, friendly guide for absolute beginners"
SITE = "https://atlasrearden8.github.io/Introduction-to-GitHub/"
CHAPTER_FILE = re.compile(r"^\d{2}-.+\.md$")


@dataclass
class Chapter:
    path: Path

    @property
    def stem(self) -> str:
        return self.path.stem

    @property
    def text(self) -> str:
        return self.path.read_text(encoding="utf-8")

    @property
    def h1(self) -> str:
        for line in self.text.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return self.stem


def chapters() -> list[Chapter]:
    return [Chapter(p) for p in sorted(GUIDE.iterdir()) if CHAPTER_FILE.match(p.name)]
