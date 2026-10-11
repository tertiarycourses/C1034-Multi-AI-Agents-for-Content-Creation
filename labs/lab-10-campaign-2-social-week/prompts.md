# Prompts — Lab 10: Campaign 2: Social Media Posts (Demo)

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-10 (one Copy button per prompt).

## PROMPT A — Claude Code: get the latest kit

```
Bring this studio up to date with the course kit.
Download each file below from
https://raw.githubusercontent.com/tertiarycourses/C1034-Multi-AI-Agents-for-Content-Creation/main/labs/horizon-studio/
into the same place here, replacing the old copy:
.claude/settings.json; scripts/approve-chat.mjs,
gate-hook.mjs, lib.mjs, publish.mjs, serve-site.mjs
and submit.mjs; data/publishing-spec.md,
channel-formats.md, connect-accounts.md,
env.example, turning-55-brief.md and
turning-55-draft.md. Touch nothing else.
Then add these rules to CLAUDE.md if they are
missing: every post links to http://localhost:8080/ with
UTM tags, never a claude.ai artifact link; a person
approves by typing "approved <id> by <name>" in the
chat; never ask me to run a command.
Then start my website and tell me in one line that
the kit is up to date.
```

## PROMPT B — Claude Code: the social team

```
Create an agent team for Week 1 social from
data/social-brief.md and strategy/calendar.csv.
Spawn two teammates using the agent types
content-creator and creative-designer; you are the
Lead.
- content-creator: 1 LinkedIn + 1 Facebook post
  with linkedin-post, facebook-post and copywriting,
  one file each in content/social/week-01/, with the
  frontmatter in data/publishing-spec.md. Each post
  links to my website, http://localhost:8080/, with
  UTM tags.
- creative-designer: one image per post (a rendered
  card in Horizon colours: LinkedIn 1200 x 627,
  Facebook 1080 x 1080) with alt text; message the
  creator for each post's hook before designing. Save
  each as a PNG beside its post and fill in the
  post's image and alt lines.
- You: fact-check and fin-compliance on every post
  and image; message fixes to the teammate who owns
  it.
Before you start, ask me how I will review: in the
artifact, or by email (then ask for the approver's
address). When a post passes, submit it for review
with scripts/submit.mjs. Publish the two posts as
an artifact. At the top, a Team chat: the messages
the teammates and you sent each other, in order,
each with who sent it. Then each post as it will
look in the feed, with its image and alt text;
under each post put two
working buttons (JavaScript): Approve turns the
card green; Request changes opens a box for my
note. A bar at the bottom asks my name once, builds
the exact lines to paste in the chat ("approved
<id> by <name>", "changes <id>: <note>") and has a
Copy button that says "Copied - now paste it in the
chat". Keep the lines on screen in case copying is
blocked. If I chose email, send ONE review email to
the approver with Gmail: the artifact link and what
passed the checks. Send nothing else; publish
nothing.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT C — Claude Code: ready to post

```
For each Week 1 post approved in
review/approvals.csv, publish a "ready to post"
artifact: the post text with a Copy button, its
image, and the steps to post it by hand on LinkedIn
or our Facebook Page. Then open the folder with the
two images on my computer. Publish nothing yourself.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Which post do you expect to do best, and why?"
- "What did the Lead send back to the writer, and why?"
- "Is anything here not ready to post? Explain in plain English."
