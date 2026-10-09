# Book information for Amazon KDP

Copy these into the "Paperback Details" page when you set up the book at <https://kdp.amazon.com>.

## Title and subtitle

| Field | Value |
|-------|-------|
| **Title** | GitHub for Complete Beginners |
| **Subtitle** | A Friendly, No-Command-Line Guide to Git, GitHub Desktop, Pull Requests, Websites, and Open Source |
| **Series** | *(leave blank)* |
| **Edition** | 1 |
| **Author** | Dylan Asdale |
| **Language** | English |

The title and subtitle together are about 130 characters. KDP allows 200.

> **A note on the word "GitHub" in the title.** Many independent books use it. Your copyright page already says the book is not affiliated with GitHub, Inc. Avoid anything on the cover that looks official, like the Octocat mascot or GitHub's logo. The cover does not use either.

## Description (paste this into KDP's description box)

KDP accepts a small set of HTML tags (`<b>`, `<i>`, `<u>`, `<br>`, `<p>`, `<ul>`, `<li>`, and headings `<h4>` to `<h6>`). This version uses only those. It is about 2,400 characters. KDP allows 4,000.

```html
<p><b>You've heard "just put it on GitHub" a hundred times. This book finally explains what that means, without a single command to type.</b></p>

<p>GitHub is where the world keeps its projects, but most guides assume you already know how to code or live in a terminal. This one doesn't. <i>GitHub for Complete Beginners</i> teaches Git, GitHub Desktop, and the GitHub website step by step, in plain English, using only buttons, menus, and your web browser.</p>

<p>Whether you write, design, teach, study, research, or just want to build something and share it, you'll learn to make your account, save your work, try ideas without fear, work with other people, publish a free website, and make your first contribution to an open-source project.</p>

<h4>Inside you'll learn how to:</h4>
<ul>
<li>Understand Git and GitHub with simple pictures and everyday comparisons</li>
<li>Set up a secure account and install GitHub Desktop</li>
<li>Create repositories, save snapshots of your work, and read your history</li>
<li>Use branches to experiment safely, and merge the good ideas</li>
<li>Open, review, and merge pull requests like a pro</li>
<li>Track tasks with issues and project boards</li>
<li>Undo almost any mistake, so you can experiment without worry</li>
<li>Write beautiful Markdown, from headings to tables to diagrams</li>
<li>Publish a website with GitHub Pages and polish your profile</li>
<li>Automate boring jobs with GitHub Actions, and protect your account and privacy</li>
<li>Use AI helpers wisely and safely</li>
</ul>

<h4>More than a reference</h4>
<ul>
<li><b>32 short chapters</b> with "Try it," "Stuck?", and "Checkpoint" sections that help every idea stick</li>
<li><b>Four guided projects:</b> a personal website, a team project, a book or documentation, and your first open-source contribution</li>
<li><b>A 30-day practice plan</b> that builds the habit one small task at a time</li>
<li><b>Copy-and-paste templates,</b> a complete cheat sheet, a plain-English glossary, a troubleshooting guide, and quizzes with answers</li>
</ul>

<p>No coding experience needed. If you can use a web browser and click buttons, you can learn this.</p>

<p><b>Start your first repository today.</b></p>
```

### The same description as plain text

You've heard "just put it on GitHub" a hundred times. This book finally explains what that means, without a single command to type.

GitHub is where the world keeps its projects, but most guides assume you already know how to code or live in a terminal. This one doesn't. GitHub for Complete Beginners teaches Git, GitHub Desktop, and the GitHub website step by step, in plain English, using only buttons, menus, and your web browser.

Whether you write, design, teach, study, research, or just want to build something and share it, you'll learn to make your account, save your work, try ideas without fear, work with other people, publish a free website, and make your first contribution to an open-source project.

Inside, you'll learn how to understand Git and GitHub, set up a secure account, create repositories and save snapshots, use branches to experiment safely, open and review pull requests, track tasks with issues, undo almost any mistake, write Markdown, publish a website with GitHub Pages, automate with GitHub Actions, protect your privacy, and use AI helpers wisely.

You also get 32 short chapters with practice sections, four guided projects, a 30-day practice plan, templates, a cheat sheet, a glossary, a troubleshooting guide, and quizzes with answers.

No coding experience needed. If you can use a web browser and click buttons, you can learn this.

## Author bio (optional, goes on your Author Central page)

*Write two or three sentences here, in your own words. For example: who you are, why you wrote this, and what you'd like readers to feel. Dylan Asdale is a ...*

## Keywords (KDP gives you seven boxes)

1. github for beginners
2. github desktop tutorial
3. learn git without command line
4. pull requests and branches guide
5. open source for beginners
6. github pages website for beginners
7. version control for non-programmers

Tip: type each phrase into Amazon's search bar. If it autocompletes, people really search for it.

## Categories (pick two in KDP's category picker)

KDP's list changes, so choose the closest fits. Good places to look:

- **Computers & Technology › Programming › Software Design, Testing & Engineering** (or the nearest Software Development category)
- **Computers & Technology › Web Development & Design** (for the Pages and website chapters)
- **Computers & Technology › Software** (general beginner guides)

## Audience

| Field | Value |
|-------|-------|
| **Reading age** | Leave blank (or 13 and up) |
| **Sexually explicit / adult content** | No |
| **Low-content or journal** | No |
| **Large print** | No |

## Print options (what the files in `kdp/out` were built for)

| Option | Setting |
|--------|---------|
| **Trim size** | 8.5 × 11 in |
| **Bleed** | Bleed (the cover has bleed). The interior has no bleed. |
| **Paper** | White |
| **Interior** | Premium color (the book uses color accents) |
| **Cover finish** | Matte, or glossy if you prefer |
| **Page count** | 252 |

### Black-and-white instead?

Premium color at 8.5 × 11 and 252 pages is much more expensive per copy than black-and-white, which pushes the list price up. If you want a lower price, print in black and white. The purple becomes gray, which still looks good. If you switch, rebuild the cover so the spine width is right:

```
python kdp/build_cover.py --pages 252 --ink bw
```

## Pricing

Check KDP's **print cost calculator** for your exact trim, ink, and page count, then set a list price above that cost so you earn a royalty. Premium color at this size will need a much higher price than black-and-white.

## Before you publish: a short checklist

- [ ] **Add real screenshots.** The online edition has dashed "Screenshot:" boxes where pictures should go. The print interior in `kdp/out` leaves those boxes out so nothing looks unfinished, but a beginner's book is far better with real screens. Capture GitHub Desktop and github.com on your own computer and add them. Then rebuild without `--no-placeholders`, or place the images into the chapters.
- [ ] **Walk through the instructions yourself.** Every menu name and button label was written from the documentation and memory. GitHub changes its screens. Click through at least the chapters you want to be most proud of, and fix anything that doesn't match.
- [ ] **Check the AI disclosure.** KDP asks, when you set up the book, whether any text, images, or translations were created with AI tools. This guide was drafted with an AI assistant (Claude) and directed and edited by you. KDP separates "AI-generated" content (which you must disclose) from "AI-assisted" content (which you don't need to). Read KDP's current definitions and answer honestly for how the book was actually made.
- [ ] **Confirm the name you publish under.** The `LICENSE` file and the copyright page both name Dylan Asdale as the author. Make sure that matches the name on your KDP account and tax information, or change it in `scripts/guide.py` and `LICENSE` before you publish.
- [ ] **Get an ISBN, or let KDP give you one.** KDP offers a free ISBN. If you use it, KDP is listed as the publisher. You can also buy your own.
- [ ] **Order a proof copy** and read it on paper before you approve it for sale.
- [ ] **Read the reviewer's view in KDP's online previewer** to check that the margins and the cover look right.
