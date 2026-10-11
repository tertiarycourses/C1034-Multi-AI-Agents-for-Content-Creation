# Prompts — Lab 07: Growth Analyst and Strategist: Cadence and Calendar

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-7 (one Copy button per prompt).

## PROMPT A — Claude Code: the analyst

```
Use the growth-analyst subagent. From
data/channel-benchmarks.csv and
data/team-capacity.md, recommend how often to
publish on LinkedIn, Facebook, the newsletter and
YouTube. Compare the extra clicks from one more
post, the unfollows or unsubscribes it costs, and
the hours → strategy/cadence.md.
Publish it as an artifact: a chart per channel of the
extra clicks against the unfollows, and the hours.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT B — Claude Code: the strategist

```
Use the growth-strategist subagent to build a
four-week calendar from Monday 2 November 2026 in
strategy/calendar.csv (columns as
data/calendar-format.csv), from the cadence,
strategy/storyboard.md and strategy/content-spec.md.
review_by two business days before each date; no
public holidays; no week over the team's hours.
Publish the four weeks as an artifact: a calendar grid
by channel, review dates marked, hours per week.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Why is the newsletter not weekly? Show me the numbers."
- "What happens if we add a third LinkedIn post a week?"
- "Which week is busiest, and does the team have the hours?"
