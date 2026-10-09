# Chapter 11: Reviews, Feedback & Teamwork 🫶

🎯 **Goals:** Learn how good teams actually work on GitHub: how to ask for a review, how to review someone else's work kindly and usefully, how to respond to feedback, and how to set simple rules that keep a shared project healthy.

You'll need a practice repository with at least one other person (a friend, a classmate, or a second GitHub account of your own).

---

## 🌍 Why reviews matter

A **review** is when someone else looks at your changes before they join the main project. It might sound scary, but reviews are one of the nicest parts of working together:

- **Fresh eyes catch mistakes** you can't see after staring at your own work.
- **You learn** from how other people solve problems.
- **Everyone understands the project**, so nothing depends on just one person.
- **Quality stays high** without anyone being the boss.

On GitHub, reviews happen inside a **pull request** (Chapter 8). This chapter is about the human side.

## 🎭 Who does what in a team?

Small teams usually don't need formal job titles, but it helps to know the roles that appear on GitHub:

| Role | What they do |
|------|--------------|
| **Author** | Makes the change and opens the pull request |
| **Reviewer** | Reads the change and gives feedback |
| **Assignee** | The person responsible for an issue or pull request |
| **Maintainer** | Looks after the project and has the final say on merging |
| **Contributor** | Anyone who adds something, big or small |

On a small project, one person can play several roles. Just be clear about who is doing what.

## 🙋 Asking for a review

When your pull request is ready:

1. Open the pull request on github.com.
2. In the right-hand sidebar, click the gear next to **Reviewers**.
3. Choose one or more people. They get a notification.
4. Write a helpful description. Tell reviewers what changed, why, and **where to look**.
5. Be patient. People have lives. If a few days pass, a polite nudge is fine: "Hi! Just checking if you've had a chance to take a look."

**Screenshot:** The right sidebar of a pull request with the **Reviewers** gear open.
{ .shot }

### Make it easy to review

- **Keep it small.** A pull request that changes three files gets a better review than one that changes thirty.
- **One purpose.** Fix one thing, or add one thing.
- **Explain your thinking** in the description.
- **Review it yourself first.** Read your own **Files changed** tab before you ask anyone else.
- **Add screenshots** if you changed something you can see.

## 🔎 How to review a pull request, step by step

1. Open the pull request and read the **description** first.
2. Click the **Files changed** tab.
3. Read the changes. Green lines were added and red lines were removed.
4. As you finish each file, tick the **Viewed** box at the top of it. Viewed files fold away, so you can see what's left.
5. To comment on a line, hover over it and click the blue **+**. Write your comment and click **Start a review** (not **Add single comment**, which sends it right away).
6. Add as many comments as you like. They stay private until you finish.
7. Click **Review changes** (top right) and write a short summary.
8. Choose how to finish:
   - **Comment:** general thoughts, not a yes or no.
   - **Approve:** this looks good and can be merged.
   - **Request changes:** something needs fixing first.
9. Click **Submit review**.

**Screenshot:** The **Review changes** box with the three options.
{ .shot }

### ✂️ Suggested changes: the friendliest tool

When you spot a typo or small improvement, don't just describe it. Show it.

1. Click the **+** on the line, then the **±** icon in the comment toolbar ("Add a suggestion").
2. GitHub copies the line into a box. Edit it to what you think it should say.
3. Submit your comment.

The author sees your proposed change and can click **Commit suggestion** to accept it in one click. No back and forth.

## 💛 Writing feedback people can use

Tone matters. Feedback is about the **work**, never about the person.

| Instead of... | Try... |
|---------------|--------|
| "This is wrong." | "I think this might mix up the two dates. Could you double-check?" |
| "Why did you do it this way?" | "I'm curious about this approach. What made you choose it?" |
| "Fix the spelling." | "Small typo here. Here's a suggestion you can accept." |
| "This is confusing." | "I got a bit lost in this paragraph. Could we add an example?" |
| (silence) | "Nice touch on the intro!" |

### A simple recipe for a good comment

1. **Say what you see.** ("This heading is much longer than the others.")
2. **Say why it matters.** ("It wraps to two lines on a phone.")
3. **Offer a way forward.** ("Maybe shorten it to 'Getting started'?")

### Label how serious each comment is

Reviewers often add a tag so authors know what's required:

- **Nit:** a tiny preference. Fix it if you like.
- **Question:** I'm not sure. Please explain.
- **Suggestion:** an idea you may take or leave.
- **Blocking:** this needs to change before merging.

### Don't forget to praise

Reviews aren't only for problems. If something is clever, clear, or kind, say so. A genuine compliment makes people braver and the work better.

## 🌱 Receiving feedback gracefully

It can sting the first time someone points out something in your work. That's normal. Here's how to turn it into a strength:

1. **Take a breath.** The comments are about the change, not about you.
2. **Read everything before you reply.**
3. **Say thanks.** Even a simple "Thanks, good catch!" keeps things warm.
4. **Ask when you're unsure.** "Could you say more about this?" is always fine.
5. **Disagree politely when you have a good reason.** Explain your thinking. The goal is the best result, not winning.
6. **Make the changes.** Open GitHub Desktop, switch to the same branch, edit, commit, and click **Push origin**. The pull request updates automatically.
7. **Mark each conversation resolved** once it's handled: click **Resolve conversation**.
8. **Ask for another look.** Click the small circular arrows next to the reviewer's name to **re-request review**.

## ✅ Approvals and merging

Common team habits:

- **At least one approval** before anything is merged.
- **The author merges** their own pull request once it's approved, or the maintainer does.
- **Delete the branch** after merging.
- **Don't merge your own work in secret.** Even on a two-person team, let someone see it first.

## 🛡️ Setting simple rules for your project

You can ask GitHub to enforce good habits so no one merges something by accident. This works on your own repositories, and it's a nice step when a team starts.

1. Open your repository and click **Settings**.
2. Click **Branches** in the left menu. On some accounts it's under **Rules → Rulesets**.
3. Click **Add branch ruleset** (or **Add classic branch protection rule**).
4. Name it, and aim it at your **default branch** (`main`).
5. Tick **Require a pull request before merging**, and set the number of approvals to **1**.
6. Save.

Now nobody can push straight to `main`. Everything goes through a pull request. Available options depend on your plan and repo type, so if a setting is missing, check GitHub's documentation.

### A pull request template

You can pre-fill every new pull request with a helpful structure.

1. On your repo, click **Add file → Create new file**.
2. Name it `.github/pull_request_template.md` (typing the slashes creates the folders).
3. Paste something like this:

````markdown
## What does this change?
<!-- A sentence or two. -->

## Why?
<!-- What problem does it solve? -->

## How to check it
- [ ] I read my own changes
- [ ] I tested it

## Related issue
Closes #
````

4. Commit it. From now on, new pull requests start with these headings.

Chapter 27 has more templates you can copy.

## 🧭 Teamwork habits that make life easy

- **Talk in issues and pull requests,** not just private messages, so everyone can see decisions.
- **Say what you're working on.** Assign yourself to an issue before you start, so two people don't do the same job.
- **Pull often.** Before you begin work each day: **Fetch origin**, then **Pull origin** in GitHub Desktop.
- **Commit small and often.** Small changes are easier to review and merge.
- **Agree on a few rules** and write them in the repository, for example in `CONTRIBUTING.md`.
- **Be kind and assume good intent.** Text can sound harsher than meant. If something feels rude, ask before you react.
- **Celebrate merges.** A small "Merged! Thanks everyone" keeps morale up.

## 💬 When people disagree

Disagreements are normal and healthy when handled well:

1. **Restate what the other person said** to make sure you understand.
2. **Focus on the goal.** What are we both trying to achieve?
3. **Offer options,** not ultimatums.
4. **Let the maintainer decide** if you're stuck, and accept the decision gracefully.
5. **Take heated discussions offline,** like a video call, then summarize the outcome in the pull request.

## 📜 A short code of conduct

A **code of conduct** states how people should treat each other. GitHub can add a standard one to your repository: in your repo, click **Add file → Create new file**, type `CODE_OF_CONDUCT.md`, and click **Choose a template**. It's a quiet but powerful signal that your project is welcoming.

## 🛠️ Try it

You need one other person (or a second account).

1. **Author:** make a branch in GitHub Desktop, add a small change, publish the branch, and open a pull request. Write a clear description and add your partner as a **Reviewer**.
2. **Reviewer:** read the pull request, tick **Viewed** on each file, leave **two comments** (one praise, one question), add one **suggested change**, and submit with **Request changes**.
3. **Author:** accept the suggestion, answer the question, push another commit, resolve the conversations, and **re-request review**.
4. **Reviewer:** approve.
5. **Author:** merge, delete the branch, and update your computer.
6. Add a **pull request template** to the repository.

## 🧯 Stuck?

- **I can't add reviewers:** On a personal repository, only people you've invited as **collaborators** can be reviewers. See Chapter 10.
- **I can't approve my own pull request:** That's by design. Someone else needs to approve it.
- **My comments disappeared:** You may not have submitted the review. Look for **Pending** at the top of the page and click **Finish your review**.
- **The merge button is greyed out:** A rule is waiting for something, like an approval. The page tells you what's missing.
- **There's a conflict:** See Chapter 6 for how to fix conflicts in GitHub Desktop.

## ✅ Checkpoint

- [ ] I can request a review and describe my changes clearly.
- [ ] I can leave line comments and use suggested changes.
- [ ] I can finish a review with Comment, Approve, or Request changes.
- [ ] I know how to respond to feedback and re-request a review.
- [ ] I've set up a simple rule or template for a project.

---

Previous: [Chapter 10](10-collaboration-and-open-source.md) · Next: **[Chapter 12: Undoing Mistakes](12-undoing-mistakes.md)**
