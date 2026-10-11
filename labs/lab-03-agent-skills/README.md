# Lab 03 — Give Each Agent Its Skills

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 1 · Topic 1 · about 45 minutes · slides 45–50**\
**Surface:** Claude Code (.claude/skills/)\
**Features:** twenty skills owned by role — research, writing, LinkedIn, Facebook, blog, newsletter, web design, lead magnet, video, analysis and compliance · SKILL.md · the "Use when" trigger · test without naming

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-3 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

The team exists, but every agent writes in its own way. Rachel wants Horizon's voice, facts and compliance rules applied the same way by every agent, every time.

## Your goal

Instructions say who an agent is; skills say how it does the job. Write each procedure once and every agent applies it the same way, every time.

## You'll build

twenty skills in .claude/skills/, wired to the agents that own them

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/skills-spec.md`
- `assets/channel-formats.md`
- `assets/brand.md`
- `assets/facts-2026.md`
- `assets/compliance-checklist.md`
- `solution/` — reference files from the verified build (each `.md` with its `.pdf`)
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 3". Run all of this lab's prompts in it.
2. **Read the spec** — skills-spec.md lists the twenty skills and who owns each.
3. **Create the skills** — Copy and paste Prompt A.
4. **Wire them up** — After the twenty skills appear in .claude/skills/, copy and paste Prompt B, then C to list every skill. The Lead's two go in CLAUDE.md, not a file.
5. **Test without naming** — In a new session ask: "Write a Facebook post about the free Money Check-up Checklist." Ask which skills were used.
6. **Break it on purpose** — Ask for a post that says "guaranteed 8% a year". fin-compliance must flag it as Critical.

## The prompts

### PROMPT A — Claude Code: twenty skills

> Read data/skills-spec.md. Create the twenty
> skills in .claude/skills/<name>/SKILL.md. Each has
> frontmatter (name, and a description that starts
> "Use when…") and short numbered steps, under 80
> lines. Use data/brand.md, data/channel-formats.md,
> data/facts-2026.md and data/compliance-checklist.md
> as the sources — do not invent rules.

### PROMPT B — Claude Code: wire them up

> Add a skills: list to each subagent in
> .claude/agents/ with its skills from
> data/skills-spec.md. Leave any other agent file as
> it is. Add to CLAUDE.md that the Lead (this session)
> runs fact-check and fin-compliance on everything
> before showing it to me.

### PROMPT C — Claude Code: see the skills

> List the skills in .claude/skills/. Show each skill,
> its owner (a subagent, or the Lead) and its
> "Use when" line in a table. Confirm there are
> twenty, that each specialist has the skills
> the spec gives it, and that fact-check and
> fin-compliance belong to the Lead (this session).

## Check your work

- [ ] Twenty folders in .claude/skills/, each with a SKILL.md.
- [ ] Every description starts "Use when…".
- [ ] Each specialist lists its own skills from the spec.
- [ ] The untold test picked sunny-voice and facebook-post.
- [ ] fin-compliance flagged "guaranteed 8%" as Critical.

## If it goes wrong

- **A skill never triggers** — Rewrite its description with the words a person would actually type.
- **I cannot see the skills** — Paste Prompt C, or open .claude/skills/ in the Files panel (the folder icon, top right) — one folder per skill, each with a SKILL.md.

## Stretch

- Add one more skill, utm-links, owned by the Content Creator.

> **Why it matters:** A skill costs almost nothing until it is needed. Keep the rules file (CLAUDE.md) short and put procedures in skills.

## Next

Lab 4 — Connect the Tools Each Agent Needs. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
