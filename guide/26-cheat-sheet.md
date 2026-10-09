# Chapter 26: Cheat Sheet 📄

Bookmark this page. Everything you do in this guide, and where to click, in one place.

---

## 🛠️ One-time setup

| Task | Where |
|------|-------|
| Install GitHub Desktop | <https://desktop.github.com> |
| Sign in | Welcome screen, **Sign in to GitHub.com** |
| Check your name and email | Settings, **Git** tab |
| Set the default branch name | Settings, **Git** tab, **Default branch name**, then `main` |
| Pick your editor | Settings, **Integrations** tab, **External editor** |

*Settings is **File → Options** on Windows and **GitHub Desktop → Settings** on Mac.*

## 🆕 Starting a project

| I want to... | Do this |
|--------------|---------|
| Make a new project on my computer | **File → New repository...** |
| Download a project from GitHub | **File → Clone repository...** |
| Clone from a web page | Green **Code** button, then **Open with GitHub Desktop** |
| Put a computer-only project on GitHub | Click **Publish repository** (top right) |
| Switch to another project | **Current repository** (top left) |
| Open the project's folder | **Repository → Show in Explorer** (Windows) or **Show in Finder** (Mac) |
| Open the project in my editor | **Repository → Open in** *(your editor)* |

## 🔁 The daily loop

| Step | Where |
|------|-------|
| 1. Get the latest | Click **Fetch origin**, then **Pull origin** if it appears |
| 2. Edit your files | In your editor, then save |
| 3. Review what changed | **Changes** tab: green is added, red is removed |
| 4. Choose files | Tick or untick the checkboxes |
| 5. Describe the change | Type a **Summary** |
| 6. Save the snapshot | Click **Commit to** *(branch name)* |
| 7. Send it to GitHub | Click **Push origin** |

## 🕰️ Looking at history

| I want to... | Do this |
|--------------|---------|
| See every past commit | **History** tab |
| See what a commit changed | Click it in **History** |
| See older versions of one file | On github.com, open the file and click **History** |

## 🌿 Branches

| I want to... | Do this |
|--------------|---------|
| See which branch I'm on | Look at **Current branch** (top bar) |
| Make a new branch | **Current branch → New Branch** |
| Switch branches | **Current branch**, then click the branch |
| Merge a branch into this one | **Branch → Merge into current branch...** |
| Bring `main` up to date in my branch | **Branch → Update from main** |
| Delete a branch | **Branch → Delete...** |
| Send a new branch to GitHub | Click **Publish branch** |
| Start a pull request | Click **Create Pull Request**, or **Branch → Create pull request** |

## 🧯 Undo and recover

| I want to... | Do this |
|--------------|---------|
| Throw away unsaved edits | Right-click the file in **Changes**, then **Discard Changes...** |
| Leave a file out of a commit | Untick it |
| Undo my last commit (not pushed) | **Undo** button at the bottom of the **Changes** tab |
| Safely undo a pushed commit | **History**, right-click the commit, **Revert Changes in Commit** |
| Pause my work to switch branches | Choose **Leave my changes** when asked |
| Cancel a merge | **Abort merge** |
| Undo a merged pull request | **Revert** button on the pull request page |
| Ignore a file | Right-click it in **Changes**, then **Ignore file** |

## 🔀 Pull requests on github.com

| I want to... | Do this |
|--------------|---------|
| Open a pull request | **Create Pull Request** in GitHub Desktop, then **Create pull request** on the website |
| Look at the changes | **Files changed** tab |
| Comment on one line | Hover over the line and click the blue **+** |
| Merge it | Green **Merge pull request** button |
| Clean up | **Delete branch** |
| Link it to an issue | Write `Closes #12` in the description |

## 🍴 Issues, forks, and more

| I want to... | Do this |
|--------------|---------|
| Create an issue | **Issues** tab, then **New issue** |
| Copy someone else's project | **Fork** button (top right of the repo page) |
| Catch my fork up | **Sync fork → Update branch**, then **Fetch origin** and **Pull origin** |
| Invite a teammate | **Settings → Collaborators → Add people** |
| Publish a website | **Settings → Pages** |

## ✍️ Markdown quick reference

```markdown
# Heading 1
## Heading 2
**bold**  *italic*  ~~strike~~
- bullet        1. numbered
[link text](https://url)   ![alt](image.png)
`inline code`
> quote
- [ ] task   - [x] done
```

## ✨ GitHub text tricks

| Type | Result |
|------|--------|
| `#12` | Link to issue or PR 12 |
| `@name` | Mention a person |
| `Closes #12` (in a PR) | Closes issue 12 automatically when the PR is merged |
| `:tada:` | A party popper emoji |

## 🫶 Reviews and teamwork

| I want to... | Do this |
|--------------|---------|
| Ask for a review | Pull request sidebar, gear next to **Reviewers** |
| Leave a line comment | Hover the line, click the blue **+**, choose **Start a review** |
| Suggest exact wording | Click the **±** icon in the comment box |
| Mark a file as read | Tick **Viewed** at the top of it |
| Finish a review | **Review changes**, pick **Comment**, **Approve**, or **Request changes**, then **Submit review** |
| Ask for another look | Click the circular arrows next to the reviewer's name |
| Require approvals | **Settings → Branches** (or **Rules → Rulesets**) |
| Pre-fill pull requests | Create `.github/pull_request_template.md` |

## 🌍 Websites and profiles

| I want to... | Do this |
|--------------|---------|
| Publish a site | **Settings → Pages**: **Deploy from a branch**, `main`, `/ (root)` |
| Make the home page | A file named `index.md` or `index.html` in the main folder |
| Add a theme | `_config.yml` containing `theme: jekyll-theme-minimal` |
| Get a short address | Name the repo `YOUR-USERNAME.github.io` |
| Make a profile README | Public repo named exactly like your username, with a `README.md` |
| Pin projects | Your profile, **Customize your pins** |
| Add a topic or description | The gear next to **About** on the repo page |
| Show a custom domain | **Settings → Pages → Custom domain** |

## 🤖 Automation

| I want to... | Do this |
|--------------|---------|
| See workflow runs | **Actions** tab |
| Create a workflow | **Add file → Create new file**, name `.github/workflows/NAME.yml` |
| Run one by hand | Add `workflow_dispatch:` under `on:`, then **Run workflow** |
| Run on a schedule | `schedule:` with a `cron:` line (times are UTC) |
| Fix a failure | Open the red run, click the failed step, read the last lines |

## 🔒 Safety checks

| I want to... | Do this |
|--------------|---------|
| See where I'm signed in | **Settings → Sessions** |
| Keep my email private | **Settings → Emails**, tick **Keep my email addresses private** |
| Change a repo's visibility | **Settings → Danger Zone → Change repository visibility** |
| Stop a secret reaching GitHub | Untick or **Ignore** the file before you commit |
| Review app access | **Settings → Applications** |
| Turn on alerts | **Settings → Code security** |

## 🏷️ Releases, wikis, and extras

| I want to... | Do this |
|--------------|---------|
| Publish a version | **Releases → Draft a new release**, create a tag like `v1.0.0` |
| Edit in the browser | Press `.` on a repository page |
| Share a snippet | <https://gist.github.com> |
| Search | Press `/`, and try `is:open label:"good first issue"` |
| See all shortcuts | Press `?` on any page |

## ✍️ Extra Markdown

````markdown
> [!NOTE]
> A callout box. Also TIP, IMPORTANT, WARNING, CAUTION.

<details>
<summary>Click to open</summary>

Hidden text.

</details>

![Alt text](images/photo.png)

Footnote.[^1]

[^1]: The note.
````

## 🏁 The GitHub flow in seven steps

1. **Fetch origin** and **Pull origin** (start fresh).
2. **Current branch → New Branch**.
3. Edit your files and save.
4. Write a **Summary** and **Commit**.
5. **Publish branch**.
6. **Create Pull Request**, then review and merge on github.com.
7. Switch to `main`, then **Fetch origin** and **Pull origin**. Repeat.

---

Previous: [Chapter 25](25-desktop-menu-tour.md) · Next: **[Chapter 27: Templates & Snippets](27-templates-and-snippets.md)**
