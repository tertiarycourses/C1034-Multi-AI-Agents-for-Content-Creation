# Prompts — Lab 03: Give Each Agent Its Skills

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-3 (one Copy button per prompt).

## PROMPT A — Claude Code: twenty skills

```
Read data/skills-spec.md. Create the twenty
skills in .claude/skills/<name>/SKILL.md. Each has
frontmatter (name, and a description that starts
"Use when…") and short numbered steps, under 80
lines. Use data/brand.md, data/channel-formats.md,
data/facts-2026.md and data/compliance-checklist.md
as the sources — do not invent rules.
```

## PROMPT B — Claude Code: wire them up

```
Add a skills: list to each subagent in
.claude/agents/ with its skills from
data/skills-spec.md. Leave any other agent file as
it is. Add to CLAUDE.md that the Lead (this session)
runs fact-check and fin-compliance on everything
before showing it to me.
```

## PROMPT C — Claude Code: see the skills

```
List the skills in .claude/skills/. Show each skill,
its owner (a subagent, or the Lead) and its
"Use when" line in a table. Confirm there are
twenty, that each specialist has the skills
the spec gives it, and that fact-check and
fin-compliance belong to the Lead (this session).
```
