# Chapter 5: Connecting Your Computer to GitHub 🔗

🎯 **Goals:** Bring GitHub projects to your computer (`clone`), send your work up (`push`), fetch others' work down (`pull`), and log in securely.

---

## The big picture

Until now, your computer's Git and GitHub were separate worlds. Now we connect them:

```
  Your computer ── git push ──►  GitHub
  Your computer ◄── git pull ──  GitHub
  Your computer ◄─ git clone ──  GitHub   (first-time download)
```

## Step 1: Choose how to log in

When your computer talks to GitHub, GitHub must know it's really you. **Your account password does not work for this.** There are three good options. Pick **one**.

### Option A: GitHub CLI (easiest for beginners) ⭐

The GitHub CLI (`gh`) is a helper tool that handles login for you.

1. Install it from <https://cli.github.com> (or `brew install gh` on Mac, `winget install GitHub.cli` on Windows).
2. Run:

   ```bash
   gh auth login
   ```

3. Choose **GitHub.com → HTTPS → Yes (authenticate Git with your credentials) → Login with a web browser**.
4. Copy the one-time code shown, press Enter, paste it in the browser page, and authorize.

Check it worked:

```bash
gh auth status
```

### Option B: Git Credential Manager (Windows & Mac)

Git for Windows includes this by default. The first time you push or clone a private repo over HTTPS, a browser window pops up asking you to sign in. Do that once, and it remembers you.

### Option C: SSH keys (popular, slightly more setup)

SSH uses a secret "key" file on your computer plus a matching public key on GitHub.

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

Press Enter to accept the defaults (setting a passphrase is a good idea). Then copy the **public** key (the file ending in `.pub`):

```bash
cat ~/.ssh/id_ed25519.pub
```

On GitHub: **Settings → SSH and GPG keys → New SSH key**, paste it, save. Test with:

```bash
ssh -T git@github.com
```

You should see a greeting with your username. 🎉

> **HTTPS vs. SSH URLs:** Each repo offers two clone addresses: one starting `https://github.com/...` and one starting `git@github.com:...`. Use whichever matches how you logged in (A and B → HTTPS; C → SSH).

## Step 2: Clone a repository

**Cloning** downloads the complete project and its whole history.

1. Go to the `hello-github` repo you made in Chapter 3.
2. Click the green **<> Code** button, and copy the URL (HTTPS or SSH).
3. In your terminal, go to where you keep projects:

   ```bash
   cd ~
   ```

4. Clone it:

   ```bash
   git clone https://github.com/YOUR-USERNAME/hello-github.git
   ```

5. Step inside:

   ```bash
   cd hello-github
   ls
   git log --oneline
   ```

You'll see your README and all the commits you made in the browser. Cloning also set up the link back to GitHub automatically; that link is called **origin**:

```bash
git remote -v
```

## Step 3: Make a change and push it

```bash
echo "Edited from my computer!" >> about.md
git status
git add about.md
git commit -m "Add a line from my computer"
git push
```

Refresh the repo on GitHub, and your change is there. That's the full loop: **edit → add → commit → push**.

## Step 4: Pull changes down

Imagine you (or a teammate) edited something on GitHub directly. Your computer doesn't know yet. To fetch it:

```bash
git pull
```

**Try it for real:** edit `README.md` in the GitHub browser editor and commit. Then in your terminal run `git pull` and look at the file. The change has arrived.

> **Habit:** run `git pull` at the start of every work session so you start from the latest version.

### `fetch` vs. `pull` (optional but useful)

- `git fetch` downloads new commits but **does not** change your files, which is a safe peek.
- `git pull` = `fetch` + merge into your current branch.

## Step 5: Connect an *existing* local project to GitHub

What about the `git-practice` folder from Chapter 4? It exists only on your computer. To publish it:

1. On GitHub, create a **new, empty** repository named `git-practice`. **Do not** tick "Add a README," because an empty repo avoids conflicts.
2. GitHub then shows setup instructions. In your `git-practice` folder, run:

   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/git-practice.git
   git branch -M main
   git push -u origin main
   ```

What those do:
- `git remote add origin URL`: "My GitHub copy is called `origin` and lives at this address."
- `git branch -M main`: makes sure your branch is named `main`.
- `git push -u origin main`: sends your commits up. The `-u` remembers the connection so later you can type just `git push` and `git pull`.

*(If you installed the GitHub CLI, there's a one-liner alternative: `gh repo create git-practice --private --source=. --push`.)*

## What if push is rejected?

If you see an error like `! [rejected] ... (fetch first)`, it means GitHub has commits you don't have yet. The fix is simple:

```bash
git pull
git push
```

Pull first (to bring in the missing commits), then push.

## Merge conflicts 😬 (they sound worse than they are)

Occasionally `git pull` stops and says **CONFLICT**. That happens when you and someone else edited *the same lines* and Git can't guess which version to keep. It asks *you* to decide. Git marks the file like this:

```
<<<<<<< HEAD
My version of the line
=======
Their version of the line
>>>>>>> origin/main
```

To resolve:

1. Open the file in your editor.
2. Decide what the final text should be (mine, theirs, or a blend).
3. Delete the three marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) and the version you don't want.
4. Save, then:

   ```bash
   git add the-file.txt
   git commit -m "Resolve merge conflict"
   ```

VS Code highlights conflicts and offers "Accept Current / Incoming / Both" buttons, which are a friendly shortcut. Conflicts are a normal part of teamwork and nothing to fear.

## 🛠️ Try it

1. Set up login with one of the three options.
2. Clone `hello-github` to your computer.
3. Make a change locally, commit, and push. Confirm it on GitHub.
4. Make a change **on GitHub**, then `git pull` it down.
5. Publish your `git-practice` project to GitHub.

## 🧯 Stuck?

| Problem | Likely fix |
|---------|-----------|
| `Authentication failed` / `password authentication is not supported` | You typed your account password. Use one of the login options above instead. |
| `Permission denied (publickey)` | SSH key isn't added to GitHub, or you cloned the HTTPS URL while expecting SSH (or vice versa). Check `git remote -v`. |
| `fatal: not a git repository` | `cd` into the project folder first. |
| `remote origin already exists` | Run `git remote -v` to see it. Change it with `git remote set-url origin NEW-URL`. |
| `src refspec main does not match any` | You have no commits yet, or your branch is named differently. Make a commit, then check with `git branch`. |

## ✅ Checkpoint

- [ ] I can log in from my computer.
- [ ] I can `clone`, `push`, and `pull`.
- [ ] I know what `origin` means.
- [ ] I'm not afraid of the word "conflict."

---

⬅️ Previous: [Chapter 4](04-git-basics.md) · ➡️ Next: **[Chapter 6: Branches & Merging](06-branches-and-merging.md)**
