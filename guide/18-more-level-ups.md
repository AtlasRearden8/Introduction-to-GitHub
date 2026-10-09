# Chapter 18: More Level-Ups 🎮

🎯 **Goals:** Discover the rest of GitHub's toolbox: editing in the cloud, releases, gists, notifications, the mobile app, wikis, and the keyboard shortcuts that make you faster. Each section stands alone, so pick whatever sounds useful.

---

## ⌨️ 1. Edit in your browser with github.dev

On any repository page, press the **period** key (`.`). A lightweight code editor opens in your browser. It looks like Visual Studio Code but there's nothing to install.

- Edit several files at once.
- Use the **Source Control** panel (the branching icon on the left) to write a commit message and commit.
- Great for quick edits on a computer where you can't install anything, like at school or a library.

You can also change `github.com` to `github.dev` in the address bar for the same effect.

## ☁️ 2. Codespaces: a computer in the cloud

A **codespace** is a full computer that lives in GitHub's cloud and is set up for your repository. Open one from **Code → Codespaces → Create codespace on main**.

- It opens in your browser with a file editor and a built-in terminal. You don't need the terminal for this guide, and you can ignore it.
- Everything runs on GitHub's computers, so a slow laptop doesn't matter.
- Free accounts get a monthly allowance of hours. **Stop** a codespace when you finish, and delete ones you don't need (in the **Codespaces** page linked from your profile menu) so the allowance lasts.

For the work in this book, GitHub Desktop and the website are all you need. Codespaces becomes handy later if you start building software.

## 🏷️ 3. Releases: label important versions

A **release** is a named, packaged version of your project, like "Version 1.0" or "Spring 2026 edition", with notes and optional downloads.

1. On your repository page, click **Releases** (right sidebar), then **Draft a new release**.
2. Click **Choose a tag**, type a version like `v1.0.0`, and choose **Create new tag**.
3. Write a **title** and **release notes**. Click **Generate release notes** if you'd like GitHub to list what changed.
4. Drag any files you'd like people to download into the box (a PDF, a zip, a template).
5. Click **Publish release**.

People can now download that exact version, even after you keep changing the project.

### 🔢 A friendly way to number versions

`v1.0.0` has three parts: **major.minor.patch**.

| Change | Bump | Example |
|--------|------|---------|
| Big change that may surprise people | Major | `1.0.0` → `2.0.0` |
| New feature, nothing breaks | Minor | `1.0.0` → `1.1.0` |
| Small fix | Patch | `1.0.0` → `1.0.1` |

## 📝 4. Gists: share a snippet

A **gist** is a mini-repository for sharing one note or snippet. It lives at <https://gist.github.com>.

- Great for sharing a short text, a checklist, or an example when you ask for help.
- Make it **public** (anyone can find it) or **secret** (anyone with the link can see it, but it isn't listed). *Secret* is not *private*, so don't put anything sensitive there.

## 📚 5. Wikis: a library for your project

Some projects keep longer documentation in a **wiki**: a collection of linked pages.

1. Open your repository's **Settings**, scroll to **Features**, and tick **Wikis**.
2. A **Wiki** tab appears. Click **Create the first page**.
3. Write in Markdown, and link pages with `[[Page name]]`.

For small projects, a few Markdown files in the repository (or a Pages site) is usually simpler.

## 💬 6. Discussions: a friendly forum

**Discussions** are for open-ended conversation that isn't a task: questions, ideas, announcements, and thank-yous.

1. In **Settings → Features**, tick **Discussions**.
2. A **Discussions** tab appears. Categories include Q&A, Ideas, and Announcements.

Use Issues for work that someone needs to **do**, and Discussions for talking.

## 🔔 7. Take control of notifications

GitHub can send you a lot of email. Tune it:

1. Click the **bell** icon to see your **notifications inbox**. Mark things done as you go.
2. **Settings → Notifications** lets you choose how you're notified (email, the web, mobile) and about what.
3. On a repository, click **Watch** and choose:
   - **Participating and @mentions:** only things you're part of (a great default).
   - **All activity:** everything. This can get noisy.
   - **Ignore:** nothing.
4. To leave a single conversation, click **Unsubscribe** in the right sidebar of an issue or pull request.

## 📱 8. GitHub on your phone

**GitHub Mobile** is a free app for iPhone and Android. It's perfect for:

- reading and replying to issues and comments
- approving or reviewing a pull request when you're away from your desk
- getting notifications
- using it as your **two-factor authentication** device, so approving a sign-in is one tap

Search "GitHub" in your phone's app store, and check the publisher is GitHub, Inc.

## 🔖 9. Stars and Lists

**Starring** a repository bookmarks it. Click **Star**, then visit your profile and open **Stars** to see them. Make **Lists** (like "Recipes", "Learning", "Inspiration") to keep them organized. It's a handy, free way to collect the projects you love.

## 🔍 10. Search like a pro

The search bar at the top finds almost anything. Narrow results with these tricks:

| Type this | To find |
|-----------|---------|
| `user:your-username` | Only your things |
| `language:markdown` | Markdown files |
| `is:open label:"good first issue"` | Beginner-friendly open issues |
| `in:readme recipes` | Repositories whose README mentions recipes |
| `stars:>500` | Popular repositories |
| `"exact phrase"` | The exact words together |

On a repository page, press **`/`** to focus the search, or **`t`** to find a file by name.

## ⌨️ 11. Keyboard shortcuts

On any GitHub page, press **`?`** to see the shortcuts for that page. Favorites:

| Key | Does |
|-----|------|
| `/` | Focus the search bar |
| `t` | Find a file in a repository |
| `.` | Open the github.dev editor |
| `g` then `i` | Go to Issues |
| `g` then `p` | Go to Pull requests |
| `c` | Create an issue (on the Issues page) |
| `?` | Show all shortcuts |

## 🎓 12. GitHub Education and free extras

- **Students and teachers** can get free access to extra GitHub tools through **GitHub Education** at <https://education.github.com>. You'll need to verify with a school email or document.
- **Maintainers of open-source projects** and other groups may qualify for free upgrades. Check GitHub's current offers.
- **GitHub Skills** (<https://skills.github.com>) offers free, hands-on courses that run inside real repositories.

## 🧭 13. Where to go next

- **GitHub Docs** (<https://docs.github.com>): the official reference for every feature.
- **GitHub Desktop docs** (<https://docs.github.com/en/desktop>): every button in the app, explained.
- **GitHub Community** (<https://github.com/orgs/community/discussions>): ask questions and read answers.
- **Chapter 31** collects more books, courses, and communities.
- **Build something.** The best learning is a real project you care about. Chapters 19–22 walk you through four.

## 🛠️ Try it

Choose at least **three**:

1. Press `.` on a repository and make an edit in github.dev.
2. Publish a release called `v1.0.0` of one of your practice repos.
3. Create a secret gist with a checklist.
4. Change your **Watch** settings on one repository.
5. Star five repositories and sort them into a List.
6. Install GitHub Mobile and use it to approve a sign-in.

## ✅ Checkpoint

- [ ] I know what github.dev, codespaces, releases, gists, and wikis are.
- [ ] I can manage my notifications.
- [ ] I know three keyboard shortcuts.
- [ ] I know where to look for free learning resources.

---

Previous: [Chapter 17](17-ai-and-github.md) · Next: **[Chapter 19: Project 1: Your Personal Website](19-project-personal-website.md)**
