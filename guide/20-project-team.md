# Chapter 20: Project 2: A Team Project 👥

🎯 **Goals:** Run a small team project from start to finish, the way real teams do: set up a shared repository, divide the work with issues, contribute through branches and pull requests, review each other, fix a conflict, and publish a release.

⏱️ **Time:** about 90 minutes, ideally across two or three short sessions.

👫 **You need:** two to four people, each with a GitHub account and GitHub Desktop. No friends handy? Use a second account of your own and play both roles. It works.

**The project:** a **Community Cookbook**. Each person adds a few recipes (or any topic you choose: a study guide, a travel list, a reading club's book reviews). You'll get a finished, published collection and a feel for teamwork.

---

## 🗺️ The plan

| Step | Who | What |
|------|-----|------|
| 1 | Owner | Create the repository and invite everyone |
| 2 | Owner | Add the README, a recipe template, and labels |
| 3 | Owner | Turn on a simple rule for `main` |
| 4 | Everyone | Clone the repository |
| 5 | Owner | Create issues, one per recipe |
| 6 | Everyone | Pick an issue, branch, write, commit, and open a pull request |
| 7 | Everyone | Review someone else's pull request |
| 8 | Everyone | Merge, and update your computers |
| 9 | Two people | Cause (and fix) a merge conflict on purpose |
| 10 | Owner | Publish the site and a release |
| 11 | Everyone | Look back: what worked? |

## 🏗️ Step 1: The owner creates the repository

1. Click **+ → New repository** and call it `community-cookbook`.
2. Make it **Public** (so the Pages site can be published) or **Private** if you prefer.
3. Tick **Add a README file** and choose a license from **Add license** (MIT is a friendly choice).
4. Click **Create repository**.

### 👋 Invite the team

1. **Settings → Collaborators → Add people**.
2. Add each teammate by username.
3. Everyone **accepts the invitation** from their email or from the notifications on GitHub.

## 📝 Step 2: Set the table

The owner edits files on github.com. Each of these is a small commit.

### The README

Replace the README with:

````markdown
# 🍲 Community Cookbook

A collection of recipes from our team, shared with love.

## 📖 Recipes
<!-- Each person adds a link here when their recipe is merged -->

## 🤝 How to add a recipe
1. Pick a recipe issue and assign it to yourself.
2. Create a branch named `recipe-your-dish`.
3. Copy `recipes/_template.md` to a new file in the `recipes` folder.
4. Fill it in, commit, and open a pull request.
5. Ask a teammate for a review.

## 📜 License
Shared under the MIT License.
````

### The recipe template

Click **Add file → Create new file**, name it `recipes/_template.md`, and paste:

````markdown
# Recipe name 🍽️

**Serves:** 4 · **Time:** 30 minutes · **Added by:** @your-username

## Ingredients
- Ingredient one
- Ingredient two

## Steps
1. First step
2. Second step

## Notes
Any tips, swaps, or family stories.
````

### Labels

On the **Issues** tab, click **Labels**. Keep **good first issue**, and add:

| Label | Color idea | Meaning |
|-------|-----------|---------|
| `recipe` | green | A recipe to write |
| `needs review` | yellow | Waiting for a teammate |
| `docs` | blue | README or guide changes |

## 🛡️ Step 3: Protect main

So nobody pushes straight to `main`:

1. **Settings → Branches** (or **Rules → Rulesets**).
2. Add a rule for `main`: **Require a pull request before merging**, with **1** approval.
3. Save.

(Chapter 11 walks through it. If you're on a private repo on the free plan, this setting may be unavailable. In that case, agree on the rule out loud: *nobody commits directly to main*.)

## 💻 Step 4: Everyone clones

In GitHub Desktop: **File → Clone repository...**, choose `community-cookbook` from the list (collaborators' repos appear under the owner's name), and click **Clone**.

## 📋 Step 5: Make the work visible

The owner creates **one issue per recipe**, for example:

- `Recipe: Grandma's pancakes`
- `Recipe: Quick vegetable curry`
- `Recipe: No-bake cookies`
- `Recipe: Spicy noodle soup`

Add the `recipe` label to each. Optional but great: create a **Project board** (Chapter 9) with **To do**, **In progress**, and **Done** columns.

Each teammate then **assigns themselves** to the issue they'll take. Assign before you start, so two people don't pick the same job.

## ✍️ Step 6: Everyone writes a recipe

Repeat this for your own issue. This is the loop you'll use on every team project.

1. **Fetch origin**, then **Pull origin**, so you have the latest.
2. Switch to `main` if you aren't on it.
3. **Current branch → New Branch**, named `recipe-your-dish`.
4. Copy `recipes/_template.md` to a new file such as `recipes/pancakes.md`. (Use **Repository → Show in Explorer / Finder**, copy the file, and rename it.)
5. Fill it in using your editor.
6. In GitHub Desktop, review the **Changes** tab, write a Summary like `Add pancake recipe`, and click **Commit to recipe-your-dish**.
7. Click **Publish branch**, then **Create Pull Request**.
8. Fill in the description, and add `Closes #N` (your issue number) so the issue closes on merge. Add your `needs review` label.
9. Ask a teammate to review (**Reviewers** in the sidebar).

## 🔎 Step 7: Review a teammate's pull request

Open someone else's pull request and:

1. Read the description.
2. Open **Files changed**, tick **Viewed**, and read the recipe.
3. Leave at least **one friendly comment** (praise something!) and **one suggestion** if you spot a typo, using the ± button.
4. Click **Review changes → Approve** (or **Request changes** if something's missing), then **Submit review**.

Chapter 11 has examples of kind, useful comments.

## ✅ Step 8: Merge and update

When a pull request has an approval:

1. The author clicks **Merge pull request**, then **Confirm merge**, then **Delete branch**.
2. Everybody switches to `main` in GitHub Desktop, clicks **Fetch origin**, then **Pull origin**.

Check: the recipe files are now on everyone's computer.

### 🔗 Add the recipe to the README

After a recipe merges, its author adds a link to the README under **Recipes**, in a tiny second pull request. That's the perfect setup for the next step.

## 😬 Step 9: Create (and fix) a conflict on purpose

Conflicts are normal. Practice them in a safe place.

1. **Two people** each create a branch and edit **the same line** in the README, for example, the first line of the **Recipes** list, with different text.
2. Both push and open pull requests.
3. Merge the first one.
4. On the second pull request, GitHub says **This branch has conflicts**. The author fixes it:
   1. In GitHub Desktop, switch to their branch.
   2. Choose **Branch → Update from main**.
   3. A conflict window appears. Click **Open in** *(editor)*.
   4. Choose the final text (maybe keep both lines), delete the `<<<<<<<`, `=======`, `>>>>>>>` lines, and save.
   5. Click **Continue merge** (or **Commit merge**), then **Push origin**.
5. The conflict warning disappears. The other person can approve, and merge.

Chapter 6 explains this in more detail. After doing it once, conflicts stop being scary.

## 🌐 Step 10: Publish it

1. **Settings → Pages**: **Deploy from a branch**, **main**, **/ (root)**.
2. Add `_config.yml` with a theme (Chapter 13), and an `index.md` copied from the README.
3. Check your site address after a minute or two.

### 🏷️ Make a release

Mark this moment: **Releases → Draft a new release**, tag `v1.0.0`, title `First edition`, click **Generate release notes**, and **Publish release**. (Chapter 18.)

## 🪞 Step 11: Look back

Teams that look back get better. Open a new issue called **Retrospective** and have everyone answer:

- 😊 What went well?
- 😕 What was confusing or slow?
- 💡 What would we do differently next time?

You'll be surprised how much you learned.

## 🌟 Stretch goals

- Add an **issue template** for recipe requests (**Settings → Features → Issues → Set up templates**).
- Add a **CONTRIBUTING.md** with the steps above, and a **CODE_OF_CONDUCT.md**.
- Add a **pull request template** (Chapter 11).
- Add a **GitHub Action** that welcomes new issues (Chapter 15).
- Make a **category index**: `desserts.md`, `soups.md`, and link recipes from them.
- Invite a friend who isn't on the team to **fork** the repo and send a recipe the open-source way (Chapter 22).

## 🧯 Stuck?

- **I can't push to the repo:** Make sure you accepted the invitation, and that you're pushing a **branch**, not `main`, if main is protected.
- **I can't merge:** A rule is waiting for an approval. Ask a teammate.
- **My branch is behind main:** **Branch → Update from main**.
- **Two people took the same recipe:** Let the first assigned person keep it. Say so kindly in the issue, and choose another.
- **Someone is stuck:** Pair up on a video call and work through it together. Chapter 29 helps too.

## ✅ Checkpoint

- [ ] Our team repository has a README, a template, and a license.
- [ ] Every issue has an owner.
- [ ] Everyone made a branch and opened a pull request.
- [ ] Everyone reviewed someone else's work.
- [ ] We resolved a conflict.
- [ ] We published a site and a release.
- [ ] We held a retrospective.

---

Previous: [Chapter 19](19-project-personal-website.md) · Next: **[Chapter 21: Project 3: Write a Book or Documentation](21-project-book-or-docs.md)**
