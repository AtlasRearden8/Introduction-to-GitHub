# Chapter 23: GitHub for Writers, Designers, Students & Researchers 🎨

🎯 **Goals:** See how people who don't write code use GitHub in everyday life. Pick the section that matches you, copy the workflow, and adapt it. Nobody is expected to read every section.

---

## 🔑 What works everywhere

No matter who you are, GitHub rewards a few simple habits:

1. **One repository per project.** Keep related files together.
2. **Plain text where you can.** Markdown (Chapter 4) is easy to compare, search, and keep forever.
3. **Commit when something is worth keeping.** Write a message your future self will understand.
4. **Use branches for experiments** (Chapter 7).
5. **Use issues as your to-do list** (Chapter 9).
6. **Use pull requests to ask for feedback** (Chapters 8 and 11).
7. **Back up by pushing.** Click **Push origin** at the end of every session.

### ⚠️ What GitHub is *not* great at

Be honest about limits:

| Kind of file | The catch |
|--------------|-----------|
| **Word, Excel, PowerPoint files** | GitHub stores them, but can't show *what changed inside*. You see "file changed" only. |
| **Photoshop, video, large design files** | They get big quickly. GitHub rejects files over 100 MB, and big files make repos slow. |
| **Anything private or confidential** | Use a **private** repository, or don't use GitHub at all. |
| **Real-time co-editing** | Two people editing at once isn't GitHub's strength. Use branches and pull requests, or a tool built for live editing. |

Tip: Markdown files (`.md`) and plain text are where GitHub shines. Many people **write in Markdown**, then export to Word or PDF when needed.

---

## ✍️ For writers

**Good for:** novels, essays, poetry, scripts, newsletters, blog posts, journalism research.

### A workflow

1. **One repository per big piece** (a book, a series of poems, a screenplay). Chapter 21 walks through the setup.
2. **Draft in Markdown.** Any plain-text editor works.
3. **Commit at milestones:** `Draft scene 3`, `Edit pass 1 complete`.
4. **Branch for experiments:** `alt-ending`, `rewrite-chapter-2`.
5. **Ask editors to review a branch** with a pull request. They comment on specific lines and suggest exact wording.
6. **Tag finished drafts** as **releases**: `draft-1`, `draft-2`.
7. **Track submissions** in an issue or project board: poem name, where sent, date, response.

### Things you can track with issues

- `Fix timeline in chapter 4`
- `Research: how did lamp-lighters work?`
- `Character sheet: Anna`
- `Query letter draft`

### 💡 Pro tips

- Keep **research, outlines, and character notes** in a `notes` folder.
- Use **callouts** (`> [!NOTE]`) in your notes to flag open questions.
- **Search your whole project** with the search box on the repo page to find every mention of a name.
- Keep unpublished work **private**.

---

## 🎨 For designers and artists

**Good for:** design systems, brand guidelines, icon sets, fonts, illustration portfolios, UX research, style guides.

### A workflow

1. **Keep exported files** (PNG, SVG, PDF) in folders by project or version.
2. **SVG files are text,** so GitHub can show you a **visual comparison** and a line-by-line diff. Prefer SVG for icons and logos.
3. **Use README files with embedded images** as a living **brand guide**: colors (with hex codes), fonts, logos, spacing rules.
4. **Use issues for feedback:** drag screenshots into comments, and tag teammates.
5. **Use pull requests** to propose changes to shared assets, and let reviewers compare **before and after** images (the **Files changed** tab has a "2-up" / "swipe" / "onion skin" view for images).
6. **Publish a portfolio** with GitHub Pages (Chapters 13 and 19).

### 🧱 A neat project structure

```
brand-guide/
├── README.md        ← the guide, with images
├── logos/
├── colors.md
├── fonts/           ← only fonts you're licensed to share!
├── icons/
└── social-templates/
```

### 💡 Pro tips

- **Don't commit** huge source files (like layered Photoshop or video). Keep the heavy originals somewhere else, and commit the exports.
- **Check licenses** for fonts, stock images, and icons before sharing them publicly.
- **Add alt text** to every image, as good design includes accessibility.
- **Name files clearly,** like `logo-primary-dark.svg`, not `final_FINAL2.svg`.

---

## 🎓 For students

**Good for:** assignments, group projects, notes, study guides, thesis drafts, a portfolio that employers can see.

### A workflow

1. **One repository per course or per big project.** Name it clearly: `bio101-notes`, `history-capstone`.
2. **Take notes in Markdown,** with a file per topic or lecture date.
3. **Keep a study checklist** with task lists (`- [ ]`).
4. **For group projects**, follow Chapter 20: issues for tasks, branches for work, pull requests for review. Teachers love seeing who did what, because the history shows it honestly.
5. **Build a portfolio:** pin your best repositories and write a profile README (Chapter 14).
6. **Apply for GitHub Education** for free extras with a school email (Chapter 18).

### 🔒 Important

- **Check your school's rules** about sharing assignments publicly. Posting solutions can break academic integrity rules. Use **private** repositories for coursework unless you're told otherwise.
- **Never upload** other students' work or personal information without permission.
- **Credit your sources.**

### 💡 Pro tips

- Make a **template repository** for notes, so each new course starts the same way. (On a repo, **Settings → General**, tick **Template repository**. Then **Use this template** creates a fresh copy.)
- Use **issues** as your assignment tracker, with **milestones** for due dates.
- Put **exam topics** in a task list and tick them as you review.
- Version your **essay drafts** so you can see how your thinking changed.

---

## 🔬 For researchers and scientists

**Good for:** research notes, protocols, data, analysis plans, supplementary materials, open science, preprints.

### A workflow

1. **One repository per study or paper.**
2. **Keep a README** that explains the project: question, methods, folder guide, how to cite.
3. **Store small data files** (text and CSV) and **documentation** of where large data lives.
4. **Record decisions** in commit messages and issues: why you excluded something, why you changed a protocol.
5. **Use releases** to freeze the exact version that matches a published paper.
6. **Add a LICENSE and a CITATION.cff file** so others can cite you correctly. (GitHub shows a **Cite this repository** button when it finds a `CITATION.cff`.)
7. **Link to a permanent archive** such as Zenodo, which can give you a DOI for a release. (Search "GitHub Zenodo integration" for the current steps.)

### 🔒 Important

- **Keep private data private.** Never commit anything with personal, patient, or participant information. Check your ethics approval and data-sharing agreements.
- **Large datasets** don't belong in a repository. Store them in an appropriate data repository and link to them.

### 💡 Pro tips

- A good **README** often becomes the "methods" section of a future paper.
- **Issues** make a great lab-meeting to-do list.
- **Pull requests** are a gentle, transparent way for collaborators to review analysis plans or write-ups.

---

## 🧑‍🏫 For teachers

**Good for:** course materials, assignments, shared lesson plans, student portfolios.

- **Share a course site** with GitHub Pages. Students always see the latest syllabus.
- **Use a template repository** for assignments, and have students **fork** or **use the template** to make their own copy.
- **Use issues** for questions, so answers are visible to everyone.
- **Use pull requests** for feedback on student work. Comments sit right next to the lines they're about.
- **GitHub Classroom** (<https://classroom.github.com>) can automate handing out and collecting assignments. It's free for teachers.
- **Apply to GitHub Education** (Chapter 18) for teacher benefits.

---

## 🏢 For small businesses, clubs, and community groups

- **Handbooks and policies** as Markdown pages, with every change tracked and dated.
- **Meeting notes** in a repository, so decisions are never lost.
- **Event pages** with GitHub Pages, as free, fast, and easy to update.
- **Volunteer task lists** with issues and project boards.
- **A public website** for a club, with several people able to edit it through pull requests.

Create an **organization** (Chapter 10) so the project isn't tied to one person's account.

---

## 🎶 For hobbyists and makers

- A **recipe collection** with photos.
- A **garden journal**, one file per season.
- A **travel itinerary** with links and maps.
- A **book club** reading list with notes.
- **Configuration files** for a game or a hobby app.
- A **family history** wiki, kept private.

Anything you want to keep, improve, and maybe share is a candidate.

---

## 🛠️ Try it

1. Pick the section above that matches you (or the closest one).
2. Create a repository for a **real thing you're working on**, using its suggested structure.
3. Add a README that explains it in three sentences.
4. Make three commits with good messages, and create two issues for next steps.
5. Decide: **public or private**? Write the reason in the README.

## ✅ Checkpoint

- [ ] I know which of my files work well on GitHub, and which don't.
- [ ] I have a repository for something real that I care about.
- [ ] I know what must stay private.
- [ ] I picked a workflow and tried part of it.

---

Previous: [Chapter 22](22-project-open-source.md) · Next: **[Chapter 24: The 30-Day Practice Plan](24-30-day-plan.md)**
