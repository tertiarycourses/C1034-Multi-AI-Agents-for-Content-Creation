# Lab 06 — Growth Analyst: Personas from Evidence

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 1 · Topic 2 · about 40 minutes · slides 72–77**\
**Surface:** Claude Code (three analyst subagents in parallel)\
**Features:** three analyst sub-agents, one per data file · counts, not impressions · confidence labels · content requirements

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-6 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

Jun Wei drafted personas from instinct: 'busy young parents who love TikTok'. Rachel is not convinced. There are 150 survey answers, 60 enquiries and 200 checklists.

## Your goal

Personas made up in a meeting steer content wrong. The Growth Analyst builds them from 150 survey answers, 60 enquiries and 200 checklists — and labels what is guesswork.

## You'll build

three evidence-based personas and the content spec — shown as artifacts, with a Word copy of each

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/survey-responses.csv`
- `assets/enquiries.csv`
- `assets/checklist-results.csv`
- `assets/persona-template.md`
- `assets/content-spec-template.md`
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 6". Run all of this lab's prompts in it.
2. **Check the data** — The CSVs and templates are already in data/. Open one and skim it.
3. **Analyse in parallel** — Copy and paste Prompt A — three analyst sub-agents, one per file.
4. **Challenge a claim** — Pick one persona statement and ask: "which rows show that?"
5. **Write the guides** — After the persona cards appear, copy and paste Prompt B: a writing guide for each persona — how to talk to them.
6. **Check the gaps** — The 60+ group must be LOW CONFIDENCE.

## The prompts

### PROMPT A — Claude Code: three analysts

> Use three growth-analyst subagents in parallel, one
> per file: data/survey-responses.csv,
> data/enquiries.csv, data/checklist-results.csv.
> Each uses audience-insights: counts with code, n
> and the file on every claim, INFERENCE and LOW
> CONFIDENCE labels, enquiry quotes verbatim with ids.
> Combine the results into three personas with
> data/persona-template.md → strategy/personas.md.
> Publish the personas as an artifact: one card each,
> with the key counts as small bar charts and the
> confidence label in colour.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT B — Claude Code: requirements

> Use the growth-strategist and the content-creator
> subagents to write a writing guide for each persona
> (data/content-spec-template.md →
> strategy/content-spec.md): what they most want to
> know, where to reach them, what to make and how
> long, the tone, the proof that convinces them, what
> we ask them to do next, and what we never say.
> Back each answer with the data: which file, and how
> many people.
> Publish it as an artifact: one card per persona with
> a one-line summary on top and the answers under
> plain headings, then one table comparing the three
> personas side by side.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Explain these personas in three sentences. Which one should we target first, and why?"
- "Which survey answers show that <a sentence from a persona>?"
- "Why is the 60+ group marked low confidence?"

## Check your work

- [ ] Three analyst sub-agents ran, one per file.
- [ ] Every persona statement carries a count and a file.
- [ ] The 60+ group is LOW CONFIDENCE (n = 12).
- [ ] The most-unticked checklist item is the retirement number.
- [ ] Enquiry quotes are verbatim, with ids.
- [ ] The writing guide answers every question for every persona.

## If it goes wrong

- **Numbers change between runs** — Insist on counting with code and showing the printed output.

## Stretch

- Ask the analyst for a filterable dashboard of the survey as an artifact.

> **Why it matters:** Ask "which rows show that?" of anything that sounds insightful. If the agent cannot point to rows, it is an inference.

## Next

Lab 7 — Growth Analyst and Strategist: Cadence and Calendar. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
