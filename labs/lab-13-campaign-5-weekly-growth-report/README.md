# Lab 13 — Campaign 5: Always On — the Weekly Growth Report

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 2 · Topic 4 · about 45 minutes · slides 136–141**\
**Surface:** Claude Code (skill, routine, Drive, Gmail)\
**Features:** the Growth Analyst's campaign-report skill · do · verify · schedule · draft-only delivery

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-13 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

The team must keep working after class. Rachel wants the Growth Analyst's report in her inbox every Monday — as a draft she decides on.

## Your goal

The team should keep working when class ends. Every Monday the Growth Analyst's report lands in Rachel's inbox as a draft — the decision stays with a person.

## You'll build

a scheduled task that drafts the weekly growth report every Monday at 8am, and one draft in Gmail

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/campaign-results.csv`
- `assets/weekly-report-brief.md`
- `assets/scheduled-task-instructions.md`
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 13". Run all of this lab's prompts in it.
2. **Put the data on Drive** — Ask: "Upload data/campaign-results.csv to my Google Drive folder Horizon Studio as a plain file, replacing any old copy."
3. **Do it once** — Copy and paste Prompt A. Refine the report until it is right.
4. **Schedule it** — After the report is right, copy and paste Prompt B into the instructions of a new routine: Routines → New routine → Local, Mondays at 8am.
5. **Run it now** — Click Run now once, approve any permission prompts, then open the Gmail draft.
6. **Pause it** — After class, pause the routine.

## The prompts

### PROMPT A — Claude Code: do it once

> Act as Horizon's Growth Analyst. Using Google
> Drive, read campaign-results.csv in the Horizon
> Studio folder. Use the campaign-report skill and
> data/weekly-report-brief.md. Leave the report as a
> Gmail DRAFT to me, subject "Horizon weekly growth
> report" and today's date. Send nothing.
> Also publish the report as an artifact: cost per chat
> by channel as a chart, and the budget split.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT B — Claude Code: the routine

> Run the campaign-report skill as Horizon's Growth
> Analyst. Read campaign-results.csv in the Horizon
> Studio folder on Google Drive and follow
> weekly-report-brief.md. Leave the report as a draft
> email to me in Gmail with the subject "Horizon
> weekly growth report" and today's date. Do not send
> it, and do not publish or approve anything.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "What is the one decision this report asks me to make?"
- "Which channel gets us a chat most cheaply, and how sure are you?"
- "What would you change in next month's budget, and why?"

## Check your work

- [ ] The report used the campaign-report skill from your folder.
- [ ] The report names the cheapest channel per chat (the newsletter).
- [ ] It recommends a budget split with a reason per channel.
- [ ] A scheduled task runs Mondays at 8am with draft-only instructions.
- [ ] A manual run left a draft — nothing was sent.
- [ ] The task is paused after class.

## If it goes wrong

- **It sent the email** — Write "draft only — never send" in both the skill and the task instructions.
- **Claude cannot upload to Drive** — Upload it yourself: drive.google.com → New → New folder "Horizon Studio" (if missing), open it → New → File upload.

## Stretch

- Add a Friday 5pm task from the Lead: what was published and what is still pending.

> **Why it matters:** Automate the preparation, not the decision. The schedule fills an inbox; a person still decides.

## Next

Lab 14 — Measure, Govern and Write the Team Playbook. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
