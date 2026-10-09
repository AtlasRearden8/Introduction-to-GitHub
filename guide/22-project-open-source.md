# Chapter 22: Project 4: Your First Open-Source Contribution 🌍

🎯 **Goals:** Make a real contribution to a real project that isn't yours. You'll learn how to choose a welcoming project, find a small task, make the change, submit it, handle feedback, and feel proud afterwards.

⏱️ **Time:** about 75 minutes, plus waiting for a reply.

> 💛 **You belong here.** Open source runs on people of every background and skill level. A fixed typo, a clearer sentence, or a translation is a real contribution, and maintainers are grateful for them.

---

## 🧠 Before you start: what "contributing" really means

Contributing doesn't mean writing code. Valuable contributions include:

| Kind | Examples |
|------|----------|
| **Documentation** | Fix a typo, clarify a confusing step, add an example |
| **Translation** | Translate a README or guide into another language |
| **Design** | Improve an image, an icon, or the layout of a page |
| **Testing** | Try the project, and report what works and what doesn't |
| **Issue triage** | Reproduce a reported bug and add the details |
| **Ideas and feedback** | Suggest improvements, politely and clearly |
| **Code** | Fix a bug or add a feature (if and when you're ready) |

For your **first** contribution, aim for something tiny, such as a typo or an unclear sentence. The goal is to learn the process, not to impress anyone.

## 🔍 Step 1: Find a welcoming project

### Where to look

- Search GitHub for projects you already use, enjoy, or are curious about.
- Use the **good first issue** label: <https://github.com/topics/good-first-issue>, or in the GitHub search bar type `label:"good first issue" is:open is:issue`.
- Try **help wanted**, **documentation**, or **beginner** labels.
- Look at <https://goodfirstissue.dev> or <https://up-for-grabs.net>, which collect beginner-friendly tasks.
- Join an event like **Hacktoberfest** (each October), which encourages beginners.

### 🕵️ Check the project's health

Before you spend time, spend two minutes checking the project is active and friendly:

| Check | Good sign |
|-------|-----------|
| **Last commit** | Within the last few months |
| **Open pull requests** | Some are being merged or answered |
| **Issues** | People get replies |
| **README** | Clear, with instructions |
| **CONTRIBUTING.md** | Exists and explains how to help |
| **CODE_OF_CONDUCT.md** | Exists |
| **Tone of comments** | Kind and patient |

If a project hasn't been touched for years, or maintainers are curt with newcomers, move on. There are plenty of welcoming ones.

## 📖 Step 2: Read the rules

Open these files in the repository, in this order:

1. **README.md** to understand what it is.
2. **CONTRIBUTING.md** to learn how they want help. **Follow it.** It may ask you to open an issue first, use a certain style, or sign something.
3. **CODE_OF_CONDUCT.md** to see how people are expected to behave.
4. **LICENSE** to know what the project allows.

Write down anything unusual: a required format for pull request titles, a template, or a rule against certain kinds of changes.

## 🎯 Step 3: Choose a small task

Look for an issue that is:

- **Clearly described** (you understand what's wanted).
- **Small** (a few lines).
- **Not already taken** (nobody is assigned, and nobody said "I'm on it" recently).

If there's no issue, you can still contribute. Read through the documentation and look for typos, outdated screenshots, or confusing steps, then open an issue first to say what you plan to fix, if the project's CONTRIBUTING file asks for that.

### 🙋 Say hello and claim it

Add a comment to the issue:

> Hi! I'm new to open source and would love to work on this. Is it still available? I plan to [one-line description of what you'll do].

Wait for a reply, which can take a day or a few. Don't start until you hear back, especially on larger tasks. Some projects automatically assign issues to the first person who asks, and the instructions will say so.

## 🍴 Step 4: Fork the project

You can't edit someone else's repository directly, so you make your own copy.

1. Open the project's page.
2. Click **Fork** (top right), then **Create fork**.
3. GitHub creates `YOUR-USERNAME/project-name`, which is yours to change freely.

## 💻 Step 5: Clone your fork with GitHub Desktop

1. On your fork's page, click the green **Code** button, then **Open with GitHub Desktop**.
2. GitHub Desktop asks how you plan to use this fork. Choose **To contribute to the parent project**, and click **Continue**.
3. Choose where to save it, and click **Clone**.

Cloning a big project can take a minute or two.

## 🌿 Step 6: Make a branch

1. **Current branch → New Branch**.
2. Name it after the task, like `fix-typo-in-install-guide`.

Never work on `main` of a fork. A branch keeps your fork tidy, and you can have several going at once.

## ✏️ Step 7: Make the change

1. **Repository → Open in** *(your editor)*.
2. Find the file (use your editor's search to look for the text).
3. Make **the smallest change that solves the problem**. Don't tidy up other things on the side. Keep changes focused.
4. Save the file.
5. In GitHub Desktop, look at the **Changes** tab. The green and red lines should be exactly what you meant, with nothing extra.

### ✅ Check your work

- For writing, **read it aloud** and check the spelling.
- If the project has rules for formatting or tests, run what **CONTRIBUTING.md** asks you to. For documentation fixes, there's often nothing to run.
- If it's a website, and the project explains how to preview it, check it.

## 💾 Step 8: Commit with a clear message

In the **Summary** box, write a short, specific message. Many projects have a style, so check CONTRIBUTING. A friendly default:

| Weak | Strong |
|------|--------|
| `update` | `Fix typo in installation instructions` |
| `changes` | `Clarify step 3 of the setup guide` |
| `fix` | `Update broken link to the contributing guide` |

Add a short **Description** if useful. Click **Commit to** *(your branch)*.

## 🚀 Step 9: Open the pull request

1. Click **Publish branch**.
2. Click **Create Pull Request**. Your browser opens.
3. Check the page: the **base repository** should be the **original project**, and the **head repository** should be **your fork**.
4. Write a **title** that matches the project's style, and a short **description**:

````markdown
## What this changes
Fixes a typo in the installation guide ("recieve" → "receive").

## Why
It was confusing for new readers.

Closes #123
````

   If the project has a **pull request template**, GitHub fills it in. Complete every section.
5. Click **Create pull request**.

Take a breath and smile. You just proposed a change to a real project.

**Screenshot:** A pull request opened from a fork, with the base and head repositories labeled.
{ .shot }

## 💬 Step 10: Handle the reaction

Maintainers are often volunteers, so replies can take days or weeks. Meanwhile:

### ✅ If they ask for changes

That's normal and a good sign! They're helping you improve it.

1. Read the comments carefully. Ask if anything is unclear.
2. In GitHub Desktop, make sure you're on the same branch.
3. Make the changes, commit, and click **Push origin**. The pull request updates automatically.
4. Reply: "Thanks! Updated." and **resolve** the conversations you've addressed.

### 🎉 If it's merged

Congratulations! You're now an open-source contributor. Your name appears in the project history forever. Add the pull request to your profile README or portfolio (Chapter 14).

### 🙏 If it's closed without merging

It happens, even to experts. Maybe the change wasn't wanted, or someone else had already done it. Read their reason, say thanks, and move on. You still learned the whole process, and the next one will be easier.

### 😴 If nobody replies

Wait at least a week or two. Then add a polite comment: "Hi! Just checking if there's anything I should change. Happy to adjust." If it's still quiet, consider trying another project.

## 🔄 Step 11: Clean up and keep your fork fresh

After your pull request is merged:

1. On github.com, click **Delete branch** on the pull request.
2. On your fork's page, click **Sync fork → Update branch** so your copy matches the original.
3. In GitHub Desktop, switch to `main`, **Fetch origin**, and **Pull origin**.
4. Delete your old local branch with **Branch → Delete...**

Before you start your *next* contribution, sync again, so you begin from the latest version.

## 🧭 Good open-source etiquette

- **Be patient and polite.** Everybody is busy. A thank-you goes a long way.
- **One change per pull request.** Don't mix unrelated fixes.
- **Follow the project's style,** even if you'd do it differently.
- **Don't take it personally.** Feedback is about the work.
- **Don't ask for the same thing twice** in quick succession. One gentle nudge is enough.
- **Give credit.** If someone helped, say thanks.
- **Be honest about AI.** If the project asks you to say when AI helped, do so (Chapter 17).
- **Respect the code of conduct.** It protects everyone, including you.

## 🛟 If you want a safe practice run first

Try GitHub's own practice repository, **`octocat/Spoon-Knife`**, or take a course at <https://skills.github.com> (look for "Contribute to open source"). These exist so you can make mistakes in public without any worry.

## 🌟 What next?

- Try a **second contribution** within a week, while the steps are fresh.
- Look for projects with **documentation** labels: you now know how to write a clear README (Chapter 4).
- Try **translating** a project you care about.
- Help another beginner, by answering a question in an issue or discussion.
- Start your own project, and add a **CONTRIBUTING.md** (Chapter 27 has a template).

## 🧯 Stuck?

- **I can't find a "good first issue" I understand:** Search for **documentation** instead, or pick a project in a subject you know well.
- **The pull request has conflicts:** In GitHub Desktop, switch to your branch and use **Branch → Update from default branch**. (Chapter 6.)
- **A check failed:** Click **Details** next to the red mark and read what it says. Fix it, and push again. Ask politely in a comment if you're stuck.
- **I committed to `main` of my fork:** It's fine, but create a branch from it and open the PR from there. Chapter 12 can help move it.
- **I'm nervous:** Totally normal. Read your own pull request one more time, then click the button. The worst outcome is a polite "no thanks."

## ✅ Checkpoint

- [ ] I found a project that looks welcoming and active.
- [ ] I read its README, contributing guide, and code of conduct.
- [ ] I forked it, cloned my fork, and made a branch.
- [ ] I made a small, focused change and committed it with a clear message.
- [ ] I opened a pull request to the original project.
- [ ] I know how to respond to feedback.

---

Previous: [Chapter 21](21-project-book-or-docs.md) · Next: **[Chapter 23: GitHub for Writers, Designers, Students & Researchers](23-github-for-everyone.md)**
