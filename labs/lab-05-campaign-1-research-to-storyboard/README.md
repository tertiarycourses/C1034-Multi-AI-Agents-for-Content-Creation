# Lab 05 — Campaign 1: Research to Storyboard, with Subagents

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 1 · Topic 1 · about 45 minutes · slides 61–67**\
**Surface:** Claude Code (subagents in parallel)\
**Features:** the Lead delegates · strategist and analyst in parallel · nine scored ideas · a human concept checkpoint · a five-beat storyboard

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-5 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

The team's first campaign: 'Know Your Number', November to January. Rachel wants research, ideas for three audiences, her choice, and a storyboard every channel follows.

## Your goal

The team's first job: find who to reach and what to say for the "Know Your Number" campaign — research in parallel, ideas scored, a person choosing, a storyboard every channel follows.

## You'll build

competitor research, the funnel, nine scored ideas, the campaign brief and a five-beat storyboard with three channel variants — shown as artifacts, with a Word copy of each

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/campaign-objective.md`
- `assets/idea-rubric.md`
- `assets/storyboard-template.md`
- `assets/firm-metrics.csv`
- `assets/services.csv`
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 5". Run all of this lab's prompts in it.
2. **Brief the Lead** — The briefs are already in data/. You are the client; your session is the Marketing Team Lead.
3. **Research in parallel** — Copy and paste Prompt A. Watch the strategist and the analyst run at the same time.
4. **Read the ideas** — Nine ideas, scored with the rubric — the top five open as an artifact beside the chat. The Lead stops for you.
5. **Choose** — Pick one idea in the artifact's Ideas tab and note its number and why — the human concept checkpoint.
6. **Storyboard** — After you have chosen, copy and paste Prompt B in the chat, replacing <number> and <one line> with your choice.
7. **Decide as Rachel** — After you have read the issues, copy and paste Prompt C. You confirm what is true about Horizon; the team removes or fixes the rest.

## The prompts

### PROMPT A — Claude Code: research and ideas

> Act as the Marketing Team Lead for the campaign
> in data/campaign-objective.md.
> Use subagents, in parallel:
> - growth-strategist: competitor-scan → save
>   research/competitive-analysis.md.
> - growth-analyst: the funnel in data/firm-metrics.csv
>   — what 40 chats a month needs → save
>   research/funnel.md.
> When both finish, the growth-strategist proposes
> three ideas each for young professionals, mid-career
> families and pre-retirees, scored with
> data/idea-rubric.md and tagged with a funnel stage
> (content-marketing) → strategy/ideas.md.
> Publish the top five as an artifact — one card per
> idea with its score, persona and funnel stage — and
> a box at the top that tells me what to do next.
> Then stop. I will choose.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT B — Claude Code: the storyboard

> I choose idea <number>, because <one line>.
> Use subagents:
> - growth-strategist: campaign-brief →
>   strategy/campaign-brief.md, then a five-beat
>   storyboard with data/storyboard-template.md →
>   strategy/storyboard.md.
> - content-creator: three channel variants that keep
>   the same claims — LinkedIn, Facebook, a 60-second
>   video.
> Then run fact-check and fin-compliance yourself and
> show me the issues before anything is final.
> Publish the brief and the storyboard as an artifact
> with a tab for the brief (goal, audience, message,
> call to action); a tab for the five beats side by side,
> each with its claim and source, and the three
> variants below; and the issues in a table.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT C — Claude Code: decide on the issues

> I confirm "no obligation" and the free checklist —
> add them to the facts sheet (data/facts-2026.md).
> Delete any other claim that is not on the facts
> sheet. Fix all the Medium and Low issues, then show
> me the updated storyboard and publish it as an
> artifact.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- *After Prompt A:* "Explain this result in three sentences. Which idea would you pick, and why?"
- "Why does idea <number> score higher than idea <number>?"
- "What does the funnel say is our biggest problem?"
- *After Prompt B:* "Explain the issues in plain English. What do I need to decide?"
- *After Prompt C:* "What changed since the last version? Is anything still not ready for Rachel?"

## Check your work

- [ ] The strategist and the analyst ran in parallel.
- [ ] The competitor analysis and the funnel are done, with sources.
- [ ] Nine scored ideas, each with its author.
- [ ] You chose the idea and recorded why.
- [ ] The storyboard has five beats; every claim has a source.
- [ ] You confirmed two claims; after Prompt C no High issue is left.

## If it goes wrong

- **The Lead did the work itself** — Ask directly for subagents, naming each agent.

## Stretch

- Ask the analyst which persona the funnel says to target first, and compare it with your choice.

> **Why it matters:** Agents diverge; a person decides. The concept checkpoint is where the campaign becomes yours.

## Next

Lab 6 — Growth Analyst: Personas from Evidence. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
