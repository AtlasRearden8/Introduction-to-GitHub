# Chapter 21: Project 3: Write a Book or Documentation 📚

🎯 **Goals:** Use GitHub as a writing studio. You'll set up a repository for a book, a set of class notes, or a project's documentation, and use branches, pull requests, and reviews as your editorial workflow. You'll end up with a published, searchable, readable site.

⏱️ **Time:** about 75 minutes to set up, then as long as you like to write.

**Why GitHub for writing?** Every change is saved with a message. You can see what changed between drafts, bring back old paragraphs, invite editors to comment on specific lines, and publish a clean website. It's version control for words.

---

## 🧭 Pick your project

Choose something you actually want to write:

| Idea | Who it's for |
|------|--------------|
| A **novel or short-story collection** | Fiction writers |
| A **guide or handbook** (like this one!) | Teachers, experts |
| **Class notes or a study guide** | Students |
| A **club or team handbook** | Organizers |
| **Documentation** for a hobby, tool, or open-source project | Makers |
| A **research notebook** | Scientists, scholars |

We'll call it `my-book` below. Use whatever name fits.

## 🏗️ Step 1: Structure your repository

A tidy layout keeps a big project understandable:

```
my-book/
├── README.md              ← what the book is and how to read it
├── index.md               ← the home page of the website
├── _config.yml            ← the website theme
├── chapters/
│   ├── 01-beginning.md
│   ├── 02-middle.md
│   └── 03-end.md
├── images/
└── notes/                 ← research, outlines, ideas
```

**Naming tip:** put numbers at the start of chapter files (`01-`, `02-`) so they stay in order. Use lowercase letters and hyphens instead of spaces.

### Create it

1. On github.com, click **+ → New repository**, name it `my-book`, tick **Add a README file**, and make it **Public** if you want a free website (or **Private** while you write).
2. Clone it with GitHub Desktop (**File → Clone repository...**).
3. In your project folder, create the `chapters`, `images`, and `notes` folders. Git only tracks folders that have files in them, so add a small placeholder file in each, such as `notes/ideas.md`.

## ✍️ Step 2: Write the first chapter

Create `chapters/01-beginning.md`:

````markdown
# Chapter 1: The Beginning

*A short line that sets the scene.*

Start writing here. Use blank lines between paragraphs.

## A section heading

Keep going...
````

Write a few paragraphs. In GitHub Desktop, look at the **Changes** tab and commit with a message such as `Draft chapter 1 opening`.

### 💾 How often should I commit?

Commit when you've done something you'd want to be able to return to: after a scene, a section, an editing pass. Short, honest messages build a diary of your writing:

| Good message | Why |
|--------------|-----|
| `Draft chapter 1 opening` | Says what you did |
| `Tighten dialogue in chapter 2` | Specific |
| `Cut the flashback; moves to notes` | Records a decision |
| `Fix timeline: Anna is 17, not 16` | Future you will thank you |

## 📜 Step 3: A home page with a table of contents

Create `index.md`:

````markdown
# My Book Title

*By Your Name*

A one-paragraph description of what this book is about.

## Contents
1. [The Beginning](chapters/01-beginning)
2. [The Middle](chapters/02-middle)
3. [The End](chapters/03-end)
````

And `_config.yml`:

```yaml
theme: jekyll-theme-minimal
title: My Book Title
description: By Your Name
```

Commit, click **Push origin**, and turn on **Settings → Pages** (Chapter 13). In a minute you have a book website.

## 🏁 Step 4: Plan the work with issues and milestones

Writing a book is a big job. Break it down.

1. Create an issue for each chapter: `Draft chapter 1`, `Draft chapter 2`, and so on.
2. Add labels such as `draft`, `needs edit`, `final`, `research`, `idea`.
3. Create **milestones** (in **Issues → Milestones**) like **First draft** (due in 4 weeks) and **Second draft**. Add each chapter's issue to a milestone. The milestone page shows a progress bar.
4. Create a **Project board** with columns **Ideas**, **Writing**, **Editing**, **Done**. Drag chapters across as you go. It's wonderfully motivating.

## 🌿 Step 5: Use branches for experiments

Not sure about a change? Try it on a branch.

- A big **rewrite** of a chapter? Make a branch `rewrite-chapter-2`.
- An **alternate ending**? Branch `alt-ending`.
- A **new structure**? Branch `restructure`.

If you like the result, merge it. If not, delete the branch. Your original is untouched. This is the superpower that word processors can't match.

To compare, use **Current branch** to switch back and forth, and read each version.

## 🧑‍🏫 Step 6: Invite editors and readers

### Editors

1. **Settings → Collaborators → Add people.**
2. Ask them to make a branch and open a pull request with their edits, or just leave comments.

### Reviewing a chapter as a pull request

When a chapter is ready for feedback:

1. Make a branch for it, such as `edit-chapter-1`.
2. Open a pull request. Describe what you'd like feedback on ("Is the opening hook strong enough?").
3. Your editor reads the **Files changed** tab, and comments on specific lines: "This sentence is long. Could we split it?"
4. They can use **suggestions** (the ± button) to propose exact rewrites, which you accept with one click.
5. You reply, make changes, and push more commits.
6. Merge when you're happy.

Chapter 11 explains the full review workflow. Every comment and change is saved, so you can always see how the chapter evolved.

### Readers, without GitHub accounts

If your repo is public and has a Pages site, anyone can read it. To get feedback from people who don't have GitHub, let them email you, or share the site address and add a note: "Typos? Ideas? Open an issue on GitHub, or email me."

## 🔍 Step 7: See exactly what changed

This is the part writers love.

1. In GitHub Desktop, open the **History** tab, click a commit, and see the added (green) and removed (red) text.
2. On github.com, open a chapter file and click **History** to see every version.
3. Click any commit and choose **View file** to read the chapter exactly as it was.
4. To compare two branches, open the repository's **Pull requests** page and start a **New pull request** just to look. You don't have to create it.

### ↩️ Getting old text back

You cut a paragraph and now you miss it?

1. Open the chapter file on github.com and click **History**.
2. Find the commit where it still existed and click **Browse files**, or click the three-dot menu and **View file**.
3. Copy the paragraph and paste it into your current chapter.

Or, if you'd like to undo a whole commit, use **Revert** in GitHub Desktop's **History** tab (Chapter 12).

## 🏷️ Step 8: Mark drafts as releases

When you finish a draft, preserve it:

1. **Releases → Draft a new release.**
2. Tag `draft-1`, title `First draft`, and a short note.
3. **Publish release.**

You can download that exact version any time. Make one for every milestone. It's like pressing a time capsule.

## 🖨️ Step 9: Make a PDF or print version

Without any special tools:

1. Open your published website or a rendered chapter on GitHub.
2. In your browser, choose **Print** (`Ctrl+P` on Windows, `Cmd+P` on Mac).
3. Choose **Save as PDF** as the destination.

For a combined book, create one long file by copying chapters into a single `full-book.md` (or ask an editor-friendly friend to help set up an automatic build). Many writers simply print chapter by chapter.

## 🌟 Stretch goals

| Idea | How |
|------|-----|
| **A cover image** | Add `images/cover.jpg` and show it on `index.md`. |
| **Footnotes** | `Text[^1]` and `[^1]: The note.` (Chapter 4). |
| **A glossary page** | `glossary.md` linked from the contents. |
| **Callout boxes** | `> [!NOTE]` blocks for asides. |
| **A word-count goal** | Use an issue checklist: `- [ ] 10,000 words`. |
| **A "Beta readers" project** | Invite 3 friends to read and comment on pull requests or issues. |
| **A changelog** | `CHANGELOG.md` listing what changed in each draft. |

## 🧯 Stuck?

- **A chapter isn't in the right order:** Rename files so the numbers are correct (`02-` before `03-`), and update the links on `index.md`.
- **My site doesn't show a chapter:** Check the link path and that the file ends in `.md`. Links don't need the `.md` on a Pages site.
- **I'm worried about losing work:** Commit often, and click **Push origin** at the end of every session. GitHub holds a safe copy.
- **I deleted something by mistake:** Chapter 12 shows how to get it back.
- **I want my draft to be private:** Keep the repo **private**. Switch it to public when you're ready to share.

## ✅ Checkpoint

- [ ] I have a repository with a clear structure and a README.
- [ ] I wrote at least one chapter and committed it with a good message.
- [ ] I can see what changed between versions.
- [ ] I used a branch to try an idea.
- [ ] I know how an editor could comment on my work in a pull request.
- [ ] I marked a draft with a release.

---

Previous: [Chapter 20](20-project-team.md) · Next: **[Chapter 22: Project 4: Your First Open-Source Contribution](22-project-open-source.md)**
