# Prompts — Lab 01: Build Your Marketing Agent Team

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-1 (one Copy button per prompt).

## PROMPT A — Claude Code: plan your team

```
Act as a marketing consultant. Interview me, the
owner of Horizon Wealth Planning, to plan my AI
marketing team. Ask one question at a time and wait
for my answer: my goal, what success looks like by
March 2027, who we want to reach, which channels we
use, how much we publish each week, and who approves
before anything goes out.
Then list 8 to 10 team members I could have,
numbered, each with a one-line job. Include the six
roles in data/team-charter.md and mark the ones you
recommend. Wait for me to choose.
Save my answers and my chosen team, with each
member's job, to data/team-design.md. This is a
plan only: do not create any agent files yet.
```

## PROMPT B — Claude Code: the charter

```
Read data/team-charter.md, data/team-design.md
and data/business-brief.md. Write CLAUDE.md for this
studio in four sections — What this is, The team,
Rules, Files — under 60 lines. The team is the one
I chose in data/team-design.md. Rules: every number
comes from data/facts-2026.md; every piece passes
fact-check and fin-compliance; nothing is published
or sent without a person's approval (the one
exception: a review email to the approver); anything
shown to me is in plain English for a business owner,
with no codes, IDs, file names or line numbers.
In Files, add two lines:
- Our copy of the site, which we edit: web/site/.
  "Start my website" runs scripts/serve-site.mjs in
  the background and opens http://localhost:8080/
- Every post links to http://localhost:8080/ with
  UTM tags, never to a claude.ai artifact link.
```
