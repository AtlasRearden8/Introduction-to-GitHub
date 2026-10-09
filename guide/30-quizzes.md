# Chapter 30: Quizzes & Answers 🧠

🎯 **Goals:** Check what stuck, and find the spots to revisit. Try each quiz **before** you open the answers, which are hidden under "Show the answers" so you can't peek by accident. Don't worry about the score. Wrong answers are the best teachers.

Each quiz matches a part of the book. Answers include the chapter to re-read.

---

## 🌱 Quiz 1: The big ideas (Chapters 1–2)

1. In your own words, what's the difference between **Git** and **GitHub**?
2. What is a **repository**?
3. What is a **commit**?
4. What is **GitHub Desktop** for?
5. Why turn on **two-factor authentication**?
6. True or false: your GitHub account password goes into GitHub Desktop when you sign in.

<details markdown="1">
<summary>Show the answers</summary>

1. **Git** is the tool that tracks changes to your files. **GitHub** is the website that stores Git projects online and adds collaboration tools. (Chapter 1)
2. A project folder that Git is tracking, including its full history. (Chapter 1)
3. A saved snapshot of your project with a short message describing what changed. (Chapter 1)
4. It's the free app that lets you use Git and GitHub from your computer by clicking buttons. (Chapter 2)
5. It protects your account even if someone learns your password, because they'd also need your second proof, like a phone code. (Chapter 2 and Chapter 16)
6. **False.** GitHub Desktop opens your browser to sign in, and you never type your password into the app. (Chapter 2)

</details>

## 📁 Quiz 2: The basics (Chapters 3–6)

1. What is the **README** for?
2. Which symbols make a heading in Markdown? Which make **bold** text?
3. In GitHub Desktop, how do you decide which files go into a commit?
4. What's the difference between **Fetch origin** and **Pull origin**?
5. What does **Push origin** do?
6. What does it mean to **clone** a repository?
7. You see two quoted pieces of text in a file separated by `=======` with `<<<<<<<` above and `>>>>>>>` below. What is it, and what should you do?

<details markdown="1">
<summary>Show the answers</summary>

1. It's the front page of a project, shown automatically below the file list, explaining what the project is. (Chapters 3 and 4)
2. `#` followed by a space makes a heading (more `#` for smaller headings). `**double asterisks**` around text make it bold. (Chapter 4)
3. Tick or untick the **checkboxes** next to each file in the **Changes** tab. (Chapter 5)
4. **Fetch** only checks GitHub for news and never changes your files. **Pull** brings the new work down into your files. (Chapter 6)
5. It sends your saved commits from your computer up to GitHub. (Chapter 6)
6. Downloading a complete copy of a GitHub repository, with its history, to your computer. (Chapter 6)
7. It's a **merge conflict**. Both sides changed the same lines. Open the file, choose the final text, delete the marker lines, save, and click **Continue merge**. (Chapter 6)

</details>

## 🌿 Quiz 3: Working together (Chapters 7–11)

1. Why would you create a **branch**?
2. If you're on `main` and you want to bring in work from `add-recipes`, which branch do you stand on before you merge?
3. What is a **pull request**?
4. How do you make an issue close automatically when a pull request is merged?
5. What's the difference between a **collaborator** and a **fork**?
6. In a review, what's the difference between **Comment**, **Approve**, and **Request changes**?
7. What is a **suggested change**, and why is it friendly?
8. Name two things that make a pull request easy to review.

<details markdown="1">
<summary>Show the answers</summary>

1. To try out an idea or do a piece of work without touching the main version. If it works, merge it. If not, delete it. (Chapter 7)
2. `main`. You stand on the branch that **receives** the work, then merge the other one in. (Chapter 7)
3. A proposal to merge your branch into another, with a page for discussion, review, and approval. (Chapter 8)
4. Write `Closes #12` (using the issue's number) in the pull request description. (Chapter 8)
5. A **collaborator** has access to work directly in your repository. A **fork** is your own copy of someone else's repository, which you change freely and propose back with a pull request. (Chapter 10)
6. **Comment** is general feedback. **Approve** says it looks good to merge. **Request changes** says something must be fixed first. (Chapter 11)
7. A reviewer proposes exact replacement text that the author can accept with one click, with no back and forth. (Chapter 11)
8. For example: keep it small, one purpose, a clear description, review it yourself first, add screenshots for visual changes. (Chapters 8 and 11)

</details>

## 🧯 Quiz 4: Safety and recovery (Chapter 12)

1. How can you tell whether you have commits that **haven't been pushed**?
2. You edited a file and want to throw the edits away. What do you do?
3. You made a commit by mistake and haven't pushed it. How do you undo it and keep your work?
4. You pushed a commit that you now regret. What's the safe way to undo it?
5. You want to switch branches but you're not ready to commit. What can you do?
6. You committed a password. What's the **first and most important** thing to do?
7. What does **Abort merge** do?

<details markdown="1">
<summary>Show the answers</summary>

1. The top-right button says **Push origin**. (Chapter 12)
2. Right-click the file in **Changes**, then **Discard Changes...** Be careful: this throws the edits away. (Chapter 12)
3. In the **Changes** tab, click **Undo**. The commit disappears but your changes return to the list. (Chapter 12)
4. In **History**, right-click the commit and choose **Revert Changes in Commit**, then **Push origin**. It adds a new commit that cancels the old one. (Chapter 12)
5. Choose **Leave my changes** when GitHub Desktop asks. They're put away safely and come back later. (Chapters 7 and 12)
6. **Revoke or replace the password** at the service that issued it. Assume it's compromised. Deleting the file isn't enough. (Chapters 12 and 16)
7. It cancels a merge in progress and puts everything back exactly as it was before. (Chapter 6)

</details>

## 🚀 Quiz 5: Publishing and automation (Chapters 13–18)

1. What file name makes a page the **front page** of a Pages site?
2. Your Pages site gives a 404 right after you set it up. What should you try first?
3. What's special about a repository named exactly like your username?
4. Where do workflow files live?
5. What does `on:` mean in a workflow?
6. Should you ever write a password in a workflow file?
7. Name two reasons to use an AI assistant carefully.

<details markdown="1">
<summary>Show the answers</summary>

1. `index.md` or `index.html`, in the main folder. (Chapter 13)
2. Wait a minute or two, then check **Settings → Pages** and the **Actions** tab for a failed build. (Chapter 13)
3. Its README appears at the top of your profile page. (Chapter 14)
4. In a folder named `.github/workflows/` in your repository. (Chapter 15)
5. It's the trigger: *when* the workflow should run (for example, on a push, a schedule, or a button press). (Chapter 15)
6. **No.** Store secrets in **Settings → Secrets and variables → Actions**, or better, don't use them at all as a beginner. (Chapters 15 and 16)
7. They can be confidently wrong, they don't know your situation, and you must never paste secrets or private data into them. (Chapter 17)

</details>

## 🔒 Quiz 6: Security (Chapter 16)

1. What's the difference between a **public** and **private** repository?
2. Why is it risky to make a repository public when its history has old files?
3. Name three things that must never go in a repository.
4. A message says "Your account will be closed in 1 hour unless you click here." What do you do?
5. Where do you review which devices are signed in to your account?

<details markdown="1">
<summary>Show the answers</summary>

1. Anyone can see a public repository. Only you and the people you invite can see a private one. (Chapter 16)
2. Making it public publishes the **whole history**, including old versions of files you've since deleted. (Chapter 16)
3. For example: passwords, API keys and tokens, other people's private information, financial or ID numbers, or anything under a confidentiality agreement. (Chapter 16)
4. Don't click. It's likely a scam. Go to github.com directly by typing the address, and check your account there. (Chapter 16)
5. **Settings → Sessions**. (Chapter 16)

</details>

## 🌈 Scenario challenges

Try to talk through these without looking. There's no single right answer.

1. **The group project.** Four classmates are building a website. Ana and Ben both changed the same line, and GitHub Desktop shows a conflict. What happens, and what should they do?
2. **The accident.** You committed on `main` when you meant to use a branch, and haven't pushed. How do you fix it?
3. **The newcomer.** A friend wants to fix a typo in a project they don't own. Walk them through it.
4. **The leak.** You notice that a public repository you made last month has an old file with an email password in its history. List your next five steps.
5. **The portfolio.** You have ten repositories, and only three are tidy. What do you do with your profile?

<details markdown="1">
<summary>Show some suggested answers</summary>

1. The second to merge sees a conflict. In GitHub Desktop, **Update from main** on their branch, open the file, choose the final text (maybe keep both lines), remove the markers, save, **Continue merge**, and **Push origin**. They should talk to each other, too. (Chapters 6 and 20)
2. Create a branch from `main` (so the commit is safe on it), switch back to `main`, **Undo** the commit and **Discard** the leftover changes, then switch to your new branch and continue. (Chapter 12)
3. Fork the project, **Open with GitHub Desktop**, choose "To contribute to the parent project", make a branch, fix the typo, commit, **Publish branch**, **Create Pull Request**, and be patient. (Chapter 22)
4. Change the email password right now. Make the repository private. Delete the file. Look for other places the password was used, and change those. Read GitHub's guide on removing sensitive data from history. (Chapters 12 and 16)
5. **Pin** the three tidy ones. Add descriptions and READMEs to others when you have time. Make rough ones **private**, or archive them. (Chapter 14)

</details>

## 📊 How did you do?

| Score | What it means |
|-------|---------------|
| **Mostly confident** | Great! Try a project from Chapters 19–22. |
| **Some gaps** | Re-read the chapters named in the answers you missed, and redo their **Try it** sections. |
| **Lots of gaps** | That's normal at this stage. Follow the **30-day plan** (Chapter 24), one small step a day. |

---

Previous: [Chapter 29](29-troubleshooting-faq.md) · Next: **[Chapter 31: Resources & Where to Go Next](31-resources.md)**
