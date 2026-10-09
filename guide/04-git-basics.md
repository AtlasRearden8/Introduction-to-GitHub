# Chapter 4: Git on Your Own Computer 💻

🎯 **Goals:** Use Git locally. You'll create a repository from scratch, track changes, make commits, and read your project's history, all using the terminal.

This is the chapter where the earlier ideas become muscle memory. Take your time.

---

## Terminal survival kit

You only need a few terminal commands to get around:

| Command | Meaning | Example |
|---------|---------|---------|
| `pwd` | **P**rint **w**orking **d**irectory: where am I? | `pwd` |
| `ls` | **L**i**s**t files here (on Windows Git Bash too) | `ls` |
| `cd folder` | **C**hange **d**irectory: go into a folder | `cd Documents` |
| `cd ..` | Go up one folder | `cd ..` |
| `mkdir name` | **M**a**k**e a **dir**ectory (folder) | `mkdir my-project` |
| `clear` | Tidy the screen | `clear` |

Tips that save a lot of frustration:
- Press **Tab** to auto-complete file and folder names.
- Press **↑** (up arrow) to bring back your previous command.
- Spaces in names need quotes: `cd "My Documents"`.

## Step 1: Make a project folder

```bash
cd ~                      # go to your home folder
mkdir git-practice        # create a folder
cd git-practice           # step inside it
pwd                       # confirm where you are
```

Anything after `#` is a comment for you to read. You don't need to type it.

## Step 2: Turn it into a repository

```bash
git init
```

Output: `Initialized empty Git repository in .../git-practice/.git/`

Git created a hidden folder named `.git`. That's where it stores the entire history. **Never edit or delete `.git` by hand.** Deleting it erases the project's history.

## Step 3: Check status, your most-used command

```bash
git status
```

You'll see "On branch main … No commits yet … nothing to commit." **Run `git status` constantly.** It always tells you what's happening and often suggests the next command.

## Step 4: Create a file

Make a file called `hello.txt`. In the terminal:

```bash
echo "Hello, Git!" > hello.txt
```

(Or create it in your editor and save it inside `git-practice`.)

```bash
git status
```

Now Git says `hello.txt` is **untracked**: it sees the file but isn't watching it yet.

## Step 5: Stage the file (`git add`)

```bash
git add hello.txt
git status
```

The file is now listed under "Changes to be committed" (in green). It's on the loading dock, ready for the snapshot.

Handy variations:

| Command | What it stages |
|---------|----------------|
| `git add file.txt` | Just that file |
| `git add folder/` | Everything in that folder |
| `git add .` | Everything changed in the current folder and below |

## Step 6: Commit (`git commit`)

```bash
git commit -m "Add hello.txt"
```

`-m` lets you write the message right there in quotes. 🎉 **That's your first local commit.**

```bash
git status
```

→ "nothing to commit, working tree clean." Everything's saved.

## Step 7: Make more changes and see the difference

Edit the file:

```bash
echo "This is my second line." >> hello.txt
```

(`>>` *adds* to the file; `>` *replaces* it.)

See what changed:

```bash
git diff
```

You'll see removed lines starting with `-` (red) and added lines starting with `+` (green). Then save it:

```bash
git add hello.txt
git commit -m "Add a second line to hello.txt"
```

> Shortcut for files Git already tracks: `git commit -am "message"` stages and commits in one go. (It won't pick up brand-new files.)

## Step 8: Read your history

```bash
git log
```

Shows each commit: a long ID (the *hash*), author, date, and message. Press **q** to quit if it shows a scrolling view.

A friendlier view:

```bash
git log --oneline
```

Example:

```
a1b2c3d Add a second line to hello.txt
9f8e7d6 Add hello.txt
```

Peek inside any commit:

```bash
git show a1b2c3d
```

(Use your own ID. The first 7 characters are enough.)

## The daily rhythm

```
   ┌─► edit files
   │      │
   │      ▼
   │   git status      ← what's changed?
   │      │
   │      ▼
   │   git add ...     ← pick what goes in the snapshot
   │      │
   │      ▼
   │   git commit -m "..."   ← save it
   └──────┘
```

## Ignoring files: `.gitignore`

Some files shouldn't be tracked: passwords, temporary files, giant downloads, system clutter (`.DS_Store` on Mac, `Thumbs.db` on Windows). Create a file named `.gitignore` listing patterns:

```
# Mac & Windows clutter
.DS_Store
Thumbs.db

# Secrets and local settings
.env
*.log

# Folders
node_modules/
```

Then commit the `.gitignore` itself. Git will politely look away from anything matching.

> 🔒 **Golden rule:** never commit passwords, API keys, or private tokens. If it's in a commit, it's in the history, even if you delete it later. Chapter 11 covers what to do if it happens.

## Good habits to start now

- **Commit small and often.** Each commit = one logical change.
- **Write meaningful messages.** Future you will thank you.
- **Check `git status` before and after.** It takes one second and prevents most confusion.
- **Don't commit unrelated changes together.**

## 🛠️ Try it

1. Create `git-practice` and run `git init`.
2. Make three files: `notes.txt`, `todo.txt`, `ideas.txt`.
3. Stage and commit them **one at a time**, each with its own message.
4. Edit `todo.txt`, run `git diff`, then commit.
5. Run `git log --oneline`. You should see 4 commits.
6. Add a `.gitignore` that ignores `*.log`; create `test.log`; confirm `git status` doesn't mention it.

## 🧯 Stuck?

- **"Author identity unknown":** Run the `git config` commands from Chapter 2.
- **A text editor opened (Vim) and I'm trapped!** You probably ran `git commit` without `-m`. In Vim: press `Esc`, type `:q!`, press Enter to leave without saving. Or type your message, press `Esc`, then `:wq` and Enter to save.
- **"not a git repository":** You're in the wrong folder. Use `pwd` and `cd` to get to your project.
- **`git add` did nothing visible:** That's normal! Run `git status` to see the effect.

## ✅ Checkpoint

You can now explain and use: `init`, `status`, `add`, `commit`, `diff`, `log`. Those six commands are the foundation of nearly everything. If these feel okay, you're in great shape.

- [ ] I can create a repo with `git init`.
- [ ] I can stage and commit changes.
- [ ] I can read the history with `git log --oneline`.

---

⬅️ Previous: [Chapter 3](03-first-repository.md) · ➡️ Next: **[Chapter 5: Connecting Your Computer to GitHub](05-remotes-clone-push-pull.md)**
