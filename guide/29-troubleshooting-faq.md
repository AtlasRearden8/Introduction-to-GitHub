# Chapter 29: Troubleshooting & FAQ 🩺

Messages can look intimidating, but they're usually trying to *help*. Read them slowly. They often contain the fix.

> 🧭 **Universal first step:** look at the **Changes** tab and the top-right button in GitHub Desktop. Between them they tell you what's changed, what's saved, and what still needs to go to GitHub.

---

## 🩺 Common problems and fixes

### GitHub Desktop says I'm not signed in, or "Authentication failed"
Your sign-in has expired or was never completed.
**Fix:** Open the settings (**File → Options** on Windows, **GitHub Desktop → Settings** on Mac), go to **Accounts**, click **Sign out**, then **Sign in** again. Your account password doesn't go into GitHub Desktop. It uses your browser to sign in.

### "Unable to find your name" or a message about who you are
GitHub Desktop doesn't know your name and email yet.
**Fix:** Open the settings, go to the **Git** tab, and fill in your **Name** and **Email**. Click **Save**.

### The Commit button is grey
**Fix:** Type a **Summary**, and make sure at least one file has a tick.

### My file isn't showing in Changes
**Fix:** Make sure you **saved** the file in your editor, that it's inside the project folder, and that GitHub Desktop has the right project open (check **Current repository**). If you ignored the file earlier, it won't appear.

### The push was rejected, or GitHub has changes I don't have
GitHub has commits you haven't downloaded.
**Fix:** Click **Fetch origin**, then **Pull origin**, resolve any conflicts, then click **Push origin** again.

### "Merge conflicts" window
Both sides changed the same lines.
**Fix:** Click **Open in** *(your editor)*, choose the final text, delete the `<<<<<<<`, `=======`, and `>>>>>>>` lines, and save. In GitHub Desktop, click **Continue merge**. To back out, click **Abort merge**. See [Chapter 6](06-clone-push-pull.md).

### "Can't switch branches" or asks what to do with my changes
You have unsaved edits.
**Fix:** Choose **Leave my changes on** *(branch)* to put them away safely, or **Bring my changes to** *(branch)* to take them with you. Or commit them first.

### I can't find my repository in the Clone window
**Fix:** Click the refresh icon in the **Clone a Repository** window. Or choose the **URL** tab and paste the web address from the green **Code** button on GitHub.

### The Publish button is missing
The project is already on GitHub. Look for **Push origin** or **Fetch origin** instead.

### I deleted a file by mistake
**Fix:** If you haven't committed yet, right-click it in **Changes** and choose **Discard Changes...** If you have, see [Chapter 12](12-undoing-mistakes.md).

### GitHub rejects a very large file
GitHub doesn't accept files over 100 MB.
**Fix:** Remove the file from the commit (untick it, or undo the commit). Large files, like videos, usually don't belong in a repo.

### "There isn't anything to compare" on a pull request
The branch has no new commits compared with `main`, or both sides are the same branch.
**Fix:** Check you committed on the right branch and clicked **Publish branch** or **Push origin**.

### Everything looks wrong after a merge
**Fix:** If the merge is still in progress, click **Abort merge**. If it's finished, see [Chapter 12](12-undoing-mistakes.md).

## 🖥️ GitHub Desktop problems

### GitHub Desktop won't open, or opens to a blank window
**Fix:** Close it completely and reopen it. Restart your computer. If it still won't start, download the latest version from <https://desktop.github.com> and install it over the top. Your projects stay safe, because they live in your folders and on GitHub.

### "Repository not found" or "Could not find" when I clone or fetch
You may be signed in as the wrong account, the repo may have been renamed or deleted, or it may be private and you don't have access.
**Fix:** Check you're signed in to the right account (settings, **Accounts**). Open the repository's web address in your browser. If it says 404, you don't have access, or the address is wrong.

### "You don't have permission" when I push
You're not a collaborator on that repository, or a branch rule is blocking direct pushes.
**Fix:** Fork the repository and work in your copy (Chapter 10), or ask the owner to add you. If `main` is protected, push to a **branch** and open a pull request.

### The folder already exists when I clone
**Fix:** Choose a different **Local path**, or move or rename the old folder. You can also use **File → Add local repository...** if that folder already is the project.

### The path is too long (Windows)
**Fix:** Clone into a short folder name close to the top of a drive, like `C:\code`, instead of deep inside Documents.

### A file is bigger than 100 MB
GitHub rejects it.
**Fix:** Untick or remove it from the commit. If you've already committed it, click **Undo** (Chapter 12). Keep large videos or datasets elsewhere.

### GitHub Desktop says "no local changes," but I edited a file
**Fix:** Did you save in your editor? Is the file inside the project folder? Is the file ignored (listed in `.gitignore`)? Check **Repository → Repository settings → Ignored files**.

### My changes look huge, with every line changed
This is usually a "line ending" difference between Windows and Mac programs.
**Fix:** Check you didn't accidentally reformat the file in your editor. If it keeps happening on a shared project, ask the maintainers how they'd like it handled.

### I want to move my project folder
**Fix:** Close GitHub Desktop, move the folder, reopen, and use **File → Add local repository...** to point to the new place. Remove the old entry from the list.

### I deleted the folder but GitHub Desktop still lists it
**Fix:** Right-click it in the repository list and choose **Remove**, or clone it again from GitHub.

## 🌐 Website and account problems

### I can't sign in to GitHub
**Fix:** Check your username and email. Use **Forgot password**. If 2FA is the problem, try a saved **recovery code**. See Chapter 16.

### I didn't get a verification email
**Fix:** Check your spam and promotions folders. Make sure the address is spelled right under **Settings → Emails**, and ask GitHub to resend it.

### I'm locked out because I lost my phone
**Fix:** Use a recovery code. If you have none, follow GitHub's account recovery steps. It takes extra proof and patience. Save new codes when you're back in.

### I see "404 Page not found" on github.com
You may be signed out of the right account, the page was renamed or deleted, or it's a private repo that you can't see.
**Fix:** Sign in, check the spelling of the address, and confirm you have access.

### I can't find the setting someone told me about
GitHub moves things around from time to time.
**Fix:** Look for the **name** of the setting in the left column of **Settings**, or use the search box on GitHub Docs.

## 🌍 GitHub Pages problems

### My Pages site shows a 404
**Fix:** Wait two or three minutes. Check **Settings → Pages** for a "Your site is live" banner. Make sure there's an `index.md` or `index.html` in the main folder, and that the repository is **public** (on the free plan).

### My site won't update
**Fix:** Open the **Actions** tab, and look for a red mark on the latest build. Click it to read the error. Then try the changes again.

### My images don't show
**Fix:** Check the file name, folder, and capital letters. `Photo.JPG` is not `photo.jpg`. Make sure you committed and pushed the image.

### The theme didn't apply
**Fix:** Check `_config.yml` for typos (`theme: jekyll-theme-minimal`) and that it's in the main folder.

## 🤖 GitHub Actions problems

### My workflow doesn't start
**Fix:** The file must be in `.github/workflows/` and end in `.yml`. Check that the trigger (`on:`) matches what you did. Open the **Actions** tab to see if there's an error.

### "Invalid workflow file"
**Fix:** Look for indentation (use spaces, never tabs), a missing colon, or quotes that don't close.

### The workflow fails with "Resource not accessible"
**Fix:** Add a `permissions:` block that lets it do what it needs (Chapter 15).

## 🔀 Pull request and issue problems

### I can't merge
**Fix:** Look at the box above the merge button. It lists what's missing: an approval, a passing check, or a conflict to fix.

### The pull request shows files I didn't change
**Fix:** You may have branched from an old `main`. In GitHub Desktop, **Branch → Update from main**, resolve conflicts, and **Push origin**. For a fork, **Sync fork** first.

### I opened the pull request against the wrong branch
**Fix:** On the pull request page, click **Edit** next to the title and change the **base** branch.

### I can't assign someone or add a reviewer
**Fix:** On a personal repository, you can only choose people who are **collaborators**. Invite them first (Chapter 10).

### I can't see the Issues tab
**Fix:** The owner may have turned them off. Look in **Settings → General → Features → Issues**.

### Someone @mentioned me and I don't know what to do
**Fix:** Read the comment. Reply with what you know, or say "I'll look at this on Friday." A friendly reply is always welcome.

## ❓ Frequently asked questions

### Do I need to use the command line?
No. Everything in this guide uses GitHub Desktop and the GitHub website. The command line is an optional extra that some people enjoy later. You can do everything you need without it.

### Is it OK to work directly on `main`?
For solo practice, sure. For anything shared or important, use branches and pull requests. Good habits start early.

### What's the difference between `master` and `main`?
Just the default branch name. `main` is the modern standard. Older repos may use `master`. They work identically.

### Does everything I push become public?
Only if the repo is **public**. Private repos are visible only to you and the people you invite. Double-check the visibility before you push anything sensitive.

### I committed something private. Help!
See [Chapter 12, Situation 11](12-undoing-mistakes.md). The key step is to revoke or replace any password or key immediately.

### What's the difference between Fetch and Pull?
**Fetch** only checks GitHub for news and never changes your files. **Pull** brings the new work down into your files.

### How often should I commit?
Whenever you finish a small, meaningful piece of work. Many small commits beat one giant one.

### Can I delete a repository?
Yes: **Settings → Danger Zone → Delete this repository**. It's permanent, so double-check.

### Can I rename a repository?
Yes: **Settings → General → Repository name**. GitHub redirects old links. In GitHub Desktop, if it complains afterward, choose **Repository → Repository settings...** and update the address under **Remote**.

### Can I undo a merged pull request?
Yes. GitHub shows a **Revert** button on merged pull requests. It opens a new pull request that cancels the first one.

### How do I stop getting so many emails?
Adjust **Settings → Notifications** on GitHub, and **Unwatch** repos you don't need.

### Is GitHub only for programmers?
Not at all. People store writing, research, designs, documentation, data, recipes, and lesson plans there.

### Do I need to be online to work?
You can edit files and **commit** without internet. You need a connection to **fetch**, **pull**, and **push**.

### What's the difference between a repository and a folder?
A repository is a folder that Git is tracking, with its full history stored in a hidden `.git` folder inside it.

### What if I want to leave a project?
You can stop contributing at any time. To stop getting notifications, click **Unwatch** or **Unsubscribe**. To remove your fork, use **Settings → Danger Zone → Delete this repository**.

### How do I change my username?
**Settings → Account → Change username**. Old links to your profile and repositories can break, so think carefully.

### Can I have more than one GitHub account?
You can, but GitHub's terms ask that personal accounts be for one person. Using a second account to **practice** on your own is common and fine.

### Is it okay to make mistakes in public repositories?
Yes. Everyone does. Commit history is part of the story. If something sensitive slips in, see Chapter 12, Situation 11.

### Is GitHub free?
Yes. The Free plan has everything this guide uses. Paid plans add things like more build minutes and extra security features for teams.

### What does GitHub Pages cost?
Nothing on the free plan for public repositories. Only a custom domain costs money, and that's paid to the domain seller.

### How do I back up my work?
Click **Push origin** after each session. GitHub holds a complete copy. You can also copy the project folder to another drive.

### How do I delete my account?
**Settings → Account → Delete account**. It can't be undone, so download anything you want to keep first.

### Which is better, GitHub Desktop or the command line?
Neither is "better." GitHub Desktop is easier to start with and does everything in this guide. The command line offers more power for people who need it later, and your skills carry over.

### Where can I ask for help?
- Search the exact message online. Someone has almost certainly hit it.
- Official GitHub Desktop docs: <https://docs.github.com/en/desktop>
- Official GitHub docs: <https://docs.github.com>
- GitHub Community discussions: <https://github.com/orgs/community/discussions>
- Ask an AI assistant. Describe what you clicked and paste the exact message you saw.

## 🧠 A mindset for when you're stuck

1. **Breathe.** Committed work is very hard to lose.
2. **Read the whole message,** slowly, from top to bottom.
3. **Look at GitHub Desktop** to see where you are: the branch, the Changes tab, and the top-right button.
4. **Don't click buttons you don't understand,** especially anything with the words "force" or "discard."
5. **Search** the message.
6. **Copy your project folder** as a backup before trying risky fixes.
7. **Ask for help.** Everyone has been where you are.

---

Previous: [Chapter 28](28-glossary.md) · Next: **[Chapter 30: Quizzes & Answers](30-quizzes.md)**

## 🎉 You made it

If you've worked through this guide, you've gone from "what is GitHub?" to creating repositories, collaborating through pull requests, tracking work with issues, and recovering from mistakes. That's a real, valuable skill set.

Keep a small project going. Commit something every few days. The buttons will become second nature before you know it.

**Welcome to GitHub. We're glad you're here.**
