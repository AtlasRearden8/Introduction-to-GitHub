# Chapter 5: GitHub Desktop on Your Computer 💻

🎯 **Goals:** Use GitHub Desktop to create a project on your own computer, save snapshots of your work, and look back through its history.

This is the chapter where the ideas from Chapter 1 become habits. Take your time.

---

## 👋 Meet GitHub Desktop

Open GitHub Desktop. Once you have a project open, the window looks like this:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Current repository ▾   │  Current branch ▾   │   Fetch origin / Push    │  ← top bar
├──────────────────────┬─────────────────────────────────────────────────┤
│ Changes | History    │                                                 │
│                      │   The file you selected, with changes           │
│ ☑ hello.txt          │   highlighted in green (added) and red          │
│ ☑ notes.txt          │   (removed)                                     │
│                      │                                                 │
│ Summary (required)   │                                                 │
│ Description          │                                                 │
│ [Commit to main]     │                                                 │
└──────────────────────┴─────────────────────────────────────────────────┘
```

| Part of the window | What it does |
|--------------------|--------------|
| **Current repository** (top left) | Switch between your projects |
| **Current branch** (top middle) | Shows which line of work you're on (Chapter 7) |
| **Fetch / Push button** (top right) | Syncs with GitHub (Chapter 6) |
| **Changes tab** | Lists every file you've changed and not yet saved |
| **History tab** | Lists every snapshot you've saved before |
| **Summary / Description** | Where you describe a snapshot before saving it |
| **Commit button** (bottom left) | Saves the snapshot |

**Screenshot:** The GitHub Desktop window with a project open, with the areas in the table labeled.
{ .shot }

## 🆕 Step 1: Create a new project

1. In the menu bar, choose **File → New repository...**
2. Fill in the form:
    - **Name:** `git-practice`
    - **Description:** `Practice project` (optional)
    - **Local path:** where on your computer to put it. The default (your Documents folder, in a `GitHub` folder) is fine.
    - Tick **Initialize this repository with a README**.
    - Leave **Git ignore** and **License** as **None** for now.
3. Click **Create repository**.

You just made a project on your computer. GitHub Desktop turned a normal folder into a **repository**, which means Git is now watching it.

**Screenshot:** The **Create a New Repository** window, filled in.
{ .shot }

### 📂 Find your project's folder

It's an ordinary folder. To open it, choose **Repository → Show in Explorer** (Windows) or **Repository → Show in Finder** (Mac). You'll see `README.md` inside. You may also see a hidden `.git` folder. That's where Git keeps your history. **Never edit or delete the `.git` folder.**

## ✏️ Step 2: Make a change

1. Choose **Repository → Open in Visual Studio Code** (or whichever editor you picked in Chapter 2). If you don't have one, use **Show in Explorer** or **Show in Finder** and open `README.md` with any plain-text editor.
2. Add a line to `README.md`, such as `This is my practice project.`
3. **Save the file** in your editor.
4. Switch back to GitHub Desktop.

Look at the **Changes** tab. `README.md` now appears in the list, and the right side shows exactly what changed: **green** lines were added and **red** lines were removed. Seeing this before you save is one of the best things about GitHub Desktop.

**Screenshot:** The Changes tab showing `README.md` with one green added line.
{ .shot }

## 💾 Step 3: Save a snapshot (commit)

At the bottom left:

1. Type a short note in the **Summary** box, such as `Add a line to the README`.
2. Click **Commit to main**.

That's it. **You just made your first commit.** The file disappears from the Changes list because it's now safely saved.

### ☑️ Choosing what goes into a commit

Each changed file has a **checkbox**. Only ticked files go into the next commit. This is handy when you've changed several things but want to save them as separate snapshots. Untick the files that don't belong, then commit.

Aim for **one commit per idea**: "Add contact page," then "Fix typo in title." Small commits make your history easy to read.

## ➕ Step 4: Add a new file

1. Make a new text file in your project folder (from **Show in Explorer** or **Show in Finder**) and name it `notes.txt`. Or create it in your editor and save it in the `git-practice` folder.
2. Type a line or two and save it.
3. In GitHub Desktop, `notes.txt` appears in **Changes** with a green **+** mark, meaning it's a new file.
4. Write a summary such as `Add notes file` and click **Commit to main**.

## 🕰️ Step 5: Look at your history

Click the **History** tab. Every commit appears in a list, newest first, with its message, author, and time.

Click any commit to see exactly which files it changed and what was added or removed. This is your time machine. Nothing you've committed is ever hidden from you.

**Screenshot:** The History tab with three commits listed and one selected.
{ .shot }

## 🔁 The daily rhythm

```
   ┌─► Edit your files and save them
   │          │
   │          ▼
   │   Look at the Changes tab    ← what changed?
   │          │
   │          ▼
   │   Tick the files you want, write a Summary
   │          │
   │          ▼
   │   Click "Commit to main"     ← saved
   └──────────┘
```

## 🙈 Keeping unwanted files out: ignoring

Some files shouldn't be tracked: private passwords, temporary files, huge downloads, or system clutter like `.DS_Store` (Mac) and `Thumbs.db` (Windows).

When one of these shows up in your Changes list:

1. **Right-click** the file.
2. Choose **Ignore file (add to .gitignore)**.

Desktop adds it to a special file called `.gitignore`, and the file stops appearing. You can also choose a ready-made list when creating a project: in the **Create a New Repository** window, pick a template from the **Git ignore** menu.

> 🔑 **Golden rule:** never save passwords, API keys, or private tokens in a project. Anything you commit stays in the history, even if you delete it later. Chapter 12 covers what to do if it happens.

## 🌱 Good habits to start now

- **Commit small and often.** Each commit should be one idea.
- **Write meaningful summaries.** Future you will be grateful.
- **Check the Changes tab before you commit.** Make sure only the files you meant are ticked.
- **Don't mix unrelated changes in one commit.**

## 🛠️ Try it

1. Create a project called `git-practice` (if you haven't already).
2. Make three files: `notes.txt`, `todo.txt`, and `ideas.txt`.
3. Commit them **one at a time**, each with its own summary. (Untick the other two each time.)
4. Edit `todo.txt`, look at the green and red lines in the Changes tab, then commit.
5. Open **History**. You should see at least five commits.
6. Make a file called `test.log`, right-click it in Changes, and ignore it. Confirm it disappears.

## 🧯 Stuck?

- **My file isn't in the Changes list:** Did you save it in your editor? Is it inside the project folder? Check with **Repository → Show in Explorer** or **Show in Finder**.
- **The Commit button is grey:** You need to type a **Summary** and have at least one file ticked.
- **"Unable to find your name"** or a similar message about who you are: Open the settings, go to the **Git** tab, and fill in your name and email (Chapter 2).
- **Too many files in Changes:** Something noisy (like a temporary folder) is being tracked. Right-click it and ignore it.

## ✅ Checkpoint

- [ ] I can create a new repository in GitHub Desktop.
- [ ] I can make a change, and see it in the Changes tab.
- [ ] I can write a summary and commit.
- [ ] I can read my project's history in the History tab.

---

Previous: [Chapter 4](04-markdown.md) · Next: **[Chapter 6: Connecting Your Computer to GitHub](06-clone-push-pull.md)**
