# Chapter 3: Your First Repository 📁

🎯 **Goals:** Create a repository on GitHub, edit a file in your browser, save your first commit, and learn Markdown, the simple formatting language you'll use all over GitHub.

This chapter happens entirely in your web browser.

---

## 📁 Create the repository

1. Click the **+** icon (top right), then **New repository**.
2. Fill in:
    - **Repository name:** `hello-github`
    - **Description:** `My very first repository`
    - **Public or Private:** Either works. *Public* means anyone can see it. *Private* means only you (and people you invite). For practice, **Private** is a fine choice.
    - Tick **Add a README file**.
3. Leave the other options alone for now.
4. Click **Create repository**.

You just made a repository. That's a real milestone.

**Screenshot:** The "Create a new repository" form, filled in.
{ .shot }

## 🔍 Tour of what you made

You'll see:

- A file called **README.md**. This is the "front door" of every project. GitHub shows it automatically below the file list.
- A **branch** menu labeled **main**.
- A **commit** count, currently 1: the first commit, which created the README.

Click **README.md**, then click the **History** (clock) icon. You'll see your first commit. Click it to see exactly what changed. This is the time machine already at work.

## ✏️ Edit a file in your browser (and make a commit)

1. Open **README.md** and click the **pencil** icon (Edit).
2. Add a few lines:

    ```markdown
    # Hello, GitHub!

    My name is **Your Name**, and this is my first repository.

    ## Things I want to learn
    - How Git works
    - How to collaborate with others
    - How to build a website
    ```

3. Click the green **Commit changes...** button.
4. In the box that appears:
    - **Commit message:** `Add introduction to README`
    - Leave **Commit directly to the main branch** selected.
5. Click **Commit changes**.

You made a **commit**. Open the file's **History** again. You now have two entries, and each one is a save point you can return to.

**Screenshot:** The **Commit changes** box with the message filled in.
{ .shot }

### 💬 What makes a good commit message?

Think of it as a short note to your future self.

| Vague | Helpful |
|-------|---------|
| `stuff` | `Add list of learning goals` |
| `fix` | `Fix typo in project title` |
| `update` | `Update README with setup steps` |

A habit worth building: start with a verb, keep it short, and say *what* changed and, if you can, *why*.

## ➕ Add a new file

1. On the repo's main page, click **Add file → Create new file**.
2. Name it `about.md`.
3. Write something about yourself or your goals.
4. Click **Commit changes...** and use the message `Add about page`.

Tip: if you type a name like `notes/ideas.md`, GitHub creates a **folder** called `notes` for you.

## ⬆️ Upload a file

**Add file → Upload files** lets you drag images or documents in from your computer. Add a picture, then commit.

## ✍️ A first taste of Markdown

Files ending in `.md` use **Markdown**: plain text with a few small symbols that GitHub turns into nice formatting. You'll use it in READMEs, issues, pull requests, and comments. Here are the basics to get you going. Chapter 4 teaches the rest.

| You type | You get |
|----------|---------|
| `# Big heading` | A large heading |
| `## Medium heading` | A smaller heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `- item` | a bullet point |
| `1. item` | a numbered list |
| `[text](https://example.com)` | a clickable link |

While you edit on GitHub, click the **Preview** tab to see how your Markdown will look before you commit.

## ⚙️ Understanding repository settings

Open the **Settings** tab on your repo. You don't need to change anything now, but know what lives here:

- **General:** rename or delete the repo, and change whether it's public or private.
- **Collaborators:** invite other people (Chapter 10).
- **Branches:** protect important branches (Chapter 10).
- **Pages:** publish a website (Chapter 13).

> ⚠️ **Careful:** The **Danger Zone** at the bottom of Settings has buttons like **Delete this repository**. GitHub asks you to type the repo's name to confirm, so you can't do it by accident.

## 🛠️ Try it

1. Create `hello-github` with a README.
2. Edit the README and use at least a heading, bold text, and a bullet list.
3. Create `about.md` and add a link to your favorite website.
4. Look at the commit history and click into one commit to see the **diff**. Green lines are additions. Red lines are removals.

## 🧯 Stuck?

- **Name already taken?** Repo names only need to be unique *within your account*. Try another.
- **Markdown looks wrong?** Blank lines matter. Put one before lists and between paragraphs.
- **Can't find the pencil icon?** Open the file first. The edit icon is at the top right of the file view.

## ✅ Checkpoint

- [ ] I created a repository.
- [ ] I made at least two commits in the browser.
- [ ] I can find a file's History and look at a commit's diff.
- [ ] I know a few Markdown tricks.

---

Previous: [Chapter 2](02-account-and-setup.md) · Next: **[Chapter 4: Markdown: Write Like a Pro](04-markdown.md)**
