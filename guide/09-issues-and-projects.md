# Chapter 9: Issues & Project Boards 📋

🎯 **Goals:** Use issues to track tasks, bugs, and ideas, then organize them with labels, milestones, and a project board.

---

## 📋 What is an issue?

An **issue** is a trackable note attached to a repository. It can be:

- A **bug** ("The button doesn't work on phones")
- A **feature idea** ("Add a dark mode")
- A **question** ("How do I install this?")
- A simple **to-do** ("Write chapter 3")

Every issue gets a number (`#1`, `#2`, …), a discussion thread, and an open/closed status. Think of it as a shared to-do list with a conversation attached to each item.

Issues work in your private practice repos too, and they're a great personal task manager.

## 🆕 Create your first issue

1. Open your repo → **Issues** tab → **New issue**.
2. **Title:** specific and short, such as `Add three more books to reading list`.
3. **Description:** write in Markdown. Be clear about what's wanted:

    ```markdown
    ## Goal
    Grow the reading list so it has at least 5 books.

    ## Tasks
    - [ ] Add a fiction book
    - [ ] Add a non-fiction book
    - [ ] Add a book a friend recommended
    ```

4. Click **Submit new issue**.

The task list renders as checkboxes. Tick them off as you go, and GitHub shows progress (like "1 of 3") in issue lists.

## 🐛 Writing a good bug report

When *reporting a problem* (to yourself or to others), include:

1. **What you did** (steps to reproduce).
2. **What you expected.**
3. **What actually happened.**
4. **Details:** device, browser, screenshots, error messages.

Example:

```markdown
**Steps:** Open the site on iPhone → tap "Menu"
**Expected:** The menu opens
**Actual:** Nothing happens
**Device:** iPhone 14, Safari
```

Great bug reports get fixed faster.

## ⚡ Superpowers inside issues

### 📣 Mentions: `@username`
Type `@` followed by a name to notify a person.

### 🔗 References: `#number`
Typing `#7` in any comment creates a clickable link to issue or PR #7, and leaves a trail in #7 showing where it was mentioned.

### 👤 Assignees
Click the gear next to **Assignees** to say who's responsible. You can assign yourself.

### 🏷️ Labels
Color-coded tags such as `bug`, `enhancement`, `documentation`, `good first issue`, `help wanted`. GitHub gives you defaults, and you can create your own under the **Labels** page.

### 🎯 Milestones
A group of issues with a shared goal and optional due date, like "Version 1.0" or "Launch week." The milestone page shows a progress bar.

### ✅ Closing issues
Click **Close issue** manually, or let a pull request do it by writing `Closes #7` in its description (Chapter 8). Closed isn't deleted; you can reopen it any time.

## 🔎 Searching and filtering

Above the issue list is a search box with handy filters:

| Type this | To find |
|-----------|---------|
| `is:open` | Open issues |
| `is:closed` | Finished ones |
| `label:bug` | Only bugs |
| `assignee:@me` | Things assigned to you |
| `milestone:"Version 1.0"` | Issues in that milestone |

Combine them: `is:open label:bug assignee:@me`.

## 🧾 Issue templates

For repos where others report issues, **templates** pre-fill a helpful structure (like the bug-report format above). Find them under **Settings → General → Features → Issues → Set up templates**. Optional for now, but a nice touch for your own projects.

## 🗂️ Project boards

**GitHub Projects** give you a visual way to organize issues, like sticky notes on a wall.

1. From your profile or repo, open the **Projects** tab → **New project**.
2. Pick the **Board** layout (columns like *Todo*, *In Progress*, *Done*), or a **Table** layout for a spreadsheet feel.
3. Click **+ Add item** and type `#` to pull in your existing issues.
4. **Drag cards** between columns as work progresses.

Tips:
- Add custom fields like *Priority* or *Due date*.
- Turn on built-in **workflows** so closing an issue automatically moves it to *Done*.
- Switch views any time (Board, Table, Roadmap).

You can plan an entire personal project, a class assignment, or a team sprint this way.

## 💬 Discussions (a gentle mention)

Some repos enable **Discussions**, a forum-like space for open-ended conversation, Q&A, and announcements that don't fit as tasks. Turn it on in **Settings → General → Features → Discussions** if your project grows a community.

## 🛠️ Try it

1. Create 3 issues in `hello-github` (for instance: "Write bio", "Add profile photo", "Add reading list entries").
2. Add a label to each and assign yourself.
3. Create a milestone named "Getting started" and add the issues to it.
4. Create a **Project** with a Board layout, and add all three issues.
5. Make a small change on a branch, open a PR containing `Closes #1`, merge it, and watch issue #1 close automatically and its card move.

## 🧯 Stuck?

- **No Issues tab:** Issues may be disabled. Enable them in **Settings → General → Features**.
- **Can't find a project board:** Projects can live on your profile (user level) or inside an organization. Check your profile's *Projects* tab as well as the repo.
- **Label I want doesn't exist:** Create it from **Issues → Labels → New label**.

## ✅ Checkpoint

- [ ] I can create, label, assign, and close an issue.
- [ ] I know how to reference issues with `#number` and close them from a PR.
- [ ] I created a project board with at least one card.

---

Previous: [Chapter 8](08-pull-requests.md) · Next: **[Chapter 10: Collaborating & Open Source](10-collaboration-and-open-source.md)**
