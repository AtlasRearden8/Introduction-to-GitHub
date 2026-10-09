# Chapter 25: GitHub Desktop Menu Tour 🧭

🎯 **Goals:** A reference for every part of GitHub Desktop: what each menu does, what the buttons and tabs mean, and which items you can safely ignore for now. Look things up here whenever you see something unfamiliar.

> 💡 **A note on versions.** GitHub Desktop is updated often. Your menus may have a few more or fewer items, or slightly different wording, than the lists below. The big ideas stay the same, and unfamiliar items are usually advanced ones you can leave alone. The official guide at <https://docs.github.com/en/desktop> is the final word.

On a **Mac**, the menu bar runs across the top of the screen, and the first menu is named **GitHub Desktop** (it holds **Settings**). On **Windows**, the menu bar sits at the top of the app window (press **Alt** if you can't see it), and **Options** lives under **File**.

---

## 🪟 The main window

```
┌──────────────────────────────────────────────────────────────────────┐
│ Current repository ▾ │ Current branch ▾ │      Fetch / Pull / Push    │
├───────────────────────┬──────────────────────────────────────────────┤
│  Changes | History    │                                              │
│  (file list)          │      The selected file or commit             │
│  Summary / Description│                                              │
│  [ Commit ]           │                                              │
└───────────────────────┴──────────────────────────────────────────────┘
```

### The top bar

| Item | What it does |
|------|--------------|
| **Current repository** | Shows the project you're in. Click it to switch projects, search, or add new ones. |
| **Current branch** | Shows the branch you're on. Click it to switch, create, or search branches. A second tab lists **Pull Requests**. |
| **Fetch origin / Pull origin / Push origin / Publish** | One button that changes. See the next table. |

### The big top-right button

| It says | Meaning | What to click it for |
|---------|---------|---------------------|
| **Fetch origin** | Nothing waiting. Click to check GitHub for news. | Starting a work session |
| **Pull origin** | GitHub has new work you don't have. | Bringing it down |
| **Push origin** | You have commits GitHub doesn't. | Sending your work up |
| **Publish repository** | The project isn't on GitHub yet. | Putting it on GitHub for the first time |
| **Publish branch** | The branch isn't on GitHub yet. | Sharing a new branch |

Small numbers and arrows next to it tell you how many commits are waiting to go up (↑) or come down (↓).

### The two tabs

| Tab | What you see |
|-----|-------------|
| **Changes** | Files you've edited and not yet committed. Tick the ones to include, write a **Summary**, and commit. |
| **History** | Every commit so far. Click one to see what it changed. Right-click for more options. |

### Inside the Changes tab

| Part | What it is |
|------|-----------|
| **Checkboxes** | Which files go into the next commit |
| **Right-click a file** | **Discard Changes**, **Ignore file**, **Open in editor**, **Show in Explorer/Finder** |
| **The diff** (right side) | Green is added, red is removed |
| **Summary** | A short message (required) |
| **Description** | Optional extra detail |
| **Commit to** *(branch)* | Saves your snapshot |
| **Undo** | Appears just after a commit, to reverse the last unpushed commit |
| **Stashed Changes** | Appears when you've put edits aside while switching branches |

### Inside the History tab

| Action | How |
|--------|-----|
| See what a commit changed | Click it |
| **Revert** a commit | Right-click → **Revert Changes in Commit** |
| Start a branch from a commit | Right-click → **Create Branch from Commit** |
| Copy a commit's ID | Right-click → **Copy SHA** (rarely needed) |
| Compare with another branch | Use the **Compare** box at the top of the History tab |

---

## 📂 The File menu

| Item | What it does |
|------|-------------|
| **New repository...** | Creates a new project on your computer (Chapter 5) |
| **Add local repository...** | Tells GitHub Desktop about a project folder that already exists on your computer and is already a repository |
| **Clone repository...** | Downloads a project from GitHub (Chapter 6) |
| **Options...** (Windows) | Opens Settings. On Mac, use **GitHub Desktop → Settings** |
| **Exit** (Windows) | Closes the app |

## ✏️ The Edit menu

Standard items: **Undo**, **Redo**, **Cut**, **Copy**, **Paste**, **Select All**, and **Find**. These work on text boxes, like the commit summary.

## 👁️ The View menu

| Item | What it does |
|------|-------------|
| **Show Changes** | Switch to the Changes tab |
| **Show History** | Switch to the History tab |
| **Show Repository List** | Opens the list of your projects |
| **Show Branches List** | Opens the branch menu |
| **Go to Summary** | Jumps your cursor to the commit Summary box |
| **Toggle Full Screen** | Fills your screen |
| **Zoom In / Zoom Out / Reset Zoom** | Makes text bigger or smaller. Handy if text is hard to read. |
| **Toggle Developer Tools** | For app developers. Ignore it. |

## 🗂️ The Repository menu

These act on the project that's currently open.

| Item | What it does |
|------|-------------|
| **Push / Pull / Fetch** | Same as the top-right button |
| **Remove...** | Takes the project out of GitHub Desktop's list. It can leave the files on your computer, and asks you what to do. Read the box carefully. |
| **View on GitHub** | Opens the project on github.com |
| **Open in** *(your editor)* | Opens the project in your editor |
| **Show in Explorer / Show in Finder** | Opens the project's folder |
| **Open in command prompt / terminal** | Opens a text window. You don't need this. |
| **Repository settings...** | Change the GitHub address, the files Git ignores, and your name and email for this project only |

## 🌿 The Branch menu

| Item | What it does | Chapter |
|------|-------------|---------|
| **New branch...** | Creates a branch | 7 |
| **Rename...** | Renames the current branch | 7 |
| **Delete...** | Deletes a branch | 7 |
| **Discard all changes...** | Throws away every unsaved edit. Careful! | 12 |
| **Stash all changes** | Puts your unsaved edits aside | 12 |
| **Compare to branch** | See how this branch differs from another | 7 |
| **Merge into current branch...** | Brings another branch's work into this one | 7 |
| **Update from** *(main)* | Brings the main branch's latest work into this branch | 7 |
| **Compare on GitHub** | Opens the comparison on the website | 8 |
| **Preview pull request** | Shows what a pull request would include | 8 |
| **Create pull request** | Opens a pull request on the website | 8 |

> 🛑 You may also see **Squash and merge into current branch** and **Rebase current branch**. These are advanced ways to tidy history. As a beginner, skip them and use **Merge into current branch**.

## ❓ The Help menu

| Item | What it does |
|------|-------------|
| **Report issue...** | Tells the GitHub Desktop team about a bug |
| **Contact GitHub Support** | Gets help from GitHub |
| **Show logs in Explorer / Finder** | Opens the app's diagnostic files. Useful if support asks. |
| **About GitHub Desktop** | Shows your version, and has a **Check for updates** button |

On Mac, **About** and **Check for Updates** are in the **GitHub Desktop** menu.

---

## ⚙️ Settings (Options)

Open it with **File → Options** (Windows) or **GitHub Desktop → Settings** (Mac). Tabs:

| Tab | What's there | Recommended |
|-----|-------------|-------------|
| **Accounts** | Your GitHub sign-in. Sign out and in here if something stops working. | Signed in |
| **Integrations** | Your **external editor** (like VS Code) and **shell** | Choose your editor |
| **Git** | Your **name and email**, and the **default branch name** | Name, email, `main` |
| **Appearance** | **Light**, **Dark**, or match your system. You may find a **Tab size** and **Show whitespace** option. | Whatever's comfortable |
| **Notifications** | Alerts, such as when a check finishes | Your choice |
| **Prompts** | Confirmation questions the app asks, such as before deleting a branch or discarding changes | **Leave these on** while learning |
| **Advanced** | Usage statistics and a few advanced options | Defaults are fine |

### 🛡️ The confirmation prompts

The **Prompts** tab lists the "Are you sure?" messages that appear before risky actions. As a beginner, **keep them all on**. They're your safety net.

---

## ⌨️ Handy keyboard shortcuts

Shortcuts are listed next to the items in the menus, so look there for your version. Some common ones:

| Windows | Mac | Does |
|---------|-----|------|
| `Ctrl + Shift + A` | `Cmd + Shift + A` | Open the project in your editor |
| `Ctrl + Shift + F` | `Cmd + Shift + F` | Show the project folder |
| `Ctrl + B` | `Cmd + B` | Open the branches list |
| `Ctrl + N` | `Cmd + N` | New repository |
| `Ctrl + O` | `Cmd + O` | Add a local repository |
| `Ctrl + Shift + O` | `Cmd + Shift + O` | Clone a repository |
| `Ctrl + 1` | `Cmd + 1` | Show the Changes tab |
| `Ctrl + 2` | `Cmd + 2` | Show the History tab |

> If a shortcut doesn't work, look for the one printed beside the menu item. It might be different in your version.

## 🔤 Icons and labels you'll see

| You see | It means |
|---------|----------|
| Green **+** next to a file | A new file |
| Orange dot, or a **pencil** | A changed file |
| Red **−** | A deleted file |
| **Conflict** warning | Two changes collide. Resolve it (Chapter 6). |
| ↑ and number | Commits ready to **push** |
| ↓ and number | Commits ready to **pull** |
| A branch icon with an arrow | The branch isn't published yet |
| A **lock** next to a repository | It's private on GitHub |

## 🧯 Stuck?

- **I can't find a menu item from this chapter:** Your version may have moved or renamed it. Use the **Help** menu or search the official docs.
- **The menu bar is hidden (Windows):** Press **Alt**.
- **The text is too small:** **View → Zoom In**.
- **The app is acting strange:** Close and reopen it. If it keeps happening, **Help → Report issue**.

## ✅ Checkpoint

- [ ] I know what the top-right button's four states mean.
- [ ] I know the difference between the Changes and History tabs.
- [ ] I can find Settings and change my editor.
- [ ] I know which menu items are advanced and safe to ignore.

---

Previous: [Chapter 24](24-30-day-plan.md) · Next: **[Chapter 26: Cheat Sheet](26-cheat-sheet.md)**
