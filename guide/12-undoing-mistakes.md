# Chapter 12: Undoing Mistakes 🧯

🎯 **Goals:** Learn the safety net. Everyone makes mistakes with Git. The difference between nervous beginners and confident ones is knowing how to recover.

> 💛 **Reassurance first:** if you've **committed** your work, it is very hard to lose it for good. Take a breath. You've got this.

**How to use this chapter:** find the situation that matches yours. You don't need to memorize anything. Come back whenever you need it.

---

## 🧭 First, a rule of thumb

Ask: **Has this change been pushed (sent to GitHub) yet?**

- **Not pushed (only on your computer):** you have more freedom to undo things quietly.
- **Already pushed:** prefer adding a **new commit that cancels the old one** (called a *revert*), so you don't disrupt anyone else.

In GitHub Desktop, you can tell at a glance. If the top-right button says **Push origin**, you have commits that are *not* on GitHub yet.

## 🗑️ Situation 1: "I edited a file and want to throw away my changes"

(The changes are **not committed** yet.)

1. In the **Changes** tab, right-click the file.
2. Choose **Discard Changes...** and confirm.

The file goes back to how it was at your last commit. To discard everything at once, choose **Discard All Changes...** from the same menu.

> ⚠️ **Careful:** Discarding permanently throws away your unsaved edits. Desktop may let you find them in your Recycle Bin or Trash, but don't count on it. Look at the green and red lines first, to be sure.

## ☑️ Situation 2: "I ticked a file by mistake"

Just **untick its checkbox** in the Changes list. Only ticked files go into the next commit, and your edits stay safe.

## ⏪ Situation 3: "I want to undo my last commit but keep my work"

(Not pushed yet.)

1. Open the **Changes** tab. At the bottom left you'll see a message about your most recent commit, with an **Undo** button.
2. Click **Undo**.

The commit disappears, and its changes return to your Changes list, ready to edit or commit again. This is also how you fix a typo in a commit message: undo the commit, then commit again with a better summary.

**Screenshot:** The bottom of the Changes tab showing the last commit and the **Undo** button.
{ .shot }

## 📎 Situation 4: "I forgot to include a file in my last commit"

(Not pushed yet.)

Click **Undo** as in Situation 3, tick the extra file, and commit everything together again. Some versions of GitHub Desktop also offer **Amend commit** when you right-click the latest commit in the **History** tab. If you see it, it does the same job.

## ↩️ Situation 5: "I want to undo a commit that's already been pushed"

Use **Revert**. It creates a *new* commit that cancels out an old one. History stays intact and safe for teammates.

1. Open the **History** tab.
2. Right-click the commit you want to undo.
3. Choose **Revert Changes in Commit**.
4. Click **Push origin**.

This is the safe, standard way to undo shared work.

## 🔀 Situation 6: "I committed on `main` but meant to use a branch"

(Not pushed yet.)

1. **First, rescue the commit.** Click **Current branch → New Branch** and create a branch (say `my-new-branch`) while still on `main`. It comes with your commit.
2. Click **Current branch** and switch back to **main**.
3. In the **Changes** tab, click **Undo** to remove the commit from `main`. (Do this once for each commit you want to move.)
4. The undone changes now show up in the Changes list on `main`. Right-click each file and choose **Discard Changes...** so `main` is clean. Your work is safe on `my-new-branch`.
5. Switch to `my-new-branch` and carry on.

Don't skip step 1. It's the step that makes everything else safe.

## 🧳 Situation 7: "I need to switch branches but I'm not ready to commit"

When you click a different branch while you have unsaved edits, GitHub Desktop asks what to do:

- **Leave my changes on this branch:** your edits are put away safely (Desktop calls this a *stash*). They return when you come back.
- **Bring my changes to the other branch:** your edits come with you.

When you come back, look for **Stashed Changes** at the top of the Changes tab. Click it, then **Restore** to bring your edits back.

## 🕰️ Situation 8: "I want to look at an old version"

In GitHub Desktop, open the **History** tab and click any commit. You can see exactly what it changed, file by file.

To see or copy an old version of a whole file, use the website:

1. On github.com, open the file and click **History**.
2. Click the commit you want, then click **Browse files** (or the **...** menu, then **View file**).
3. Copy the old text and paste it into your current file, or click **Raw** and save it.

## 📄 Situation 9: "I deleted a file by accident"

If you haven't committed yet, the deleted file shows up in **Changes** with a red mark. Right-click it and choose **Discard Changes...** The file comes back.

If you already committed the deletion, open **History**, right-click that commit, and choose **Revert Changes in Commit**. Or open the file's earlier version on github.com, as in Situation 8.

## 🌿 Situation 10: "I deleted a branch I still needed"

- **If you published the branch** (it's on GitHub): click **Fetch origin**. Open **Current branch** and find it in the list. If you deleted it on GitHub after merging a pull request, open that pull request and click **Restore branch**.
- **If you never published it:** the branch is only on your computer, and GitHub Desktop can't bring it back. This is why publishing a branch (even as a draft pull request) is a cheap form of backup.

## 🔑 Situation 11: "I accidentally committed a secret (password, API key)"

This is serious but fixable.

1. **Assume the secret is compromised.** Immediately **revoke or replace** it at the service that issued it. Change the password, or delete the key and make a new one. This is the step that actually protects you.
2. Removing the secret from your history takes advanced tools. GitHub explains how in its guide **Removing sensitive data from a repository**. Ask for help if you need it.
3. Add the file to your ignore list (right-click it in **Changes**, then **Ignore file**) so it doesn't happen again.

Deleting the file in a new commit is **not enough**. The secret remains in the old commits.

## 🛑 Situation 12: "I'm in the middle of a merge and it's a mess"

When GitHub Desktop shows the conflict window, click **Abort merge**. Everything goes back to exactly how it was before the merge started.

## ↩️ Situation 13: "I merged a pull request and want to undo it"

1. On github.com, open the merged pull request.
2. Click **Revert** near the bottom.
3. GitHub opens a new pull request that cancels the first one. Merge that.
4. In GitHub Desktop, **Fetch origin** and **Pull origin** to update your computer.

## 📋 Quick guide: which undo tool?

| I want to... | Do this |
|--------------|---------|
| Throw away unsaved edits | Right-click the file in **Changes**, then **Discard Changes...** |
| Leave a file out of a commit | Untick its checkbox |
| Fix my last commit (not pushed) | **Undo** in the Changes tab, then commit again |
| Undo a pushed commit safely | **History**, right-click the commit, **Revert Changes in Commit** |
| Pause work to switch branches | Choose **Leave my changes** when asked |
| Cancel a merge in progress | **Abort merge** |
| Undo a merged pull request | **Revert** button on the pull request page |

## ⚠️ The risky ones (use with care)

| Action | Why it's risky |
|--------|----------------|
| **Discard Changes** | Throws away unsaved edits right away |
| **Undo** a commit | Fine on its own, but check you're undoing the one you meant |
| **Force push** | If GitHub Desktop ever offers a **Force push** button, stop. It overwrites GitHub's history and can erase teammates' work. Ask someone before you click it. |
| **Deleting an unpublished branch** | Its commits exist nowhere else |

Before you click any of these, pause and ask yourself, "Do I really mean this?"

## 🛠️ Try it (in a throwaway project)

1. Edit a file, then discard the edit with **Discard Changes...**
2. Make a commit with a typo in the summary, then click **Undo** and commit again with it fixed.
3. Make a commit, click **Push origin**, then use **Revert Changes in Commit** and push again.
4. **Fire drill:** create a branch with a commit and publish it. Delete the branch on your computer, then click **Fetch origin** and bring it back from the list. Doing this once makes you fearless.

## ✅ Checkpoint

- [ ] I know the difference between "not yet committed," "committed on my computer," and "pushed to GitHub."
- [ ] I can discard changes, undo a commit, and revert a pushed commit.
- [ ] I know how to abort a merge.
- [ ] I know which actions are risky.

---

Previous: [Chapter 11](11-reviews-and-teamwork.md) · Next: **[Chapter 13: GitHub Pages: Build a Website](13-github-pages.md)**
