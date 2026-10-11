# Lab 09 — The Lead Magnet: a Checklist and Its Welcome Emails

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 2 · Topic 3 · about 50 minutes · slides 94–101**\
**Surface:** Claude Code (artifact, Gmail drafts, Marketing plugin, your Horizon skills)\
**Features:** lead-magnet skill · a printable A4 checklist as an artifact · the Marketing plugin's email sequence · newsletter and sunny-voice · drafts only

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-9 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

Day 2. Before the campaign weeks start, Rachel wants the thing that turns readers into leads: the Money Check-up Checklist, designed to be downloaded, and the emails that follow it.

## Your goal

The Money Check-up Checklist is what turns a reader into a lead. Make it worth downloading — a branded checklist — and write the welcome emails that follow the download.

## You'll build

the Money Check-up Checklist as a printable A4 page (artifact and PDF) and on your copy of Horizon's website, and three welcome emails — shown as artifacts, with a Word copy of each

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/checklist-items.md`
- `assets/brand.md`
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 9". Run all of this lab's prompts in it.
2. **Design it** — Copy and paste Prompt A. The checklist opens as an artifact; ask in the chat for any change.
3. **Write the welcome emails** — After the checklist looks right, copy and paste Prompt B. The three emails also appear as drafts in your Gmail.
4. **Check it** — After the three emails are saved, copy and paste Prompt C.
5. **Put it on the website** — After the checks pass, copy and paste Prompt D. Your copy of the website opens in your browser, with the checklist behind an email box.

## The prompts

### PROMPT A — Claude Code: the checklist

> Use the lead-magnet skill. Turn
> data/checklist-items.md into the "Money Check-up
> Checklist": a title with one promise, the ten items
> as tick boxes, one figure from data/facts-2026.md,
> the next step (book a free chat) and the full
> disclaimer. Lay it out as a printable A4 page in
> the colours and fonts in data/brand.md and publish
> it as an artifact. Save a PDF of it in
> content/lead-magnet/.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT B — Claude Code: the welcome emails

> Use the Marketing plugin's email sequence to write
> three welcome emails for people who download the
> checklist: day 0 (here it is), day 3 (the item most
> people miss — the retirement number), day 7 (book a
> free chat). Follow the newsletter and sunny-voice
> skills → content/email/welcome-sequence.md.
> Then, using the Gmail connector, create the
> three emails as DRAFTS in my Gmail, addressed to
> me. Send nothing.
> Publish the three emails as an artifact: one tab per
> email, laid out as it will look in the inbox.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT C — Claude Code: check it

> Run fact-check and fin-compliance on the checklist
> text and the three emails. Show the issues in one
> table, with a fix for each. Once I agree, make the
> fixes in the files and in the Gmail drafts.
> Publish the table as an artifact, coloured by
> severity.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT D — Claude Code: put it on the website

> Add the checked Money Check-up Checklist to
> Horizon's website in web/site/index.html, as a new
> section before the reviews, in the site's style:
> the title and promise, what's inside, and an email
> box with a required consent tick box. Once a valid
> email is entered, show the ten items as tick boxes
> and a "Print or save as PDF" button. Add "Free
> checklist" to the menu. Change nothing else on the
> site. Then start my website if it is not running,
> and open it.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Which checklist item do people most often miss, and why does it matter?"
- "Read the day 3 email as a 55-year-old. Is anything unclear?"
- "Explain each issue in one line: what is wrong, and the fix."

## Check your work

- [ ] The checklist uses Horizon's colours and all ten items.
- [ ] It makes one promise and ends with the full disclaimer.
- [ ] Three emails, each with a subject under 50 characters, are drafts in your Gmail — nothing was sent.
- [ ] Each email has one call to action, unsubscribe and the disclaimer.
- [ ] fin-compliance shows no Critical or High issue.
- [ ] The checklist is on your copy of the website: email and consent first, then the ten tick boxes.

## If it goes wrong

- **No drafts in Gmail** — Type /mcp: Gmail must be connected (Lab 4). Then say "create the Gmail drafts again".
- **The PDF is missing** — Say: "save the checklist as a PDF in content/lead-magnet/".

## Stretch

- Ask for a 1080x1350 social card that promotes the checklist, published as an artifact.

> **Why it matters:** A lead magnet earns an email address. Give real value first; the call to action comes last.

## Next

Lab 10 — Campaign 2: Social Media Posts (Demo). Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
