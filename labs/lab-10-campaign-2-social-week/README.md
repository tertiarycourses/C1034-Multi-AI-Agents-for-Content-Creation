# Lab 10 — Campaign 2: Social Media Posts (Demo)

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 2 · Topic 3 · about 50 minutes · slides 109–116**\
**Surface:** Claude Code (agent team) → LinkedIn, Facebook\
**Features:** the publisher kit and its hook · an agent team: creator, designer, Lead · teammates message each other · human approval → you post

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-10 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

Week 1 of the campaign starts Monday. As a demo, one LinkedIn post and one Facebook post, each with a visual — and Rachel's one rule: nothing goes out unless a person approved that exact version.

## Your goal

A demo of Week 1: one LinkedIn and one Facebook post, each with a visual. Copy and design must agree, the Lead must check every claim — and only a person can approve.

## You'll build

two posts with images, reviewed, approved by you and posted by you (or, optionally, through the API) — shown as artifacts, with a Word copy of each

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/social-brief.md`
- `assets/publisher-kit/`
- `assets/publishing-spec.md`
- `assets/approvals-format.csv`
- `assets/connect-accounts.md`
- `assets/env.example`
- `assets/sample-calendar.csv`
- `solution/` — reference files from the verified build (each `.md` with its `.pdf`)
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 10". Run all of this lab's prompts in it.
2. **Get the latest kit** — Copy and paste Prompt A. Claude downloads the newest course files into your folder and starts your website. Your own work stays as it is.
3. **Test the gate** — Ask Claude to approve a post itself. The gate must block it.
4. **Start the team** — After Claude says the kit is up to date, copy and paste Prompt B. The Lead starts two teammates and tells you as each one starts and finishes.
5. **Watch them talk** — The review page opens with a Team chat: the designer asking the creator for each hook, and the Lead's fixes.
6. **Approve as a person** — Review in the artifact (or open the review email and click its link). Click Approve or Request changes on each post, then Copy in the bottom bar and paste into the chat.
7. **Get ready to post** — After you have approved the posts, copy and paste Prompt C. Each post appears with a Copy button for its text, and the folder with the two images opens on your computer.
8. **Post it yourself** — Paste the text, add the image, Post — on LinkedIn and a test Facebook Page. Or stop at the preview.
9. **Optional: post through the apps** — Follow "Optional: post through LinkedIn and Facebook" in this lab's README.

## The prompts

### PROMPT A — Claude Code: get the latest kit

> Bring this studio up to date with the course kit.
> Download each file below from
> https://raw.githubusercontent.com/tertiarycourses/C1034-Multi-AI-Agents-for-Content-Creation/main/labs/horizon-studio/
> into the same place here, replacing the old copy:
> .claude/settings.json; scripts/approve-chat.mjs,
> gate-hook.mjs, lib.mjs, publish.mjs, serve-site.mjs
> and submit.mjs; data/publishing-spec.md,
> channel-formats.md, connect-accounts.md,
> env.example, turning-55-brief.md and
> turning-55-draft.md. Touch nothing else.
> Then add these rules to CLAUDE.md if they are
> missing: every post links to http://localhost:8080/ with
> UTM tags, never a claude.ai artifact link; a person
> approves by typing "approved <id> by <name>" in the
> chat; never ask me to run a command.
> Then start my website and tell me in one line that
> the kit is up to date.

### PROMPT B — Claude Code: the social team

> Create an agent team for Week 1 social from
> data/social-brief.md and strategy/calendar.csv.
> Spawn two teammates using the agent types
> content-creator and creative-designer; you are the
> Lead.
> - content-creator: 1 LinkedIn + 1 Facebook post
>   with linkedin-post, facebook-post and copywriting,
>   one file each in content/social/week-01/, with the
>   frontmatter in data/publishing-spec.md. Each post
>   links to my website, http://localhost:8080/, with
>   UTM tags.
> - creative-designer: one image per post (a rendered
>   card in Horizon colours: LinkedIn 1200 x 627,
>   Facebook 1080 x 1080) with alt text; message the
>   creator for each post's hook before designing. Save
>   each as a PNG beside its post and fill in the
>   post's image and alt lines.
> - You: fact-check and fin-compliance on every post
>   and image; message fixes to the teammate who owns
>   it.
> Before you start, ask me how I will review: in the
> artifact, or by email (then ask for the approver's
> address). When a post passes, submit it for review
> with scripts/submit.mjs. Publish the two posts as
> an artifact. At the top, a Team chat: the messages
> the teammates and you sent each other, in order,
> each with who sent it. Then each post as it will
> look in the feed, with its image and alt text;
> under each post put two
> working buttons (JavaScript): Approve turns the
> card green; Request changes opens a box for my
> note. A bar at the bottom asks my name once, builds
> the exact lines to paste in the chat ("approved
> <id> by <name>", "changes <id>: <note>") and has a
> Copy button that says "Copied - now paste it in the
> chat". Keep the lines on screen in case copying is
> blocked. If I chose email, send ONE review email to
> the approver with Gmail: the artifact link and what
> passed the checks. Send nothing else; publish
> nothing.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT C — Claude Code: ready to post

> For each Week 1 post approved in
> review/approvals.csv, publish a "ready to post"
> artifact: the post text with a Copy button, its
> image, and the steps to post it by hand on LinkedIn
> or our Facebook Page. Then open the folder with the
> two images on my computer. Publish nothing yourself.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Which post do you expect to do best, and why?"
- "What did the Lead send back to the writer, and why?"
- "Is anything here not ready to post? Explain in plain English."

## Optional: post through LinkedIn and Facebook

About 20 minutes, after you have approved the posts. Use test accounts only: your own LinkedIn profile and a test Facebook Page you manage. Skip any post you already posted by hand. The link in each post opens your own website, so it works only on your computer.

1. **Make your key file** — Ask Claude Code: "Make my .env file from data/env.example and open it in a text editor." Your keys go only in this file — never in the chat.
2. **LinkedIn app** — Go to linkedin.com/developers → Create app (link it to a LinkedIn Page; a test Page is fine). Under Products add Share on LinkedIn and Sign In with LinkedIn using OpenID Connect.
3. **LinkedIn key** — Auth → OAuth 2.0 tools → create a token with openid, profile and w_member_social. Paste it after LINKEDIN_ACCESS_TOKEN= in .env and save.
4. **Your LinkedIn ID** — Ask Claude Code: "Look up my LinkedIn author ID with the token in .env and fill it in. Do not show me the token."
5. **Facebook app** — Go to developers.facebook.com → Create app → Business. Open Tools → Graph API Explorer and pick your app. Add pages_manage_posts, pages_read_engagement and pages_show_list, then Generate token and choose your test Page.
6. **Facebook key** — Click Get Page Access Token. Paste it after FB_PAGE_TOKEN= in .env, and your Page ID (Page → About → Page transparency) after FB_PAGE_ID=. Save. This key lasts about an hour, so do it just before you post.
7. **Dry run** — Type: "Do a dry run of publishing the approved Week 1 posts and show each one as an artifact. Wait for my go." Each one should show your key partly hidden (like LITO…), not "missing".
8. **Go** — Type "go" for each post you want live. It appears on LinkedIn or your Facebook Page with its image, and the artifact shows its link.

## Check your work

- [ ] The gate stopped Claude from approving.
- [ ] Two teammates ran; the Lead said when each started and finished.
- [ ] The Team chat shows the designer and the creator messaging each other.
- [ ] Two posts with images from the designer, alt text and UTM links.
- [ ] You reviewed in the artifact or by email and pasted the approval in the chat; the rows show your name and a hash.
- [ ] You posted the approved text and image yourself (or, optionally, through the API after you said go).

## If it goes wrong

- **You got subagents, not a team** — Check you are in the current horizon-studio folder from the course, start a new session and ask for "an agent team" by name.
- **LinkedIn returns 426** — LINKEDIN_VERSION must be a recent YYYYMM.

## Stretch

- Add the growth-analyst to suggest the best posting time per post from channel-benchmarks.csv.
- Link each LinkedIn post to the Lab 8 blog article.

> **Why it matters:** Subagents report to one boss; teammates also talk to each other. A designer who can ask the writer for the hook makes a better image.

## Next

Lab 11 — Campaign 3: Newsletter and a Landing Page. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
