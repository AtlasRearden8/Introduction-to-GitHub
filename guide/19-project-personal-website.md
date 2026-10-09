# Chapter 19: Project 1: Your Personal Website 🚀

🎯 **Goals:** Build and publish a personal website, using nearly everything you've learned so far: repositories, GitHub Desktop, branches, pull requests, issues, Markdown, and GitHub Pages. This is a guided project. Go at your own pace, and have fun with it.

⏱️ **Time:** about 90 minutes, split across a few sessions if you like.

**What you'll end up with:** a free website at `https://YOUR-USERNAME.github.io` with a home page, an About page, a Projects page, and a Contact page, all editable from your own computer.

---

## 🗺️ The plan

| Step | What you'll do | Skills used |
|------|----------------|-------------|
| 1 | Decide what your site is for | Planning |
| 2 | Create the repository | Chapter 3 |
| 3 | Publish a first page | Chapter 13 |
| 4 | Bring it to your computer | Chapter 6 |
| 5 | Build the pages on a branch | Chapters 7 and 8 |
| 6 | Review and merge with a pull request | Chapter 8 |
| 7 | Polish, test, and share | Chapter 13 |

> 💡 You'll even track your own to-do list with **issues**. Real projects work this way.

## 🧠 Step 1: Decide what your site is for

Grab a piece of paper or open a note and answer these:

1. **Who is it for?** (Future employers? Friends? People who might hire you? Fans of your work?)
2. **What should they learn in 10 seconds?** (Who you are and what you do.)
3. **What do you want them to do next?** (Read your work? Contact you? Follow you?)
4. **Which pages do you need?**

A good starter set:

| Page | Purpose |
|------|---------|
| **Home** | A friendly welcome and a one-sentence "who I am" |
| **About** | Your story, interests, and skills |
| **Projects** or **Work** | The things you've made, with links |
| **Contact** | How to reach you |

> 🔒 **Decide what you're happy to publish.** Your site is public. You don't have to include your photo, your last name, your city, or your email address. A contact form link or a social profile link works too.

## 📦 Step 2: Create the repository

1. Click **+ → New repository**.
2. For **Repository name**, type `YOUR-USERNAME.github.io`, with your exact GitHub username (all lowercase).
3. Make it **Public**.
4. Tick **Add a README file**.
5. Click **Create repository**.

GitHub treats this name specially. It's your **user site**.

## 🌐 Step 3: Publish a first page

Before anything fancy, make sure publishing works.

1. Click **Add file → Create new file**, name it `index.md`, and type:

````markdown
# Hello, world!

My website is coming soon.
````

2. Commit it.
3. Go to **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then **main** and **/ (root)**, then **Save**.
4. After a minute or two, visit `https://YOUR-USERNAME.github.io`.

You should see your page. If you see a **404**, wait a bit and check Chapter 13's troubleshooting table.

## 📋 Step 4: Make a to-do list with issues

Real projects track their work. Let's do the same:

1. On your repo, click **Issues → New issue** and create these (one issue each):
   - `Add a theme`
   - `Write the About page`
   - `Write the Projects page`
   - `Write the Contact page`
   - `Add a photo or picture`
   - `Check the site on a phone`
2. Optional: create a **Project board** with columns **To do**, **Doing**, **Done**, and add the issues (Chapter 9).

You'll tick these off as you go.

## 💻 Step 5: Bring it to your computer

1. In GitHub Desktop, choose **File → Clone repository...**
2. Pick `YOUR-USERNAME.github.io` and click **Clone**.
3. Open the project folder: **Repository → Show in Explorer** (Windows) or **Show in Finder** (Mac).
4. Open it in your editor: **Repository → Open in** *(your editor)*.

## 🌿 Step 6: Work on a branch

Even solo, branches keep `main` safe, meaning your published site never shows half-finished work.

1. In GitHub Desktop, click **Current branch → New Branch**.
2. Name it `build-site` and click **Create branch**.

### 🎨 Add a theme

Create a file called `_config.yml` in your project folder:

```yaml
theme: jekyll-theme-minimal
title: Your Name
description: A short line about you
show_downloads: false
```

Replace `Your Name` and the description. (Chapter 13 lists other themes you can try.)

Commit it in GitHub Desktop: Summary `Add theme`, then **Commit to build-site**. Close issue 1 later with the pull request.

### 🏠 Write the Home page

Replace the contents of `index.md`:

````markdown
# Hi, I'm YOUR NAME 👋

I'm a **WHAT YOU DO** who loves **WHAT YOU LOVE**.

Take a look around:

- [About me](about)
- [My projects](projects)
- [Get in touch](contact)
````

Commit: `Write home page`.

### 🙋 Write the About page

Create `about.md`:

````markdown
# About me

[Home](index) · [Projects](projects) · [Contact](contact)

## My story
Two or three sentences about where you're from, what you do, and what you're learning.

## Things I'm good at
- Skill or strength
- Another one
- And another

## Things I love
- Hobbies and interests

## Currently learning
- GitHub (obviously!)
````

Commit: `Add About page`.

### 🧩 Write the Projects page

Create `projects.md`. Include things you've actually made. Your `hello-github` and `markdown-playground` repos count!

````markdown
# Projects

[Home](index) · [About](about) · [Contact](contact)

## 📚 Reading list
A collection of books I want to read. [See it on GitHub](https://github.com/YOUR-USERNAME/hello-github)

## ✍️ Markdown playground
Where I practice formatting. [See it on GitHub](https://github.com/YOUR-USERNAME/markdown-playground)

## 🌱 Coming soon
Something exciting!
````

Commit: `Add Projects page`.

### 📬 Write the Contact page

Create `contact.md`. Pick **only** contact methods you're comfortable sharing.

````markdown
# Contact

[Home](index) · [About](about) · [Projects](projects)

I'd love to hear from you!

- GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)
- Other profile or portfolio: [link](https://example.com)
````

Commit: `Add Contact page`.

### 🖼️ Add a picture

1. Make a folder called `images` in the project folder.
2. Drop one picture in, such as `me.jpg` (or any image you like, such as a favorite photo or your own artwork). Make it a sensible size, since huge photos load slowly.
3. Add it to `about.md`:

````markdown
![A friendly description of the picture](images/me.jpg)
````

4. Commit: `Add picture to About page`.

Look at the **Changes** tab before each commit to make sure only the files you meant are ticked.

### 🔼 Publish the branch

Click **Publish branch** in GitHub Desktop.

## 🔀 Step 7: Open a pull request and review yourself

1. Click **Create Pull Request** in GitHub Desktop. Your browser opens.
2. Title: `Build my personal website`.
3. In the description, list what you did and link the issues so they close when you merge:

````markdown
## What this does
Adds a theme and the Home, About, Projects, and Contact pages.

Closes #1
Closes #2
Closes #3
Closes #4
Closes #5
````

(Use the actual issue numbers.)

4. Click **Create pull request**.
5. Open **Files changed** and read every line as if you were a stranger. Look for typos, broken links, and anything you'd rather not make public.
6. When you're happy, click **Merge pull request → Confirm merge**, then **Delete branch**.

In GitHub Desktop, switch to `main`, click **Fetch origin**, then **Pull origin**.

## ✨ Step 8: Test it like a visitor

Wait a couple of minutes, then open `https://YOUR-USERNAME.github.io`.

- [ ] Every page loads.
- [ ] Every link works. Click them all.
- [ ] Pictures show, and they have alt text.
- [ ] It looks good on your **phone**.
- [ ] Nothing private is visible.
- [ ] The text is easy to read.
- [ ] You spelled your own name correctly.

Close the last issue (`Check the site on a phone`) once you've tested it.

## 🎁 Step 9: Share it!

- Add the address to your **GitHub profile**: **Edit profile → Website** (Chapter 14).
- Link it from your **profile README**.
- Send it to a friend. A real reader is the best test.

## 🌟 Stretch goals

Choose a few:

| Idea | How |
|------|-----|
| **A blog** | Change `theme` to `minima`. Create a folder `_posts` and add files named like `2026-10-09-my-first-post.md`, starting with three lines of front matter (`---`, `title: My first post`, `---`). Posts appear on your home page. |
| **A custom domain** | Chapter 13 explains it. |
| **A favicon** | Add a small `favicon.ico` image to the root. |
| **Better navigation** | Put the same one-line menu at the top of every page. |
| **A 404 page** | Add `404.md` with a friendly message. |
| **A "Now" page** | `now.md` with what you're focused on this month. |
| **A resume page** | Add your résumé, and a PDF to download. |

## 🧯 Stuck?

- **The site shows my README instead of my page:** You need `index.md` (or `index.html`) in the main folder.
- **A page gives 404:** The file name must match the link. `about.md` becomes `/about`. Check spelling and capitals.
- **The theme didn't change:** Check `_config.yml` for typos and that it's in the root folder. Look at the **Actions** tab for a red mark.
- **My image is missing:** The path and capitalization must match exactly. Make sure you committed the image and pushed.
- **I forgot to switch branches:** Chapter 12 shows how to move a commit.

## ✅ Checkpoint

- [ ] My site is live at `YOUR-USERNAME.github.io`.
- [ ] It has Home, About, Projects, and Contact pages.
- [ ] I built it on a branch and merged it with a pull request.
- [ ] I tracked the work with issues.
- [ ] I've shared it with someone.

---

Previous: [Chapter 18](18-more-level-ups.md) · Next: **[Chapter 20: Project 2: A Team Project](20-project-team.md)**
