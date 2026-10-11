# Prompts — Lab 14: Measure, Govern and Write the Team Playbook

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-14 (one Copy button per prompt).

## PROMPT A — Claude Code: compare

```
Use the growth-analyst subagent. From
data/run-log.csv compare the patterns we used —
one agent, subagents, agent teams and the scheduled task
— on minutes, tokens, defects caught before a person
and human edits. Which pattern pays off for which
job? Save reports/agent-comparison.md.
Publish it as an artifact: one chart per measure,
comparing the patterns.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPT B — Claude Code: the playbook

```
Write strategy/team-playbook.md with
data/playbook-outline.md. Include the roster: for
each agent its instructions file in .claude/agents/, its
skills, connectors, model and what it may never do;
the approval matrix by risk; the rules in
data/responsible-ai-checklist.md; and what to do when
a wrong post goes out. Then run fin-compliance on
it.
Publish the playbook as an artifact: the roster as
cards, the approval matrix as a table.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "In one line each: when should we use one agent, subagents and an agent team?"
- "Who must approve a post that has a CPF figure in it?"
- "A wrong post went out. What are the first three things we do?"
