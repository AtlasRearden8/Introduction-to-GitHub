# Chapter 17: Using AI With GitHub 🧠

🎯 **Goals:** Learn how to use AI helpers as a patient tutor and writing partner while you learn GitHub, how to ask good questions, how to check what they tell you, and how to stay safe. No technical background needed.

> 💡 **A note on timing:** AI tools change quickly. Product names, menus, and prices in this chapter may look different by the time you read it. The habits, which matter most, stay the same.

---

## 🌟 What AI helpers are good at

Think of an AI assistant as a very well-read friend who is available at any hour, never gets tired of questions, and sometimes confidently says something wrong. Used well, it can:

| Task | Example |
|------|---------|
| **Explain** | "What's the difference between fetch and pull in GitHub Desktop?" |
| **Translate an error** | "GitHub Desktop says 'merge conflicts.' What does that mean and what should I click?" |
| **Draft text** | "Write a friendly README for my recipe collection." |
| **Improve text** | "Make this pull request description clearer." |
| **Summarize** | "Summarize this long issue thread in five bullet points." |
| **Plan** | "Give me a one-week plan to practice branches." |
| **Quiz you** | "Ask me five questions about pull requests, one at a time." |
| **Suggest names and messages** | "Suggest three clear commit messages for this change." |

## 🚧 What they're not good at

- **They can be wrong, with total confidence.** This is called a *hallucination*. A made-up menu name or step can sound perfectly real.
- **They may be out of date.** GitHub's buttons change.
- **They don't know your situation** unless you tell them. They can't see your screen.
- **They can't be responsible** for your project. You are.

**The golden rule:** *Trust, but verify.* If an AI tells you to click something and you don't see it, don't force it. Check GitHub's official documentation.

## 🛡️ Staying safe (please read this part)

> 🔑 **Never paste secrets into an AI chat.** No passwords, API keys, tokens, recovery codes, or private keys. Treat a chat window like a postcard that other people might read.

Also:

- **Don't paste private or sensitive information:** other people's personal details, client data, health or financial records, or anything you've promised to keep confidential.
- **Check what your AI service does with your conversations.** Some let you turn off the use of your chats for training. Look in its privacy settings.
- **Don't run commands or install programs** an AI suggests unless you understand them. This guide never needs them.
- **Be careful with licensing.** AI-written text and pictures can raise questions about who owns them. For important projects, check the rules of the tool you use, and say when AI helped.
- **Be honest.** If your class, job, or open-source project has rules about AI help, follow them. Many projects ask you to say if AI helped with a contribution.

## 💬 How to ask good questions

A good prompt has three ingredients: **context**, **the exact problem**, and **what you want back**.

### The recipe

> **I'm** [who you are and what you know]. **I'm trying to** [goal]. **I did** [what you clicked], and **I saw** [the exact message]. **Please** [what you want: explain, give steps, a simple answer].

### Weak vs. strong

| Weak | Strong |
|------|--------|
| "GitHub is broken." | "I'm a beginner using GitHub Desktop on Windows. I clicked **Push origin** and got a message that says 'push rejected.' What does that mean, and what should I click next?" |
| "Write a README." | "Write a friendly README for a public repository called `recipe-collection`, a collection of my family's recipes. Include sections for how to browse, how to contribute a recipe, and a license note. Keep it warm and short." |
| "Fix this." | "Here is my pull request description [paste]. Make it clearer for a reviewer who doesn't know the project, but keep my own voice." |

### Handy follow-ups

- "Explain that like I'm new to this."
- "Give me just the next step, not the whole list."
- "How can I double-check that in GitHub's own documentation?"
- "What could go wrong with this?"
- "Show me where to click, in GitHub Desktop, not the command line."

That last one is useful. Many answers online use the command line. You can always ask for the **GitHub Desktop** or **website** version.

## 🧰 Eight ways to use AI while learning GitHub

### 1. Decode an error

Paste the message (with any private details removed) and ask what it means and what to click. Compare with Chapter 29.

### 2. Practice with a tutor

> "Be my GitHub tutor. I just finished the chapter on branches in a beginner guide that uses GitHub Desktop. Ask me one question at a time. Give me feedback after each answer. Start easy."

### 3. Write a README

Give it facts: what the project is, who it's for, what's inside. Then **edit** the draft so it sounds like you, and check every claim.

### 4. Polish a pull request description

Paste your draft and ask for improvements. Make sure it still says what *you* actually changed.

### 5. Turn messy notes into an issue

> "Turn these notes into a clear GitHub issue with a title, a short description, and a checklist of tasks: [notes]."

### 6. Summarize a long discussion

Paste a long issue thread and ask for the decisions and open questions. Check the summary against the thread.

### 7. Brainstorm names and structure

Repository names, folder layouts, labels, and milestones. Ask for several options, then choose.

### 8. Proofread

Ask it to fix spelling and grammar **without changing your meaning**, and to list what it changed.

## 🤖 AI built into GitHub

GitHub has its own AI assistant called **GitHub Copilot**. What you see depends on your plan and settings, and features change often, so treat this as a map and not a manual.

- **Copilot Chat on github.com:** Look for a Copilot icon near the top of the page. It opens a chat where you can ask questions about GitHub, a repository, or a file. You can ask it to explain a file or a pull request.
- **Summaries:** In some places, such as when you write a pull request description, a Copilot button can draft a summary of your changes for you to edit.
- **Commit messages:** Some versions of GitHub Desktop can suggest a commit message for you. If you see a sparkle icon near the **Summary** box, that's probably it. Always read the suggestion and fix it so it says what you really did.
- **In editors:** Copilot can also suggest text as you type in code editors. You don't need this for the work in this guide.

Copilot has a free tier with limits and paid plans for more. Students, teachers, and maintainers of popular open-source projects can sometimes get paid features at no cost. Check <https://github.com/features/copilot> for what's currently offered.

> 🔒 **Check the privacy settings.** In **Settings → Copilot**, you can see and change what's shared. Make choices on purpose.

## ✅ Checking an AI's answer

Before you act on advice:

1. **Does it match what's on your screen?** If a button it names isn't there, stop.
2. **Does it match the official docs?** Search for the feature name plus "GitHub Docs".
3. **Is it reversible?** If a step can delete or overwrite something, double-check, or make a backup copy of your project folder first.
4. **Ask a second time, differently.** If the answers disagree, be suspicious.
5. **Ask a person.** A teacher, friend, or a community forum can settle things.

## 🙋 Using AI in open-source and team projects

- **Read the project's rules** about AI contributions.
- **Say so** if AI helped write your change, if the project asks.
- **Understand what you submit.** You're responsible for it, and reviewers will ask you questions.
- **Don't flood maintainers** with large, unchecked, AI-generated pull requests. Small, careful contributions are welcome. Large careless ones waste volunteers' time.
- **Be kind about other people's AI use,** and focus on the quality of the work.

## 🛠️ Try it

1. Ask an AI assistant to explain "fork vs. clone" to a beginner, then compare its answer with Chapter 10.
2. Give it your **own** notes about a project and ask for a README draft. Edit it until it sounds like you, and check each fact.
3. Ask it to quiz you on Chapter 8 (Pull Requests), one question at a time.
4. **Safety drill:** look at the last thing you typed into any AI chat. Was there a password, key, or private detail? If so, change that secret and remember the rule.

## 🧯 Stuck?

- **The AI gave steps that don't match my screen:** Tell it exactly what you see ("I don't see a button called X; the menu has A, B, and C") and ask again. Or check the docs.
- **It keeps suggesting the command line:** Say "I only use GitHub Desktop and the GitHub website. Give me those steps."
- **I don't know if it's right:** Treat it as a clue, not a fact. Verify before you click.

## ✅ Checkpoint

- [ ] I know what AI helpers are good at and where they fail.
- [ ] I never paste secrets or private information into a chat.
- [ ] I can write a prompt with context, a clear problem, and what I want.
- [ ] I check answers against my screen or the official docs.
- [ ] I'm honest about when AI helped.

---

Previous: [Chapter 16](16-security-and-privacy.md) · Next: **[Chapter 18: More Level-Ups](18-more-level-ups.md)**
