# Chapter 8: Pull Requests 🔀

🎯 **Goals:** Open, review, and merge a pull request. This is the feature GitHub is famous for, and the heart of working together.

---

## 🔀 What is a pull request?

A **pull request** (PR) says:

> "I made some changes on a branch. Please **pull** them into `main`. Here's what I did and why. Take a look!"

It creates a dedicated page where you can:

- See exactly what changed (the *diff*).
- Discuss with comments.
- Ask for reviews and get approvals.
- See automatic checks.
- Merge when everyone's happy.

Even when you work **alone**, pull requests are valuable. They give you a checkpoint to review your own work before it lands in `main`.

## 🚀 Your first pull request, step by step

### 🌿 1. Make a branch and a change (in GitHub Desktop)

In your `hello-github` project:

1. Click **Fetch origin**, and **Pull origin** if it appears, so `main` is up to date.
2. Click **Current branch → New Branch**, name it `add-reading-list`, and click **Create branch**.
3. Create a file called `reading-list.md` in the project folder with a title and a book, for example:

    ```markdown
    # My Reading List
    - A book I want to read
    ```

4. In GitHub Desktop, tick the file, write the summary `Add reading list`, and click **Commit to add-reading-list**.
5. Click **Publish branch** (top right).

### 📬 2. Open the pull request

GitHub Desktop makes this easy. After you publish, it shows a button: **Create Pull Request**. Click it. (You can also choose **Branch → Create pull request** from the menu bar.)

Your web browser opens to GitHub with the page for a new pull request already set up.

If you'd rather start from the website, go to your repo on github.com. You'll likely see a yellow banner: **add-reading-list had recent pushes**, with a **Compare & pull request** button. Click it. If you don't see the banner, go to **Pull requests → New pull request**, set **base** to `main` and **compare** to `add-reading-list`.

**Screenshot:** GitHub Desktop with the **Create Pull Request** button showing.
{ .shot }

### 📝 3. Fill in the details

- **Title:** short and clear, such as `Add reading list`.
- **Description:** explain what you did and why. For example:

  ```markdown
  ## What this does
  Adds a starter reading list file.

  ## Why
  I want a place to track books.
  ```

- Notice **base** (where changes will go, `main`) and **compare** (your branch).

Click **Create pull request**.

**Screenshot:** The **Open a pull request** page with the title and description filled in.
{ .shot }

### 👓 4. Read the page

Your pull request has tabs:

| Tab | What it shows |
|-----|---------------|
| **Conversation** | The description, comments, status of checks, and the merge button |
| **Commits** | The commits included |
| **Checks** | Automatic test results (if the repo has any) |
| **Files changed** | The diff: green means added, red means removed |

### 🔎 5. Review your own work

Go to **Files changed**. Hover over a line and click the blue **+** to leave a comment on that exact line. Reading your own changes with fresh eyes catches typos and leftover mess.

Click **Review changes** to submit your comments. When you review someone else's pull request, you choose one of:

- **Comment:** general feedback.
- **Approve:** looks good.
- **Request changes:** needs fixes before merging.

### ✅ 6. Merge it

Back on the **Conversation** tab, click the green **Merge pull request**, then **Confirm merge**.

Then click **Delete branch** to tidy up.

### 🔄 7. Update your computer (in GitHub Desktop)

1. Click **Current branch** and switch to **main**.
2. Click **Fetch origin**, then **Pull origin**.
3. Your computer's `main` now has the reading list.

You can also delete your local copy of the old branch: choose **Branch → Delete...**

The full cycle is complete.

## 🔀 Three ways to merge

On the merge button you'll see a dropdown arrow with these options:

| Option | What it does | When it shines |
|--------|--------------|----------------|
| **Create a merge commit** | Keeps every commit and adds a joining commit | Keeping the full history |
| **Squash and merge** | Combines all of the pull request's commits into **one** | Keeping `main` tidy (very popular) |
| **Rebase and merge** | Replays the commits onto `main` in a straight line | People who like a perfectly straight history |

As a beginner, any is fine. **Squash and merge** is a great default.

## ⭐ Writing a great pull request

- **One purpose per PR.** Small PRs are reviewed faster and cause fewer problems.
- **A clear title.** Describe the change, not the process.
- **Explain the "why."** Reviewers can see the *what* in the diff.
- **Add screenshots** if you changed something visual (drag images into the description box).
- **Link related issues** (see below).

## 🔗 Linking pull requests to issues

In the pull request description, write:

```markdown
Closes #12
```

When the PR is merged, **issue #12 closes automatically**. Other words that work: `Fixes #12`, `Resolves #12`.

## 📝 Draft pull requests

Not ready yet? On the green button, use the dropdown arrow and choose **Create draft pull request**. It signals "work in progress, please don't merge." Click **Ready for review** when you're done.

## 💛 Receiving feedback gracefully

If someone comments on your pull request:

- Feedback is about the **work**, not about you.
- Reply, ask questions, or just say thanks.
- To make requested changes, **commit on the same branch** in GitHub Desktop and click **Push origin**. The pull request updates automatically.
- When a comment has been dealt with, click **Resolve conversation**.

## 🙌 Giving feedback kindly

- Be specific and constructive. *"Could we rename this for clarity?"* beats *"This is bad."*
- Praise good work too. A "nice touch!" goes a long way.
- Use **suggestions**: in a review comment, click the **±** icon to propose exact replacement text the author can accept with one click.

## 🛡️ Checks and protected branches

Teams often set rules like "at least one approval before merging" or "tests must pass." You'll see these as status messages on the pull request. They're guardrails, not roadblocks.

## 🛠️ Try it

1. Complete the seven steps above, start to finish.
2. Open a second PR where you deliberately leave a **line comment** on your own changes, then fix it with another commit and watch the PR update.
3. Open a **draft** PR and mark it **Ready for review**.
4. Try **Squash and merge** on a PR with two commits, and compare how `main`'s History looks.
5. **Ask a friend** to review a PR, or practice reviewing with a second account.

## 🧯 Stuck?

- **No "Compare & pull request" banner:** Use **Pull requests → New pull request**. Make sure you clicked **Publish branch** or **Push origin** in GitHub Desktop first.
- **"There isn't anything to compare":** The branch has no new commits compared with `main`, or you picked the same branch for both sides.
- **The merge button is grey or says there are conflicts:** In GitHub Desktop, switch to your branch and choose **Branch → Update from main**, resolve any conflicts (Chapter 6), and **Push origin**. Or click **Resolve conflicts** on the website to fix it right there.
- **I merged the wrong thing:** Chapter 12 shows how to undo a merged pull request safely.

## ✅ Checkpoint

- [ ] I opened, read, and merged a pull request.
- [ ] I know where to find the changes and leave a comment on a line.
- [ ] I can link a PR to an issue with `Closes #number`.
- [ ] I understand why PRs are useful even when working alone.

---

Previous: [Chapter 7](07-branches-and-merging.md) · Next: **[Chapter 9: Issues & Project Boards](09-issues-and-projects.md)**
