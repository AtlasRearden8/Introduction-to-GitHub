# Chapter 10: Undoing Mistakes 🧯

🎯 **Goals:** Learn the safety net. Everyone makes Git mistakes. The difference between nervous beginners and confident ones is knowing how to recover.

> 💛 **Reassurance first:** if you've **committed** your work, Git almost never truly loses it. Even "lost" commits can usually be found again (see `reflog` below). Take a breath. You've got this.

**How to use this chapter:** find the situation that matches yours. You don't need to memorize anything. Come back whenever you need it.

---

## First, a rule of thumb

Ask: **Has this change been pushed/shared yet?**

- **Not shared (only on your computer):** you have more freedom to rewrite things.
- **Already pushed/shared:** prefer **adding a new commit that undoes it** (`git revert`) rather than rewriting history, so you don't disrupt anyone else.

## Situation 1: "I edited a file and want to throw away my changes"

(The changes are **not committed** yet.)

```bash
git restore filename.txt
```

⚠️ This **permanently discards** the uncommitted edits to that file. Check with `git status` and `git diff` first.

## Situation 2: "I staged a file by mistake"

(You ran `git add` but haven't committed.)

```bash
git restore --staged filename.txt
```

The file goes back to "modified but not staged." Your edits stay safe.

## Situation 3: "I made a typo in my last commit message"

(Not yet pushed.)

```bash
git commit --amend -m "Corrected message"
```

## Situation 4: "I forgot to include a file in my last commit"

(Not yet pushed.)

```bash
git add forgotten-file.txt
git commit --amend --no-edit
```

## Situation 5: "I want to undo my last commit but keep my work"

(Not yet pushed.)

```bash
git reset --soft HEAD~1
```

The commit disappears, but your changes remain **staged**, ready to recommit. `HEAD~1` means "one commit before the current one."

Variation: `git reset HEAD~1` (the default "mixed" mode) un-commits *and* un-stages, but still keeps your edits in your files.

## Situation 6: "I want to undo a commit that's already been pushed"

Use **revert**. It creates a *new* commit that cancels out an old one, and history stays intact and safe for teammates.

```bash
git log --oneline            # find the commit's ID
git revert a1b2c3d           # undo that commit
git push
```

This is the safe, standard way to undo shared work. It works on merge commits too, though those need an extra flag. Look up `git revert -m 1` when you get there.

## Situation 7: "I committed on `main` but meant to use a branch"

(Not yet pushed.)

```bash
git branch my-new-branch     # create a branch holding the current commits
git reset --hard origin/main # put main back to match GitHub
git switch my-new-branch     # continue your work here
```

⚠️ `--hard` discards uncommitted changes, so commit or stash first. Your commits are safe on `my-new-branch`.

## Situation 8: "I need to switch branches but I'm not ready to commit"

Shelve your work temporarily:

```bash
git stash            # tuck changes away
git switch other-branch
# ...do things...
git switch original-branch
git stash pop        # bring your changes back
```

`git stash list` shows what's shelved.

## Situation 9: "I want to look at an old version, just to see it"

```bash
git log --oneline
git show a1b2c3d              # view that commit
git switch --detach a1b2c3d   # look around at the old snapshot
git switch main               # return to the present
```

"Detached HEAD" sounds dramatic but just means "you're viewing an old snapshot, not on a branch." Don't commit there unless you create a branch first (`git switch -c rescue-branch`). Going back to `main` ends it.

Restore just *one file* from an older commit:

```bash
git restore --source a1b2c3d filename.txt
```

## Situation 10: "I deleted a file by accident"

If it was committed before:

```bash
git restore filename.txt
```

If you already committed the deletion, restore it from the commit before:

```bash
git restore --source HEAD~1 filename.txt
```

## Situation 11: "I deleted a branch / lost commits / did a bad reset"

Git quietly records everywhere `HEAD` has been for a while. This is your ultimate safety net:

```bash
git reflog
```

You'll see entries like `a1b2c3d HEAD@{3}: commit: Add recipes`. Find the moment before things went wrong, then:

```bash
git switch -c recovered a1b2c3d
```

Your lost work is back on a new branch named `recovered`. 🪄

## Situation 12: "I accidentally committed a secret (password, API key)"

This is serious but fixable.

1. **Assume the secret is compromised.** Immediately **revoke or rotate** it at the service that issued it (change the password, delete and recreate the key). This is the step that actually protects you.
2. Removing it from Git history requires rewriting history with a tool such as `git filter-repo` (see GitHub's docs: *"Removing sensitive data from a repository"*). It's more advanced, so ask for help if needed.
3. Add the file to `.gitignore` so it doesn't happen again.

Deleting the file in a new commit is **not enough**; the secret remains in the old commits.

## Situation 13: "I'm in the middle of a merge and it's a mess"

Cancel the merge and return to how things were before:

```bash
git merge --abort
```

Similarly `git rebase --abort` cancels a rebase.

## Cheat table: which undo tool?

| I want to… | Use |
|------------|-----|
| Discard uncommitted edits | `git restore file` |
| Unstage a file | `git restore --staged file` |
| Fix last commit message / add a forgotten file | `git commit --amend` |
| Un-commit, keep my work | `git reset --soft HEAD~1` |
| Undo a pushed commit safely | `git revert <id>` |
| Pause work temporarily | `git stash` / `git stash pop` |
| Recover "lost" commits | `git reflog` |
| Cancel a merge in progress | `git merge --abort` |

## ⚠️ The dangerous ones (use with care)

| Command | Why it's risky |
|---------|----------------|
| `git reset --hard` | Throws away uncommitted changes immediately |
| `git clean -fd` | Deletes untracked files permanently (preview first with `git clean -nd`) |
| `git push --force` | Overwrites the remote's history and can erase teammates' work. If you must, prefer `git push --force-with-lease`, and never on shared branches without asking |

Before running anything in this table: pause, run `git status`, and ask "do I really mean this?"

## 🛠️ Try it (in a throwaway repo!)

1. Edit a file, then discard the edit with `git restore`.
2. Stage a file, then unstage it.
3. Make a commit with a typo in the message and fix it with `--amend`.
4. Make a commit, then undo it with `git reset --soft HEAD~1`. Notice your changes remain.
5. Make a commit, push it, and `git revert` it.
6. **Fire drill:** create a branch with a commit, delete the branch with `git branch -D name`, then bring it back using `git reflog`. Doing this once makes you fearless.

## ✅ Checkpoint

- [ ] I know the difference between "not yet committed," "committed locally," and "pushed."
- [ ] I can unstage, amend, revert, and stash.
- [ ] I know `git reflog` exists and what it's for.
- [ ] I know which commands are dangerous.

---

⬅️ Previous: [Chapter 9](09-collaboration-and-open-source.md) · ➡️ Next: **[Chapter 11: Level-Ups](11-level-ups.md)**
