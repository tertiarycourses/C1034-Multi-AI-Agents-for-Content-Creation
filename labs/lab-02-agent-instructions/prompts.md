# Prompts — Lab 02: Form the Team: Instructions for Each Agent

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-2 (one Copy button per prompt).

## PROMPT A — Claude Code: five subagents

```
Read data/role-specs.md. Create five project
subagents in .claude/agents/ — growth-strategist,
content-creator, creative-designer, website-designer
and growth-analyst. Each file has:
- frontmatter: name; a description that says when to
  use it; tools; model (opus for the strategist,
  sonnet for the others)
- a body with: the job, what it reads, what it
  delivers, the connectors it may use, what it must
  never do, and how it reports back.
No skills line yet — we add skills in Lab 3.
```

## PROMPT B — Claude Code: see the team

```
List the subagents in .claude/agents/. For each,
show the file name, the name, the one-line
description and the model, in a table. Then confirm
there are five, and that none of them is the
Marketing Team Lead — the Lead is this session.
If any other file is there, list it and ask me
before moving it to _archive/.
```

## PROMPT C — Claude Code: meet the team

```
Use each of the five subagents once, in parallel.
Ask each: "In one line, who are you, and what is
the first thing you would do for Horizon's goal of
40 booked chats a month?" Show me the five answers
in a table.
```
