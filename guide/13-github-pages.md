# Chapter 13: GitHub Pages: Build a Website 🌐

🎯 **Goals:** Publish a real website for free, straight from a repository. You'll make a simple page, give it a theme, add pictures and extra pages, and learn how to fix the usual snags.

This whole chapter works in your web browser, with a little help from GitHub Desktop if you prefer to edit files on your computer.

---

## 💡 What is GitHub Pages?

**GitHub Pages** takes the files in a repository and turns them into a website that anyone can visit. There's no server to rent and nothing to install. Every time you save a change to the repo, the website updates.

People use it for:

- a personal website or online résumé
- a portfolio of their work
- documentation for a project
- a blog
- an event page or a class website

This very guide is published with GitHub Pages.

## 🏠 Two kinds of Pages sites

| Kind | Repository name | Address |
|------|-----------------|---------|
| **Project site** | Any name, like `my-first-site` | `https://YOUR-USERNAME.github.io/my-first-site/` |
| **User site** | Exactly `YOUR-USERNAME.github.io` | `https://YOUR-USERNAME.github.io/` |

You can have **one** user site and as many project sites as you like. We'll start with a project site, then make a user site in Chapter 19.

> 🔓 **Remember:** On the free plan, a Pages site needs a **public** repository, and a published site is visible to **everyone on the internet**. Don't put anything private in it.

## 🚀 Your first site in five minutes

1. Click **+ → New repository**.
2. Name it `my-first-site`. Make it **Public**. Tick **Add a README file**. Click **Create repository**.
3. On the repo page, click **Add file → Create new file**.
4. Name it `index.md`. (This is the front page of your site.)
5. Paste in:

````markdown
# Hello, world! 👋

Welcome to my very first website. I made it with **GitHub Pages**.

## About me
I'm learning how to use GitHub, one click at a time.

## My favorite things
- Good food
- Good books
- Good friends

[Visit GitHub](https://github.com)
````

6. Click **Commit changes...**, write `Add home page`, and commit.
7. Click **Settings** (top of the repo), then **Pages** in the left menu.
8. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
9. Under **Branch**, choose **main** and the **/ (root)** folder, then click **Save**.
10. Wait one or two minutes, then refresh the page. A banner appears: **Your site is live at...** with the address.

Click the link. You have a website.

**Screenshot:** The **Pages** settings with `main` and `/ (root)` chosen and the green "Your site is live" banner.
{ .shot }

### 🔄 Updating it

Edit `index.md` (the pencil icon), commit, and wait a minute. The live site changes. You can edit on github.com, or in GitHub Desktop on your computer and click **Push origin**. Either way works.

### 👀 Watching it build

Every update runs a small automatic job. Click the **Actions** tab to see it: a yellow dot while it's working, then a green check when your changes are live. A red mark means something went wrong. Click it to read why.

## 🎨 Give it a theme

Right now the site is plain. GitHub can wrap it in a ready-made theme.

1. Click **Add file → Create new file**.
2. Name it `_config.yml`. (The underscore matters.)
3. Type:

```yaml
theme: jekyll-theme-cayman
title: My First Site
description: A site I built with GitHub Pages
```

4. Commit it, and wait a minute.

Reload your site: it now has a colorful header and a clean layout. Other themes you can swap in (change the `theme:` line):

| Theme name | Look |
|------------|------|
| `jekyll-theme-minimal` | Clean sidebar layout |
| `jekyll-theme-slate` | Dark and bold |
| `jekyll-theme-midnight` | Dark with a glow |
| `jekyll-theme-hacker` | Green on black |
| `jekyll-theme-architect` | Structured and professional |
| `jekyll-theme-leap-day` | Friendly and warm |
| `jekyll-theme-time-machine` | Retro |

You can preview them at <https://pages.github.com/themes/>. Keep the exact spelling. A mistake will make the build fail, and you'll see a red mark in **Actions**.

## 📄 Add more pages

Every `.md` file you add becomes a page.

1. Create `about.md` with some text.
2. Your site now has a page at `https://YOUR-USERNAME.github.io/my-first-site/about`.
3. Link to it from your home page:

```markdown
[About me](about)
```

Try a few: `projects.md`, `contact.md`, `blog.md`. Link them together so visitors can click around.

### 🧭 A simple menu

Put a line at the top of each page:

```markdown
[Home](index) · [About](about) · [Projects](projects) · [Contact](contact)
```

## 🖼️ Add pictures

1. Click **Add file → Upload files** and drag a picture in. Commit it.
2. Put images in a folder to stay tidy: when you create or upload, use a name like `images/me.jpg`.
3. Show it on a page:

```markdown
![A smiling person in a garden](images/me.jpg)
```

Always write real alt text between the brackets. It helps people who use screen readers, and it shows if the picture can't load.

**Tip:** Resize large photos before uploading. Pages load faster and are kinder to phones. Most computers have a built-in way to shrink a picture, and free sites like Squoosh (<https://squoosh.app>) work well.

## 🧱 Go further with HTML

Markdown is easy, but sometimes you want more control. You can mix in HTML, the language web pages are made of. Create `index.html` instead of `index.md`, or write HTML inside your Markdown files.

A tiny but complete HTML page:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Page</title>
    <style>
      body { font-family: sans-serif; max-width: 40rem; margin: 3rem auto; padding: 0 1rem; }
      h1 { color: rebeccapurple; }
    </style>
  </head>
  <body>
    <h1>Hello!</h1>
    <p>This page is written in HTML.</p>
  </body>
</html>
```

Notes:

- If a repository has **both** `index.html` and `index.md`, the HTML one wins.
- A site with a **theme** only styles Markdown pages. A plain `index.html` shows exactly what you wrote.
- The `<meta name="viewport">` line makes your page look right on phones.

You don't need to learn HTML to have a good site. Many beautiful Pages sites are all Markdown.

## 🌍 Your own address (custom domain)

Instead of `username.github.io`, you can use an address you own, like `www.yourname.com`.

1. Buy a domain from a domain seller. This costs money, usually around ten to fifteen dollars a year.
2. In your repo, go to **Settings → Pages**. Under **Custom domain**, type your domain and click **Save**.
3. At your domain seller, add the **DNS settings** that GitHub's documentation lists (a short list of address records).
4. Back in **Pages**, tick **Enforce HTTPS** once it becomes available. This makes your site secure.

DNS can take from a few minutes to a day to settle. GitHub's guide, **Configuring a custom domain for your GitHub Pages site**, has the exact records. A custom domain is optional. The free address is perfectly respectable.

## 🧹 Keep it tidy

- **Pick a good repository name,** since it appears in the address.
- **Add a `README.md`** so visitors to the repo (not the site) understand what it is.
- **Use lowercase file names without spaces,** like `my-photo.jpg`.
- **Don't store secrets or private files.** Everything in a public repo is public.
- **Add a `404.md`** if you want a friendly "page not found" message.

## 🧯 Troubleshooting

| Problem | What to try |
|---------|-------------|
| **404 – page not found** | Wait a couple of minutes. Check **Settings → Pages** says your site is live. Make sure the file is named `index.md` or `index.html` in the root folder. |
| **The site doesn't update** | Open **Actions**. A failed build shows a red mark. Click it to read the error. |
| **A picture is broken** | File names are case-sensitive. `Photo.JPG` and `photo.jpg` are different. Check the path, and that you committed the file. |
| **The theme isn't applied** | Check `_config.yml` for typos. The file must be in the root folder. |
| **Build error about YAML** | Indentation or a missing space after a colon. In YAML, write `theme: name` with a space. |
| **Links lead to the wrong place** | On a project site, include the repo name in full links, or use relative links like `about` and `images/me.jpg`. |
| **The Pages option is missing** | On the free plan, the repository must be **public**. |

## 🛠️ Try it

1. Publish `my-first-site` with a home page.
2. Add a theme with `_config.yml`.
3. Add an `about` page and link the two together.
4. Add a picture with alt text.
5. Open your site on your phone and check that it looks good.
6. **Bonus:** change the theme and see how the look changes. Pick your favorite.

## ✅ Checkpoint

- [ ] I published a site with GitHub Pages and I know its address.
- [ ] I can add pages and pictures.
- [ ] I can change the theme.
- [ ] I know how to read the **Actions** tab when something goes wrong.
- [ ] I understand that my site is public.

---

Previous: [Chapter 12](12-undoing-mistakes.md) · Next: **[Chapter 14: Your Profile & Portfolio](14-profile-and-portfolio.md)**
