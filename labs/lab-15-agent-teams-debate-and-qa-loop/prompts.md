# Prompts — Lab 15: Agent Teams: A Strategy Debate and a QA Loop

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-15 (one Copy button per prompt).

## PROMPT A — Claude Code: the strategy debate

```
Create an agent team to test the strategy in
data/turning-55-brief.md before we spend on it.
You are the Lead and the judge: do not argue.
Spawn two teammates:
- advocate, using the agent type growth-strategist:
  argue FOR the strategy.
- critic, using the agent type growth-analyst:
  argue AGAINST it.
- Both: cite data/campaign-results.csv,
  strategy/personas.md, data/facts-2026.md or
  data/compliance-checklist.md for every point;
  message each other directly; rebut twice at most.
- You: write strategy/turning-55-decision.md with
  the pros, the cons, your verdict (go / go with
  conditions / no-go) and the conditions.
Publish the decision as an artifact with the verdict
on top, the pros and cons in two columns, the debate
(the messages the advocate and critic sent each
other, in order) and what I do next. Then wait for
my decision.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT B — Claude Code: the QA loop

```
Clean up the debate team, then create a new agent
team for Part 2 of data/turning-55-brief.md, using
my decision. Spawn three teammates:
- writer, agent type content-creator: rewrite
  data/turning-55-draft.md into
  content/turning-55/email.md and
  content/turning-55/video-script.md.
- qa-auditor: audit each piece with fact-check and
  fin-compliance; write review/turning-55-qa.md, one
  section per round, PASS or FAIL per check. On
  FAIL, message the writer directly with the lines
  to fix and audit again. Three rounds at most.
- designer, agent type creative-designer: once a
  piece passes, ask the writer for its headline and
  make one thumbnail with alt text.
- You, the Lead: never write or fix content. When
  everything passes, submit each piece with
  scripts/submit.mjs. Publish nothing.
Publish the QA report as an artifact, one row per
round, PASS or FAIL per check, in colour.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT C — Claude Code: shut down

```
Ask every teammate to shut down, then clean up
the team. Show me the final task list and how many
QA rounds each piece needed. Publish it as an
artifact.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Summarise the debate: the best point for, the best point against, and your verdict."
- "What failed in the first QA round, in plain English?"
- "How many rounds did each piece need, and why?"
