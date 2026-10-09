# Chapter 6: Branches & Merging 🌿

🎯 **Goals:** Understand why branches exist, create and switch between them, and merge them together. This is the superpower that makes confident experimentation possible.

---

## The idea

Imagine your project is a story and `main` is the polished, published version. You want to try rewriting the ending. You wouldn't scribble on the published copy. You'd make a **photocopy**, experiment there, and only swap it in if you love it.

A **branch** is that photocopy, except it's lightweight and free.

```
main:        A───B───C───────────────G   ← safe, stable version
                      \             /
my-idea:               D───E───F──┘      ← experiments live here, then merge back
```

Each letter is a commit. The branch `my-idea` split off at C, got its own commits (D, E, F), and then was **merged** into `main` as G.

**Why branches are wonderful:**
- `main` stays clean and working.
- You can work on several ideas in parallel.
- If an experiment fails, delete the branch. No harm done.
- On GitHub, branches are how pull requests (Chapter 7) work.

## Branch commands

Work inside any repo, such as your `hello-github` clone.

### See your branches

```bash
git branch
```

The `*` marks the one you're on. Right now that's `main`.

### Create and switch to a new branch

```bash
git switch -c add-recipes
```

`-c` means "create." Translation: "make a new branch called `add-recipes` and move me onto it."

Naming tips: short, lowercase, hyphens, describing the work, such as `fix-typo`, `add-contact-page`, `update-readme`.

### Make a commit on the branch

```bash
echo "# Pancakes" > recipes.md
git add recipes.md
git commit -m "Add pancake recipe"
```

### Switch back to main to see the difference

```bash
git switch main
ls
```

`recipes.md` has **vanished**! It's not lost. It lives on your other branch. Switch back and it returns:

```bash
git switch add-recipes
ls
```

This feels like magic the first time. Git is swapping your files to match whichever branch you're on.

> Older tutorials use `git checkout` instead of `git switch`. Both work; `switch` is simply clearer.

## Merging a branch

Once you're happy with the work on `add-recipes`, bring it into `main`:

```bash
git switch main          # go to the branch that should RECEIVE the changes
git merge add-recipes    # bring in the other branch's work
```

**Rule of thumb:** you stand on the branch that is *receiving*, then name the branch that is *giving*.

Check the result:

```bash
git log --oneline --graph
```

The `--graph` option draws the branch shape in text.

### Clean up

After merging, the branch has done its job:

```bash
git branch -d add-recipes
```

(`-d` is the safe delete. Git refuses if the branch has unmerged work.)

## Two flavors of merge (just so the messages make sense)

- **Fast-forward:** `main` hasn't moved since you branched, so Git just slides `main` forward. No extra commit. Message: *"Fast-forward."*
- **Merge commit:** both branches have new work, so Git creates a special commit that joins them.

You don't need to choose. Git picks the right one.

## Merge conflicts, revisited

If two branches changed the *same lines*, Git asks you to resolve the conflict, exactly like in Chapter 5: open the file, choose the final text, remove the `<<<<<<<` markers, then `git add` and `git commit`.

## Branches and GitHub

Push a branch to GitHub:

```bash
git push -u origin add-recipes
```

On the repo page you'll see a banner offering **Compare & pull request**. That's the doorway into Chapter 7.

See all branches (including GitHub's):

```bash
git branch -a
```

Download a teammate's branch:

```bash
git fetch
git switch their-branch-name
```

Delete a branch on GitHub from your terminal:

```bash
git push origin --delete add-recipes
```

(GitHub also offers a *Delete branch* button after merging a pull request.)

## Keeping your branch up to date with main

If `main` moved ahead while you worked, bring those updates into your branch:

```bash
git switch main
git pull
git switch add-recipes
git merge main
```

## A healthy branching workflow (the "GitHub flow")

This simple recipe is used by teams of all sizes:

1. `main` is always in a good state.
2. For every new piece of work, **create a branch** from `main`.
3. **Commit** as you go.
4. **Push** the branch and open a **pull request**.
5. **Review** and discuss.
6. **Merge** into `main`.
7. **Delete** the branch and start fresh next time.

## 🛠️ Try it

1. In `hello-github`, create a branch called `add-favorites`.
2. Add a file `favorites.md` listing three favorite things, and commit.
3. Switch to `main`, confirm the file disappears, switch back, confirm it returns.
4. Switch to `main`, merge the branch, and view `git log --oneline --graph`.
5. Delete the merged branch.
6. **Bonus (conflict practice):** on two different branches, change the same line of a file differently. Merge both into `main` and resolve the conflict.

## 🧯 Stuck?

- **"Your local changes would be overwritten by checkout/switch":** You have uncommitted work. Commit it, or temporarily shelve it with `git stash` (and bring it back with `git stash pop`).
- **"Which branch am I on?"** `git branch` (or `git status`).
- **I committed on `main` by accident!** Don't panic. Chapter 10 shows how to move that commit to a branch.
- **`git merge` says "Already up to date."** The branch you named has nothing new for the branch you're on.

## ✅ Checkpoint

- [ ] I can create, list, switch, and delete branches.
- [ ] I can merge one branch into another.
- [ ] I can push a branch to GitHub.
- [ ] I can describe the "GitHub flow" in my own words.

---

⬅️ Previous: [Chapter 5](05-remotes-clone-push-pull.md) · ➡️ Next: **[Chapter 7: Pull Requests](07-pull-requests.md)**
