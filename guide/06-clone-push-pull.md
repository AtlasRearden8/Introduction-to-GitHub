# Chapter 6: Connecting Your Computer to GitHub 🔗

🎯 **Goals:** Bring GitHub projects to your computer (**clone**), send your work up to GitHub (**push**), and fetch other people's work down (**pull**).

---

## 🔗 The big picture

So far, your computer and GitHub have been separate worlds. Now we connect them:

```
  Your computer ── Push ──►  GitHub
  Your computer ◄── Pull ──  GitHub
  Your computer ◄─ Clone ──  GitHub   (first-time download)
```

You already signed in to GitHub from GitHub Desktop in Chapter 2, so there is no extra login to set up. If you ever see a sign-in error, see "Stuck?" at the end of this chapter.

## 📥 Step 1: Clone a repository

**Cloning** downloads a complete project and its whole history to your computer.

Let's clone the `hello-github` project you made in Chapter 3.

1. In GitHub Desktop, choose **File → Clone repository...**
2. Click the **GitHub.com** tab. You'll see a list of your repositories.
3. Click **hello-github**.
4. Check the **Local path**. This is where the project will be saved on your computer. The default is fine.
5. Click **Clone**.

**Screenshot:** The **Clone a Repository** window with `hello-github` selected.
{ .shot }

When it finishes, the project is open in GitHub Desktop. Click the **History** tab: you'll see all the commits you made in your browser. Cloning also set up the link back to GitHub automatically. GitHub Desktop calls that link **origin**.

### ⚡ A shortcut from the website

On any repository page on github.com, click the green **Code** button and choose **Open with GitHub Desktop**. Your browser hands the project to the app, and it offers to clone it.

## ⬆️ Step 2: Make a change and push it

1. In GitHub Desktop, choose **Repository → Open in Visual Studio Code** (or **Show in Explorer / Finder** and use any text editor).
2. Open `about.md`, add a line such as `Edited from my computer!`, and **save** the file.
3. Back in GitHub Desktop, the change shows up in **Changes**.
4. Write a summary like `Add a line from my computer` and click **Commit to main**.

Notice that the top-right button now says **Push origin**, with a small number or arrow showing you have a commit waiting. Your commit exists only on your computer so far.

5. Click **Push origin**.

Open your repo on github.com and refresh the page. Your change is there. That's the full loop: **edit, commit, push**.

**Screenshot:** The top-right button showing **Push origin** with a small "1" or up arrow.
{ .shot }

## ⬇️ Step 3: Pull changes down

Imagine you (or a teammate) changed something on GitHub directly. Your computer doesn't know yet. Let's try it for real:

1. On github.com, open `README.md` in your repo, click the pencil, add a line, and commit.
2. Back in GitHub Desktop, click the top-right button. It says **Fetch origin**. Click it.
3. GitHub Desktop checks GitHub and notices there's something new. The button now says **Pull origin**. Click it.
4. Open `README.md` on your computer. The change has arrived.

> 🔁 **Habit:** at the start of every work session, click **Fetch origin** (and **Pull origin** if it appears), so you always start from the latest version.

### 🔍 Fetch and Pull: what's the difference?

- **Fetch origin** just *checks* GitHub for news. It doesn't change any of your files, so it's always safe.
- **Pull origin** actually *brings the new work down* into your files.

The same button shows whichever one applies. When there's nothing to do, it says **Fetch origin**.

## 🚀 Step 4: Put an existing project on GitHub

What about the `git-practice` project you made in Chapter 5? It exists only on your computer. To put it on GitHub:

1. In GitHub Desktop, use **Current repository** (top left) to switch to `git-practice`.
2. Click the blue **Publish repository** button at the top right.
3. Keep the **Name** as `git-practice`. Tick **Keep this code private** if you want it private.
4. Click **Publish repository**.

It's now on GitHub at `github.com/YOUR-USERNAME/git-practice`. From now on, it works just like `hello-github`: commit, then **Push origin**.

**Screenshot:** The **Publish Repository** window.
{ .shot }

## 🚫 What if Push is rejected?

Sometimes GitHub Desktop tells you that the push can't go through because GitHub has new commits you don't have yet. The fix is simple:

1. Click **Fetch origin**, then **Pull origin**.
2. Click **Push origin** again.

Pull first (to bring in the missing work), then push.

## 😬 Merge conflicts (they sound worse than they are)

Occasionally a pull (or a merge, in Chapter 7) stops and tells you there are **conflicts**. This happens when you and someone else changed *the very same lines*, and GitHub Desktop can't guess which version to keep. It asks *you* to decide.

You'll see a window listing the **conflicted files**. Here's how to fix them:

1. Click **Open in Visual Studio Code** (or your editor). Desktop opens the file for you.
2. In the file, you'll see markers like this:

    ```
    <<<<<<< HEAD
    My version of the line
    =======
    Their version of the line
    >>>>>>> origin/main
    ```

    The text between `<<<<<<<` and `=======` is **yours**. The text between `=======` and `>>>>>>>` is **theirs**.

3. Decide what the final text should be: yours, theirs, or a blend. **Delete the three marker lines** and whatever you don't want to keep.

    In Visual Studio Code, you can skip the manual editing: above each conflict it shows buttons like **Accept Current Change**, **Accept Incoming Change**, and **Accept Both Changes**. Click the one you want.

4. **Save** the file.
5. Back in GitHub Desktop, the file shows a green tick once the conflict markers are gone. When all files are ticked, click **Continue merge** (or **Commit merge**).

If you'd rather not deal with it right now, click **Abort merge**. Everything goes back to exactly how it was before.

**Screenshot:** The **Resolve conflicts** window in GitHub Desktop, with one conflicted file listed.
{ .shot }

Conflicts are a normal part of teamwork and nothing to fear.

## 🛠️ Try it

1. Clone `hello-github` to your computer.
2. Make a change on your computer, commit it, and click **Push origin**. Confirm it on GitHub.
3. Make a change **on GitHub**, then use **Fetch origin** and **Pull origin** to bring it down.
4. Publish your `git-practice` project to GitHub.
5. **Bonus:** use **Open with GitHub Desktop** from a repo page on github.com.

## 🧯 Stuck?

| Problem | Likely fix |
|---------|-----------|
| **Authentication failed** or a sign-in prompt keeps appearing | Open the settings (**File → Options** on Windows, **GitHub Desktop → Settings** on Mac), go to **Accounts**, click **Sign out**, then **Sign in** again. |
| The **Push origin** button doesn't appear | You haven't committed anything yet, or everything is already pushed. Check the **History** tab. |
| **Publish repository** is missing | The project is already on GitHub. Look for **Push origin** or **Fetch origin** instead. |
| The repo isn't in the clone list | Click the refresh icon in the **Clone a Repository** window, or choose the **URL** tab and paste the address from the green **Code** button. |
| The push was rejected | **Fetch origin**, **Pull origin**, then **Push origin** again. |

## ✅ Checkpoint

- [ ] I can clone a repo from GitHub.
- [ ] I can commit and **Push origin**.
- [ ] I can **Fetch origin** and **Pull origin**.
- [ ] I know what "origin" means.
- [ ] I'm not afraid of the word "conflict."

---

Previous: [Chapter 5](05-github-desktop.md) · Next: **[Chapter 7: Branches & Merging](07-branches-and-merging.md)**
