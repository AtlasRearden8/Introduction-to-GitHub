# Chapter 11: Level-Ups 🎮

🎯 **Goals:** Get a taste of GitHub's most exciting extras: publishing a free website, a profile README, automation with Actions, coding in the cloud, and keeping your projects secure. Each section stands alone. Pick what excites you.

---

## 1. GitHub Pages: a free website in minutes 🌐

**GitHub Pages** turns a repository into a live website at no cost.

### Publish a simple site

1. Create a new **public** repo called `my-first-site` (with a README).
2. **Add file → Create new file**, name it `index.html`, and paste:

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>My First Site</title>
     </head>
     <body>
       <h1>Hello, world! 👋</h1>
       <p>This website is hosted on GitHub.</p>
     </body>
   </html>
   ```

3. Commit it.
4. Go to **Settings → Pages**.
5. Under **Build and deployment → Source**, choose **Deploy from a branch**, select branch **main** and folder **/ (root)**, then **Save**.
6. Wait a minute or two, then refresh. GitHub shows your site's address, usually `https://YOUR-USERNAME.github.io/my-first-site/`.

You're a web publisher now! Edit `index.html`, commit, and the live site updates.

### A personal site at your root address
A repo named exactly `YOUR-USERNAME.github.io` publishes to `https://YOUR-USERNAME.github.io/`.

### No HTML? No problem
Pages can also build Markdown into a site using **Jekyll** (built in). Many people use Pages for portfolios, documentation, blogs, and event pages.

> Note: Pages availability for *private* repos depends on your plan. Public repos work on Free.

## 2. Your profile README ✨

GitHub has a hidden trick: create a **public** repo whose name is **exactly your username**, add a `README.md`, and its contents appear at the top of your profile page.

1. Create a new public repo named `YOUR-USERNAME` (GitHub will show a "✨ special repository" notice).
2. Initialize it with a README.
3. Edit it: introduce yourself, list interests, link to projects.

Example ideas: a short bio, what you're learning, how to reach you, a few favorite projects.

## 3. GitHub Actions: automation 🤖

**Actions** run tasks automatically when something happens in your repo: tests on every pull request, a website build on every push, a weekly reminder.

Workflows are small text files in `.github/workflows/`, written in YAML.

### A tiny example

Create `.github/workflows/hello.yml`:

```yaml
name: Say Hello

on:
  push:
    branches: [main]

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Print a greeting
        run: echo "Hello from GitHub Actions! 🎉"
```

Commit and push it. Open the **Actions** tab. You'll see the workflow running (a yellow dot, then a green ✅). Click into it to read the output.

**Reading the file:**
- `on:` is the trigger (here, pushes to `main`).
- `jobs:` are groups of work; each runs on a fresh virtual computer (`runs-on`).
- `steps:` are the individual tasks, in order.

You can find ready-made workflows via **Actions → New workflow**. Public repos get generous free usage; private repos have a monthly free allowance.

## 4. Codespaces and `github.dev`: coding in the browser ☁️

- **github.dev**: on any repo page, press the `.` (period) key. A lightweight VS Code editor opens in your browser, which is great for quick edits with nothing to install.
- **Codespaces**: a full cloud development computer for your repo (**<> Code → Codespaces → Create codespace**). Includes a terminal where you can run Git commands and code. Free accounts receive a monthly allowance of usage, so check your current limits in Settings.

Handy if you can't install software (say, on a school or library computer).

## 5. Keeping things secure 🔒

Good habits protect you and your work:

- **Use 2FA** (you already did!).
- **Never commit secrets** (passwords, API keys, tokens). Use `.gitignore` for files like `.env`.
- **Review what you stage:** `git status` and `git diff --staged` before committing.
- **Dependabot** (under **Settings → Code security**) can alert you about known vulnerabilities in the libraries your project uses and can propose updates.
- **Secret scanning** can warn you when a recognized key is accidentally pushed (availability depends on repo type).
- **Be careful with public repos:** anything you push is visible to the world, including history.
- Be wary of **unexpected links, emails, and requests** claiming to be from GitHub; check the address and when in doubt go to github.com directly.

## 6. Releases and tags 🏷️

A **tag** marks a specific commit, like "version 1.0." A **release** wraps a tag with notes and downloadable files.

```bash
git tag v1.0.0
git push origin v1.0.0
```

Then on GitHub: **Releases → Draft a new release**, choose the tag, write notes, publish.

## 7. Gists: share snippets 📝

A **gist** (<https://gist.github.com>) is a mini-repo for sharing a single snippet or note, public or secret-link. Handy for sharing code to ask for help.

## 8. Keyboard shortcuts ⌨️

On any GitHub page, press `?` to see shortcuts. Favorites:

| Key | Does |
|-----|------|
| `/` | Focus search |
| `t` | File finder in a repo |
| `.` | Open github.dev editor |
| `g` then `i` | Go to Issues |
| `g` then `p` | Go to Pull requests |

## 9. Where to go next 🧭

- **GitHub Skills** (<https://skills.github.com>): free, interactive courses that run inside real repos.
- **GitHub Docs** (<https://docs.github.com>): the official reference.
- **Pro Git book** (<https://git-scm.com/book>): free, deep, and excellent.
- **Learn more Git:** `rebase`, `cherry-pick`, `bisect`, hooks, submodules, when you're curious.
- **Build something:** the best learning is a real project you care about.

## 🛠️ Try it

Choose at least **two**:

1. Publish `my-first-site` with GitHub Pages.
2. Create your profile README.
3. Add the hello-world Action and watch it run.
4. Press `.` on a repo to open github.dev and make an edit.

## ✅ Checkpoint

- [ ] I published something to the web (or know exactly how to).
- [ ] I know what Actions do and where workflows live.
- [ ] I have good security habits.

---

⬅️ Previous: [Chapter 10](10-undoing-mistakes.md) · ➡️ Next: **[Chapter 12: Cheat Sheet](12-cheat-sheet.md)**
