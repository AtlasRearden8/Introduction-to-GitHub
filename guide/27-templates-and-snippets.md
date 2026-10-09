# Chapter 27: Templates & Snippets 🧩

Copy, paste, and adapt. Every template in this chapter works in your browser: on a repository page, click **Add file → Create new file**, type the file name shown, paste the text, and commit. Where you see words in CAPITAL LETTERS, replace them with your own.

> 💡 Typing a path like `.github/ISSUE_TEMPLATE/bug.md` in the name box creates the folders for you.

---

## 📘 README templates

### 🌱 A simple, friendly README

````markdown
# PROJECT NAME

One sentence that says what this is and who it's for.

## ✨ What's inside
- Thing one
- Thing two
- Thing three

## 🚀 How to use it
1. Step one
2. Step two

## 🤝 How to help
Found a typo or have an idea? [Open an issue](../../issues) or send a pull request.

## 📄 License
Released under the MIT License.
````

### 🖼️ A portfolio project README

````markdown
# PROJECT NAME

> A one-line pitch. What does it do, and why does it matter?

![Screenshot or cover image](images/cover.png)

## 🎯 The goal
Why I made this, in two or three sentences.

## 🧰 What I used
- Tool or skill one
- Tool or skill two

## 🛠️ What I did
- My part in the project
- Something I'm proud of

## 💡 What I learned
- Lesson one
- Lesson two

## 🔗 Links
- [Live site](https://example.com)
- [My profile](https://github.com/YOUR-USERNAME)
````

### 📚 A writing project README

````markdown
# BOOK OR PROJECT TITLE

*A one-line description.* By YOUR NAME.

**Status:** First draft · **Word count:** 12,000 / 60,000

## 📖 Read it
[Open the table of contents](index.md)

## 🗂️ How this repo is organized
- `chapters/` the manuscript
- `notes/` research and outlines
- `images/` pictures and diagrams

## 💬 Feedback
Spotted a typo or have a thought? Open an issue, or comment on a pull request.

## ©️ Copyright
© YEAR YOUR NAME. All rights reserved.
````

### 🍲 A collection README (recipes, links, notes)

````markdown
# COLLECTION NAME

A collection of THINGS, shared with love.

## 📑 Contents
- [Item one](items/one.md)
- [Item two](items/two.md)

## ➕ How to add yours
1. Copy `items/_template.md`.
2. Fill it in.
3. Open a pull request.
````

### 🌟 A profile README

````markdown
# Hi, I'm YOUR NAME 👋

I'm a **WHAT YOU DO** who loves **WHAT YOU LOVE**.

## 🌱 What I'm up to
- Currently learning: SOMETHING
- Working on: A PROJECT

## 🛠️ Things I've made
- [Project one](https://github.com/YOUR-USERNAME/project-one) — a short line
- [Project two](https://github.com/YOUR-USERNAME/project-two) — a short line

## 📫 Say hello
Find me on [WHEREVER](https://example.com).
````

## 🤝 Community files

### CONTRIBUTING.md

````markdown
# Contributing to PROJECT NAME

Thank you for wanting to help! Every contribution matters, from fixing a typo
to suggesting a big idea.

## Ways to help
- Report a problem or suggest an idea by opening an **issue**
- Improve the writing or documentation
- Add something new, using a **pull request**

## Making a change
1. **Fork** this repository (or ask to be added as a collaborator).
2. Create a **branch** with a short name, like `fix-typo-in-intro`.
3. Make your change and **commit** it with a clear message.
4. **Publish** the branch and open a **pull request**.
5. A maintainer will review it. Please be patient, and don't worry about
   mistakes. We'll help.

## Style
- Keep changes small and focused.
- Write in a friendly, plain style.
- Use Markdown headings, lists, and links.

## Be kind
Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).
````

### CODE_OF_CONDUCT.md (a short, friendly version)

For serious projects, use GitHub's template: **Add file → Create new file**, name it `CODE_OF_CONDUCT.md`, and click **Choose a template**. For a small project, this works:

````markdown
# Code of Conduct

We want this to be a welcoming place for everyone.

## What we expect
- Be kind and respectful.
- Assume good intentions, and ask questions before reacting.
- Give feedback about the work, never about the person.
- Welcome newcomers, and be patient with beginners.

## What isn't okay
- Harassment, insults, or discrimination of any kind
- Sharing other people's private information
- Unwelcome attention or comments

## If something happens
Contact the maintainers at CONTACT-EMAIL. We'll take reports seriously and
keep them private.
````

### SECURITY.md

````markdown
# Security

If you discover a problem that could affect people's safety or privacy, please
email CONTACT-EMAIL instead of posting it publicly. We'll reply within a week.
````

## 📝 Issue and pull request templates

### 🐛 Bug report (`.github/ISSUE_TEMPLATE/bug_report.md`)

````markdown
---
name: Bug report
about: Something isn't working as expected
title: "[Bug] "
labels: bug
---

## What happened?
A clear description of the problem.

## What did you expect?
What should have happened instead?

## Steps to reproduce
1. Go to ...
2. Click on ...
3. See the problem

## Details
- Device and browser:
- Screenshot (drag it in here):
````

### ✨ Idea / feature request (`.github/ISSUE_TEMPLATE/idea.md`)

````markdown
---
name: Idea
about: Suggest something new
title: "[Idea] "
labels: enhancement
---

## What's your idea?

## Why would it help?

## Anything else?
````

### ❓ Question (`.github/ISSUE_TEMPLATE/question.md`)

````markdown
---
name: Question
about: Ask for help or information
title: "[Question] "
labels: question
---

## What are you trying to do?

## What have you tried?
````

### 🔀 Pull request template (`.github/pull_request_template.md`)

````markdown
## What does this change?
<!-- One or two sentences. -->

## Why?
<!-- What problem does it solve? -->

## Checklist
- [ ] I read my own changes first
- [ ] I checked links and spelling
- [ ] Nothing private is included

Closes #
````

## 🙈 A `.gitignore` for everyday projects

Create a file named `.gitignore`. (In GitHub Desktop you can also right-click a file in **Changes** and choose **Ignore file**.)

```
# Mac and Windows clutter
.DS_Store
Thumbs.db
desktop.ini

# Temporary and backup files
*.tmp
*.bak
*~
~$*

# Private notes and settings
.env
secrets.txt
private/

# Logs
*.log
```

## 💬 Commit message cookbook

A good commit message finishes the sentence: *"This commit will..."*

| Situation | Example |
|-----------|---------|
| Adding something | `Add contact page` |
| Fixing something | `Fix broken link on About page` |
| Updating | `Update resume with new job` |
| Removing | `Remove outdated screenshots` |
| Writing | `Draft chapter 3 opening` |
| Editing | `Tighten dialogue in chapter 2` |
| Reorganizing | `Move notes into a notes folder` |
| Documenting | `Explain setup steps in README` |
| Reverting | `Revert "Add unfinished page"` |
| Housekeeping | `Tidy file names` |

**Tips:** start with a verb, keep the first line short (under about 50 characters), and say *what* changed. Use the **Description** box for the *why*.

## 📬 Pull request description templates

### A bug fix

````markdown
## Problem
What was wrong, and where.

## Fix
What I changed.

## How I checked
How I know it works.

Fixes #NUMBER
````

### A content change

````markdown
## What I changed
- Added ...
- Rewrote ...

## Why
The old text was confusing because ...

## Preview
(Screenshot, if it looks different.)
````

## 🏷️ Release notes template

````markdown
## 🎉 What's new
- A new thing
- Another new thing

## 🛠️ Improvements
- Something that got better

## 🐛 Fixes
- Something that was broken and now isn't

## 🙏 Thanks
Thanks to @USERNAME for their help!
````

## 📆 Status update template (for team issues)

````markdown
## ✅ Done this week
- 

## 🔨 In progress
- 

## 🚧 Blocked or need help
- 

## 🎯 Next week
- 
````

## 📚 Citation file (`CITATION.cff`)

If others might cite your project, this file adds a **Cite this repository** button:

````yaml
cff-version: 1.2.0
message: "If you use this, please cite it as below."
title: "PROJECT TITLE"
authors:
  - family-names: "LAST NAME"
    given-names: "FIRST NAME"
date-released: 2026-01-01
version: "1.0.0"
url: "https://github.com/YOUR-USERNAME/PROJECT"
````

## 🌐 Starter `_config.yml` for GitHub Pages

```yaml
theme: jekyll-theme-minimal
title: SITE TITLE
description: A short description of the site
show_downloads: false
```

## 🎨 Markdown snippets to keep handy

````markdown
> [!NOTE]
> Helpful information.

> [!TIP]
> A shortcut or hint.

> [!WARNING]
> Be careful here.

<details>
<summary>Click to expand</summary>

Hidden content goes here.

</details>

| Column A | Column B |
|----------|----------|
| One      | Two      |

- [ ] A task to do
- [x] A task that's done
````

## 🛠️ Try it

1. Add a **README**, **LICENSE**, and **CONTRIBUTING.md** to one of your repositories.
2. Create an **issue template** and open a new issue to see it.
3. Add a **pull request template** and open a pull request to see it.
4. Keep this page bookmarked. It's the one you'll come back to.

---

Previous: [Chapter 26](26-cheat-sheet.md) · Next: **[Chapter 28: Glossary](28-glossary.md)**
