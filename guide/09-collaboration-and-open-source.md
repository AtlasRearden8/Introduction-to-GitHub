# Chapter 9: Collaborating & Open Source 🤝

🎯 **Goals:** Work with other people: invite collaborators, use forks, and make your first contribution to a project that isn't yours.

---

## Two ways to collaborate

| Situation | Approach |
|-----------|----------|
| **You and trusted teammates** share a project | Add them as **collaborators**; everyone makes branches in the *same* repo. |
| **A project you don't own** (open source, a classmate's repo) | **Fork** it, make changes in your copy, and propose them with a pull request. |

## Path 1: Collaborators

### Invite someone
1. Repo → **Settings → Collaborators** (called *Collaborators and teams* in some views) → **Add people**.
2. Enter their GitHub username or email. They get an invitation to accept.

Collaborators on a personal repo can push branches and open pull requests there.

### Team workflow

1. Everyone `clone`s the repo.
2. Before starting: `git switch main && git pull`.
3. Each person works on their **own branch** for their own task.
4. Open a PR; someone else reviews and merges.
5. Everyone pulls the updated `main` regularly.

Rule that prevents most headaches: **one branch per task, small PRs, pull often.**

### Protect `main`
In **Settings → Branches** (or **Rules → Rulesets**), you can require pull requests and approvals before anything merges into `main`. This stops accidental direct pushes. Available features vary by repo type and plan. Check the docs for yours.

### Organizations
An **organization** is a shared account for groups (a company, class, club) with teams and permissions. Create one from the ➕ menu → **New organization**. The free tier works fine for learning.

## Path 2: Forks and open source

### What is open source?
Software (and other projects) whose files are public and that others may use, study, and improve, according to the terms of a **license**. Millions of projects welcome beginners. You don't have to write code; documentation fixes, typo corrections, translations, and design feedback all count.

### What is a fork?
A **fork** is *your own copy* of someone else's repository, living in your account. You have full control of your copy, and the original owner's project is untouched until they accept your pull request.

```
  Original repo (octocat/project)
        │  Fork (button on GitHub)
        ▼
  Your fork (you/project)
        │  git clone
        ▼
  Your computer ──► edit & commit ──► git push ──► your fork ──► Pull request ──► Original repo
```

## Your first open-source style contribution (safe practice)

GitHub maintains a repo built for exactly this: **`octocat/Spoon-Knife`**.

1. Visit <https://github.com/octocat/Spoon-Knife> and click **Fork** (top right) → **Create fork**.
2. Clone *your* fork:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Spoon-Knife.git
   cd Spoon-Knife
   ```

3. Create a branch and make a small change (for instance, edit the `README.md`):

   ```bash
   git switch -c my-first-contribution
   # edit a file, then:
   git add .
   git commit -m "Practice contribution"
   git push -u origin my-first-contribution
   ```

4. On your fork's GitHub page, click **Compare & pull request**. Notice the **base repository** is the original (`octocat/Spoon-Knife`). Write a friendly description and open the PR.

For this practice repo, nobody expects your PR to be merged. It's a safe sandbox. You've just done the same steps used for contributing to real projects.

## Keeping your fork in sync

The original project moves on while your fork stays behind. On your fork's page, click **Sync fork → Update branch**. Then on your computer:

```bash
git switch main
git pull
```

## Finding a real project to contribute to 🔍

- Search GitHub for the label **`good first issue`** (or visit <https://github.com/topics/good-first-issue>).
- Look at projects you already use and love.
- Start tiny: fix a typo, clarify a confusing sentence, improve an example.
- Check the repo has recent activity and a welcoming tone.

### Before you contribute: read these files

| File | Why |
|------|-----|
| `README.md` | What the project is |
| `CONTRIBUTING.md` | The project's rules for contributing, which you should follow |
| `CODE_OF_CONDUCT.md` | How people are expected to behave |
| `LICENSE` | What others may do with the work |

### Contribution etiquette
- **Comment on the issue first** ("I'd like to work on this. Is it still open?") to avoid duplicate work.
- Keep PRs small and focused.
- Be patient; maintainers are often volunteers.
- Be gracious if a PR is declined. It's part of the process, and you learned something.

## Licenses (the short version)

A repo without a license is, legally, "all rights reserved," meaning others can't safely reuse it. If you want to share your work, add a license. Popular choices:

- **MIT**: very permissive; do almost anything, keep the notice.
- **Apache 2.0**: permissive, with patent language.
- **GPL**: others who distribute changes must also share them under the GPL.
- **Creative Commons (CC BY, etc.)**: common for writing and art.

GitHub makes this easy when creating a repo (the **Add license** dropdown), or add it later with **Add file → Create new file** and name it `LICENSE`. GitHub will offer templates. (Not legal advice; pick deliberately for important work.)

## Make *your* project welcoming

Add these to your own repos when you're ready:
- A clear **README** (what it is, how to use it).
- A **LICENSE**.
- A **CONTRIBUTING.md** explaining how others can help.
- Issue labels like `good first issue`.

## Following and community

- **Follow** people to see their activity on your dashboard.
- **Star** repos you like.
- **Watch** repos to get notifications (choose carefully, as it can get noisy).
- **Sponsor** maintainers if you can and want to.

## 🛠️ Try it

1. Invite a friend (or a second account of your own) as a collaborator to a practice repo; have them clone it, make a branch, and open a PR for you to review.
2. Fork `octocat/Spoon-Knife`, make a change on a branch, and open a PR.
3. Search `label:"good first issue"` on GitHub and bookmark three that interest you. Read their `CONTRIBUTING.md`.
4. Add a LICENSE to `hello-github`.

## 🧯 Stuck?

- **Can't push to someone else's repo:** You need to fork it first (or be a collaborator).
- **Fork is behind:** Use **Sync fork** on GitHub.
- **PR shows way too many changes:** You may have branched from an outdated `main`. Sync your fork, create a fresh branch, and re-apply your edit.

## ✅ Checkpoint

- [ ] I know the difference between collaborating directly and forking.
- [ ] I forked a repo and opened a PR from the fork.
- [ ] I know where to find beginner-friendly issues and what files to read first.

---

⬅️ Previous: [Chapter 8](08-issues-and-projects.md) · ➡️ Next: **[Chapter 10: Undoing Mistakes](10-undoing-mistakes.md)**
