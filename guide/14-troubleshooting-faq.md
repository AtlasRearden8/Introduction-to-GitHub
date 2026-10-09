# Chapter 14: Troubleshooting & FAQ 🩺

Errors look intimidating, but they're usually Git trying to *help* in a very literal way. Read the message slowly. It often contains the fix.

> **Universal first step:** run `git status`. It explains the current situation and often suggests the next command.

---

## Common errors and fixes

### `fatal: not a git repository (or any of the parent directories): .git`
You're in a folder that isn't a repo.
**Fix:** `pwd` to see where you are; `cd` into your project; or run `git init` if you meant to start one.

### `Author identity unknown` / `Please tell me who you are`
Git doesn't know your name/email yet.
**Fix:**
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### `remote: Support for password authentication was removed` / `Authentication failed`
GitHub doesn't accept your account password for Git operations.
**Fix:** log in with the GitHub CLI (`gh auth login`), Git Credential Manager, or SSH. See [Chapter 5](05-remotes-clone-push-pull.md).

### `Permission denied (publickey)`
SSH can't prove who you are.
**Fix:** make sure your public key is added in GitHub **Settings → SSH and GPG keys**, then test `ssh -T git@github.com`. Or switch the remote to HTTPS: `git remote set-url origin https://github.com/USER/REPO.git`.

### `! [rejected] main -> main (fetch first)` or `(non-fast-forward)`
GitHub has commits you don't.
**Fix:** `git pull`, resolve any conflicts, then `git push`.

### `error: failed to push some refs`
Usually the same cause as above.
**Fix:** read the lines before it. Most often `git pull` first.

### `fatal: refusing to merge unrelated histories`
You're combining two repos that started separately (common when you create a repo with a README on GitHub *and* another locally).
**Fix:** if you're sure, `git pull origin main --allow-unrelated-histories`. To avoid it next time, create the GitHub repo *empty*.

### `CONFLICT (content): Merge conflict in file.txt`
Both sides changed the same lines.
**Fix:** open the file, pick the final text, delete the `<<<<<<<`, `=======`, `>>>>>>>` lines, then `git add file.txt` and `git commit`. To bail out: `git merge --abort`.

### `error: Your local changes to the following files would be overwritten`
You have uncommitted edits that conflict with what you're trying to do.
**Fix:** commit them, or `git stash`, do your operation, then `git stash pop`.

### `nothing to commit, working tree clean`
Not an error! No changes to save.

### `Changes not staged for commit`
You edited files but haven't run `git add`.
**Fix:** `git add file` then `git commit`.

### `fatal: pathspec 'file' did not match any files`
Git can't find that filename. Check spelling, capitalization, and your current folder (`ls`).

### `fatal: remote origin already exists`
The link is already set.
**Fix:** `git remote -v` to see it; change with `git remote set-url origin NEW-URL`.

### `error: src refspec main does not match any`
You have no commits yet, or your branch is named differently.
**Fix:** make a first commit; run `git branch` to see the branch name; rename with `git branch -M main`.

### `error: failed to push` because of a large file
GitHub rejects files over 100 MB.
**Fix:** remove the file from the commit; consider **Git LFS** for big files. Check `.gitignore`.

### I'm stuck in a weird text editor (Vim)!
Press `Esc`, type `:q!`, press Enter to quit without saving. To save instead: `Esc`, `:wq`, Enter.

### The terminal looks frozen after `git log`
You're in a pager. Press `q` to exit.

### Everything is red / weird after a merge
`git merge --abort` returns you to before the merge.

## Frequently asked questions

### Do I have to use the terminal?
No! GitHub's website handles many things, and apps like **GitHub Desktop** (<https://desktop.github.com>) and editors like **VS Code** provide point-and-click Git. Learning the terminal commands, though, makes everything else make sense.

### Is it OK to work directly on `main`?
For solo practice, sure. For anything shared or important, use branches and pull requests. Good habits start early.

### What's the difference between `master` and `main`?
Just the default branch name. `main` is the modern standard; older repos may use `master`. They work identically.

### Does everything I push become public?
Only if the repo is **public**. Private repos are visible only to you and people you invite. Double-check the visibility before pushing anything sensitive.

### I committed something private. Help!
See [Chapter 10, Situation 12](10-undoing-mistakes.md). The key step is to revoke/rotate any secret immediately.

### What's the difference between `git pull` and `git fetch`?
`fetch` downloads without changing your files. `pull` = `fetch` + merge.

### How often should I commit?
Whenever you complete a small, meaningful piece of work. Many small commits beat one giant one.

### What's the difference between `git add .` and `git add -A`?
In modern Git they behave essentially the same when run from the top of your repo. Both stage new, modified, and deleted files.

### Can I delete a repository?
Yes: **Settings → Danger Zone → Delete this repository**. It's permanent, so double-check.

### Can I rename a repository?
Yes: **Settings → General → Repository name**. GitHub redirects old links. Update your local remote with `git remote set-url origin NEW-URL`.

### Can I undo a merged pull request?
Yes. GitHub shows a **Revert** button on merged PRs, which opens a new PR that undoes it.

### How do I stop getting so many emails?
Adjust **Settings → Notifications**, and un-**Watch** repos you don't need.

### Is GitHub only for programmers?
Not at all. People store writing, research, designs, documentation, data, recipes, and lesson plans there.

### Where can I ask for help?
- Search the exact error message online. Someone has almost certainly hit it.
- Official docs: <https://docs.github.com>
- GitHub Community discussions: <https://github.com/orgs/community/discussions>
- Stack Overflow, with the `git` or `github` tag.
- Ask an AI assistant. Paste the exact error text and what you were trying to do.

## A mindset for when you're stuck 🧠

1. **Breathe.** Committed work is very hard to lose.
2. **Read the whole error**, slowly, top to bottom.
3. **Run `git status`** and **`git log --oneline`** to see where you are.
4. **Don't run commands you don't understand** (especially ones with `--force` or `--hard`).
5. **Search** the error message.
6. **Copy your project folder** as a backup before experimenting with risky fixes.
7. **Ask for help**; everyone has been where you are.

---

⬅️ Previous: [Chapter 13](13-glossary.md) · 🏠 [Back to the start](index.md)

## 🎉 You made it!

If you've worked through this guide, you've gone from "what is GitHub?" to creating repositories, collaborating through pull requests, tracking work with issues, and recovering from mistakes. That's a real, valuable skill set.

Keep a small project going. Commit something every few days. The commands will become second nature before you know it.

**Welcome to GitHub. We're glad you're here.** 💚
