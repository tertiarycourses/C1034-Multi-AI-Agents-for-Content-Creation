# Prompts — Lab 11: Campaign 3: Newsletter and a Landing Page

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-11 (one Copy button per prompt).

## PROMPT A — Claude Code: the newsletter team

```
Create an agent team for the November Sunny
Sunday email (data/newsletter-brief.md,
data/newsletter-spec.md) and its landing page
(data/landing-page-brief.md). Spawn three teammates:
content-creator, website-designer and growth-analyst.
- content-creator: issue.md (id nl-2026-11) with
  newsletter, and the landing-page copy.
- website-designer: web/checklist/index.html with
  lead-magnet, web-design and landing-page from the
  approved copy; page-qa.
- growth-analyst: recipients.csv and excluded.csv
  from data/subscribers.csv.
Before you start, ask me how I will review: in the
artifact, or by email (then ask for the approver's
address). You check everything, then submit
nl-2026-11 and publish the issue as an artifact,
laid out as the email, with the counts of
recipients and excluded, and two working buttons
(JavaScript): Approve turns the page green; Request
changes opens a box for my note. A bar at the
bottom asks my name once, builds the exact line to
paste in the chat ("approved <id> by <name>" or
"changes <id>: <note>") and has a Copy button that
says "Copied - now paste it in the chat". Keep the
line on screen in case copying is blocked. If I
chose email, send ONE review email to the approver
with Gmail: the artifact link and what passed the
checks. Only
after I approve, build newsletter.html and .txt and
publish the page as an artifact.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT B — Claude Code: Gmail drafts

```
Using the Gmail connector, create a DRAFT of
newsletter.html for each address in recipients.csv,
plus one draft addressed to me only. Send nothing.
Publish a report as an artifact: how many drafts, how many
people were excluded, and why, in a table.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Explain the email in three sentences. What do we want readers to do?"
- "Who was left off the mailing list, and why?"
- "What did the landing-page check look at, and did it pass?"
