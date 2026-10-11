# Prompts — Lab 06: Growth Analyst: Personas from Evidence

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-6 (one Copy button per prompt).

## PROMPT A — Claude Code: three analysts

```
Use three growth-analyst subagents in parallel, one
per file: data/survey-responses.csv,
data/enquiries.csv, data/checklist-results.csv.
Each uses audience-insights: counts with code, n
and the file on every claim, INFERENCE and LOW
CONFIDENCE labels, enquiry quotes verbatim with ids.
Combine the results into three personas with
data/persona-template.md → strategy/personas.md.
Publish the personas as an artifact: one card each,
with the key counts as small bar charts and the
confidence label in colour.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT B — Claude Code: requirements

```
Use the growth-strategist and the content-creator
subagents to write a writing guide for each persona
(data/content-spec-template.md →
strategy/content-spec.md): what they most want to
know, where to reach them, what to make and how
long, the tone, the proof that convinces them, what
we ask them to do next, and what we never say.
Back each answer with the data: which file, and how
many people.
Publish it as an artifact: one card per persona with
a one-line summary on top and the answers under
plain headings, then one table comparing the three
personas side by side.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Explain these personas in three sentences. Which one should we target first, and why?"
- "Which survey answers show that <a sentence from a persona>?"
- "Why is the 60+ group marked low confidence?"
