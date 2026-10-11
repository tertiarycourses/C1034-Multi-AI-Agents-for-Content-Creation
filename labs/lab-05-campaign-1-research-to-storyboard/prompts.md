# Prompts — Lab 05: Campaign 1: Research to Storyboard, with Subagents

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-5 (one Copy button per prompt).

## PROMPT A — Claude Code: research and ideas

```
Act as the Marketing Team Lead for the campaign
in data/campaign-objective.md.
Use subagents, in parallel:
- growth-strategist: competitor-scan → save
  research/competitive-analysis.md.
- growth-analyst: the funnel in data/firm-metrics.csv
  — what 40 chats a month needs → save
  research/funnel.md.
When both finish, the growth-strategist proposes
three ideas each for young professionals, mid-career
families and pre-retirees, scored with
data/idea-rubric.md and tagged with a funnel stage
(content-marketing) → strategy/ideas.md.
Publish the top five as an artifact — one card per
idea with its score, persona and funnel stage — and
a box at the top that tells me what to do next.
Then stop. I will choose.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT B — Claude Code: the storyboard

```
I choose idea <number>, because <one line>.
Use subagents:
- growth-strategist: campaign-brief →
  strategy/campaign-brief.md, then a five-beat
  storyboard with data/storyboard-template.md →
  strategy/storyboard.md.
- content-creator: three channel variants that keep
  the same claims — LinkedIn, Facebook, a 60-second
  video.
Then run fact-check and fin-compliance yourself and
show me the issues before anything is final.
Publish the brief and the storyboard as an artifact
with a tab for the brief (goal, audience, message,
call to action); a tab for the five beats side by side,
each with its claim and source, and the three
variants below; and the issues in a table.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT C — Claude Code: decide on the issues

```
I confirm "no obligation" and the free checklist —
add them to the facts sheet (data/facts-2026.md).
Delete any other claim that is not on the facts
sheet. Fix all the Medium and Low issues, then show
me the updated storyboard and publish it as an
artifact.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- *After Prompt A:* "Explain this result in three sentences. Which idea would you pick, and why?"
- "Why does idea <number> score higher than idea <number>?"
- "What does the funnel say is our biggest problem?"
- *After Prompt B:* "Explain the issues in plain English. What do I need to decide?"
- *After Prompt C:* "What changed since the last version? Is anything still not ready for Rachel?"
