# Chapter 15: Automation with GitHub Actions 🤖

🎯 **Goals:** Understand what GitHub Actions does, and set up a few small helpers that do boring jobs for you automatically: say hello to new issues, run on a schedule, and run when you press a button. You'll copy and paste workflows, so no programming is needed.

This chapter is optional but fun. If you're short on time, read the first two sections and come back later.

---

## 💡 What are Actions?

**GitHub Actions** is a robot that lives in your repository. You tell it:

> "**When** this happens, **do** these steps."

For example:

- When someone opens an issue, post a friendly welcome.
- Every Monday morning, add a reminder.
- When a pull request is opened, check that the links all work.
- When you press a button, build something.

The robot runs on a computer GitHub provides, so you don't need to leave your own computer switched on.

### 🧩 The words you'll meet

| Word | Meaning | Everyday comparison |
|------|---------|---------------------|
| **Workflow** | One automation, saved as a small text file | A recipe |
| **Event** | The thing that starts it (a push, an issue, a schedule) | "When the doorbell rings..." |
| **Job** | A group of steps that run together | One section of the recipe |
| **Step** | A single task | "Stir for two minutes" |
| **Runner** | The computer that carries it out | The kitchen |
| **Action** | A ready-made step someone else wrote | A ready-made sauce |

Workflows are written in **YAML**, a simple format where indentation matters. You won't write much. You'll copy examples and change a few words.

## 📍 Where Actions live

- Workflow files live in a folder named `.github/workflows/` inside your repository.
- The **Actions** tab shows every run, with a green check for success and a red mark for failure.

**Screenshot:** The **Actions** tab showing a list of workflow runs with green checks.
{ .shot }

## 🧪 Example 1: Say hello

1. Open one of your practice repositories on github.com.
2. Click **Add file → Create new file**.
3. In the name box, type `.github/workflows/hello.yml`. Typing the slashes creates the folders.
4. Paste in:

```yaml
name: Say Hello

on:
  push:
    branches: [main]

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Print a greeting
        run: echo "Hello from GitHub Actions!"
```

5. Click **Commit changes...** and commit directly to `main`.
6. Click the **Actions** tab. You'll see **Say Hello** running (a yellow dot), then finishing (a green check).
7. Click the run, then **greet**, then **Print a greeting**. You'll see your message.

### 📖 Reading the file

```yaml
name: Say Hello          # a label shown in the Actions tab

on:                      # WHEN to run
  push:
    branches: [main]     # whenever something is saved to main

jobs:                    # WHAT to do
  greet:                 # a name for this job
    runs-on: ubuntu-latest   # the kind of computer to use
    steps:               # the tasks, in order
      - name: Print a greeting
        run: echo "Hello from GitHub Actions!"
```

> ⚠️ **YAML is picky about spaces.** Use spaces, never tabs. Keep the indentation exactly as shown (two spaces per level). If a workflow fails to start, check the indentation first.

## 🔘 Example 2: A button you can press

Sometimes you want to run something only when you choose. Add `workflow_dispatch` to the triggers:

```yaml
name: Manual Hello

on:
  workflow_dispatch:

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - run: echo "You pressed the button!"
```

Save it as `.github/workflows/manual.yml`. Then:

1. Click the **Actions** tab.
2. Choose **Manual Hello** in the list on the left.
3. Click **Run workflow**, then the green **Run workflow** button.

## ⏰ Example 3: Run on a schedule

You can run a workflow at set times using **cron**, a short code for "every so often":

```yaml
name: Weekly Check-in

on:
  schedule:
    - cron: "0 9 * * 1"
  workflow_dispatch:

jobs:
  checkin:
    runs-on: ubuntu-latest
    steps:
      - run: echo "It's Monday morning. Time for a check-in!"
```

Reading `0 9 * * 1`: minute `0`, hour `9`, any day of the month, any month, **Monday** (`1`). Times are in **UTC**, which may differ from your time zone.

| Cron | Meaning |
|------|---------|
| `0 9 * * 1` | Every Monday at 9:00 UTC |
| `0 0 * * *` | Every day at midnight UTC |
| `*/30 * * * *` | Every 30 minutes |
| `0 12 1 * *` | The first day of each month at noon UTC |

Scheduled workflows can run a little late, and GitHub may pause them in repositories with no activity for a long time.

## 👋 Example 4: Welcome every new issue

This one posts a friendly comment whenever someone opens an issue. It uses a ready-made Action called `github-script`.

Save as `.github/workflows/welcome.yml`:

````yaml
name: Welcome new issues

on:
  issues:
    types: [opened]

permissions:
  issues: write

jobs:
  welcome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: "Thanks for opening an issue! 👋 Someone will take a look soon."
            })
````

Test it: open a new issue in the repo, wait half a minute, and refresh. A comment appears.

### 🔎 What's new here

- `uses:` means "use a ready-made Action." `actions/github-script@v7` is published by GitHub itself.
- `permissions:` tells GitHub what the workflow is allowed to touch. It only needs permission to write issue comments, nothing more. That's a safe habit: **give only the permissions required.**

## 🧰 Start from a template

You don't have to write workflows from scratch.

1. Click the **Actions** tab.
2. Click **New workflow**.
3. Browse the ready-made suggestions, and click **Configure** on one that looks interesting.
4. Read it. Edit if you need to. Click **Commit changes**.

Reading a template is also a great way to learn.

## 🪲 When a workflow fails

1. Click the **Actions** tab and open the red run.
2. Click the failed job, then the step with the red mark.
3. Read the **last few lines** of the log. The error is usually right there.
4. Edit the workflow file, commit, and try again.

Common causes:

| Symptom | Likely reason |
|---------|---------------|
| "Invalid workflow file" | Indentation or a missing colon. Compare closely with the example. |
| Nothing runs | The file isn't in `.github/workflows/`, or the trigger doesn't match what you did. |
| "Resource not accessible by integration" | The workflow needs a `permissions:` line. |
| The schedule doesn't fire | Scheduled runs are on the default branch only, and may be delayed. |

To run again without changing anything, open the run and click **Re-run all jobs**.

## 🔐 Secrets (a short, safe introduction)

Some automations need a password or key. Never write one in a workflow file. Store it as a **secret**:

1. In your repo, open **Settings → Secrets and variables → Actions**.
2. Click **New repository secret**, give it a name and value, and save.
3. A workflow can then use it, and GitHub hides its value in the logs.

As a beginner, you can skip secrets entirely. Just remember the rule: **a password should never appear in a file you commit.** Chapter 16 has more.

## 🛡️ Safety notes

- **Only use Actions you trust.** Prefer ones from `actions/` (published by GitHub) or well-known authors, and read what they do.
- **Be careful with pull requests from strangers.** A workflow can run code. GitHub holds back workflows from first-time contributors until someone approves them, which is a good thing.
- **Mind your limits.** Public repositories get generous free minutes. Private repositories get a monthly free allowance. Check **Settings → Billing** if you run many jobs.
- **Switch things off** you don't need: on the **Actions** tab, choose a workflow, click the **...** menu, and pick **Disable workflow**.

## 📛 A status badge

You can show whether your workflow is passing on your README:

1. Open the **Actions** tab and choose the workflow.
2. Click the **...** menu at the top right, then **Create status badge**.
3. Copy the Markdown and paste it into your README.

## 🛠️ Try it

1. Add the **Say Hello** workflow and read its output in the Actions tab.
2. Add the **manual** version and press **Run workflow**.
3. Add the **welcome** workflow, open an issue, and watch the comment appear.
4. Break a workflow on purpose (remove a colon), see the red mark, and fix it.
5. **Bonus:** browse **Actions → New workflow** and read two templates.

## ✅ Checkpoint

- [ ] I can explain a workflow, an event, a job, and a step.
- [ ] I created a workflow file in `.github/workflows/`.
- [ ] I can find a run, open its log, and spot the error.
- [ ] I know that secrets never belong in files.

---

Previous: [Chapter 14](14-profile-and-portfolio.md) · Next: **[Chapter 16: Security & Privacy](16-security-and-privacy.md)**
