"""Shared helpers: the chapter list, in reading order, read from the guide/ folder.

The book is organised in Parts. Each Part starts at a chapter number; chapter files are named NN-slug.md.
`scripts/sync_toc.py` rewrites the site menu, the contents tables and the Previous/Next links from this data.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "guide"
TITLE = "Introduction to GitHub"  # the website's name
SUBTITLE = "A complete, friendly guide for absolute beginners"

# The book (PDF and print edition)
BOOK_TITLE = "GitHub for Complete Beginners"
BOOK_SUBTITLE = "A Friendly, No-Command-Line Guide to Git, GitHub Desktop, Pull Requests, Websites, and Open Source"
BOOK_TAGLINE = "32 chapters · 4 guided projects · a 30-day plan"
AUTHOR = "Dylan Asdale"
YEAR = 2026
SITE = "https://atlasrearden8.github.io/Introduction-to-GitHub/"
CHAPTER_FILE = re.compile(r"^(\d{2})-.+\.md$")

# (first chapter number, emoji, name, one-line description)
PARTS = [
    (0, "🌱", "Start Here", "Meet the ideas, make your account, and get set up."),
    (3, "🛠️", "The Basics", "Your first repository, Markdown, and GitHub Desktop."),
    (7, "🤝", "Working Together", "Branches, pull requests, issues, and open source."),
    (12, "🧯", "Mastery", "Undo anything, publish websites, automate, and stay safe."),
    (19, "🚀", "Real Projects", "Four guided projects and a 30-day plan to make it stick."),
    (25, "📎", "Reference", "Cheat sheets, templates, glossary, troubleshooting, and quizzes."),
]

# chapter number -> (what you will learn, time)
BLURBS = {
    0: ("How this guide works and the big picture", "10 min"),
    1: ("The core ideas, with no jargon pile-ups", "15 min"),
    2: ("Sign up, secure your account, install GitHub Desktop", "30 min"),
    3: ("Create a project, edit files in your browser", "30 min"),
    4: ("Format anything: headings, links, images, tables", "30 min"),
    5: ("Create a project, save snapshots, read your history", "45 min"),
    6: ("Clone, push, pull, and fixing conflicts", "45 min"),
    7: ("Safe experimenting, and combining work", "45 min"),
    8: ("The heart of GitHub collaboration", "45 min"),
    9: ("Track tasks, bugs, and ideas", "30 min"),
    10: ("Forks, teamwork, your first contribution", "60 min"),
    11: ("Review kindly, get reviewed well, work as a team", "40 min"),
    12: ("Your safety net: discard, undo, revert, recover", "40 min"),
    13: ("Publish a real website for free", "45 min"),
    14: ("Make a profile people remember", "30 min"),
    15: ("Let GitHub do the boring work for you", "45 min"),
    16: ("Protect your account, your work, and your privacy", "40 min"),
    17: ("Use AI helpers safely and well", "35 min"),
    18: ("Codespaces, releases, gists, and shortcuts", "30 min"),
    19: ("Build and publish a site about you", "90 min"),
    20: ("Run a small team project from start to finish", "90 min"),
    21: ("Write a book, notes, or documentation together", "75 min"),
    22: ("Make a real contribution to someone else's project", "75 min"),
    23: ("How writers, designers, students, and researchers use GitHub", "30 min"),
    24: ("A day-by-day plan to build the habit", "30 days"),
    25: ("Every menu and button in GitHub Desktop", "reference"),
    26: ("Where to click, on one page", "reference"),
    27: ("Copy-and-paste READMEs, issue forms, and more", "reference"),
    28: ("Every term in plain English", "reference"),
    29: ("Fixes for common problems, plus FAQ", "reference"),
    30: ("Test yourself, with answers", "reference"),
    31: ("Books, courses, and communities", "reference"),
}


@dataclass
class Chapter:
    path: Path

    @property
    def num(self) -> int:
        return int(CHAPTER_FILE.match(self.path.name).group(1))

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

    @property
    def title(self) -> str:
        """Title without the 'Chapter N:' prefix and without the trailing emoji."""
        t = re.sub(r"^Chapter \d+:\s*", "", self.h1)
        return re.sub(r"\s*[^\w\s.,!?&:;'\"()/-]+\s*$", "", t).strip()

    @property
    def emoji(self) -> str:
        m = re.search(r"\s*([^\w\s.,!?&:;'\"()/-]+)\s*$", self.h1)
        return m.group(1) if m else ""


def chapters() -> list[Chapter]:
    return [Chapter(p) for p in sorted(GUIDE.iterdir()) if CHAPTER_FILE.match(p.name)]


def part_for(num: int):
    current = PARTS[0]
    for part in PARTS:
        if part[0] <= num:
            current = part
    return current
