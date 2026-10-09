# Chapter 1: What Are Git and GitHub? 💡

🎯 **Goals:** Understand the big ideas before touching any tools. This is the most important chapter, because once these ideas click, everything else is just details.

---

## The problem Git solves

Have you ever had files like this?

```
Essay.docx
Essay_v2.docx
Essay_v2_FINAL.docx
Essay_v2_FINAL_actually_final.docx
Essay_v2_FINAL_actually_final_USE_THIS_ONE.docx
```

That's a (very human) attempt at **version control**: keeping track of how your work changes over time.

Now imagine:
- You want to go back to how things looked last Tuesday.
- Five people are editing the same project at once.
- You want to try a risky idea without wrecking your good version.

Doing this with copies of files gets messy fast. **Git** solves all of it, cleanly.

## Git: your project's time machine ⏳

**Git** is a free program that runs on your computer. It watches a folder and lets you:

- **Save snapshots** of your project at moments you choose.
- **Look back** at every snapshot and see what changed, when, and why.
- **Travel back** to any earlier snapshot.
- **Branch off** to experiment, then merge good ideas back.

Think of it like a video game's save system. You can save at any point, and if you make a mistake, you load an earlier save.

Git was created in 2005 by Linus Torvalds (who also created Linux). It's now the most widely used version control system in the world.

## GitHub: Git's home on the internet 🌐

**GitHub** is a *website* (and company) that stores Git projects online and adds tools for working with other people.

| | **Git** | **GitHub** |
|---|---|---|
| What is it? | A program on your computer | A website / online service |
| Needs internet? | No | Yes |
| Main job | Track changes to files | Host projects, share, and collaborate |
| Analogy | Microsoft Word's "track changes" engine | Google Docs-style sharing, comments, and teamwork on top |

A common comparison: **Git is to GitHub as photography is to Instagram.** Git does the core job; GitHub is the place you share it and interact with others.

> Other websites do a similar job (GitLab, Bitbucket). The Git skills you learn here work with all of them.

## The vocabulary you need (just the essentials)

Don't memorize these. Just read them once. You'll meet each again with hands-on practice. A full list is in the [Glossary](13-glossary.md).

### Repository ("repo")
A **project folder that Git is tracking**, including its full history. When someone says "check out my repo," they mean "look at my project."

### Commit
A **saved snapshot** of your project, with a short message describing what changed. Commits are the save points of your time machine. Example message: *"Add contact page"*.

### Branch
A **separate line of work**. The main line is usually called `main`. You can create a branch, make changes without affecting `main`, and later merge them in if you like the result. It's like writing in a copy of the document you can throw away.

### Merge
**Combining** the changes from one branch into another.

### Remote
A copy of your repository **hosted somewhere else**, such as on GitHub. The standard nickname for your main remote is `origin`.

### Clone
**Downloading** a full copy of a GitHub repository onto your computer.

### Push / Pull
- **Push**: send your new commits from your computer **up** to GitHub.
- **Pull**: bring new commits from GitHub **down** to your computer.

### Pull Request ("PR")
A **proposal** to merge your branch into another. It opens a discussion page where people can review, comment, and approve. It's the signature feature of GitHub.

### Issue
A **note or task** attached to a repo: a bug report, a feature idea, a question, a to-do.

### Fork
Your **own personal copy** of someone else's repository on GitHub. This lets you experiment freely and then propose your changes back to them.

## How it all fits together

```
        YOUR COMPUTER                              GITHUB (online)
   ┌────────────────────┐                    ┌────────────────────┐
   │  Your files        │                    │  Your repository   │
   │  + Git history     │  ── push ───────►  │  (the remote)      │
   │  (local repo)      │  ◄─────── pull ──  │                    │
   └────────────────────┘                    └─────────┬──────────┘
                                                       │
                                        Issues • Pull requests • Collaborators
                                        Pages • Actions • Discussions
```

And the loop you'll repeat every day looks like this:

```
  edit files  ──►  stage changes  ──►  commit (save a snapshot)  ──►  push to GitHub
```

That's the core of it. Everything else is built on top.

## The three "places" your changes live

This one idea clears up most beginner confusion. On your computer, Git has three areas:

```
 ┌──────────────────┐   git add   ┌──────────────────┐  git commit  ┌──────────────────┐
 │ WORKING FOLDER   │ ──────────► │  STAGING AREA    │ ───────────► │  REPOSITORY      │
 │ (files you edit) │             │ (a "loading dock"│              │ (permanent       │
 │                  │             │  for your next   │              │  history of      │
 │                  │             │  snapshot)       │              │  commits)        │
 └──────────────────┘             └──────────────────┘              └──────────────────┘
```

Analogy: you're taking a group photo. The **working folder** is everyone milling around. The **staging area** is the people you've told to line up. The **commit** is the photo being taken.

Why have a staging area at all? It lets you choose *exactly* which changes go into each snapshot, which keeps your history tidy.

## Why bother? Real reasons people love it

- **Safety:** nothing you've committed is truly lost.
- **Clarity:** you can see who changed what, and why.
- **Freedom to experiment:** branches make risky ideas cheap.
- **Teamwork:** many people can work on one project without overwriting each other.
- **Portfolio:** your GitHub profile becomes a living showcase of your work.
- **Not just for code!** People use GitHub for books, recipes, research, legal documents, design files, course notes, and more. Anything that's mostly text works especially well.

## ✅ Checkpoint

Without peeking, try to answer in your own words:

1. What's the difference between Git and GitHub?
2. What is a commit?
3. What's the difference between *push* and *pull*?
4. Why might you create a branch?

If you can give a rough answer to each, you're ready. Rough is fine. You'll lock it in through practice.

---

⬅️ Previous: [Chapter 0](00-start-here.md) · ➡️ Next: **[Chapter 2: Create Your Account & Get Set Up](02-account-and-setup.md)**
