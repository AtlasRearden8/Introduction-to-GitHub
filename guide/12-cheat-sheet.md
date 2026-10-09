# Chapter 12: Cheat Sheet 📄

Bookmark this page. Every command from the guide, in one place.

---

## One-time setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --list
```

## Starting a repository

| Command | Does |
|---------|------|
| `git init` | Turn the current folder into a repo |
| `git clone URL` | Download a repo from GitHub |
| `git remote add origin URL` | Link a local repo to GitHub |
| `git remote -v` | Show remote links |

## The daily loop

| Command | Does |
|---------|------|
| `git status` | What's changed? (use constantly) |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git add file` | Stage a file |
| `git add .` | Stage everything here |
| `git commit -m "msg"` | Save a snapshot |
| `git commit -am "msg"` | Stage tracked files + commit |
| `git push` | Upload commits to GitHub |
| `git pull` | Download + merge from GitHub |
| `git fetch` | Download without merging |

## History

| Command | Does |
|---------|------|
| `git log` | Full history |
| `git log --oneline` | Compact history |
| `git log --oneline --graph --all` | Branch picture |
| `git show <id>` | One commit's details |
| `git blame file` | Who changed each line |

## Branches

| Command | Does |
|---------|------|
| `git branch` | List local branches |
| `git branch -a` | List all (including remote) |
| `git switch name` | Move to a branch |
| `git switch -c name` | Create + move to new branch |
| `git merge name` | Merge `name` into the current branch |
| `git branch -d name` | Delete a merged branch |
| `git branch -D name` | Force-delete a branch |
| `git push -u origin name` | Push a new branch and remember it |
| `git push origin --delete name` | Delete a remote branch |

## Undo and recover

| Want to… | Command |
|----------|---------|
| Discard uncommitted edits | `git restore file` |
| Unstage a file | `git restore --staged file` |
| Fix last commit | `git commit --amend` |
| Un-commit, keep work | `git reset --soft HEAD~1` |
| Safely undo a pushed commit | `git revert <id>` |
| Shelve work | `git stash` / `git stash pop` |
| Find "lost" commits | `git reflog` |
| Abort a merge | `git merge --abort` |
| Restore old version of a file | `git restore --source <id> file` |

## Tags

```bash
git tag v1.0.0
git push origin v1.0.0
```

## GitHub CLI (optional helper)

| Command | Does |
|---------|------|
| `gh auth login` | Log in |
| `gh repo clone owner/repo` | Clone |
| `gh repo create` | Create a repo |
| `gh pr create` | Open a pull request |
| `gh pr list` | List pull requests |
| `gh issue create` | Create an issue |
| `gh issue list` | List issues |

## Markdown quick reference

```markdown
# Heading 1
## Heading 2
**bold**  *italic*  ~~strike~~
- bullet        1. numbered
[link text](https://url)   ![alt](image.png)
`inline code`
> quote
- [ ] task   - [x] done
```

Code block: three backticks, optional language, code, three backticks.

## GitHub text tricks

| Type | Result |
|------|--------|
| `#12` | Link to issue/PR 12 |
| `@name` | Mention a person |
| `Closes #12` (in a PR) | Auto-closes issue 12 on merge |
| `:tada:` | 🎉 |

## The GitHub flow in seven lines

```bash
git switch main && git pull           # 1. start fresh
git switch -c my-change               # 2. new branch
# ...edit files...                    # 3. work
git add . && git commit -m "Message"  # 4. save
git push -u origin my-change          # 5. upload
# open PR on GitHub, review, merge    # 6. propose + merge
git switch main && git pull           # 7. update, then repeat!
```

## Terminal basics

| Command | Does |
|---------|------|
| `pwd` | Where am I? |
| `ls` | List files |
| `cd folder` / `cd ..` | Enter / leave a folder |
| `mkdir name` | Make a folder |
| `clear` | Clean the screen |
| `Tab` | Auto-complete |
| `↑` | Previous command |

---

⬅️ Previous: [Chapter 11](11-level-ups.md) · ➡️ Next: **[Chapter 13: Glossary](13-glossary.md)**
