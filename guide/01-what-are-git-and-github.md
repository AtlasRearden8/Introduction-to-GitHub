# Chapter 1: What Are Git and GitHub? 💡

🎯 **Goals:** Understand the big ideas before you touch any tools. This is the most important chapter. Once these ideas click, everything else is just details.

---

## 🗂️ The problem Git solves

Have you ever had files like this?

```
Essay.docx
Essay_v2.docx
Essay_v2_FINAL.docx
Essay_v2_FINAL_actually_final.docx
Essay_v2_FINAL_actually_final_USE_THIS_ONE.docx
```

That's a very human attempt at **version control**: keeping track of how your work changes over time.

Now imagine:

- You want to see how things looked last Tuesday.
- Five people are editing the same project at once.
- You want to try a risky idea without wrecking your good version.

Doing all this with copies of files gets messy fast. **Git** solves it cleanly.

## ⏳ Git: your project's time machine

**Git** is a free tool that watches a folder on your computer. It lets you:

- **Save snapshots** of your project whenever you choose.
- **Look back** at every snapshot and see what changed, when, and why.
- **Go back** to any earlier snapshot.
- **Try things out** on the side, and keep only the ideas you like.

Think of a video game's save system. You can save at any point, and if you make a mistake, you load an earlier save.

You will never type a Git command in this guide. **GitHub Desktop** (Chapter 2) does the Git work for you when you click its buttons.

## 🌐 GitHub: Git's home on the internet

**GitHub** is a *website* that stores your projects online and adds tools for working with other people.

| | **Git** | **GitHub** |
|---|---|---|
| What is it? | The tool that tracks changes | A website that stores projects online |
| Needs internet? | No | Yes |
| Main job | Remember every version of your files | Share projects, discuss changes, and collaborate |
| Everyday comparison | The "track changes" feature in a word processor | Shared documents with comments and teamwork on top |

A helpful comparison: **Git is to GitHub as photography is to Instagram.** Git does the core job. GitHub is where you share it and interact with others.

**GitHub Desktop** is the free app that connects the two. It lives on your computer, uses Git to save your work, and sends it up to GitHub when you ask it to.

## 📚 The vocabulary you need

Don't memorize these. Just read them once. You'll meet each one again with hands-on practice, and the [Glossary](28-glossary.md) lists them all.

### 📁 Repository ("repo")
A **project folder** that Git is tracking, including its full history. When someone says "check out my repo," they mean "look at my project."

### 💾 Commit
A **saved snapshot** of your project, with a short message describing what changed. Commits are the save points of your time machine. Example message: *"Add contact page"*.

### 🌿 Branch
A **separate line of work**. The main line is called `main`. You can create a branch, make changes without touching `main`, and bring them in later if you like the result. It's like working on a copy of a document that you can throw away.

### 🔀 Merge
**Combining** the changes from one branch into another.

### ☁️ Remote
A copy of your repository **stored somewhere else**, such as on GitHub. GitHub Desktop calls your GitHub copy **origin**.

### 📥 Clone
**Downloading** a full copy of a GitHub repository onto your computer.

### 🔄 Push and Pull
- **Push** means sending your new commits **up** from your computer to GitHub.
- **Pull** means bringing new commits **down** from GitHub to your computer.

### 📬 Pull request ("PR")
A **proposal** to merge your branch into another. It opens a page where people can review, comment, and approve. It is GitHub's signature feature.

### 📝 Issue
A **note or task** attached to a project: a bug report, an idea, a question, a to-do.

### 🍴 Fork
**Your own personal copy** of someone else's repository on GitHub. It lets you experiment freely and then suggest your changes back to the original owner.

## 🧭 How it all fits together

```
        YOUR COMPUTER                              GITHUB (online)
   ┌────────────────────┐                    ┌────────────────────┐
   │  Your files        │                    │  Your repository   │
   │  + their history   │  ── Push ───────►  │  (the remote)      │
   │  (GitHub Desktop)  │  ◄─────── Pull ──  │                    │
   └────────────────────┘                    └─────────┬──────────┘
                                                       │
                                        Issues • Pull requests • Collaborators
                                        Pages • Actions • Discussions
```

The loop you'll repeat every time you work looks like this:

```
  Edit your files  ──►  Commit (save a snapshot)  ──►  Push to GitHub
```

That's the core of it. Everything else is built on top.

## 🌟 Why bother?

- **Safety:** nothing you've committed is truly lost.
- **Clarity:** you can see who changed what, and why.
- **Freedom to experiment:** branches make risky ideas cheap.
- **Teamwork:** many people can work on one project without overwriting each other.
- **Portfolio:** your GitHub profile becomes a living showcase of your work.
- **Not just for code.** People use GitHub for books, recipes, research, legal documents, course notes, and more. Anything that's mostly text works especially well.

## ✅ Checkpoint

Without peeking, try to answer in your own words:

1. What's the difference between Git and GitHub?
2. What is a commit?
3. What's the difference between *push* and *pull*?
4. Why might you create a branch?

If you can give a rough answer to each, you're ready. Rough is fine. You'll lock it in through practice.

---

Previous: [Chapter 0](00-start-here.md) · Next: **[Chapter 2: Create Your Account & Get Set Up](02-account-and-setup.md)**
