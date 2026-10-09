# Chapter 2: Create Your Account & Get Set Up 🛠️

🎯 **Goals:** Create a GitHub account, secure it, take a tour of the website, and install GitHub Desktop on your computer.

---

## 🆕 Part A: Create your GitHub account

1. Go to <https://github.com> and click **Sign up**.
2. Enter your **email**, a strong **password**, and a **username**.
3. Complete the verification puzzle, and confirm your email when GitHub sends you a code.

**Screenshot:** The GitHub sign-up page with the email, password, and username boxes.
{ .shot }

### 🏷️ Choosing a username

Your username appears in your profile address (`github.com/yourname`) and on everything you do. Tips:

- Pick something you'd be comfortable putting on a résumé.
- Keep it short and easy to spell.
- Lowercase letters, numbers, and hyphens are allowed.
- You *can* change it later, but links to your old name will break, so choose carefully.

### 🎁 The free plan is plenty

GitHub's **Free** plan includes unlimited public and private repositories and everything in this guide. You never need to upgrade to learn.

## 🔐 Part B: Secure your account

GitHub requires **two-factor authentication (2FA)** for people who contribute code, so set it up now. 2FA means signing in takes your password *and* a second proof that it's really you, like a code from your phone.

1. Click your **profile picture** (top right), then **Settings**.
2. Choose **Password and authentication**.
3. Under **Two-factor authentication**, click **Enable** and follow the steps. An authenticator app on your phone, a security key, or a passkey all work.
4. **Save your recovery codes** somewhere safe, such as a password manager, or printed and stored securely. If you lose your phone, these are your way back in.

> This feels like a chore, but it protects all the work you're about to do.

## 🧭 Part C: Take a tour of GitHub

After you sign in, spend five minutes just looking around.

| Where | What's there |
|-------|--------------|
| **Top-left logo or Dashboard** | Your home feed, with activity from projects you follow |
| **Search bar (top)** | Find repositories, people, code, and issues across GitHub |
| **+ icon (top right)** | Create a new repository, and more |
| **Bell icon** | Notifications |
| **Profile picture** | Your profile, repositories, settings, and sign out |

Explore a public project to see what a repository page looks like. Try <https://github.com/github/docs>, or search for something you love ("recipes," "chess," "photography").

Here is the layout of a repository page:

```
┌─────────────────────────────────────────────────────────────────┐
│ owner / repo-name                        Star      Fork         │
├─────────────────────────────────────────────────────────────────┤
│ Code | Issues | Pull requests | Actions | Projects | ...        │  ← tabs
├─────────────────────────────────────────────────────────────────┤
│ [main ▾]   file list (folders and files)          [Code ▾]      │
│                                                                 │
│ README.md shown below the files: the project's front door       │
└─────────────────────────────────────────────────────────────────┘
```

- **Code:** the files.
- **Issues:** tasks, bugs, and ideas.
- **Pull requests:** proposed changes.
- **Actions:** automation (Chapter 15).
- **Star:** bookmarks a repo and tells its author "nice work."

**Screenshot:** A real repository page with the tabs, file list, and green **Code** button labeled.
{ .shot }

## ✨ Part D: Set up your profile (optional)

In **Settings → Public profile** you can add a photo, name, and short bio. Nothing is required. Share only what you're comfortable with.

## 💻 Part E: Install GitHub Desktop

GitHub Desktop is a free app from GitHub. It lets you work with your projects on your own computer by clicking buttons. It includes everything it needs, so there is nothing else to download.

1. Go to <https://desktop.github.com> and click **Download**.
2. Open the file you downloaded and let it install. The default options are fine.
3. Launch **GitHub Desktop**.

> 🐧 **On Linux?** GitHub doesn't make an official Desktop app for Linux. You can still follow every website step in this guide. For the Desktop parts, look for a community-built version, or work in the browser until you're comfortable.

**Screenshot:** The GitHub Desktop welcome screen with the **Sign in to GitHub.com** button.
{ .shot }

## 🔑 Part F: Sign in and tell GitHub Desktop who you are

1. On the welcome screen, click **Sign in to GitHub.com**.
2. Your web browser opens. Sign in to GitHub if asked, then click **Authorize desktop**.
3. Your browser asks to open GitHub Desktop. Click **Open**.
4. GitHub Desktop shows a **Configure Git** screen. It fills in your **name** and **email** from your account. Check that they look right, then click **Finish**.

Every snapshot you save (a *commit*) is stamped with this name and email.

> 🔒 **Privacy tip:** Commits in public repositories are public. If you'd rather not show your real email, GitHub offers a private "noreply" address. On github.com, go to **Settings → Emails** and tick **Keep my email addresses private**. Copy the `...@users.noreply.github.com` address shown there. Then in GitHub Desktop, open the settings and go to the **Git** tab:
>
> - **Windows:** **File → Options**
> - **Mac:** **GitHub Desktop → Settings**
>
> Paste the address into the **Email** box and click **Save**.

### 🌳 Set the default branch name

In the same settings window, on the **Git** tab, set **Default branch name for new repositories** to **main**. This matches GitHub and keeps things simple later.

## ✏️ Part G: Choose an editor

You'll need something to edit files. Good options:

- **Visual Studio Code** (free, popular, beginner-friendly): <https://code.visualstudio.com>
- **Notepad++** (Windows), **TextEdit in plain-text mode** (Mac), or any plain-text editor.
- **Not** a word processor like Microsoft Word. Those add hidden formatting that makes it hard to see what changed.

If you install Visual Studio Code, GitHub Desktop can open your projects in it with one click. In the settings, open the **Integrations** tab and choose your editor under **External editor**.

## 🛠️ Try it

1. Create your account and turn on 2FA.
2. Star one repository that interests you.
3. Install GitHub Desktop and sign in.
4. Open the settings, go to the **Git** tab, and check that your name and email are correct.

## 🧯 Stuck?

- **GitHub Desktop doesn't open after you click Authorize:** Go back to the app and click **Sign in to GitHub.com** again. If your browser asks permission to open GitHub Desktop, choose **Open**.
- **Didn't get the email code:** Check your spam folder, then use "resend" on GitHub.
- **Locked out of 2FA:** Use a saved recovery code. This is why you saved them.

## ✅ Checkpoint

- [ ] I can sign in to GitHub.
- [ ] 2FA is on and my recovery codes are saved.
- [ ] GitHub Desktop is installed and I'm signed in.
- [ ] My name and email look right in the Git settings.

---

Previous: [Chapter 1](01-what-are-git-and-github.md) · Next: **[Chapter 3: Your First Repository](03-first-repository.md)**
