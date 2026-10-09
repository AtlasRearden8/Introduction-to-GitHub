# Chapter 7: Pull Requests 🔀

🎯 **Goals:** Open, review, and merge a pull request. This is the feature GitHub is famous for, and the heart of working together.

---

## What is a pull request?

A **pull request** (PR) says:

> "I made some changes on a branch. Please **pull** them into `main`. Here's what I did and why. Take a look!"

It creates a dedicated page where you can:
- See exactly what changed (the *diff*).
- Discuss with comments.
- Request reviews and get approvals.
- Run automatic checks.
- Merge when everyone's happy.

Even when you work **alone**, pull requests are valuable: they give you a checkpoint to review your own work before it lands in `main`.

## Your first pull request, step by step

### 1. Make a branch and a change

In your `hello-github` clone:

```bash
git switch main
git pull
git switch -c add-reading-list
echo "# My Reading List" > reading-list.md
echo "- A book I want to read" >> reading-list.md
git add reading-list.md
git commit -m "Add reading list"
git push -u origin add-reading-list
```

### 2. Open the pull request

Go to your repo on GitHub. You'll likely see a yellow banner: **"add-reading-list had recent pushes — Compare & pull request."** Click it.

(If not: **Pull requests tab → New pull request**, choose `base: main` and `compare: add-reading-list`.)

### 3. Fill in the details

- **Title:** short and clear, such as `Add reading list`.
- **Description:** explain what and why. For example:

  ```markdown
  ## What this does
  Adds a starter reading list file.

  ## Why
  I want a place to track books.

  ## Notes
  - [ ] Add more books later
  ```

- Notice **base** (where changes will go, `main`) and **compare** (your branch).

Click **Create pull request**. 🎉

### 4. Read the page

Your PR has tabs:

| Tab | What it shows |
|-----|---------------|
| **Conversation** | Description, comments, status of checks, merge button |
| **Commits** | The commits included |
| **Checks** | Automated test results (if the repo has any) |
| **Files changed** | The diff: green = added, red = removed |

### 5. Review your own work

Go to **Files changed**. Hover over a line and click the blue **+** to leave a comment on that exact line. Reading your own diff with fresh eyes catches typos and leftover mess.

Click **Review changes** to submit comments. When reviewing someone else's PR you choose one of:
- **Comment**: general feedback.
- **Approve**: looks good!
- **Request changes**: needs fixes before merging.

### 6. Merge it

Back on the **Conversation** tab, click the green **Merge pull request** → **Confirm merge**.

Then click **Delete branch** to tidy up.

### 7. Update your computer

```bash
git switch main
git pull
git branch -d add-reading-list
```

Your local `main` now has the reading list. The full cycle is complete! 🌟

## Three ways to merge (you'll see this dropdown)

| Option | What it does | When it shines |
|--------|--------------|----------------|
| **Create a merge commit** | Keeps every commit and adds a joining commit | Preserving full history |
| **Squash and merge** | Combines all the PR's commits into **one** | Keeping `main` tidy (very popular) |
| **Rebase and merge** | Replays commits onto `main` in a straight line | Linear history fans |

As a beginner, any is fine. **Squash and merge** is a great default.

## Writing a great pull request

- **One purpose per PR.** Small PRs are reviewed faster and break less.
- **Clear title.** Describe the change, not the process.
- **Explain the "why."** Reviewers can see the *what* in the diff.
- **Add screenshots** if you changed something visual (drag images into the description).
- **Link related issues** (see below).

## Linking pull requests to issues

In the PR description, write:

```markdown
Closes #12
```

When the PR merges, **issue #12 closes automatically**. Other keywords that work: `Fixes #12`, `Resolves #12`.

## Draft pull requests

Not ready yet? Choose **Create draft pull request**. It signals "work in progress, don't merge." Click **Ready for review** when you're done.

## Receiving feedback gracefully 💛

If someone comments on your PR:

- Feedback is about the **work**, not about you.
- Reply, ask questions, or just say thanks.
- To make requested changes, commit on the **same branch** and push. The PR updates automatically.
- When a comment is addressed, click **Resolve conversation**.

## Giving feedback kindly

- Be specific and constructive: *"Could we rename this for clarity?"* beats *"This is bad."*
- Praise good work too. A "nice touch!" goes a long way.
- Use **suggestions**: in a review comment, click the ± icon to propose exact replacement text the author can accept with one click.

## Checks and branch protection (a peek ahead)

Teams often configure rules like "at least one approval before merging" or "tests must pass." You'll see these as status messages on the PR. They're guardrails, not roadblocks.

## 🛠️ Try it

1. Complete the seven steps above, start to finish.
2. Open a second PR where you deliberately leave a **line comment** on your own diff, then fix it with another commit and watch the PR update.
3. Open a **draft** PR and mark it ready.
4. Try **Squash and merge** on a PR with two commits and look at how `main`'s history differs.
5. **Ask a friend** to review a PR, or practice reviewing with a second account.

## 🧯 Stuck?

- **No "Compare & pull request" banner:** Use *Pull requests → New pull request*. Make sure the branch is pushed (`git push -u origin branch-name`).
- **"There isn't anything to compare":** The branch has no new commits relative to `main`, or you picked the same branch for both sides.
- **Merge button is grey or says conflicts:** Merge `main` into your branch locally (Chapter 6), resolve conflicts, push again. Or click **Resolve conflicts** to fix it in the browser.
- **Merged the wrong thing:** Chapter 10 shows how to revert a merge safely.

## ✅ Checkpoint

- [ ] I opened, read, and merged a pull request.
- [ ] I know where to find the diff and leave line comments.
- [ ] I can link a PR to an issue with `Closes #number`.
- [ ] I understand why PRs are useful even when working alone.

---

⬅️ Previous: [Chapter 6](06-branches-and-merging.md) · ➡️ Next: **[Chapter 8: Issues & Project Boards](08-issues-and-projects.md)**
