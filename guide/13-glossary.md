# Chapter 13: Glossary 📖

Every term in plain English, alphabetized. Don't try to memorize; look things up whenever you need.

---

**Actions (GitHub Actions)**: GitHub's built-in automation. Runs tasks, like tests or website builds, when events happen in a repo.

**Add / Stage**: Telling Git "include this change in my next commit." (`git add`)

**Amend**: Modify the most recent commit (message or contents). (`git commit --amend`)

**Base branch**: In a pull request, the branch the changes will be merged *into*, usually `main`.

**Blame**: A view showing who last changed each line of a file, and in which commit.

**Branch**: A separate line of development inside a repo, letting you work without affecting other lines.

**Checkout**: The older command for switching branches or restoring files. Newer commands `switch` and `restore` do these jobs more clearly.

**Cherry-pick**: Copy a single commit from one branch onto another.

**CLI**: Command-line interface, a tool you use by typing commands. (`git` and `gh` are CLIs.)

**Clone**: Download a complete copy of a repository, with history, to your computer.

**Codespace**: A cloud-hosted development environment for a repo, opened in your browser.

**Collaborator**: Someone you've given access to work directly in your repository.

**Commit**: A saved snapshot of your project with a message. The basic unit of Git history.

**Commit hash / SHA**: The long unique ID of a commit, like `a1b2c3d4e5…`. The first 7 characters usually suffice.

**Compare**: In a pull request, the branch that contains your new changes.

**Conflict (merge conflict)**: When two sets of changes touch the same lines and Git needs a human to choose the result.

**Contributor**: Anyone who adds to a project.

**Dependabot**: A GitHub feature that alerts you about vulnerable dependencies and can propose updates.

**Detached HEAD**: A state where you're viewing an old commit rather than being on a branch. Harmless; switch to a branch to leave.

**Diff**: A comparison showing what changed between two versions. Added lines are green (`+`), removed lines are red (`-`).

**Directory**: Another word for folder.

**Draft pull request**: A pull request marked as unfinished and not ready for review or merge.

**Fast-forward**: A merge where Git just moves a branch pointer forward because no divergent work exists.

**Fetch**: Download new commits from the remote without changing your working files.

**Fork**: Your own copy of someone else's repository, stored in your GitHub account.

**Gist**: A tiny repository for sharing a snippet or note.

**Git**: The free version control program that tracks changes on your computer.

**GitHub**: The website/service that hosts Git repositories and adds collaboration tools.

**GitHub Pages**: Free website hosting straight from a repository.

**`.gitignore`**: A file listing patterns of files Git should not track.

**Hash**: See *Commit hash*.

**HEAD**: Git's pointer to "where you are now": the current commit or branch.

**Hosting**: Storing something on a server so it's accessible online.

**HTTPS / SSH**: The two ways to connect to GitHub from your computer. HTTPS uses web-style addresses and a token or login helper; SSH uses key pairs.

**Issue**: A trackable item (bug, task, idea, question) attached to a repo.

**Label**: A colored tag on issues and pull requests, like `bug` or `documentation`.

**License**: A file stating what others are allowed to do with your project.

**Local**: On your own computer (versus *remote*).

**Main**: The conventional name of a repo's primary branch. (Older repos may use `master`.)

**Maintainer**: A person responsible for managing a project, who reviews and merges contributions.

**Markdown**: A simple way of formatting text using symbols like `#` and `**`, widely used on GitHub.

**Merge**: Combine changes from one branch into another.

**Merge commit**: A commit that joins two lines of history.

**Milestone**: A named goal that groups issues and pull requests, often with a due date.

**Open source**: Projects whose source is public and which others may use or improve according to a license.

**Organization**: A shared GitHub account for groups, with teams and permissions.

**Origin**: The default nickname for the main remote repository.

**Personal access token (PAT)**: A special password-like string used instead of your account password for certain Git operations. Many beginners can avoid it by using `gh auth login`.

**Pull**: Download changes from the remote and merge them into your current branch.

**Pull request (PR)**: A proposal to merge one branch into another, with discussion and review.

**Push**: Upload your local commits to a remote repository.

**README**: The front-page file (`README.md`) describing a project.

**Rebase**: An advanced way to move or replay commits onto a different starting point, producing a straighter history.

**Reflog**: Git's private diary of where `HEAD` has been. It is a lifesaver for recovering lost work.

**Release**: A packaged, named version of a project on GitHub, usually tied to a tag.

**Remote**: A copy of a repository hosted elsewhere, such as GitHub.

**Repository (repo)**: A project folder tracked by Git, including its history.

**Resolve (conflict)**: Choosing the final content when Git can't merge automatically.

**Restore**: Bring a file back to an earlier state, or unstage it. (`git restore`)

**Revert**: Create a new commit that undoes an earlier commit, safe for shared history.

**Review**: Examining a pull request and responding with comments, approval, or requested changes.

**Reset**: Move the current branch back to an earlier commit. Powerful; use carefully.

**Shell / Terminal**: A text window where you type commands.

**SSH key**: A pair of files (private and public) used to prove your identity without a password.

**Squash**: Combine multiple commits into one.

**Stage / Staging area**: The "loading dock" where changes wait before being committed.

**Star**: A bookmark-and-applause button on repos.

**Stash**: Temporarily shelve uncommitted changes. (`git stash`)

**Tag**: A label pinned to a specific commit, often used for versions (`v1.0.0`).

**Tracked / Untracked**: Whether Git is watching a file (tracked) or has never been told about it (untracked).

**Upstream**: The remote branch your local branch is linked to; also commonly used to mean the original project that a fork came from.

**Version control**: Systems that record changes over time so you can recall specific versions.

**Watch**: Subscribe to notifications about a repository.

**Working directory / working tree**: The actual files and folders you see and edit.

**Workflow**: A GitHub Actions automation file, or generally a way of working (as in "GitHub flow").

**YAML**: A human-readable format used for GitHub Actions workflow files.

---

⬅️ Previous: [Chapter 12](12-cheat-sheet.md) · ➡️ Next: **[Chapter 14: Troubleshooting & FAQ](14-troubleshooting-faq.md)**
