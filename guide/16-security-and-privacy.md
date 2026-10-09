# Chapter 16: Security & Privacy 🔒

🎯 **Goals:** Keep your account, your projects, and your personal information safe. This chapter is a friendly checklist. You can do almost everything in it in about half an hour, and you'll be ahead of most people on the internet.

---

## 🧭 The big picture

Security on GitHub comes down to four questions:

1. **Can someone sneak into my account?** (Account security)
2. **Can someone see things I didn't mean to share?** (Privacy and visibility)
3. **Did I leave any passwords in my files?** (Secrets)
4. **Can I trust what I'm using and running?** (Trust)

You'll tackle each one.

## 🔐 Part 1: Lock down your account

### Strong, unique password

- Use a **long** password (a phrase of several random words is great).
- Use one that **you don't use anywhere else.** If another website leaks your password, attackers try it on GitHub.
- Use a **password manager** to remember it. Most browsers have one built in, and dedicated ones are even better.

### Two-factor authentication (2FA)

You turned this on in Chapter 2. Let's make it stronger:

1. Click your profile picture, then **Settings → Password and authentication**.
2. Check that **Two-factor authentication** says **Enabled**.
3. Add **more than one method** so you have a backup: an authenticator app plus a **passkey** or a security key.
4. Click **View your recovery codes** and make sure you've **saved them somewhere safe** (like your password manager, or printed in a drawer).

### Passkeys

A **passkey** lets you sign in with your fingerprint, face, or device PIN instead of typing a password. They can't be tricked by fake websites. If you see **Add a passkey**, it's well worth setting up.

### Review where you're signed in

1. **Settings → Sessions** shows every device and browser that's signed in.
2. If anything looks unfamiliar, click **Revoke**.

### Review your email addresses

**Settings → Emails.** Remove any address you no longer own. Keep one you check regularly, because GitHub sends security alerts there.

## 🙈 Part 2: Control what people can see

### Public or private?

| | Public repository | Private repository |
|---|---|---|
| **Who can see it** | Everyone on the internet | Only you and people you invite |
| **Search engines** | Can find it | Can't |
| **Good for** | Work you want to share | Practice, drafts, personal notes |
| **Pages site (free plan)** | Yes | No |

**Rule of thumb:** when in doubt, start **private**. You can make something public later, whenever you're ready.

### Change a repository's visibility

1. Open the repository and click **Settings**.
2. Scroll to the **Danger Zone** at the bottom.
3. Click **Change repository visibility** and follow the prompts.

> ⚠️ Making a repository public publishes **its entire history**, including old versions of files. Look through your commits first (the **History** tab in GitHub Desktop, or the clock icon on a file) to be sure nothing private is hidden in the past.

### Keep your email private

1. **Settings → Emails.**
2. Tick **Keep my email addresses private**.
3. Copy the `...@users.noreply.github.com` address shown.
4. In GitHub Desktop, open the settings, go to the **Git** tab, and use that address as your **Email** (Chapter 2).

If you ever see **Block command line pushes that expose my email**, you can tick it too. It's an extra safeguard.

### What's on your profile?

Open your profile in a private browsing window. Is there anything on it, such as a location, a company, or a photo, that you'd rather not share? Edit it (Chapter 14).

## 🗝️ Part 3: Never commit secrets

A **secret** is anything that proves who you are or gives access to something:

- passwords
- API keys and tokens (long strings of letters and numbers)
- private keys and certificate files
- database addresses with passwords in them
- anything marked "do not share"

**Why it's dangerous:** a commit lasts forever in the project history. Even if you delete the file in a later commit, the secret is still in the older one. Automated programs scan public repositories constantly, looking for keys. A leaked key can be found and misused within minutes.

### How to avoid it

- **Look before you commit.** In GitHub Desktop's **Changes** tab, read the green and red lines. Do you see a password? Untick that file.
- **Ignore private files.** Right-click a file in **Changes** and choose **Ignore file**, so it never shows up again.
- **Keep secrets out of your project folder** altogether, if you can.
- **Use a password manager** to store keys, not a text file in a repo.

### GitHub helps you

- **Secret scanning** watches for known kinds of keys and tokens. For public repositories it is on automatically, and GitHub may warn the service that issued the key.
- **Push protection** can **block** a push that contains a recognized secret, and tells you what it found. If you see it, take it seriously.
- You can see or adjust these under **Settings → Code security** (the exact options depend on your repository and plan).

### If you do leak a secret

1. **Assume it's compromised.** Don't wait.
2. **Revoke or replace it right away** at the service that issued it. Change the password or delete the key and make a new one. This is the step that actually protects you.
3. **Remove it from the project** (delete the file and commit).
4. Understand that **the old commits still contain it.** Cleaning history takes advanced tools, so see GitHub's guide **Removing sensitive data from a repository**, or ask someone experienced.
5. **Check for misuse** (unexpected charges or activity) at the affected service.

Chapter 12 has the step-by-step in "Situation 11".

## 🧹 Part 4: Personal information

Think twice before putting these in **any** repository, especially a public one:

| Don't share | Why |
|-------------|-----|
| Home address, phone number, birth date | Easy to misuse |
| Other people's private details (names, photos, messages) | They didn't agree to it |
| Customer, client, student, or patient information | Often legally protected |
| Financial or identity numbers | Can lead to fraud |
| Anything under an agreement not to share | You could break a promise or a contract |
| Photos with hidden location data | Some photos record where they were taken |

If you're working with data about people, ask whether you're allowed to share it. If you aren't sure, keep the repository **private** and ask.

### Respect other people's work

- Don't upload other people's **copyrighted** material (books, songs, paid courses, photos you don't have the right to use).
- **Credit** what you borrow, and respect licenses (Chapter 10).
- When using someone else's picture, check that you have permission, or use free-to-use libraries and give credit as the license requires.

## 🎣 Part 5: Spotting tricks and scams

Attackers often try to trick **people** rather than computers. Watch out for:

- **Urgent emails** that say your account will be closed unless you click something now.
- **Fake sign-in pages** that look like GitHub but have a slightly different address.
- **Messages asking for your password, a 2FA code, or a recovery code.** GitHub staff will never ask for these.
- **A stranger who says "just run this" or "just install this"** and gives you a link.
- **Job offers or "collaboration" requests** that need you to download and run files.

### Safe habits

- **Check the address bar.** It should say `github.com`.
- **Go straight to github.com** (type it yourself or use a bookmark) instead of clicking links in messages.
- **Never share a code** that was sent to your phone or email.
- If a pull request or issue comment includes a strange link, **don't click it.**
- When in doubt, **ask someone you trust** before acting.

## 🔌 Part 6: Third-party apps and access

Over time you may have given apps permission to use your account, such as a sign-in with GitHub or a tool that reads your repositories.

1. **Settings → Applications.**
2. Open **Authorized OAuth Apps** and **Authorized GitHub Apps**.
3. **Revoke** anything you don't recognize or no longer use.

Also check **Settings → Developer settings → Personal access tokens** (the page may look technical). If you see any you didn't create, **delete** them. You don't need personal access tokens for anything in this guide.

## 📦 Part 7: Trusting what you use

- **Prefer well-known sources.** A project with lots of users, recent activity, and a clear README is usually safer than an unknown one.
- **Read before you run.** Never copy and run something you don't understand.
- **Be careful with downloads.** Get software from the official website, not a random link.
- **Keep an eye on warnings.** If GitHub's **Dependabot** alerts you that a tool your project uses has a known problem, read it. Turn alerts on under **Settings → Code security**.

## 🏛️ Part 8: Tell people how to report problems

If you build something others use, add a short **security policy**:

1. In your repository, click **Add file → Create new file**.
2. Name it `SECURITY.md`.
3. Write how someone can report a problem **privately**, for example, an email address.

````markdown
# Security

If you find a security problem, please email me at SECURITY-EMAIL rather than
opening a public issue. I'll reply within a week.
````

## 🚨 What to do if you think your account was hacked

Don't panic. Take these steps in order:

1. **Change your GitHub password** right away, from a device you trust.
2. **Revoke all sessions:** **Settings → Sessions**, then sign out everywhere.
3. **Check 2FA:** make sure it's on, and generate **new recovery codes**.
4. **Review recent activity:** **Settings → Security log** shows what happened and when.
5. **Revoke unknown apps and tokens** (Part 6).
6. **Check your repositories** for changes you didn't make, and use **Revert** on anything suspicious (Chapter 12).
7. **Change your email password** too, in case it was the way in.
8. If you can't get in, use **Forgot password** and your **recovery codes**, and contact GitHub Support.

## 📋 Your security checklist

Copy this into a note or an issue and tick it off:

- [ ] Strong, unique password in a password manager
- [ ] 2FA turned on, with more than one method
- [ ] Recovery codes saved safely
- [ ] A passkey added (if available)
- [ ] Sessions reviewed
- [ ] Email kept private, noreply address used in GitHub Desktop
- [ ] Repositories set to the right visibility
- [ ] Nothing private in any public repository or its history
- [ ] Unused apps and tokens revoked
- [ ] Dependabot alerts turned on
- [ ] I know what to do if a secret leaks

## 🛠️ Try it

1. Walk through the checklist above and tick what you can.
2. Open your profile in a private window and review what's public.
3. Look through the **History** of a public repo for anything you'd rather not have shared.
4. Revoke one app or session you don't use.

## 🧯 Stuck?

- **I can't find Sessions or Security log:** They're in **Settings**, in the left column under **Access** or **Archives**. GitHub rearranges the menu now and then, so look for the names.
- **I lost my 2FA device:** Use a saved recovery code. If you have none, follow GitHub's account recovery steps, which require extra proof of identity and can take a while. This is why saving codes matters.
- **I made a repository public by mistake:** Switch it back to private right away in **Settings → Danger Zone**. Then treat anything in it as seen, and change any passwords it contained.

## ✅ Checkpoint

- [ ] My account has a strong password and 2FA with a backup.
- [ ] I know the difference between public and private, and I chose well.
- [ ] I know what a secret is and how to avoid committing one.
- [ ] I can spot a scam message.
- [ ] I know what to do if something goes wrong.

---

Previous: [Chapter 15](15-github-actions.md) · Next: **[Chapter 17: Using AI With GitHub](17-ai-and-github.md)**
