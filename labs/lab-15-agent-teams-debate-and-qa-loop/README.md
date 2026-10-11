# Lab 15 — Agent Teams: A Strategy Debate and a QA Loop

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 2 · Topic 4 · about 40 minutes · slides 153–159**\
**Surface:** Claude Code (agent teams: Lead, teammates, shared task list, direct messages)\
**Features:** an advocate and a critic argue the pros and cons · the Lead judges · a writer and a QA Auditor loop until PASS · FAIL goes straight back to the writer · human approval

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-15 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

January is for people turning 55. Before Horizon spends on a CPF explainer for them, Rachel wants it argued both ways — and the intern's draft checked until it passes.

## Your goal

Subagents only report back. In a team the agents talk: two teammates argue a strategy before Horizon spends on it, and a QA Auditor sends a failed draft straight back to the writer — round after round — without the Lead in the middle.

## You'll build

the decision (pros, cons, verdict), then an email, a video script and a thumbnail that passed QA, submitted for your approval — shown as artifacts, with a Word copy of each

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/turning-55-brief.md`
- `assets/turning-55-draft.md`
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 15". Run all of this lab's prompts in it.
2. **Part 1: the debate** — Copy and paste Prompt A. The advocate and the critic message each other; the decision page shows their debate.
3. **Decide** — Read the decision artifact. Reply "go", "go with conditions" or "no-go" — the call is yours.
4. **Part 2: the QA loop** — After you have made the call, copy and paste Prompt B. The audit fails on round 1; watch the auditor message the writer directly.
5. **Approve as a person** — Read the pieces and the QA artifact, then type in the chat: approved <id> by <your name> (or: changes <id>: what to fix).
6. **Shut down** — After you have approved the pieces, copy and paste Prompt C. The Lead stops each teammate and cleans up the team.

## The prompts

### PROMPT A — Claude Code: the strategy debate

> Create an agent team to test the strategy in
> data/turning-55-brief.md before we spend on it.
> You are the Lead and the judge: do not argue.
> Spawn two teammates:
> - advocate, using the agent type growth-strategist:
>   argue FOR the strategy.
> - critic, using the agent type growth-analyst:
>   argue AGAINST it.
> - Both: cite data/campaign-results.csv,
>   strategy/personas.md, data/facts-2026.md or
>   data/compliance-checklist.md for every point;
>   message each other directly; rebut twice at most.
> - You: write strategy/turning-55-decision.md with
>   the pros, the cons, your verdict (go / go with
>   conditions / no-go) and the conditions.
> Publish the decision as an artifact with the verdict
> on top, the pros and cons in two columns, the debate
> (the messages the advocate and critic sent each
> other, in order) and what I do next. Then wait for
> my decision.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT B — Claude Code: the QA loop

> Clean up the debate team, then create a new agent
> team for Part 2 of data/turning-55-brief.md, using
> my decision. Spawn three teammates:
> - writer, agent type content-creator: rewrite
>   data/turning-55-draft.md into
>   content/turning-55/email.md and
>   content/turning-55/video-script.md.
> - qa-auditor: audit each piece with fact-check and
>   fin-compliance; write review/turning-55-qa.md, one
>   section per round, PASS or FAIL per check. On
>   FAIL, message the writer directly with the lines
>   to fix and audit again. Three rounds at most.
> - designer, agent type creative-designer: once a
>   piece passes, ask the writer for its headline and
>   make one thumbnail with alt text.
> - You, the Lead: never write or fix content. When
>   everything passes, submit each piece with
>   scripts/submit.mjs. Publish nothing.
> Publish the QA report as an artifact, one row per
> round, PASS or FAIL per check, in colour.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPT C — Claude Code: shut down

> Ask every teammate to shut down, then clean up
> the team. Show me the final task list and how many
> QA rounds each piece needed. Publish it as an
> artifact.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Summarise the debate: the best point for, the best point against, and your verdict."
- "What failed in the first QA round, in plain English?"
- "How many rounds did each piece need, and why?"

## Check your work

- [ ] The advocate and the critic messaged each other; every point cites a file.
- [ ] The decision has pros, cons, a verdict — and you made the call.
- [ ] Round 1 of the QA report FAILED: the FRS figure, CPF LIFE "from 55", the promised payout, the advice and the missing disclaimer.
- [ ] The auditor sent the fixes to the writer directly; a later round PASSED.
- [ ] You approved by typing in the chat; the rows show your name and a hash.
- [ ] Both teams were shut down and cleaned up.

## If it goes wrong

- **Claude cannot find turning-55-brief.md** — Your folder is an older download. Ask: "Download turning-55-brief.md and turning-55-draft.md from https://raw.githubusercontent.com/tertiarycourses/C1034-Multi-AI-Agents-for-Content-Creation/main/labs/horizon-studio/data/ into data/." Then paste Prompt A again.
- **You got subagents, not a team** — Ask for "an agent team" by name in a new session.
- **The loop never ends** — Remind the Lead: three rounds at most, then escalate to me.
- **A task stays blocked** — Tell the Lead to check the task list and nudge the teammate who owns it.

## Stretch

- Add a third debater, a pre-retiree persona, who argues from the customer's side.
- Run Part 2 with subagents instead and compare: how many times did the Lead have to relay a fix?

> **Why it matters:** Use subagents when only the result matters; use a team when the agents must talk — to argue, or to send work back. Every teammate is its own Claude session, so teams cost more tokens.

## Next

The course summary, then the assessment.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
