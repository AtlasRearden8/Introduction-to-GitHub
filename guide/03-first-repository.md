# Chapter 3: Your First Repository 📁

🎯 **Goals:** Create a repository on GitHub, edit a file in your browser, make your first commit, and learn Markdown, the simple formatting language you'll use everywhere on GitHub.

No terminal needed in this chapter. Just your browser.

---

## Create the repository

1. Click the **➕** icon (top right) → **New repository**.
2. Fill in:
   - **Repository name:** `hello-github`
   - **Description:** `My very first repository`
   - **Public** or **Private:** Either works. Public means anyone can see it. Private means only you (and people you invite). For practice, **Private** is a fine choice.
   - ✅ **Add a README file**
3. Leave the other options alone for now.
4. Click **Create repository**.

🎉 **You just made a repository.** Take a moment. That's a real milestone.

## Tour of what you made

You'll see:
- A file called **README.md**. The "front door" of every project. GitHub displays it automatically below the file list.
- A branch picker labeled **main**.
- A **commit** count (currently 1: the initial commit that created the README).

Click **README.md**, then click the **History** (clock) icon. You'll see your first commit. Click it to see exactly what changed. This is the time machine already at work.

## Edit a file in your browser (and make a commit!)

1. Open **README.md** and click the **✏️ pencil** (Edit) icon.
2. Add a few lines:

   ```markdown
   # Hello, GitHub!

   My name is **Your Name**, and this is my first repository.

   ## Things I want to learn
   - How Git works
   - How to collaborate with others
   - How to build a website
   ```

3. Click **Commit changes…** (green button).
4. In the box that appears:
   - **Commit message:** `Add introduction to README`
   - Keep **Commit directly to the main branch** selected.
5. Click **Commit changes**.

You made a **commit**. Visit the file's **History** again. You now have two entries, each a save point you can return to.

### What makes a good commit message?

Think of it as a short note to your future self.

| ❌ Vague | ✅ Helpful |
|---------|-----------|
| `stuff` | `Add list of learning goals` |
| `fix` | `Fix typo in project title` |
| `update` | `Update README with setup steps` |

Habit worth building: start with a verb, keep it under ~50 characters, say *what* and ideally *why*.

## Add a new file

1. On the repo's main page click **Add file → Create new file**.
2. Name it `about.md`.
3. Write something about yourself or your goals.
4. Commit with the message `Add about page`.

Tip: if you type a name like `notes/ideas.md`, GitHub creates a **folder** called `notes` for you.

## Upload a file

**Add file → Upload files** lets you drag images or documents from your computer. Add a picture, then commit.

## Learn Markdown ✍️

Files ending in `.md` use **Markdown**: plain text with tiny symbols that GitHub turns into nice formatting. You'll use it in READMEs, issues, pull requests, and comments.

### The essentials

| You type | You get |
|----------|---------|
| `# Big heading` | A large heading |
| `## Medium heading` | A smaller heading |
| `### Small heading` | Smaller still |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `~~strikethrough~~` | ~~strikethrough~~ |
| `- item` or `* item` | • a bullet point |
| `1. item` | a numbered list |
| `[text](https://example.com)` | a clickable link |
| `![description](image.png)` | an image |
| `` `code` `` | `inline code` |
| `> quote` | a quoted block |
| `---` | a horizontal line |

### Code blocks

Wrap code in three backticks. Add the language name for colors:

````markdown
```python
print("Hello!")
```
````

### Task lists (great on GitHub)

```markdown
- [x] Create my account
- [x] Make my first repo
- [ ] Learn branches
```

Renders as checkboxes you can tick in issues and pull requests.

### Tables

```markdown
| Name  | Role     |
|-------|----------|
| Ana   | Designer |
| Ben   | Writer   |
```

### Emoji

Type `:tada:` to get 🎉 or `:rocket:` to get 🚀.

### Preview before you save

While editing on GitHub, click the **Preview** tab to see how your Markdown will look before committing.

## Understanding repository settings (a quick look)

Open the **Settings** tab on your repo. You don't need to change anything now, but know what lives here:

- **General:** rename or delete the repo, change visibility (public/private).
- **Collaborators:** invite others (Chapter 9).
- **Branches:** protect important branches (Chapter 9).
- **Pages:** publish a website (Chapter 11).

> ⚠️ The **Danger Zone** at the bottom of Settings has buttons like *Delete this repository*. GitHub asks you to type the repo's name to confirm, so you can't do it by accident.

## 🛠️ Try it

1. Create `hello-github` with a README.
2. Edit the README and use at least a heading, bold text, and a bullet list.
3. Create `about.md` and add a link to your favorite website.
4. Look at the commit history and click into one commit to see the "diff": green lines are additions, red lines are removals.

## 🧯 Stuck?

- **Name already taken?** Repo names only need to be unique *within your account*. Try another.
- **Markdown looks wrong?** Blank lines matter. Put one before lists and between paragraphs.
- **Can't find the pencil icon?** Open the file first; the edit icon is at the top right of the file view.

## ✅ Checkpoint

- [ ] I created a repository.
- [ ] I made at least two commits through the browser.
- [ ] I can find a file's History and view a commit's diff.
- [ ] I know a few Markdown tricks.

---

⬅️ Previous: [Chapter 2](02-account-and-setup.md) · ➡️ Next: **[Chapter 4: Git on Your Own Computer](04-git-basics.md)**
