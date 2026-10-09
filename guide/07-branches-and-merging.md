# Chapter 7: Branches & Merging 🌿

🎯 **Goals:** Understand why branches exist, create and switch between them in GitHub Desktop, and merge them together. This is the superpower that makes confident experimenting possible.

---

## 💡 The idea

Imagine your project is a story and `main` is the polished, published version. You want to try rewriting the ending. You wouldn't scribble on the published copy. You'd make a **photocopy**, experiment there, and swap it in only if you love it.

A **branch** is that photocopy, except it's free and instant.

```
main:        A───B───C───────────────G   ← safe, stable version
                      \             /
my-idea:               D───E───F──┘      ← experiments live here, then merge back
```

Each letter is a commit. The branch `my-idea` split off at C, got its own commits (D, E, F), and was then **merged** into `main` as G.

**Why branches are wonderful:**

- `main` stays clean and working.
- You can work on several ideas at the same time.
- If an experiment fails, delete the branch. No harm done.
- On GitHub, branches are how pull requests (Chapter 8) work.

## 🧭 The Current Branch menu

Everything about branches in GitHub Desktop starts at the top bar, at the button labeled **Current branch**. It shows which branch you're on right now (usually `main`). Click it to see a list of your branches, a **New Branch** button, and a search box.

Work inside any project, such as your `hello-github` clone.

**Screenshot:** The **Current branch** menu open, showing `main`, a **New Branch** button, and a search box.
{ .shot }

## 🌱 Create a branch

1. Click **Current branch** (top middle).
2. Click **New Branch**.
3. Type a name, such as `add-recipes`.
4. Make sure it says it will be based on **main**, then click **Create branch**.

Naming tips: keep it short, lowercase, with hyphens, and say what the work is. Good examples are `fix-typo`, `add-contact-page`, and `update-readme`.

The top bar now says **Current branch: add-recipes**. Any commit you make now goes on this branch, and `main` is untouched.

## 💾 Make a commit on the branch

1. Create a new file in your project folder called `recipes.md` with a line like `# Pancakes`, and save it.
2. In GitHub Desktop, tick the file in **Changes**, write a summary (`Add pancake recipe`), and click **Commit to add-recipes**.

Notice the commit button now names your branch instead of `main`.

## 🔄 Switch back to main and see the difference

1. Click **Current branch**, then choose **main**.
2. Open your project folder. **`recipes.md` has vanished.**

It's not lost. It lives on your other branch. Switch back and it returns:

1. Click **Current branch**, then choose **add-recipes**.
2. `recipes.md` is back in the folder.

This feels like magic the first time. GitHub Desktop is swapping your files to match whichever branch you're on.

### 🧳 If you have unsaved changes when you switch

If you've edited files but haven't committed them, GitHub Desktop asks what to do with them:

- **Leave my changes on add-recipes:** your edits are put away safely and come back when you return to that branch.
- **Bring my changes to main:** your edits come along with you to the other branch.

Either choice is safe. "Leave my changes" is the right one most of the time.

## 🔀 Merge a branch

Once you're happy with the work on `add-recipes`, bring it into `main`:

1. Switch to the branch that should **receive** the work: click **Current branch** and choose **main**.
2. In the menu bar, choose **Branch → Merge into current branch...**
3. Choose **add-recipes** from the list. GitHub Desktop tells you how many commits will be brought in.
4. Click **Create a merge commit** (the button names the branches involved).

**Rule of thumb:** first stand on the branch that is *receiving*, then choose the branch that is *giving*.

Open your project folder. `recipes.md` is now on `main`. Click **History** to see the merge.

**Screenshot:** The **Merge into current branch** window with `add-recipes` selected.
{ .shot }

### 🧹 Clean up

After merging, the branch has done its job. To delete it:

1. Switch to a different branch (such as `main`).
2. Choose **Branch → Delete...**, pick or confirm the branch, and confirm.

Deleting a merged branch loses nothing. Its commits are now part of `main`.

## ✌️ Two kinds of merge (so the messages make sense)

- **Fast-forward:** `main` hasn't moved since you branched, so it simply slides forward. No extra commit.
- **Merge commit:** both branches have new work, so a special commit joins them.

You don't need to choose. GitHub Desktop picks the right one.

## 😬 Merge conflicts, revisited

If two branches changed the *same lines*, you'll get a conflict window, just like in Chapter 6. Open the file in your editor, choose the final text, delete the `<<<<<<<` marker lines, save, and click **Continue merge**. You can always click **Abort merge** to back out.

## ☁️ Branches and GitHub

A branch you create in GitHub Desktop is only on your computer until you send it up.

1. With your branch selected, click **Publish branch** (top right). This appears instead of **Push origin** the first time.
2. Open your repo on github.com. A yellow banner appears: **Compare & pull request**. That's the doorway into Chapter 8.

To see all the branches on GitHub, open the **branch menu** (labeled `main` with a small arrow) on the repo page and look through the list.

### 📥 Download a teammate's branch

1. Click **Fetch origin** so GitHub Desktop learns about new branches.
2. Click **Current branch** and look for the branch name in the list (use the search box).
3. Click it. GitHub Desktop downloads it and switches to it.

### 🗑️ Delete a branch on GitHub

GitHub shows a **Delete branch** button after you merge a pull request. You can also delete branches on the repo's **Branches** page (open the branch menu and click **View all branches**).

## 🔃 Keep your branch up to date with main

If `main` moved ahead while you worked, bring those updates into your branch:

1. Switch to your branch.
2. Choose **Branch → Update from main**.

GitHub Desktop merges the latest `main` into your branch. (If `main` on GitHub has news, **Fetch origin** and **Pull origin** first.)

## 🏆 A healthy workflow: the "GitHub flow"

This simple recipe is used by teams of all sizes:

1. `main` is always in a good state.
2. For every new piece of work, **create a branch** from `main`.
3. **Commit** as you go.
4. **Publish** the branch and open a **pull request**.
5. **Review** and discuss.
6. **Merge** into `main`.
7. **Delete** the branch and start fresh next time.

## 🛠️ Try it

1. In `hello-github`, create a branch called `add-favorites`.
2. Add a file `favorites.md` listing three favorite things, and commit.
3. Switch to `main`, and confirm the file disappears. Switch back, and confirm it returns.
4. Switch to `main`, then choose **Branch → Merge into current branch...** and merge `add-favorites`.
5. Look at **History**, then delete the merged branch.
6. **Bonus (conflict practice):** on two different branches, change the same line of a file differently. Merge both into `main` and resolve the conflict.

## 🧯 Stuck?

- **"Which branch am I on?"** Look at the **Current branch** button in the top bar.
- **I can't switch branches:** You have unsaved changes. Choose **Leave my changes** or **Bring my changes** when asked, or commit them first.
- **I committed on `main` by accident:** Don't panic. Chapter 12 shows how to move that commit onto a branch.
- **Merge says "no commits to merge" or is greyed out:** The branch you picked has nothing new for the branch you're on.

## ✅ Checkpoint

- [ ] I can create, switch, and delete branches.
- [ ] I can merge one branch into another.
- [ ] I can publish a branch to GitHub.
- [ ] I can describe the "GitHub flow" in my own words.

---

Previous: [Chapter 6](06-clone-push-pull.md) · Next: **[Chapter 8: Pull Requests](08-pull-requests.md)**
