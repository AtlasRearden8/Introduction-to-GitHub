# Chapter 10: Collaborating & Open Source 🤝

🎯 **Goals:** Work with other people: invite collaborators, use forks, and make your first contribution to a project that isn't yours.

---

## 🤝 Two ways to collaborate

| Situation | Approach |
|-----------|----------|
| **You and trusted teammates** share a project | Add them as **collaborators**. Everyone makes branches in the *same* repo. |
| **A project you don't own** (open source, a classmate's repo) | **Fork** it, make changes in your copy, and propose them with a pull request. |

## 👥 Path 1: Collaborators

### 💌 Invite someone

1. On your repo, open **Settings → Collaborators** (called **Collaborators and teams** in some views), then click **Add people**.
2. Enter their GitHub username or email. They get an invitation to accept.

Collaborators on a personal repo can create branches and open pull requests there.

### 🔁 Team workflow in GitHub Desktop

1. Everyone **clones** the repo (Chapter 6).
2. Before starting, click **Fetch origin** and **Pull origin** so you have the latest `main`.
3. Each person works on their **own branch** for their own task (Chapter 7).
4. **Publish** the branch and open a pull request. Someone else reviews and merges it.
5. Everyone pulls the updated `main` regularly.

A rule that prevents most headaches: **one branch per task, small pull requests, pull often.**

### 🛡️ Protect `main`

In **Settings → Branches** (or **Rules → Rulesets**), you can require pull requests and approvals before anything is merged into `main`. This stops accidental direct changes. What's available depends on your repo type and plan, so check GitHub's docs for yours.

### 🏢 Organizations

An **organization** is a shared account for groups (a company, class, or club) with teams and permissions. Create one from the **+** menu, then **New organization**. The free tier works fine for learning.

## 🍴 Path 2: Forks and open source

### 🌍 What is open source?

Software (and other projects) whose files are public and that other people may use, study, and improve, under the terms of a **license**. Millions of projects welcome beginners. You don't have to write code. Documentation fixes, typo corrections, translations, and design feedback all count.

### 🍴 What is a fork?

A **fork** is *your own copy* of someone else's repository, living in your account. You have full control of your copy, and the original owner's project is untouched until they accept your pull request.

```
  Original repo (octocat/project)
        │  Fork (button on GitHub)
        ▼
  Your fork (you/project)
        │  Clone (GitHub Desktop)
        ▼
  Your computer ──► edit and commit ──► Push ──► your fork ──► Pull request ──► Original repo
```

## 🎓 Your first open-source style contribution (safe practice)

GitHub keeps a repository built for exactly this: **`octocat/Spoon-Knife`**.

1. Visit <https://github.com/octocat/Spoon-Knife> and click **Fork** (top right), then **Create fork**.
2. Clone *your* fork. On your fork's page, click the green **Code** button, then **Open with GitHub Desktop**. (Or use **File → Clone repository...** in GitHub Desktop and pick it from the list.)
3. GitHub Desktop asks how you plan to use the fork. Choose **To contribute to the parent project**, then click **Continue**.
4. Create a branch: **Current branch → New Branch**, named `my-first-contribution`.
5. Make a small change, such as editing `README.md`, and save it.
6. In GitHub Desktop, commit it with a summary like `Practice contribution`.
7. Click **Publish branch**, then **Create Pull Request**.
8. On the page that opens, notice that the **base repository** is the original (`octocat/Spoon-Knife`). Write a friendly description and click **Create pull request**.

For this practice repo, nobody expects your PR to be merged. It's a safe sandbox. You've just done the same steps used for contributing to real projects.

**Screenshot:** The GitHub Desktop prompt asking whether you're contributing to the parent project.
{ .shot }

## 🔄 Keeping your fork up to date

The original project moves on while your fork stays behind. To catch up:

1. On your fork's page on github.com, click **Sync fork**, then **Update branch**.
2. In GitHub Desktop, click **Fetch origin**, then **Pull origin**.

## 🔍 Finding a real project to contribute to

- Search GitHub for the label **`good first issue`**, or visit <https://github.com/topics/good-first-issue>.
- Look at projects you already use and love.
- Start tiny: fix a typo, clarify a confusing sentence, or improve an example.
- Check that the repo has recent activity and a welcoming tone.

### 📖 Before you contribute: read these files

| File | Why |
|------|-----|
| `README.md` | What the project is |
| `CONTRIBUTING.md` | The project's rules for contributing, which you should follow |
| `CODE_OF_CONDUCT.md` | How people are expected to behave |
| `LICENSE` | What others may do with the work |

### 🙏 Contribution etiquette

- **Comment on the issue first** ("I'd like to work on this. Is it still open?") to avoid duplicate work.
- Keep PRs small and focused.
- Be patient. Maintainers are often volunteers.
- Be gracious if a PR is declined. It's part of the process, and you learned something.

## ⚖️ Licenses (the short version)

A repo without a license is, legally, "all rights reserved," which means other people can't safely reuse it. If you want to share your work, add a license. Popular choices:

- **MIT:** very permissive. Do almost anything, and keep the notice.
- **Apache 2.0:** permissive, with patent language.
- **GPL:** anyone who distributes changes must also share them under the GPL.
- **Creative Commons (CC BY and others):** common for writing and art.

GitHub makes this easy when you create a repo (the **Add license** dropdown). You can also add one later with **Add file → Create new file** and naming it `LICENSE`. GitHub then offers templates. (This isn't legal advice, so choose deliberately for important work.)

## 🏡 Make *your* project welcoming

When you're ready, add these to your own repos:

- A clear **README** (what it is and how to use it).
- A **LICENSE**.
- A **CONTRIBUTING.md** explaining how others can help.
- Issue labels such as `good first issue`.

## 🌟 Following and community

- **Follow** people to see their activity on your dashboard.
- **Star** repos you like.
- **Watch** repos to get notifications (choose carefully, as it can get noisy).
- **Sponsor** maintainers if you can and want to.

## 🛠️ Try it

1. Invite a friend (or a second account of your own) as a collaborator on a practice repo. Have them clone it, make a branch, and open a PR for you to review.
2. Fork `octocat/Spoon-Knife`, make a change on a branch, and open a PR.
3. Search `label:"good first issue"` on GitHub and bookmark three that interest you. Read their `CONTRIBUTING.md`.
4. Add a LICENSE to `hello-github`.

## 🧯 Stuck?

- **I can't push to someone else's repo:** You need to fork it first, or be invited as a collaborator.
- **My fork is behind:** Use **Sync fork** on GitHub, then **Fetch origin** and **Pull origin** in GitHub Desktop.
- **My PR shows way too many changes:** You may have branched from an out-of-date `main`. Sync your fork, create a fresh branch, and redo your edit.

## ✅ Checkpoint

- [ ] I know the difference between collaborating directly and forking.
- [ ] I forked a repo and opened a PR from the fork.
- [ ] I know where to find beginner-friendly issues and which files to read first.

---

Previous: [Chapter 9](09-issues-and-projects.md) · Next: **[Chapter 11: Reviews, Feedback & Teamwork](11-reviews-and-teamwork.md)**
