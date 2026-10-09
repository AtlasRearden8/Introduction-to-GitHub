# Chapter 2: Create Your Account & Get Set Up 🛠️

🎯 **Goals:** Create a GitHub account, secure it, tour the interface, and install Git on your computer.

---

## Part A: Create your GitHub account

1. Go to <https://github.com> and click **Sign up**.
2. Enter your **email**, a strong **password**, and a **username**.
3. Complete the verification puzzle and confirm your email when GitHub sends you a code.

### Choosing a username

Your username appears in your profile URL (`github.com/yourname`) and on everything you do. Tips:

- Pick something you'd be comfortable putting on a résumé.
- Keep it short and easy to spell.
- Lowercase letters, numbers, and hyphens are allowed.
- You *can* change it later, but links to your old name will break, so choose thoughtfully.

### The free plan is plenty

GitHub's **Free** plan includes unlimited public and private repositories and everything in this guide. You never need to upgrade to learn.

## Part B: Secure your account 🔐

GitHub requires **two-factor authentication (2FA)** for people who contribute code, so set it up now.

1. Click your **profile picture** (top right) → **Settings**.
2. Choose **Password and authentication**.
3. Under **Two-factor authentication**, click **Enable** and follow the steps. An authenticator app on your phone, a security key, or a passkey all work.
4. **Save your recovery codes** somewhere safe (a password manager, or printed and stored securely). If you lose your phone, these are your way back in.

> 💬 This feels like a chore, but it protects all the work you're about to do.

## Part C: Take a tour of GitHub

After signing in, spend five minutes just looking around.

| Where | What's there |
|-------|--------------|
| **Top-left logo / Dashboard** | Your home feed, with activity from projects you follow |
| **Search bar (top)** | Find repositories, people, code, and issues across GitHub |
| **➕ icon (top right)** | Create a new repository, import, and more |
| **Bell icon** | Notifications |
| **Profile picture** | Your profile, repositories, settings, sign out |

**Explore** a public project to see what a repository page looks like. Try <https://github.com/github/docs> or search for something you love ("recipes," "chess," "photography").

Anatomy of a repository page:

```
┌─────────────────────────────────────────────────────────────────┐
│ owner / repo-name                        ⭐ Star   🍴 Fork     │
├─────────────────────────────────────────────────────────────────┤
│ <> Code | Issues | Pull requests | Actions | Projects | ...     │  ← tabs
├─────────────────────────────────────────────────────────────────┤
│ [main ▾]   file list (folders & files)          [<> Code ▾]     │
│                                                                 │
│ README.md rendered below the files — the project's front door   │
└─────────────────────────────────────────────────────────────────┘
```

- **Code**: the files.
- **Issues**: tasks, bugs, ideas.
- **Pull requests**: proposed changes.
- **Actions**: automation (Chapter 11).
- **⭐ Star**: bookmarks a repo and says "nice work" to its author.

## Part D: Set up your profile (optional but fun)

In **Settings → Public profile** you can add a photo, name, and short bio. Nothing is required. Share only what you're comfortable with.

## Part E: Install Git on your computer

Git runs locally, so you install it separately from your GitHub account.

### First, check if you already have it

Open a terminal (see [Chapter 0](00-start-here.md)) and type:

```bash
git --version
```

If you see something like `git version 2.43.0`, you already have it. Skip to Part F. If you see "command not found," install it:

### Windows
1. Download **Git for Windows** from <https://git-scm.com/download/win>.
2. Run the installer. **The default options are fine**: keep clicking **Next**, then **Install**.
3. When it finishes, search the Start menu for **Git Bash**. That's your terminal.

### Mac
1. Open Terminal and run `git --version`.
2. If Git isn't installed, macOS offers to install the **Command Line Tools**. Click **Install** and wait.
3. Alternative: install [Homebrew](https://brew.sh), then run `brew install git`.

### Linux
- Debian / Ubuntu: `sudo apt update && sudo apt install git`
- Fedora: `sudo dnf install git`
- Arch: `sudo pacman -S git`

Then verify:

```bash
git --version
```

## Part F: Tell Git who you are

Every commit you make is stamped with a name and email. Set them once:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

> 🔒 **Privacy tip:** Commits are public in public repos. If you'd rather not expose your real email, GitHub offers a private "noreply" address. Find it under **Settings → Emails**, and check **"Keep my email addresses private."** Use the `...@users.noreply.github.com` address shown there in the command above.

Also set the default branch name to `main`, matching GitHub:

```bash
git config --global init.defaultBranch main
```

Check your settings any time:

```bash
git config --list
```

## Part G: Choose an editor

You'll need something to edit files. Options:

- **Visual Studio Code** (free, popular, beginner-friendly): <https://code.visualstudio.com>
- **Notepad++** (Windows), **TextEdit in plain-text mode** (Mac), or any plain-text editor.
- **Not** a word processor like Microsoft Word. Those add hidden formatting that Git can't compare well.

Optionally tell Git to use VS Code for commit messages:

```bash
git config --global core.editor "code --wait"
```

## 🛠️ Try it

1. Create your account and enable 2FA.
2. Star one repository that interests you ⭐.
3. Install Git and run `git --version`.
4. Run the two `git config` commands with your own details, then `git config --list` to confirm.

## 🧯 Stuck?

- **"git: command not found" after installing:** Close the terminal and open a fresh one.
- **Didn't get the email code:** Check spam, then use "resend" on GitHub.
- **Locked out of 2FA:** Use a saved recovery code. This is why you saved them!

## ✅ Checkpoint

- [ ] I can log in to GitHub.
- [ ] 2FA is on and recovery codes are saved.
- [ ] `git --version` works.
- [ ] `git config --list` shows my name and email.

---

⬅️ Previous: [Chapter 1](01-what-are-git-and-github.md) · ➡️ Next: **[Chapter 3: Your First Repository](03-first-repository.md)**
