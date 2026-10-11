# Multi AI Agents for Content Creation — Learner Guide

C1034 · Version 1.0 · Tertiary Infotech Academy Pte Ltd (UEN 201200696W)

## How to Use This Guide

This guide carries the full step-by-step for every lab in the course. The slides explain the idea; this guide is what you follow at the keyboard. Every lab also has its own folder in the lab pack with a README, the prompts as Markdown and PDF, the assets you need and an evidence checklist.

Before you start, have ready:

- The Claude desktop app on a Pro plan or above, signed in. Every lab runs in Code mode, in your horizon-studio folder — you type plain English, never code.
- Set up by the trainer: Claude Code, Node.js, Python and ffmpeg.
- A personal Google account for Drive, Gmail and Calendar — never an employer's. A free Firecrawl account.
- The lab pack (labs/), unzipped. Keep one working folder, horizon-studio, from Lab 1 to Lab 15.

Prompts appear as shaded quotes — paste them as written. Code, commands and configuration appear in grey monospace blocks. Product menus change between releases: if a name here differs from your screen, follow the screen and tell the trainer.

## The Scenario: Horizon Wealth Planning

Rachel Goh founded Horizon Wealth Planning in 2010. Fifteen years and 1,200 clients later, almost every new client still comes through a referral — and referrals are slowing. Younger Singaporeans look for money help on LinkedIn, Facebook, YouTube and in their inbox, and Horizon is invisible there.

Rachel has a website, three planners, a part-time marketer (Jun Wei) and S$4,000 a month. She wants 40 booked free chats a month by March 2027 — without hiring a marketing team. So you will build her one, made of AI agents, with Claude and Claude Code:

- Marketing Team Lead — plans, assigns, checks, hands to a person
- Growth Strategist — research, positioning, briefs, storyboards
- Content Creator — posts, newsletter, scripts, page copy
- Creative Designer — images, thumbnails, the video
- Website Designer — landing pages, published and QA-checked
- Growth Analyst — personas, cadence, results, weekly report

First you form the team: instructions, skills and connectors for each agent. Then the team runs five campaigns together. Financial content is regulated, so a person approves every piece before it goes out. The data is fictitious but consistent, and every email address resolves to your own inbox.

## About This Course

#### Learning Outcomes

By the end of the two days you will be able to:

- **LO1 · Conceptualise** — Conceptualise content ideas that meet marketing objectives, and map them into digital storyboards.
- **LO2 · Identify** — Identify content requirements from customer preferences, and decide how often to publish.
- **LO3 · Determine** — Determine content types and styles, and the modes and processes for distributing content.
- **LO4 · Develop** — Develop guidelines for executing the content strategy, with suitable delivery modes and responsible AI practices.

#### Course Outline

Four topics over two days. Day 1 forms the team; Day 2 runs its campaigns.

1. **T1 · Ideation and Storyboarding** — The studio, the team's instructions, skills and connectors; Campaign 1. Labs 1–5.
1. **T2 · Audience and Requirements** — Personas from evidence; cadence and calendar; the first blog article. Labs 6–8.
1. **T3 · Creation and Coordination** — Lead magnet, social week, newsletter + landing page, video — behind a human gate. Labs 9–12.
1. **T4 · Distribution and Responsible AI** — The weekly report on a schedule; the playbook; agent teams at work. Labs 13–15.

#### Lab Materials

Fifteen labs, each in its own folder with a README, prompts (MD and PDF), assets, an evidence checklist and, where useful, a solution.

| Day | Labs | Topic |
|---|---|---|
| 1 | 1 Agent team · 2 Instructions · 3 Skills · 4 Connectors | T1 · form the team |
| 1 | 5 Campaign 1: research to storyboard | T1 · Campaign 1 |
| 1 | 6 Personas · 7 Cadence and calendar · 8 Blog article | T2 · audience, content |
| 2 | 9 Lead magnet · 10 Social week · 11 Newsletter + landing page · 12 Video | T3 · Campaigns 2–4 |
| 2 | 13 Weekly report · 14 Playbook · 15 Agent teams: debate + QA loop | T4 · Campaign 5 |

Tip: One horizon-studio folder from Lab 1 to Lab 15 — the team keeps what it learns.

#### Code Mode, Every Lab

The Claude desktop app in Code mode (</>), in your horizon-studio folder — every lab. You type plain English, never code.

| Use | Labs | What it is for |
|---|---|---|
| Claude Code | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | Everything: the team's folder, agents, skills, connectors, artifacts and routines. Each lab starts a new session named after the lab. |

Tip: Everything the team makes is saved in horizon-studio, so the next lab's session picks up where the last one stopped.

#### Lesson Plan (9:30 AM – 5:30 PM)

One 30-minute lunch, no separate tea breaks. Full timings and slide numbers are in the Lesson Plan.

| Block | Day 1 — Form the Team | Day 2 — Run the Campaigns |
|---|---|---|
| Morning 1 | 9:30–10:55  Welcome · Topic 1 · Lab 1 | 9:30–11:35  Topic 3 · Labs 9–10 |
| Morning 2 | 10:55–12:45  Labs 2–3 | 11:35–12:40  Lab 11 |
| Afternoon 1 | 13:15–15:00  Labs 4–5 | 13:10–15:20  Lab 12 · recap · Topic 4 · Lab 13 |
| Afternoon 2 | 15:00–17:30  Topic 2 · Labs 6–8 · review | 15:20–17:30  Lab 14 · Agent teams lab · summary |

Tip: Both days run 9:30 AM – 5:30 PM: 7.5 instructional hours with one 30-minute lunch.

## Topic 1 — Multi-AI-Agent Content Ideation and Digital Storyboarding

Slides 10–68. In this topic you will:

- AI agents, the tools, and Horizon's story
- Why a team of agents
- A home for the team; Horizon's public website
- Form the team: instructions, skills, connectors
- Campaign 1: research, ideas and a storyboard

### Key ideas for Lab 1

#### The Claude Suite of Products

Anthropic's products all run on the same Claude models — they differ in where they run and who they are for.

- **Claude** — Chat and Cowork, now one app — web, desktop and mobile. Ask, write, analyse; work on a folder of files.
- **Claude Code** — The agentic tool for building: terminal, VS Code, the desktop Code tab and the web.
- **Claude Design** — Polished UI, prototypes and front-end designs from a prompt.
- **Claude for Microsoft** — Claude inside Microsoft 365 apps such as Excel, PowerPoint and Outlook.
- **Claude for Chrome** — A browser agent that reads pages, clicks and fills forms in your own Chrome.
- **Claude for Science** — Speeds up research workflows for scientists and labs.

#### What Is Claude (Chat + Cowork)?

Chat and Cowork are now one product: Claude, in the desktop app on a paid plan. In this course every lab runs in Code mode instead, so your folder is always in view.

- **Chat** — Ask, draft, analyse and research with web search; projects keep shared files and instructions.
- **Cowork** — Works on a folder on your computer: plans and runs multi-step tasks, and runs sub-agents in parallel when asked.
- **Connectors and skills** — Google Drive, Gmail, Calendar, Microsoft 365; build your own skills with /skill-creator.
- **Artifacts and scheduled tasks** — Pages and documents shared by link; tasks that run on a schedule from an Instructions field.

#### What Is Claude Code?

An agentic tool: describe a goal in plain English and Claude plans, writes, runs and checks the work — editing files, running commands and using tools for you.

- **Runs where you work** — The terminal, VS Code, the Claude desktop Code tab and the web.
- **Agentic** — Plans multi-step tasks and acts on them — not just answers or autocompletes.
- **Tool-using** — Reads and writes files, runs commands, calls MCP connectors and publishes artifacts.
- **Extensible — the team's home** — CLAUDE.md, subagents, agent teams, skills and hooks. You build Horizon's team here (Labs 1–5, 10–12).

#### Claude for Microsoft, Chrome and Science

The same Claude models, working inside the apps you already use. Not needed for the labs — good to know.

- **Claude for Microsoft** — Claude inside Microsoft 365 — Excel, PowerPoint, Word and Outlook — working on the file you have open.
- **Claude for Chrome** — An extension that lets Claude navigate, click, type and fill forms in your browser, with your sign-ins. You approve sensitive actions.
- **Claude for Science** — Claude for researchers and labs: literature review, data analysis and connections to scientific tools and databases.

#### A Brief History of AI, 2023–2026

- **2023 · Prompt Engineering** — ChatGPT goes mainstream; Anthropic launches Claude (March). Results depend on how you word the prompt.
- **2024 · Context Engineering** — Models call tools. Anthropic open-sources the Model Context Protocol (Nov). Results depend on what the model can see.
- **2025 · Harness Engineering** — E.g. Claude Code and Codex. The system around the model gives rise to agentic AI: task-oriented agents that plan, act and check their work.
- **2026 · AI Agents** — Always-on agents that work 24/7 on their own, e.g. OpenClaw and Hermes Agent; Claude Code agent teams talk to each other.

From wording one prompt, to curating context, to engineering the system around the model — and now, agents that work around the clock.

#### What Is a Harness?

The model is the brain. The harness is everything built around it that turns a model into an agent able to finish long tasks.

- **The agentic loop** — Plans, acts, checks the result and repeats until the goal is met.
- **Tools and context** — Files, commands, search and connectors (MCP); instructions, memory and skills loaded at the right moment.
- **Guardrails and checks** — Permission modes, approvals, hooks and tests — what it must ask before it acts.
- **Harnesses you will meet** — Claude Code and Claude in class; also Codex, Gemini CLI and OpenClaw.

#### The Agentic Loop

Every agent runs the same repeating cycle. A team is several loops, side by side.

1. **Gather context** — Reads the prompt, CLAUDE.md, its instructions, files and skills.
1. **Plan** — Decides the next step — or proposes a plan for you to approve.
1. **Take action** — Calls a tool: writes a file, searches, uses a connector, starts a subagent.
1. **Verify** — Checks the result: a count, a test, the Lead's review.
1. **Repeat** — Loops until the goal is met — then reports what it did.

Tip: Goal in → context → action → verification → repeat → goal met.

#### Why the Loop Matters

Running a team of agents is steering loops, not typing commands.

- **Give direction, not micro-steps** — State the goal, the inputs and "done when". Let each loop work out the steps.
- **Verification is everything** — An agent is only as good as its checks: a facts sheet, a test, the Lead's review.
- **Steer mid-loop** — Read the plan, interrupt, correct the course — do not wait for a wrong final answer.
- **Context is the fuel** — What an agent can see decides what it can do: the brief, the data, the skills.

#### Agentic AI vs AI Agents

Both use tools, skills and memory. The difference is how long they live and what starts them.

| Feature | Agentic AI — task-oriented | AI agents — always on, 24/7 |
|---|---|---|
| Tool calling | Yes — files, search, connectors, subagents. | Yes — plus chat apps, the browser and other agents. |
| Skills | Yes — loads SKILL.md procedures when the task matches. | Yes — and can write and improve its own skills. |
| Memory | Within the task, plus project memory across sessions. | Long-term memory about you and your work. |
| Availability | Starts when you give it a task; stops when done. | Runs 24/7 on a computer or server. |
| Started by | You, with a task. | You, a schedule, a message or another agent. |
| In this course | A Claude Code session running a campaign (Labs 1–5, 10–12). | The scheduled weekly report (Lab 13). |

Tip: Rule of thumb: a job with an end → agentic AI; a job that recurs → an always-on agent.

#### What Is an Agent Made Of?

A model on its own can only answer. Wrap it with these parts and it can act — and check what it did.

**The Brain — Claude** (the model): Reads the goal, plans the next step and picks the part to use.

**The agent:**

- **Instructions** — Its job and rules — CLAUDE.md and an agent file.
- **Tools** — Actions: read and write files, search, run code, use a connector.
- **Skills** — Saved procedures it loads when the task matches — SKILL.md.
- **Memory** — What it keeps between sessions: preferences, past fixes.
- **Knowledge base** — Trusted sources only: Horizon's facts sheet, brand and compliance rules.
- **Guardrails** — Permissions, approvals and hooks — what it must ask first.

You build every one of these for Horizon's six agents in Labs 2–4.

#### Build a Marketing Team, Then Run Campaigns

Horizon Wealth Planning has a website, a goal of 40 booked chats a month — and no marketing team. You build one, made of AI agents.

1. **Form the team** — A Lead and five specialists: instructions, skills, connectors (Labs 1–4).
1. **Campaign 1** — Research, ideas and a storyboard (Lab 5).
1. **Know the audience** — Personas, requirements, cadence (Labs 6–7).
1. **First content** — A blog article and the lead magnet (Labs 8–9).
1. **Campaigns 2–4** — Social week, newsletter + landing page, video (Labs 10–12).
1. **Campaign 5** — Always on: the weekly report; the playbook (13–14).

#### Meet Horizon Wealth Planning

The firm's public website — the same link for every learner. You do not build it; every campaign points back here.

- **Plain English** — Retirement, CPF, insurance and investing — no jargon, no hard sell.
- **One goal** — Turn visitors into booked free 30-minute chats.
- **Regulated** — Financial content: general information only, never a promised return.

#### Your AI Marketing Team

One Lead and five specialists — each with instructions, its own skills and connectors.

**Marketing Team Lead** — plans · assigns · checks · hands to a person.

- **Growth Strategist** — Research, positioning, briefs, storyboards.
- **Content Creator** — Posts, newsletter, scripts, page copy.
- **Creative Designer** — Images, thumbnails, the video.
- **Website Designer** — Landing pages, published and checked.
- **Growth Analyst** — Personas, cadence, results, reports.

Nothing reaches a customer unless a person approved that exact version.

#### Who Does What

Each agent's job, the skills it owns and the connectors it may use.

| Agent | Job | Skills | Connectors |
|---|---|---|---|
| Team Lead | Plans, assigns, checks, hands to a person | fact-check, fin-compliance | Google Drive (read), Gmail (drafts only) |
| Growth Strategist | Research, positioning, briefs, storyboards | competitor-scan, campaign-brief, content-marketing | web search, Firecrawl (search, scrape), Google Drive (read) |
| Content Creator | Posts, newsletter, scripts, page copy | sunny-voice, copywriting, channel-formats, linkedin-post, facebook-post, blog-post, newsletter | Google Drive (docs), Gmail (drafts only) |
| Creative Designer | Images, thumbnails, the video | brand-visuals, video-render | Bash for Pillow (images) and ffmpeg (video) |
| Website Designer | Landing pages, published and checked | web-design, landing-page, lead-magnet, page-qa | artifacts (publish), built-in browser (check) |
| Growth Analyst | Personas, cadence, results, reports | audience-insights, campaign-report | Google Drive and Sheets (read), Bash for Python |

Tip: You build every part of this table in Labs 2, 3 and 4.

#### The Tools for This Edition

The Claude Edition: two Claude products, one studio.

| Tool | What the team uses it for | Labs |
|---|---|---|
| Claude Code | Every lab, in Code mode: agent and skill files, subagents, agent teams, the approval gate, routines, the video | Labs 1–15 |
| Claude artifacts | Every result from Lab 5 on; Horizon's website (given), your blog post and the landing page | Labs 1, 5–15 |
| Customize | Connectors (Drive, Gmail, Calendar, Firecrawl) and the Marketing plugin — added once, used by both | Lab 4 |

Tip: Every external post, email and video passes one gate: a person approves the exact version.

#### Why a Team of Agents?

The Lead runs specialists in parallel, each in its own context, then combines what they return.

- **Faster** — Research, copy and design run at the same time.
- **Focused** — Each agent holds only its own job and its own skills.
- **Specialised** — Its own instructions, tools, connectors and model.
- **Second opinion** — The Lead checks work it did not write.
- **The cost** — More tokens and more to review. Split only work that is truly independent.

#### Get the Tools Ready

Install once; every lab says which tool to open.

- **Claude desktop** — Claude and Claude Code in one app
- **No commands** — The trainer readies Claude Code
1. **Claude desktop** — Install from claude.com/download and sign in on a paid plan.
1. **Claude Code** — Open it from the desktop app; the trainer has set it up before class.
1. **Sign in with your claude.ai account** — Connectors, plugins and artifacts need it — not an API key.
1. **Already installed for you** — The helpers behind the approval gate and the video. You never run them yourself.
1. **A personal Google account** — For Drive and Gmail — never an employer's.

Note: Claude Code and artifacts need a Pro, Max, Team or Enterprise plan.

#### A Home for the Team

Before you hire agents, give them shared rules, shared facts and a website to point to.

- **CLAUDE.md** — The team charter every agent reads at the start of every session. Under 60 lines.
- **data/** — The facts sheet, brand, compliance checklist and business brief — the only sources agents may use.
- **Horizon's public website** — Given, not built: each learner opens their own local copy; the public copy is on GitHub Pages.

### Lab 1 — Build Your Marketing Agent Team

**The story so far:** October 2026. Rachel has a website and a goal: 40 booked chats a month by March. She has no marketing team. Before you hire one made of agents, give it a home — shared rules, shared facts — and open your own copy of Horizon's website.

**Goal:** Before anyone builds a team, the team needs a home: one folder of shared facts and rules, and your own copy of Horizon's website — the one every post links to.

**You'll build:** horizon-studio/ with CLAUDE.md, the shared data, and your own copy of the site running at http://localhost:8080/

**Horizon's website**

- **Your website (the link in every post):** http://localhost:8080/
- **Public site (to look at only):** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/

**Folder structure**

```
labs/
└── horizon-studio/     ← choose this folder
    ├── content/        posts, newsletter, scripts (agents fill it)
    ├── data/           every lab's briefs and data, ready to read
    ├── README.md
    ├── reports/        campaign results, the weekly report
    ├── research/       market and competitor research
    ├── review/         approvals
    ├── strategy/       briefs, personas, calendar
    └── web/
        └── site/
            └── index.html  the local copy of Horizon's site
```

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code  ·  **Time:** 30 min  ·  **Slides:** 30–34

**Lab folder:** labs/lab-01-studio-and-website/ — assets: horizon-site.html, team-charter.md, business-brief.md, brand.md, facts-2026.md, compliance-checklist.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-1

**Step-by-step**

1. **Choose Code mode and the folder** — In the Claude desktop app switch to Code mode (the </> button at the top), not Work mode — Code shows every file and opens artifacts beside the chat. Under Project or folder choose Add folder (not New project) and pick the ready-made labs/horizon-studio.
1. **Trust it** — Sign in with your claude.ai account and trust the folder. Click the session title at the top and rename it "Lab 1" — every lab gets its own session.
1. **Plan your team** — Copy and paste Prompt A. Answer as Horizon's owner and pick your team — keep the six charter roles. It is a plan only: Lab 2 builds the agents.
1. **Write the charter** — After Claude saves data/team-design.md, copy and paste Prompt B. Open CLAUDE.md — every agent reads it.
1. **Open the website** — Ask: "Start my website." It opens at http://localhost:8080/ — your own copy of Horizon's website; Labs 8 and 9 add to it, and every post links to it. Check the calculator shows S$693,138.

**PROMPT A — Claude Code: plan your team**

> Act as a marketing consultant. Interview me, the owner of Horizon Wealth Planning, to plan my AI marketing team. Ask one question at a time and wait for my answer: my goal, what success looks like by March 2027, who we want to reach, which channels we use, how much we publish each week, and who approves before anything goes out. Then list 8 to 10 team members I could have, numbered, each with a one-line job. Include the six roles in data/team-charter.md and mark the ones you recommend. Wait for me to choose. Save my answers and my chosen team, with each member's job, to data/team-design.md. This is a plan only: do not create any agent files yet.

**PROMPT B — Claude Code: the charter**

> Read data/team-charter.md, data/team-design.md and data/business-brief.md. Write CLAUDE.md for this studio in four sections — What this is, The team, Rules, Files — under 60 lines. The team is the one I chose in data/team-design.md. Rules: every number comes from data/facts-2026.md; every piece passes fact-check and fin-compliance; nothing is published or sent without a person's approval (the one exception: a review email to the approver); anything shown to me is in plain English for a business owner, with no codes, IDs, file names or line numbers. In Files, add two lines:
> - Our copy of the site, which we edit: web/site/. "Start my website" runs scripts/serve-site.mjs in the background and opens http://localhost:8080/
> - Every post links to http://localhost:8080/ with UTM tags, never to a claude.ai artifact link.

**Check your work**

- ☐  Claude shows horizon-studio as the chosen folder.
- ☐  data/team-design.md holds your answers and the team you chose, with the six charter roles in it — and no agent files yet.
- ☐  CLAUDE.md has the four sections and is under 60 lines.
- ☐  Its rules name the facts sheet, the two checks and the human approval.
- ☐  CLAUDE.md names your copy of the site and the link every post points to.
- ☐  Your website opens at http://localhost:8080/; the calculator shows S$693,138.

**If it goes wrong**

- **The website does not open** — Say: "Start my website again." If the page still does not load, say: "Open web/site/index.html in my web browser."
- **It created agent files already** — Not yet — say "Move everything in .claude/agents/ to _archive/. We build the team in Lab 2." The plan in data/team-design.md is all Lab 1 needs.

**Stretch**

- Ask: "Read web/site/index.html. In five bullets: who it is for, the offer, the main call to action, what the calculator does, and the disclaimer."
- Ask for a one-paragraph summary of the site from the point of view of a busy 35-year-old parent.

Why it matters: Shared context first, agents second. Every agent you add later starts from these files, so a wrong rule here is wrong everywhere.

### Key ideas for Lab 2

#### Anatomy of an Agent

A Markdown file in .claude/agents/. The same file works as a subagent or as an agent-team teammate.

**.claude/agents/content-creator.md**

```
---
name: content-creator
description: Use for Horizon copy — posts, newsletter,
  video scripts and page copy, in the Sunny voice.
tools: Read, Write, Edit, Grep, Glob
model: sonnet
skills:
  - sunny-voice
  - copywriting
  - channel-formats
  - linkedin-post
  - facebook-post
  - blog-post
  - newsletter
---
You are Horizon Wealth Planning's Content Creator.
## What you read   the brief, facts-2026.md, brand.md
## What you deliver   content files, ready for review
## Connectors   Google Drive (docs), Gmail (drafts only)
## Never   add a number not on the facts sheet; send;
           approve or publish for real
## Report back   what, where, anything unverified
```

#### Good Agent Instructions

Five parts, every time. The "Never" part matters most in a regulated firm.

- **The job** — One sentence: what this agent is for. The description decides when Claude delegates to it.
- **Reads and delivers** — Which files it may use; what it hands back, and where.
- **Never** — Its hard limits: no invented figures, no sending, no publishing, no approving.
- **Report back** — Three lines: what, where, anything unverified — so the Lead can combine results.

### Lab 2 — Form the Team: Instructions for Each Agent

**The story so far:** Rachel sketches the team on a whiteboard: a Lead and five specialists. Each needs a clear job, and a clear line it must never cross — this is a regulated firm.

**Goal:** A team is a set of clear jobs. Write each agent's instructions once — its job, what it reads, what it delivers and what it must never do — and every campaign can call on it.

**You'll build:** .claude/agents/: growth-strategist, content-creator, creative-designer, website-designer, growth-analyst

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (subagent files)  ·  **Time:** 40 min  ·  **Slides:** 37–42

**Lab folder:** labs/lab-02-agent-instructions/ — assets: role-specs.md, team-org-chart.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-2

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 2". Run all of this lab's prompts in it.
1. **Read the roles** — Open role-specs.md: one Lead and five specialists, each with a job, skills, connectors and limits.
1. **Write the instructions** — Copy and paste Prompt A. It builds the five specialists from the charter; extra ideas stay in team-design.md.
1. **See the team** — After the five files appear in .claude/agents/, copy and paste Prompt B. The Lead is not a file — it is you, in this session.
1. **Read one closely** — Open .claude/agents/content-creator.md. Is the "Never" section strict enough for a regulated firm?
1. **Meet the team** — After the list shows five agents, copy and paste Prompt C. Each agent introduces itself in one line — in its own context.
1. **Tighten one** — Change one instruction you disagree with and save it. It is your team.

**PROMPT A — Claude Code: five subagents**

> Read data/role-specs.md. Create five project subagents in .claude/agents/ — growth-strategist, content-creator, creative-designer, website-designer and growth-analyst. Each file has:
> - frontmatter: name; a description that says when to use it; tools; model (opus for the strategist, sonnet for the others)
> - a body with: the job, what it reads, what it delivers, the connectors it may use, what it must never do, and how it reports back. No skills line yet — we add skills in Lab 3.

**PROMPT B — Claude Code: see the team**

> List the subagents in .claude/agents/. For each, show the file name, the name, the one-line description and the model, in a table. Then confirm there are five, and that none of them is the Marketing Team Lead — the Lead is this session. If any other file is there, list it and ask me before moving it to _archive/.

**PROMPT C — Claude Code: meet the team**

> Use each of the five subagents once, in parallel. Ask each: "In one line, who are you, and what is the first thing you would do for Horizon's goal of 40 booked chats a month?" Show me the five answers in a table.

**Check your work**

- ☐  Five files exist in .claude/agents/, one per specialist.
- ☐  Each has a name, a "use when" description, tools and a model.
- ☐  Your session acts as the Marketing Team Lead.
- ☐  Five agents answered, each in its own context.
- ☐  Every agent has a "never" rule that blocks publishing.
- ☐  You changed one instruction and can say why.

**If it goes wrong**

- **A subagent never runs** — Name it: "use the growth-strategist subagent" or @agent-growth-strategist.
- **There are more than five files** — Files such as marketing-team-lead, compliance-reviewer or community-manager come from an earlier run. Let Prompt B move them to _archive/: the Lead is your session, and the fin-compliance skill (Lab 3) does the compliance review.
- **/agents says the wizard has been removed** — Expected — it only prints a reminder now. Paste Prompt B to list the team, or open .claude/agents/ in the Files panel (the folder icon, top right).

**Stretch**

- Add a sixth agent, community-manager, that drafts replies to comments — and decide what it must never do.

Why it matters: Clear jobs beat clever prompts. An agent that knows what it must never do is safer than one that is merely told to be careful.

### Key ideas for Lab 3

#### Twenty Skills, Owned by Role

Instructions say who an agent is; skills say how it does the job.

| Agent | Skills |
|---|---|
| Team Lead | fact-check, fin-compliance |
| Growth Strategist | competitor-scan, campaign-brief, content-marketing |
| Content Creator | sunny-voice, copywriting, channel-formats, linkedin-post, facebook-post, blog-post, newsletter |
| Creative Designer | brand-visuals, video-render |
| Website Designer | web-design, landing-page, lead-magnet, page-qa |
| Growth Analyst | audience-insights, campaign-report |

Tip: Master copies in skills/; .claude/skills/ — Claude Code reads them from your folder.

#### Anatomy of a Skill

Frontmatter (the trigger), then short steps. Free until it is needed.

**.claude/skills/campaign-brief/SKILL.md**

```
---
name: campaign-brief
description: Use when planning a Horizon campaign.
  Objective, audience, message, proof, channels,
  CTA, measures, and a five-beat storyboard.
---
# Campaign brief
1. Objective: one measurable action (e.g. chats booked).
2. Audience: the persona(s) from strategy/personas.md, with evidence.
3. Core message in one sentence; proof from data/facts-2026.md only.
4. Channels and formats; one call to action; measures and a date.
5. Storyboard in five beats — hook, tension, proof, resolution, action —
   each with visual, words, claim and source.
6. Never: returns, fee amounts, invented clients, fear.

```

### Lab 3 — Give Each Agent Its Skills

**The story so far:** The team exists, but every agent writes in its own way. Rachel wants Horizon's voice, facts and compliance rules applied the same way by every agent, every time.

**Goal:** Instructions say who an agent is; skills say how it does the job. Write each procedure once and every agent applies it the same way, every time.

**You'll build:** twenty skills in .claude/skills/, wired to the agents that own them

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (.claude/skills/)  ·  **Time:** 45 min  ·  **Slides:** 45–50

**Lab folder:** labs/lab-03-agent-skills/ — assets: skills-spec.md, channel-formats.md, brand.md, facts-2026.md, compliance-checklist.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-3

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 3". Run all of this lab's prompts in it.
1. **Read the spec** — skills-spec.md lists the twenty skills and who owns each.
1. **Create the skills** — Copy and paste Prompt A.
1. **Wire them up** — After the twenty skills appear in .claude/skills/, copy and paste Prompt B, then C to list every skill. The Lead's two go in CLAUDE.md, not a file.
1. **Test without naming** — In a new session ask: "Write a Facebook post about the free Money Check-up Checklist." Ask which skills were used.
1. **Break it on purpose** — Ask for a post that says "guaranteed 8% a year". fin-compliance must flag it as Critical.

**PROMPT A — Claude Code: twenty skills**

> Read data/skills-spec.md. Create the twenty skills in .claude/skills/<name>/SKILL.md. Each has frontmatter (name, and a description that starts "Use when…") and short numbered steps, under 80 lines. Use data/brand.md, data/channel-formats.md, data/facts-2026.md and data/compliance-checklist.md as the sources — do not invent rules.

**PROMPT B — Claude Code: wire them up**

> Add a skills: list to each subagent in .claude/agents/ with its skills from data/skills-spec.md. Leave any other agent file as it is. Add to CLAUDE.md that the Lead (this session) runs fact-check and fin-compliance on everything before showing it to me.

**PROMPT C — Claude Code: see the skills**

> List the skills in .claude/skills/. Show each skill, its owner (a subagent, or the Lead) and its "Use when" line in a table. Confirm there are twenty, that each specialist has the skills the spec gives it, and that fact-check and fin-compliance belong to the Lead (this session).

**Check your work**

- ☐  Twenty folders in .claude/skills/, each with a SKILL.md.
- ☐  Every description starts "Use when…".
- ☐  Each specialist lists its own skills from the spec.
- ☐  The untold test picked sunny-voice and facebook-post.
- ☐  fin-compliance flagged "guaranteed 8%" as Critical.

**If it goes wrong**

- **A skill never triggers** — Rewrite its description with the words a person would actually type.
- **I cannot see the skills** — Paste Prompt C, or open .claude/skills/ in the Files panel (the folder icon, top right) — one folder per skill, each with a SKILL.md.

**Stretch**

- Add one more skill, utm-links, owned by the Content Creator.

Why it matters: A skill costs almost nothing until it is needed. Keep the rules file (CLAUDE.md) short and put procedures in skills.

### Key ideas for Lab 4

#### Connectors for Each Agent

Add once in the desktop app: Customize → Connectors, and the Marketing plugin.

| Agent | May use | Limit |
|---|---|---|
| Team Lead | Google Drive (read), Gmail (drafts only) | reads; drafts only |
| Growth Strategist | web search, Firecrawl (search, scrape), Google Drive (read) | cite every source |
| Content Creator | Google Drive (docs), Gmail (drafts only) | Gmail: drafts only |
| Creative Designer | Bash for Pillow (images) and ffmpeg (video) | no fake "clients" |
| Website Designer | artifacts (publish), built-in browser (check) | publish after approval |
| Growth Analyst | Google Drive and Sheets (read), Bash for Python | no personal data |

Tip: Use your personal Google account — never an employer's.

#### Least Privilege

A regulated firm gives each agent only what its job needs.

- **Ask of each connector** — Does this agent's job need it? If not, it does not get it.
- **Drafts, not sends** — Email is drafted, posts are files, pages wait — a person sends and publishes.
- **Write it down** — Each agent's instructions name its connectors and limits; its tools line removes what it does not need.

### Lab 4 — Connect the Tools Each Agent Needs

**The story so far:** The analyst cannot read the data, the designer has no design tool and the creator cannot draft an email. Connect each agent to what its job needs — and nothing more.

**Goal:** An agent can only do the job if it can reach the tools — and a regulated firm only lets each agent reach the tools its job needs. Connect them, then test each one.

**You'll build:** every specialist tested on its own connector, with its limits written into its instructions

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude desktop app (Customize → Connectors), Claude Code  ·  **Time:** 40 min  ·  **Slides:** 53–57

**Lab folder:** labs/lab-04-agent-connectors/ — assets: connectors-setup.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-4

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 4". Run all of this lab's prompts in it.
1. **Add the connectors** — Desktop app: Customize → Connectors → Discover. Add (+) Google Drive, Gmail, Google Calendar and Firecrawl; sign in to each.
1. **Add the plugin** — In the chat type /plugin marketplace add anthropics/knowledge-work-plugins, then /plugin install marketing@knowledge-work-plugins.
1. **Check** — Start a new session. Type /mcp: the four connectors are listed. Type /plugin: Marketing is installed.
1. **Put the data on Drive** — Ask: "Create a Google Drive folder named Horizon Studio and upload every file in data/ to it as plain files — do not convert them."
1. **Give each agent its connectors** — Copy and paste Prompt A, then start a new session so the agents reload.
1. **Test each agent** — After the new session opens, copy and paste Prompt B — one small job per agent, each on its own connector.

**PROMPT A — Claude Code: give each agent its connectors**

> Read data/connectors-setup.md. For each subagent in .claude/agents/, replace its tools line with the one given there, add the disallowedTools line where one is given, and update its "Connectors" section: what it may use, and that Gmail is drafts only. Change nothing else.

**PROMPT B — Claude Code: test each agent**

> First tell me which connectors and plugins you can use. Then run these five checks, each by its own subagent:
> 1. growth-strategist: Firecrawl — search for one 2026 news item about financial planning in Singapore, scrape it and cite it.
> 2. growth-analyst: Google Drive — read firm-metrics.csv from Horizon Studio; report average monthly enquiries.
> 3. content-creator: Gmail — a DRAFT to me with the subject "Connector test". Do not send.
> 4. creative-designer: render a 1080x1080 test card in Horizon colours and save it in content/test/.
> 5. website-designer: built-in browser — open our own copy of the site (web/site/index.html) at 375px wide and report any problem. Report each result in one line. If a check fails, say which tool was missing.

**Check your work**

- ☐  /mcp lists Google Drive, Gmail, Google Calendar and Firecrawl; /plugin shows Marketing.
- ☐  Five checks ran, each by its own agent.
- ☐  The Gmail test is a draft in your inbox — nothing was sent.
- ☐  The analyst read the CSV from Drive, not from the local folder.
- ☐  Each agent's tools line names only the connectors its job needs.

**If it goes wrong**

- **Insufficient scope** — Reconnect and grant read access to the Horizon Studio folder.
- **Claude cannot upload to Drive** — Check Google Drive is in /mcp. Or upload the files yourself: drive.google.com → New → New folder "Horizon Studio", open it → New → File upload.
- **An agent says it has no Drive or Gmail tools** — Its tools line does not name the connector, or the session is old. Paste Prompt A again, then start a new session.
- **A connector is missing from /mcp** — Customize → Connectors → Yours: it must be there and signed in — if not, find it under Discover and click +. Then start a new session.
- **/mcp shows no connectors at all** — Type /status: you must be signed in with your claude.ai account, not an API key.
- **The Marketing plugin is not listed** — Type /plugin: it must be installed and enabled. Start a new session. Its optional connectors (HubSpot, Ahrefs and others) are not needed.
- **The browser check fails** — Skip check 5 and open the site on your phone instead.

**Stretch**

- Give Google Calendar to the Lead only, for review deadlines.

Why it matters: Least privilege is a design decision, not a setting. Ask of each connector: does this agent's job need it?

### Key ideas for Lab 5

#### How the Team Runs a Campaign

Campaign 1, "Know Your Number": research in parallel, a person chooses, the team makes it concrete.

1. **Lead briefs** — Reads the campaign objective; assigns the work.
1. **Research** — Strategist (competitors) and Analyst (funnel) in parallel.
1. **Ideas** — Nine ideas for three audiences, scored with the rubric.
1. **You choose** — The human concept checkpoint.
1. **Storyboard** — Strategist storyboards; Creator writes three variants; Lead checks.

#### The Five-Beat Storyboard

Every channel tells the same story with the same claims.

1. **Hook** — The viewer's own question: "Do I have enough to retire?"
1. **Tension** — What goes wrong when nobody knows their number.
1. **Proof** — One verifiable fact, e.g. the 2026 Full Retirement Sum.
1. **Resolution** — How Horizon helps — a 30-minute chat, a one-page plan.
1. **Action** — One next step: the checklist or a free chat.

#### Financial Content Is Regulated

The Lead checks every piece against twelve rules (compliance-checklist.md).

| Rule | What it means | If broken |
|---|---|---|
| C1 · Not advice | General information only — say so | Critical |
| C2 · No promises | No guaranteed or "risk-free" returns | Critical |
| C3 · Label illustrations | Assumptions shown; not guaranteed | Critical |
| C5 · No performance | Never client returns or "average" returns | Critical |
| C9 · Consent | Marketing only to people who opted in | Critical |
| C11 · Facts sheet | Every figure from facts-2026.md | Critical |

Tip: MAS Guidelines on Standards of Conduct for Digital Advertising Activities apply from 25 March 2026.

### Lab 5 — Campaign 1: Research to Storyboard, with Subagents

**The story so far:** The team's first campaign: 'Know Your Number', November to January. Rachel wants research, ideas for three audiences, her choice, and a storyboard every channel follows.

**Goal:** The team's first job: find who to reach and what to say for the "Know Your Number" campaign — research in parallel, ideas scored, a person choosing, a storyboard every channel follows.

**You'll build:** competitor research, the funnel, nine scored ideas, the campaign brief and a five-beat storyboard with three channel variants — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (subagents in parallel)  ·  **Time:** 45 min  ·  **Slides:** 61–67

**Lab folder:** labs/lab-05-campaign-1-research-to-storyboard/ — assets: campaign-objective.md, idea-rubric.md, storyboard-template.md, firm-metrics.csv, services.csv

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-5

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 5". Run all of this lab's prompts in it.
1. **Brief the Lead** — The briefs are already in data/. You are the client; your session is the Marketing Team Lead.
1. **Research in parallel** — Copy and paste Prompt A. Watch the strategist and the analyst run at the same time.
1. **Read the ideas** — Nine ideas, scored with the rubric — the top five open as an artifact beside the chat. The Lead stops for you.
1. **Choose** — Pick one idea in the artifact's Ideas tab and note its number and why — the human concept checkpoint.
1. **Storyboard** — After you have chosen, copy and paste Prompt B in the chat, replacing <number> and <one line> with your choice.
1. **Decide as Rachel** — After you have read the issues, copy and paste Prompt C. You confirm what is true about Horizon; the team removes or fixes the rest.

**PROMPT A — Claude Code: research and ideas**

> Act as the Marketing Team Lead for the campaign in data/campaign-objective.md. Use subagents, in parallel:
> - growth-strategist: competitor-scan → save research/competitive-analysis.md.
> - growth-analyst: the funnel in data/firm-metrics.csv — what 40 chats a month needs → save research/funnel.md. When both finish, the growth-strategist proposes three ideas each for young professionals, mid-career families and pre-retirees, scored with data/idea-rubric.md and tagged with a funnel stage (content-marketing) → strategy/ideas.md. Publish the top five as an artifact — one card per idea with its score, persona and funnel stage — and a box at the top that tells me what to do next. Then stop. I will choose. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: the storyboard**

> I choose idea <number>, because <one line>. Use subagents:
> - growth-strategist: campaign-brief → strategy/campaign-brief.md, then a five-beat storyboard with data/storyboard-template.md → strategy/storyboard.md.
> - content-creator: three channel variants that keep the same claims — LinkedIn, Facebook, a 60-second video. Then run fact-check and fin-compliance yourself and show me the issues before anything is final. Publish the brief and the storyboard as an artifact with a tab for the brief (goal, audience, message, call to action); a tab for the five beats side by side, each with its claim and source, and the three variants below; and the issues in a table. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT C — Claude Code: decide on the issues**

> I confirm "no obligation" and the free checklist — add them to the facts sheet (data/facts-2026.md). Delete any other claim that is not on the facts sheet. Fix all the Medium and Low issues, then show me the updated storyboard and publish it as an artifact. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- **After Prompt A:** "Explain this result in three sentences. Which idea would you pick, and why?"
- "Why does idea <number> score higher than idea <number>?"
- "What does the funnel say is our biggest problem?"
- **After Prompt B:** "Explain the issues in plain English. What do I need to decide?"
- **After Prompt C:** "What changed since the last version? Is anything still not ready for Rachel?"

**Check your work**

- ☐  The strategist and the analyst ran in parallel.
- ☐  The competitor analysis and the funnel are done, with sources.
- ☐  Nine scored ideas, each with its author.
- ☐  You chose the idea and recorded why.
- ☐  The storyboard has five beats; every claim has a source.
- ☐  You confirmed two claims; after Prompt C no High issue is left.

**If it goes wrong**

- **The Lead did the work itself** — Ask directly for subagents, naming each agent.

**Stretch**

- Ask the analyst which persona the funnel says to target first, and compare it with your choice.

Why it matters: Agents diverge; a person decides. The concept checkpoint is where the campaign becomes yours.

### Topic 1 recap

#### Where You Are Now

The team exists and has run its first campaign. But who exactly is it for — and how often should it publish?

- **Formed  ·  Labs 1–4** — A studio, the public website, six agents with instructions, skills and connectors.
- **Campaign 1  ·  Lab 5** — Research in parallel, nine scored ideas, your choice, a storyboard.
- **What is missing** — Evidence about the audience and a cadence the team can deliver. That is Topic 2.

## Topic 2 — Audience Research and Content Requirement Analysis

Slides 69–91. In this topic you will:

- The Growth Analyst: personas from evidence
- Content requirements every agent can follow
- How often to publish: value, fatigue and capacity
- The calendar the team will run

### Key ideas for Lab 6

#### Evidence Before Personas

Lab 6: the Growth Analyst builds personas the way an analyst would.

1. **Collect** — 150 survey answers, 60 enquiries, 200 checklists.
1. **Count** — With code. Every claim has an n and a file.
1. **Segment** — By age band and life stage.
1. **Persona** — Worries, channels, formats, trust — with evidence.
1. **Requirement** — What each persona needs from every piece.

#### Observed, Inferred or Low Confidence?

Three labels keep a persona honest.

| Label | Example | Use it |
|---|---|---|
| Observed | 30–39s chose Facebook, LinkedIn and YouTube equally (survey, n = 44) | As fact, with the count |
| INFERENCE | "They are short of time on weekdays" — not asked | As a hypothesis to test |
| LOW CONFIDENCE | The 60+ group (n = 12) | Never alone; get more data |
| Verbatim | "I am 54 and not sure if my CPF will be enough." (E-id) | Exactly as written, with the id |

Tip: Ask "which rows show that?" of anything that sounds insightful.

### Lab 6 — Growth Analyst: Personas from Evidence

**The story so far:** Jun Wei drafted personas from instinct: 'busy young parents who love TikTok'. Rachel is not convinced. There are 150 survey answers, 60 enquiries and 200 checklists.

**Goal:** Personas made up in a meeting steer content wrong. The Growth Analyst builds them from 150 survey answers, 60 enquiries and 200 checklists — and labels what is guesswork.

**You'll build:** three evidence-based personas and the content spec — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (three analyst subagents in parallel)  ·  **Time:** 40 min  ·  **Slides:** 72–77

**Lab folder:** labs/lab-06-personas-from-evidence/ — assets: survey-responses.csv, enquiries.csv, checklist-results.csv, persona-template.md, content-spec-template.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-6

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 6". Run all of this lab's prompts in it.
1. **Check the data** — The CSVs and templates are already in data/. Open one and skim it.
1. **Analyse in parallel** — Copy and paste Prompt A — three analyst sub-agents, one per file.
1. **Challenge a claim** — Pick one persona statement and ask: "which rows show that?"
1. **Write the guides** — After the persona cards appear, copy and paste Prompt B: a writing guide for each persona — how to talk to them.
1. **Check the gaps** — The 60+ group must be LOW CONFIDENCE.

**PROMPT A — Claude Code: three analysts**

> Use three growth-analyst subagents in parallel, one per file: data/survey-responses.csv, data/enquiries.csv, data/checklist-results.csv. Each uses audience-insights: counts with code, n and the file on every claim, INFERENCE and LOW CONFIDENCE labels, enquiry quotes verbatim with ids. Combine the results into three personas with data/persona-template.md → strategy/personas.md. Publish the personas as an artifact: one card each, with the key counts as small bar charts and the confidence label in colour. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: requirements**

> Use the growth-strategist and the content-creator subagents to write a writing guide for each persona (data/content-spec-template.md → strategy/content-spec.md): what they most want to know, where to reach them, what to make and how long, the tone, the proof that convinces them, what we ask them to do next, and what we never say. Back each answer with the data: which file, and how many people. Publish it as an artifact: one card per persona with a one-line summary on top and the answers under plain headings, then one table comparing the three personas side by side. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Explain these personas in three sentences. Which one should we target first, and why?"
- "Which survey answers show that <a sentence from a persona>?"
- "Why is the 60+ group marked low confidence?"

**Check your work**

- ☐  Three analyst sub-agents ran, one per file.
- ☐  Every persona statement carries a count and a file.
- ☐  The 60+ group is LOW CONFIDENCE (n = 12).
- ☐  The most-unticked checklist item is the retirement number.
- ☐  Enquiry quotes are verbatim, with ids.
- ☐  The writing guide answers every question for every persona.

**If it goes wrong**

- **Numbers change between runs** — Insist on counting with code and showing the printed output.

**Stretch**

- Ask the analyst for a filterable dashboard of the survey as an artifact.

Why it matters: Ask "which rows show that?" of anything that sounds insightful. If the agent cannot point to rows, it is an inference.

### Key ideas for Lab 7

#### Finding the Right Frequency

Lab 7: the Analyst finds where more posts stop paying; the Strategist plans four weeks.

1. **Value** — Extra clicks from one more post a week.
1. **Fatigue** — Unfollows and unsubscribes it costs.
1. **Effort** — Hours per piece, against 12 a week.
1. **Review** — Two business days for Rachel's sign-off.
1. **Calendar** — Four weeks the team can actually deliver.

Tip: A third LinkedIn post a week brings more unfollows than value. Weekly emails make unsubscribes jump.

### Lab 7 — Growth Analyst and Strategist: Cadence and Calendar

**The story so far:** Jun Wei has 12 hours a week and Rachel needs two business days to review anything. How often should each channel run, and what goes out when?

**Goal:** Post too little and nobody remembers you; too much and people unfollow. The analyst finds the point where more stops paying; the strategist turns it into four deliverable weeks.

**You'll build:** how often to post on each channel, and a four-week calendar — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (subagents)  ·  **Time:** 35 min  ·  **Slides:** 79–84

**Lab folder:** labs/lab-07-cadence-and-calendar/ — assets: channel-benchmarks.csv, team-capacity.md, calendar-format.csv

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-7

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 7". Run all of this lab's prompts in it.
1. **Check the data** — The assets are already in data/. Open one and skim it.
1. **Find the sweet spot** — Copy and paste Prompt A.
1. **Question it** — Why is the newsletter not weekly? The answer is in the unsubscribes.
1. **Plan four weeks** — After the analyst recommends a cadence, copy and paste Prompt B.
1. **Check the buffers** — Every review date is two business days ahead; nothing on a holiday.

**PROMPT A — Claude Code: the analyst**

> Use the growth-analyst subagent. From data/channel-benchmarks.csv and data/team-capacity.md, recommend how often to publish on LinkedIn, Facebook, the newsletter and YouTube. Compare the extra clicks from one more post, the unfollows or unsubscribes it costs, and the hours → strategy/cadence.md. Publish it as an artifact: a chart per channel of the extra clicks against the unfollows, and the hours. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: the strategist**

> Use the growth-strategist subagent to build a four-week calendar from Monday 2 November 2026 in strategy/calendar.csv (columns as data/calendar-format.csv), from the cadence, strategy/storyboard.md and strategy/content-spec.md. review_by two business days before each date; no public holidays; no week over the team's hours. Publish the four weeks as an artifact: a calendar grid by channel, review dates marked, hours per week. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Why is the newsletter not weekly? Show me the numbers."
- "What happens if we add a third LinkedIn post a week?"
- "Which week is busiest, and does the team have the hours?"

**Check your work**

- ☐  The cadence gives a frequency per channel with the evidence.
- ☐  A third LinkedIn post a week costs far more unfollows than it earns.
- ☐  It explains the unsubscribe jump at weekly emails.
- ☐  The calendar covers four weeks in the required columns.
- ☐  Every review_by date is two business days before publishing.
- ☐  No week is over 12 hours.

**If it goes wrong**

- **Dates fall on weekends** — Say: "publish Monday to Saturday; the newsletter is Sunday 8am only".

**Stretch**

- Ask Claude to add the four review deadlines to your Google Calendar.

Why it matters: Frequency is a capacity decision as much as an audience one. A calendar the team cannot deliver is fiction.

### Key ideas for Lab 8

#### From Storyboard to Content

Lab 8: the first real piece — a blog article every post can link to.

- **One prompt, the whole job** — Research, draft, fact-check, fix and post — a quick blog in one go. A person still reads it last.
- **Straight onto your copy of the site** — The article lands on the copy of Horizon's site in your folder, opened in your browser. The public site never changes.
- **Your skills know Horizon** — blog-post, sunny-voice, fact-check and fin-compliance: the voice, the facts and the rules.

### Lab 8 — Content Creator: A Quick Blog Article

**The story so far:** Jun Wei has the storyboard and the personas. Rachel wants the first real piece today: a blog article that people searching for CPF top-ups will find — and that every post can link to.

**Goal:** The storyboard is the plan; now make the first piece, fast. A blog article is the hub every post, email and video links to — and one prompt can take it from research to a checked post.

**You'll build:** a 500-700-word blog article with dated sources, checked and fixed and posted on your own copy of Horizon's website, opened in your browser, with a Word copy

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (Firecrawl, your Horizon skills) → your copy of Horizon's website  ·  **Time:** 40 min  ·  **Slides:** 86–90

**Lab folder:** labs/lab-08-blog-article/ — assets: facts-2026.md, brand.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-8

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 8". Run all of this lab's prompts in it.
1. **Write and post it** — Copy and paste the prompt. Claude researches, writes, checks and fixes the article, then posts it to your copy of Horizon's website.
1. **Read it on the site** — Your copy of the website opens in your browser: your article is first under "From our blog". Say what to change, if anything.

**PROMPT — Claude Code: a quick blog**

> Write a quick blog article for Horizon and post it to the website. Use the blog-post, sunny-voice, fact-check and fin-compliance skills.
> 1. Pick one topic from strategy/storyboard.md that a Singaporean would search for. Use Firecrawl to find two current sources (CPF Board, MAS or MoneySense), each with its date.
> 2. Write 500-700 words: a title under 60 characters, every figure from data/facts-2026.md, one call to action (book a free 30-minute chat) and the full disclaimer → content/blog/<slug>.md.
> 3. Run fact-check and fin-compliance; fix every issue and list each fix in one line.
> 4. Add it to the blog in web/site/index.html as one new post, built like the posts already there. Change nothing else on the site. Then start my website if it is not running, and open it. Write for a business owner, in plain English. Save a Word copy (.docx) of the article.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Summarise the article in three sentences. Who is it for?"
- "Why did you pick this topic, and who will search for it?"
- "What did the checks find, and how did you fix it?"

**Check your work**

- ☐  Two sources, each with a date and a link.
- ☐  The title is under 60 characters.
- ☐  Every figure is from Horizon's 2026 facts.
- ☐  The fixes are listed; no Critical or High issue is left.
- ☐  One call to action and the full disclaimer at the end.
- ☐  Your article is first under "From our blog" on your copy of the website.

**If it goes wrong**

- **Firecrawl finds nothing** — Type /mcp: Firecrawl must be connected — or say "use web search instead".
- **The site looks unchanged** — Refresh the browser page. Or say: "open my website again".
- **The browser does not open** — Say: "Start my website again."

**Stretch**

- Ask for two LinkedIn posts and one Facebook post that link to the article, with linkedin-post and facebook-post.

Why it matters: One prompt can run the whole job — research, writing and checks. A person still reads the result before it goes anywhere.

### Topic 2 recap

#### Day 1: The Team Is Ready

Everything the campaigns need tomorrow is in place.

1. **Home** — Shared rules and facts; Horizon's public website (Lab 1).
1. **Team** — Six agents: instructions, skills, connectors (Labs 2–4).
1. **Campaign 1** — Research, ideas and a storyboard (Lab 5).
1. **Audience** — Personas and requirements from evidence (Lab 6).
1. **Plan** — Cadence and a four-week calendar (Lab 7).
1. **Content** — The first blog article, checked (Lab 8).

## Topic 3 — Multi-Channel Content Creation and Agent Workflow Coordination

Slides 92–132. In this topic you will:

- Subagents or an agent team?
- The lead magnet: a checklist people want, and its emails
- Human in the loop — enforced, not requested
- Campaigns 2–4: social week, newsletter + landing page, video
- From approval to LinkedIn, Facebook, email and YouTube

### Key ideas for Lab 9

#### Content That Earns a Sign-up

Lab 9: the Money Check-up Checklist and the emails that follow it.

1. **Promise** — One problem, one promise: know where you stand in 10 minutes.
1. **Design** — Artifacts: printable pages, cards and previews.
1. **Opt-in** — A required PDPA consent box; the newsletter opt-in separate.
1. **Welcome emails** — Day 0, day 3, day 7 — value first, then a free chat.
1. **Measure** — Downloads, then chats booked.

Tip: Lab 11 builds the landing page that offers it.

### Lab 9 — The Lead Magnet: a Checklist and Its Welcome Emails

**The story so far:** Day 2. Before the campaign weeks start, Rachel wants the thing that turns readers into leads: the Money Check-up Checklist, designed to be downloaded, and the emails that follow it.

**Goal:** The Money Check-up Checklist is what turns a reader into a lead. Make it worth downloading — a branded checklist — and write the welcome emails that follow the download.

**You'll build:** the Money Check-up Checklist as a printable A4 page (artifact and PDF) and on your copy of Horizon's website, and three welcome emails — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (artifact, Gmail drafts, Marketing plugin, your Horizon skills)  ·  **Time:** 50 min  ·  **Slides:** 94–101

**Lab folder:** labs/lab-09-lead-magnet/ — assets: checklist-items.md, brand.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-9

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 9". Run all of this lab's prompts in it.
1. **Design it** — Copy and paste Prompt A. The checklist opens as an artifact; ask in the chat for any change.
1. **Write the welcome emails** — After the checklist looks right, copy and paste Prompt B. The three emails also appear as drafts in your Gmail.
1. **Check it** — After the three emails are saved, copy and paste Prompt C.
1. **Put it on the website** — After the checks pass, copy and paste Prompt D. Your copy of the website opens in your browser, with the checklist behind an email box.

**PROMPT A — Claude Code: the checklist**

> Use the lead-magnet skill. Turn data/checklist-items.md into the "Money Check-up Checklist": a title with one promise, the ten items as tick boxes, one figure from data/facts-2026.md, the next step (book a free chat) and the full disclaimer. Lay it out as a printable A4 page in the colours and fonts in data/brand.md and publish it as an artifact. Save a PDF of it in content/lead-magnet/. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: the welcome emails**

> Use the Marketing plugin's email sequence to write three welcome emails for people who download the checklist: day 0 (here it is), day 3 (the item most people miss — the retirement number), day 7 (book a free chat). Follow the newsletter and sunny-voice skills → content/email/welcome-sequence.md. Then, using the Gmail connector, create the three emails as DRAFTS in my Gmail, addressed to me. Send nothing. Publish the three emails as an artifact: one tab per email, laid out as it will look in the inbox. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT C — Claude Code: check it**

> Run fact-check and fin-compliance on the checklist text and the three emails. Show the issues in one table, with a fix for each. Once I agree, make the fixes in the files and in the Gmail drafts. Publish the table as an artifact, coloured by severity. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT D — Claude Code: put it on the website**

> Add the checked Money Check-up Checklist to Horizon's website in web/site/index.html, as a new section before the reviews, in the site's style:
> the title and promise, what's inside, and an email box with a required consent tick box. Once a valid email is entered, show the ten items as tick boxes and a "Print or save as PDF" button. Add "Free checklist" to the menu. Change nothing else on the site. Then start my website if it is not running, and open it.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Which checklist item do people most often miss, and why does it matter?"
- "Read the day 3 email as a 55-year-old. Is anything unclear?"
- "Explain each issue in one line: what is wrong, and the fix."

**Check your work**

- ☐  The checklist uses Horizon's colours and all ten items.
- ☐  It makes one promise and ends with the full disclaimer.
- ☐  Three emails, each with a subject under 50 characters, are drafts in your Gmail — nothing was sent.
- ☐  Each email has one call to action, unsubscribe and the disclaimer.
- ☐  fin-compliance shows no Critical or High issue.
- ☐  The checklist is on your copy of the website: email and consent first, then the ten tick boxes.

**If it goes wrong**

- **No drafts in Gmail** — Type /mcp: Gmail must be connected (Lab 4). Then say "create the Gmail drafts again".
- **The PDF is missing** — Say: "save the checklist as a PDF in content/lead-magnet/".

**Stretch**

- Ask for a 1080x1350 social card that promotes the checklist, published as an artifact.

Why it matters: A lead magnet earns an email address. Give real value first; the call to action comes last.

### Key ideas for Lab 10

#### Subagents vs Agent Teams

Both run agents in parallel, each with its own context. The difference is who they talk to.

**Subagents** — a team lead starts them; each works in its own context and returns only its result: Strategist (returns a brief); Creator (returns copy); Designer (returns images).

**Agent team** — a team lead keeps a shared task list; teammates claim tasks and message each other directly: Creator (shares hooks); Designer (asks for copy); Analyst (flags segments).

Use subagents when only the result matters. Use a team when the agents need to talk.

#### Which Pattern When?

From the Claude Code documentation, applied to the team.

|  | Subagents | Agent team |
|---|---|---|
| Talks to | Returns a result to the Lead | Teammates message each other directly |
| Coordination | The Lead manages everything | A shared task list; teammates claim tasks |
| Best for | Research, analysis, one-off reviews | Copy ↔ design ↔ review loops |
| Cost | Lower: results are summarised back | Higher: every teammate is its own Claude session |
| Campaigns | Lab 5 (and sub-agents in Claude: Labs 6, 15) | Labs 10, 11, 12 |

Tip: Agent teams are experimental; your studio folder already has them switched on.

#### Running an Agent Team

In Claude Code. Describe the team in plain words.

1. **Already on** — Your studio folder switches agent teams on — nothing to set.
1. **Name the agent types** — "Spawn teammates using the agent types content-creator and creative-designer."
1. **Watch** — ↑ ↓ and Enter open a teammate; Ctrl+T shows the task list.
1. **Steer** — Message any teammate directly; tell the Lead to wait.
1. **Shut down** — "Ask the teammates to shut down" when done.

Tip: Teammates load CLAUDE.md, skills and connectors — but not the Lead's conversation. One team per session.

#### Human in the Loop, Enforced

A rule in a prompt persuades. The publisher kit builds a gate that holds.

- **Only people approve** — You type "approved <id> by <your name>". The gate reads your own message — an agent cannot write one.
- **The approved words go out** — The approval stores a hash. Edit one word and publish --live refuses until a person approves again.
- **A hook stops agents** — The gate blocks agents from approving, editing the approval records, or publishing unapproved items.

#### How the Gate Works

Already in your studio folder. You never run it — you just type.

1. **Submit** — The Lead puts a checked piece up for review.
1. **You read** — The post, the image, the email or the video.
1. **You type** — "approved <id> by <your name>" — or "changes <id>: what to fix".
1. **Recorded** — Your name, the time and a fingerprint of the exact words.
1. **Publish** — Only approved, unchanged pieces. Edit one word and it needs you again.

Tip: The gate is a hook: it reads your own message, and blocks any agent that tries to approve or publish on its own.

#### The Publishing APIs

publish.mjs is a dry run by default. Tokens live only in .env.

| Channel | Endpoint | Permission |
|---|---|---|
| LinkedIn | POST api.linkedin.com/rest/posts  (LinkedIn-Version: YYYYMM) | w_member_social — your own profile |
| Facebook | POST graph.facebook.com/<version>/<page-id>/feed | Page token: pages_manage_posts |
| YouTube | Resumable upload to youtube/v3/videos, privacy private | youtube.upload; unaudited projects stay private |
| Newsletter | No API — HTML + text files, then Gmail drafts | Consent = yes, unsubscribed = no |

Tip: No accounts? Every lab works in dry-run mode: you see the exact request that would be sent.

#### Campaign 2: A Social Media Week

Lab 10, a demo: one LinkedIn and one Facebook post, each with a visual.

1. **Lead** — Reads the brief and the calendar; assigns the posts.
1. **Content Creator** — Two posts with hooks, UTM links, disclaimers.
1. **Creative Designer** — One image per post, with alt text.
1. **Lead review** — fact-check and fin-compliance; fixes go back.
1. **You** — Approve on the review page and paste the line in the chat; then post it yourself (or, optionally, through the API).

### Lab 10 — Campaign 2: Social Media Posts (Demo)

**The story so far:** Week 1 of the campaign starts Monday. As a demo, one LinkedIn post and one Facebook post, each with a visual — and Rachel's one rule: nothing goes out unless a person approved that exact version.

**Goal:** A demo of Week 1: one LinkedIn and one Facebook post, each with a visual. Copy and design must agree, the Lead must check every claim — and only a person can approve.

**You'll build:** two posts with images, reviewed, approved by you and posted by you (or, optionally, through the API) — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (agent team) → LinkedIn, Facebook  ·  **Time:** 50 min  ·  **Slides:** 109–116

**Lab folder:** labs/lab-10-campaign-2-social-week/ — assets: social-brief.md, publisher-kit/, publishing-spec.md, approvals-format.csv, connect-accounts.md, env.example, sample-calendar.csv

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-10

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 10". Run all of this lab's prompts in it.
1. **Get the latest kit** — Copy and paste Prompt A. Claude downloads the newest course files into your folder and starts your website. Your own work stays as it is.
1. **Test the gate** — Ask Claude to approve a post itself. The gate must block it.
1. **Start the team** — After Claude says the kit is up to date, copy and paste Prompt B. The Lead starts two teammates and tells you as each one starts and finishes.
1. **Watch them talk** — The review page opens with a Team chat: the designer asking the creator for each hook, and the Lead's fixes.
1. **Approve as a person** — Review in the artifact (or open the review email and click its link). Click Approve or Request changes on each post, then Copy in the bottom bar and paste into the chat.
1. **Get ready to post** — After you have approved the posts, copy and paste Prompt C. Each post appears with a Copy button for its text, and the folder with the two images opens on your computer.
1. **Post it yourself** — Paste the text, add the image, Post — on LinkedIn and a test Facebook Page. Or stop at the preview.
1. **Optional: post through the apps** — Follow "Optional: post through LinkedIn and Facebook" in this lab's README.

**PROMPT A — Claude Code: get the latest kit**

> Bring this studio up to date with the course kit. Download each file below from https://raw.githubusercontent.com/tertiarycourses/C1034-Multi-AI-Agents-for-Content-Creation/main/labs/horizon-studio/ into the same place here, replacing the old copy:
> .claude/settings.json; scripts/approve-chat.mjs, gate-hook.mjs, lib.mjs, publish.mjs, serve-site.mjs and submit.mjs; data/publishing-spec.md, channel-formats.md, connect-accounts.md, env.example, turning-55-brief.md and turning-55-draft.md. Touch nothing else. Then add these rules to CLAUDE.md if they are missing: every post links to http://localhost:8080/ with UTM tags, never a claude.ai artifact link; a person approves by typing "approved <id> by <name>" in the chat; never ask me to run a command. Then start my website and tell me in one line that the kit is up to date.

**PROMPT B — Claude Code: the social team**

> Create an agent team for Week 1 social from data/social-brief.md and strategy/calendar.csv. Spawn two teammates using the agent types content-creator and creative-designer; you are the Lead.
> - content-creator: 1 LinkedIn + 1 Facebook post with linkedin-post, facebook-post and copywriting, one file each in content/social/week-01/, with the frontmatter in data/publishing-spec.md. Each post links to my website, http://localhost:8080/, with UTM tags.
> - creative-designer: one image per post (a rendered card in Horizon colours: LinkedIn 1200 x 627, Facebook 1080 x 1080) with alt text; message the creator for each post's hook before designing. Save each as a PNG beside its post and fill in the post's image and alt lines.
> - You: fact-check and fin-compliance on every post and image; message fixes to the teammate who owns it. Before you start, ask me how I will review: in the artifact, or by email (then ask for the approver's address). When a post passes, submit it for review with scripts/submit.mjs. Publish the two posts as an artifact. At the top, a Team chat: the messages the teammates and you sent each other, in order, each with who sent it. Then each post as it will look in the feed, with its image and alt text; under each post put two working buttons (JavaScript): Approve turns the card green; Request changes opens a box for my note. A bar at the bottom asks my name once, builds the exact lines to paste in the chat ("approved <id> by <name>", "changes <id>: <note>") and has a Copy button that says "Copied - now paste it in the chat". Keep the lines on screen in case copying is blocked. If I chose email, send ONE review email to the approver with Gmail: the artifact link and what passed the checks. Send nothing else; publish nothing. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT C — Claude Code: ready to post**

> For each Week 1 post approved in review/approvals.csv, publish a "ready to post" artifact: the post text with a Copy button, its image, and the steps to post it by hand on LinkedIn or our Facebook Page. Then open the folder with the two images on my computer. Publish nothing yourself. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Which post do you expect to do best, and why?"
- "What did the Lead send back to the writer, and why?"
- "Is anything here not ready to post? Explain in plain English."

**Optional: post through LinkedIn and Facebook**

About 20 minutes, after you have approved the posts. Use test accounts only: your own LinkedIn profile and a test Facebook Page you manage. Skip any post you already posted by hand. The link in each post opens your own website, so it works only on your computer.

1. **Make your key file** — Ask Claude Code: "Make my .env file from data/env.example and open it in a text editor." Your keys go only in this file — never in the chat.
1. **LinkedIn app** — Go to linkedin.com/developers → Create app (link it to a LinkedIn Page; a test Page is fine). Under Products add Share on LinkedIn and Sign In with LinkedIn using OpenID Connect.
1. **LinkedIn key** — Auth → OAuth 2.0 tools → create a token with openid, profile and w_member_social. Paste it after LINKEDIN_ACCESS_TOKEN= in .env and save.
1. **Your LinkedIn ID** — Ask Claude Code: "Look up my LinkedIn author ID with the token in .env and fill it in. Do not show me the token."
1. **Facebook app** — Go to developers.facebook.com → Create app → Business. Open Tools → Graph API Explorer and pick your app. Add pages_manage_posts, pages_read_engagement and pages_show_list, then Generate token and choose your test Page.
1. **Facebook key** — Click Get Page Access Token. Paste it after FB_PAGE_TOKEN= in .env, and your Page ID (Page → About → Page transparency) after FB_PAGE_ID=. Save. This key lasts about an hour, so do it just before you post.
1. **Dry run** — Type: "Do a dry run of publishing the approved Week 1 posts and show each one as an artifact. Wait for my go." Each one should show your key partly hidden (like LITO…), not "missing".
1. **Go** — Type "go" for each post you want live. It appears on LinkedIn or your Facebook Page with its image, and the artifact shows its link.

**Check your work**

- ☐  The gate stopped Claude from approving.
- ☐  Two teammates ran; the Lead said when each started and finished.
- ☐  The Team chat shows the designer and the creator messaging each other.
- ☐  Two posts with images from the designer, alt text and UTM links.
- ☐  You reviewed in the artifact or by email and pasted the approval in the chat; the rows show your name and a hash.
- ☐  You posted the approved text and image yourself (or, optionally, through the API after you said go).

**If it goes wrong**

- **You got subagents, not a team** — Check you are in the current horizon-studio folder from the course, start a new session and ask for "an agent team" by name.
- **LinkedIn returns 426** — LINKEDIN_VERSION must be a recent YYYYMM.

**Stretch**

- Add the growth-analyst to suggest the best posting time per post from channel-benchmarks.csv.
- Link each LinkedIn post to the Lab 8 blog article.

Why it matters: Subagents report to one boss; teammates also talk to each other. A designer who can ask the writer for the hook makes a better image.

### Key ideas for Lab 11

#### Campaign 3: Newsletter + Landing Page

Lab 11: three specialists, one email and one page, consent first.

1. **Content Creator** — The issue and the landing-page copy.
1. **Website Designer** — The checklist page, page-qa, then a Claude artifact.
1. **Growth Analyst** — Recipients by consent: 31 of 40.
1. **Lead** — Checks everything; the build waits for you.
1. **Drafts** — Gmail drafts — one to you to test. Nothing sent.

#### Consent Decides Who Gets Mail

The PDPA, applied by an agent that counts.

- **Opt-in only** — consent = yes and unsubscribed = no. Everyone else goes to excluded.csv with a reason.
- **Every email carries** — An unsubscribe link, Horizon's address and the short disclaimer.
- **The page collects little** — Name, email, a required consent box, a separate unticked newsletter opt-in.

### Lab 11 — Campaign 3: Newsletter and a Landing Page

**The story so far:** The Sunny Sunday email books chats most cheaply. November's issue promotes a new landing page for the free checklist — and must reach only the 31 people who opted in.

**Goal:** The Sunny Sunday email books chats most cheaply — if it is right and reaches only people who said yes. This issue promotes a new landing page for the Money Check-up Checklist.

**You'll build:** the November newsletter, its recipient list, the landing page published, and Gmail drafts — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (agent team) → Claude artifact, Gmail  ·  **Time:** 60 min  ·  **Slides:** 119–124

**Lab folder:** labs/lab-11-campaign-3-newsletter-and-landing-page/ — assets: newsletter-brief.md, newsletter-spec.md, landing-page-brief.md, site-brief.md, checklist-items.md, subscribers.csv

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-11

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 11". Run all of this lab's prompts in it.
1. **Start the campaign** — Copy and paste Prompt A.
1. **Approve the words** — Review the issue in the artifact (or the review email's link). Click Approve or Request changes, then Copy and paste into the chat.
1. **Publish the page** — The website designer runs page-qa and publishes web/checklist/ as a Claude artifact.
1. **Check the list** — Only people with consent = yes and unsubscribed = no are on the recipient list.
1. **Create the drafts** — After the page is published and the list checked, copy and paste Prompt B.
1. **Send one test** — Send only the draft addressed to yourself, and read it on your phone.

**PROMPT A — Claude Code: the newsletter team**

> Create an agent team for the November Sunny Sunday email (data/newsletter-brief.md, data/newsletter-spec.md) and its landing page (data/landing-page-brief.md). Spawn three teammates:
> content-creator, website-designer and growth-analyst.
> - content-creator: issue.md (id nl-2026-11) with newsletter, and the landing-page copy.
> - website-designer: web/checklist/index.html with lead-magnet, web-design and landing-page from the approved copy; page-qa.
> - growth-analyst: recipients.csv and excluded.csv from data/subscribers.csv. Before you start, ask me how I will review: in the artifact, or by email (then ask for the approver's address). You check everything, then submit nl-2026-11 and publish the issue as an artifact, laid out as the email, with the counts of recipients and excluded, and two working buttons (JavaScript): Approve turns the page green; Request changes opens a box for my note. A bar at the bottom asks my name once, builds the exact line to paste in the chat ("approved <id> by <name>" or "changes <id>: <note>") and has a Copy button that says "Copied - now paste it in the chat". Keep the line on screen in case copying is blocked. If I chose email, send ONE review email to the approver with Gmail: the artifact link and what passed the checks. Only after I approve, build newsletter.html and .txt and publish the page as an artifact. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: Gmail drafts**

> Using the Gmail connector, create a DRAFT of newsletter.html for each address in recipients.csv, plus one draft addressed to me only. Send nothing. Publish a report as an artifact: how many drafts, how many people were excluded, and why, in a table.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Explain the email in three sentences. What do we want readers to do?"
- "Who was left off the mailing list, and why?"
- "What did the landing-page check look at, and did it pass?"

**Check your work**

- ☐  Three specialists worked on the campaign; the Lead checked all.
- ☐  You reviewed nl-2026-11 in the artifact or by email and approved it in the chat before the build.
- ☐  The landing page passed page-qa and is published.
- ☐  The recipient list holds 31 people; 9 are excluded, with reasons.
- ☐  The email has unsubscribe, address and disclaimer.
- ☐  Drafts only — nothing was sent to the list.

**If it goes wrong**

- **The build started before approval** — Tell the Lead the build waits for review/approvals.csv to say approved.

**Stretch**

- Ask for two subject lines to A/B test, with a reason for each.

Why it matters: Consent decides who gets mail — not the agent and not the deadline. Marketing to people who did not opt in breaks the PDPA.

### Key ideas for Lab 12

#### Campaign 4: The YouTube Explainer

Lab 12: the team writes and designs; you approve twice.

- **Strategist and Creator** — The angle, then 5–7 scenes with words on screen and a description with chapters and an AI disclosure.
- **Creative Designer** — Storyboard, thumbnail, then the render with video-render — ffmpeg, 1920×1080, under 90 s.
- **Upload privately** — Approve the words, then the finished video. It uploads as private; a person makes it public.

### Lab 12 — Campaign 4: The YouTube Explainer

**The story so far:** Pre-retirees say they would rather watch than read. Rachel wants the first 'Money in Plain English' video, uploaded privately until she has watched it.

**Goal:** Pre-retirees would rather watch than read. The team makes "Your CPF retirement sums in 60 seconds" — and it goes up privately until a person has watched it.

**You'll build:** the script, storyboard and thumbnail, the video, and a private YouTube upload (or dry run) — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (agent team, render, upload)  ·  **Time:** 55 min  ·  **Slides:** 126–131

**Lab folder:** labs/lab-12-campaign-4-youtube-explainer/ — assets: youtube-brief.md, video-spec.md, sample-explainer.mp4

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-12

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 12". Run all of this lab's prompts in it.
1. **Script it as a team** — Copy and paste Prompt A.
1. **Approve the script** — Read the scenes, title and description in the storyboard artifact; type: approved yt-ep01-script by <your name>.
1. **Render it** — After you approve the script, copy and paste Prompt B. The designer runs video-render.
1. **Approve the video** — Ask the Lead to submit the video, watch ep01.mp4 to the end, then approve yt-ep01.
1. **Upload** — After you approve the video, copy and paste Prompt C. It goes up as private.
1. **Disclose** — In YouTube Studio, answer the altered or synthetic content question before making it public.

**PROMPT A — Claude Code: the video team**

> Create an agent team for YouTube episode 1 from data/youtube-brief.md. Spawn three teammates:
> growth-strategist (the angle and hook), content-creator (content/video/ep01/scenes.json, 5-7 scenes, and ep01.md with title, tags, description, chapters and the AI disclosure) and creative-designer (a storyboard of the scenes and a thumbnail, using brand-visuals). You fact-check and fin-compliance the script, then submit it as yt-ep01-script. Publish nothing. Publish the storyboard as an artifact: one frame per scene with its words, visual and timing, and the thumbnail. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPTS B and C — Claude Code: render and upload**

> PROMPT B
> Use the creative-designer subagent with video-render on the approved scenes.json → content/video/ep01/ep01.mp4 (data/video-spec.md). Check its length and size. Do not change approved words. Publish the checks as an artifact: length, size, resolution and every scene, PASS or FAIL.

> PROMPT C
> Do a dry run of the YouTube upload for yt-ep01 (scripts/publish.mjs). If I say "go", upload it for real — as PRIVATE. Publish the request, then the YouTube Studio link, as an artifact.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Walk me through the video scene by scene, in plain English."
- "Which figure on screen should I double-check, and against what?"
- "What does the AI disclosure say, and why do we need it?"

**Check your work**

- ☐  The strategist, creator and designer each delivered their part.
- ☐  You approved the script, then the finished video.
- ☐  ep01.mp4 is 1920x1080, under 90 seconds, every scene present.
- ☐  Every figure on screen matches Horizon's 2026 facts.
- ☐  The description has chapters, link, disclaimer and AI disclosure.
- ☐  The upload is private (or the dry run printed the request).

**If it goes wrong**

- **The video will not render** — Ask the trainer, or use sample-explainer.mp4 to test the upload.

**Stretch**

- Ask the designer for a 30-second vertical Short from the same scenes.

Why it matters: Approve twice: once for the words, once for the finished video. Rendering can break what the script got right.

### Topic 3 recap

#### Where You Are Now

Three campaigns, every piece checked by the Lead and approved by a person. But the team stops when you close the laptop.

- **Gate  ·  Lab 10** — People approve, hashes hold, a hook stops agents.
- **Campaigns  ·  Labs 10–12** — Social week, newsletter + landing page, the video.
- **What is missing** — A team that works every week on its own — and rules to govern it. That is Topic 4.

## Topic 4 — Content Distribution, Strategy Guidelines and Responsible AI Practices

Slides 133–164. In this topic you will:

- Campaign 5: always on, with a scheduled task
- Responsible AI for financial content
- Measure the patterns; write the team playbook
- Agent teams at work: argue a strategy, then a QA loop

### Key ideas for Lab 13

#### From Skill to Schedule

Lab 13: do the job once, keep it as a skill, let a schedule run it.

1. **Do** — The Growth Analyst writes the weekly report once, from Drive.
1. **Verify** — Fix the sections until the report is right.
1. **Skill** — campaign-report holds the procedure.
1. **Schedule** — A scheduled task runs it every Monday at 8am.
1. **Review** — It leaves a Gmail draft — a person decides.

Tip: Pause scheduled tasks you are not using.

#### Automate the Preparation, Not the Decision

What a scheduled agent should and should not do for a regulated firm.

- **Prepare** — Read the data, run the skill, draft the report, flag what needs a decision.
- **Draft, never send** — Write "draft only — never send, publish or approve" in the skill AND the schedule.
- **Keep a human gate** — The schedule fills an inbox. A named person still decides.

### Lab 13 — Campaign 5: Always On — the Weekly Growth Report

**The story so far:** The team must keep working after class. Rachel wants the Growth Analyst's report in her inbox every Monday — as a draft she decides on.

**Goal:** The team should keep working when class ends. Every Monday the Growth Analyst's report lands in Rachel's inbox as a draft — the decision stays with a person.

**You'll build:** a scheduled task that drafts the weekly growth report every Monday at 8am, and one draft in Gmail

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (skill, routine, Drive, Gmail)  ·  **Time:** 45 min  ·  **Slides:** 136–141

**Lab folder:** labs/lab-13-campaign-5-weekly-growth-report/ — assets: campaign-results.csv, weekly-report-brief.md, scheduled-task-instructions.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-13

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 13". Run all of this lab's prompts in it.
1. **Put the data on Drive** — Ask: "Upload data/campaign-results.csv to my Google Drive folder Horizon Studio as a plain file, replacing any old copy."
1. **Do it once** — Copy and paste Prompt A. Refine the report until it is right.
1. **Schedule it** — After the report is right, copy and paste Prompt B into the instructions of a new routine: Routines → New routine → Local, Mondays at 8am.
1. **Run it now** — Click Run now once, approve any permission prompts, then open the Gmail draft.
1. **Pause it** — After class, pause the routine.

**PROMPT A — Claude Code: do it once**

> Act as Horizon's Growth Analyst. Using Google Drive, read campaign-results.csv in the Horizon Studio folder. Use the campaign-report skill and data/weekly-report-brief.md. Leave the report as a Gmail DRAFT to me, subject "Horizon weekly growth report" and today's date. Send nothing. Also publish the report as an artifact: cost per chat by channel as a chart, and the budget split. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: the routine**

> Run the campaign-report skill as Horizon's Growth Analyst. Read campaign-results.csv in the Horizon Studio folder on Google Drive and follow weekly-report-brief.md. Leave the report as a draft email to me in Gmail with the subject "Horizon weekly growth report" and today's date. Do not send it, and do not publish or approve anything.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "What is the one decision this report asks me to make?"
- "Which channel gets us a chat most cheaply, and how sure are you?"
- "What would you change in next month's budget, and why?"

**Check your work**

- ☐  The report used the campaign-report skill from your folder.
- ☐  The report names the cheapest channel per chat (the newsletter).
- ☐  It recommends a budget split with a reason per channel.
- ☐  A scheduled task runs Mondays at 8am with draft-only instructions.
- ☐  A manual run left a draft — nothing was sent.
- ☐  The task is paused after class.

**If it goes wrong**

- **It sent the email** — Write "draft only — never send" in both the skill and the task instructions.
- **Claude cannot upload to Drive** — Upload it yourself: drive.google.com → New → New folder "Horizon Studio" (if missing), open it → New → File upload.

**Stretch**

- Add a Friday 5pm task from the Lead: what was published and what is still pending.

Why it matters: Automate the preparation, not the decision. The schedule fills an inbox; a person still decides.

### Key ideas for Lab 14

#### Responsible AI in the Team

Each risk has a control you built in this course.

| Risk | Control | Where |
|---|---|---|
| Wrong figure | fact-check skill; the Lead's review; facts sheet | Labs 3, 5, 10–12 |
| Read as advice or a promise | fin-compliance; disclaimers; no returns | Labs 3, 10–12 |
| An agent with too much access | Least-privilege connectors per agent | Lab 4 |
| Unapproved post | Approval typed by a person, hash, gate | Lab 10 |
| Marketing without consent | The Analyst filters by consent | Lab 11 |
| Undisclosed AI media | Description line + YouTube disclosure | Lab 12 |

Tip: Keep keys in .env, client data out of prompts, and the approval records for audit.

#### Measure What Matters

Lab 14: the numbers decide next month — and which patterns earn their tokens.

- **Cost per chat** — Spend ÷ chats booked shows which channel works: email first, YouTube last.
- **Defects before a person** — A Lead that catches mistakes saves the reviewer's time; one agent alone caught none.
- **The playbook** — Roster, instructions, skills, connectors, approval matrix, incidents — so the team runs without you.

### Lab 14 — Measure, Govern and Write the Team Playbook

**The story so far:** Eight weeks in. Rachel asks which ways of running agents earned their tokens, and how the team runs safely after you leave.

**Goal:** Rachel asks: which patterns earned their tokens, and how does the team run safely after you leave? Answer with numbers, then with a playbook a new hire can follow.

**You'll build:** the agent-pattern comparison and the team playbook — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (subagents)  ·  **Time:** 50 min  ·  **Slides:** 144–149

**Lab folder:** labs/lab-14-team-playbook/ — assets: run-log.csv, playbook-outline.md, responsible-ai-checklist.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-14

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 14". Run all of this lab's prompts in it.
1. **Check the data** — The assets are already in data/. Open one and skim it.
1. **Compare the patterns** — Copy and paste Prompt A.
1. **Write the playbook** — After the Lead shows the comparison, copy and paste Prompt B.
1. **Review it as Rachel** — Add one rule of your own and say why.

**PROMPT A — Claude Code: compare**

> Use the growth-analyst subagent. From data/run-log.csv compare the patterns we used — one agent, subagents, agent teams and the scheduled task — on minutes, tokens, defects caught before a person and human edits. Which pattern pays off for which job? Save reports/agent-comparison.md. Publish it as an artifact: one chart per measure, comparing the patterns. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: the playbook**

> Write strategy/team-playbook.md with data/playbook-outline.md. Include the roster: for each agent its instructions file in .claude/agents/, its skills, connectors, model and what it may never do; the approval matrix by risk; the rules in data/responsible-ai-checklist.md; and what to do when a wrong post goes out. Then run fin-compliance on it. Publish the playbook as an artifact: the roster as cards, the approval matrix as a table. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "In one line each: when should we use one agent, subagents and an agent team?"
- "Who must approve a post that has a CPF figure in it?"
- "A wrong post went out. What are the first three things we do?"

**Check your work**

- ☐  The comparison shows the one-agent baseline caught 0 defects.
- ☐  It says which pattern suits which job, with numbers.
- ☐  The roster lists all six agents with skills and connectors.
- ☐  The approval matrix says who approves CPF and tax figures.
- ☐  It has an incident procedure, and your own rule.

**If it goes wrong**

- **The playbook is generic** — Say: "use our actual agents, files and numbers".

**Stretch**

- Turn the playbook into a skill, team-playbook, for the Lead.

Why it matters: Teams cost more tokens. The run log shows what you buy with them: defects caught before a person, and fewer edits.

### Key ideas for Lab 15

#### Subagents vs Agent Teams

Same work, different wiring: who spawns whom, and who talks to whom.

**Subagents** — a main agent spawns each subagent; each works in its own context, and its result is reported back to the main agent. Subagents never talk to each other.

**Agent team** — a Team Lead spawns the team and assigns tasks on a shared task list. Teammates claim tasks, update their status and message each other directly while they work.

Subagents report back to one agent. Teammates share a task list and talk to each other.

#### A Team That Argues

Lab 15, Part 1: test a strategy before Horizon spends on it.

**Advocate · growth-strategist**

- Argues FOR the "Turning 55" CPF explainer
- Cites results, personas and the facts sheet
- Answers the critic directly — two rebuttals

**Critic · growth-analyst**

- Argues AGAINST it — cost, timing, audience
- Every point backed by a file, not an opinion
- The Lead judges; a person makes the call

#### The QA Loop

Lab 15, Part 2: a failed audit goes straight back to the writer — not through the Lead.

**Writer** — content-creator: rewrites the intern's draft into an email and a video script. **QA Auditor** — fact-check + fin-compliance; PASS or FAIL per check, every round logged.

On **FAIL**, the auditor messages the writer directly with the lines to fix, and audits again. On **PASS**: Designer (asks the writer for the headline; one image) → Lead (submits for approval; never rewrites) → Person (approves the exact version).

The audit fails when:

- A figure is not in facts-2026.md
- A promise of savings or returns
- Advice ("everyone should…")
- A wrong age or a missing disclaimer

Three rounds at most — then the Lead escalates to a person.

### Lab 15 — Agent Teams: A Strategy Debate and a QA Loop

**The story so far:** January is for people turning 55. Before Horizon spends on a CPF explainer for them, Rachel wants it argued both ways — and the intern's draft checked until it passes.

**Goal:** Subagents only report back. In a team the agents talk: two teammates argue a strategy before Horizon spends on it, and a QA Auditor sends a failed draft straight back to the writer — round after round — without the Lead in the middle.

**You'll build:** the decision (pros, cons, verdict), then an email, a video script and a thumbnail that passed QA, submitted for your approval — shown as artifacts, with a Word copy of each

**USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Surface:** Claude Code (agent teams: Lead, teammates, shared task list, direct messages)  ·  **Time:** 40 min  ·  **Slides:** 153–159

**Lab folder:** labs/lab-15-agent-teams-debate-and-qa-loop/ — assets: turning-55-brief.md, turning-55-draft.md

**Copy the prompts: **https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-15

**Step-by-step**

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 15". Run all of this lab's prompts in it.
1. **Part 1: the debate** — Copy and paste Prompt A. The advocate and the critic message each other; the decision page shows their debate.
1. **Decide** — Read the decision artifact. Reply "go", "go with conditions" or "no-go" — the call is yours.
1. **Part 2: the QA loop** — After you have made the call, copy and paste Prompt B. The audit fails on round 1; watch the auditor message the writer directly.
1. **Approve as a person** — Read the pieces and the QA artifact, then type in the chat: approved <id> by <your name> (or: changes <id>: what to fix).
1. **Shut down** — After you have approved the pieces, copy and paste Prompt C. The Lead stops each teammate and cleans up the team.

**PROMPT A — Claude Code: the strategy debate**

> Create an agent team to test the strategy in data/turning-55-brief.md before we spend on it. You are the Lead and the judge: do not argue. Spawn two teammates:
> - advocate, using the agent type growth-strategist:
>   argue FOR the strategy.
> - critic, using the agent type growth-analyst:
>   argue AGAINST it.
> - Both: cite data/campaign-results.csv, strategy/personas.md, data/facts-2026.md or data/compliance-checklist.md for every point; message each other directly; rebut twice at most.
> - You: write strategy/turning-55-decision.md with the pros, the cons, your verdict (go / go with conditions / no-go) and the conditions. Publish the decision as an artifact with the verdict on top, the pros and cons in two columns, the debate (the messages the advocate and critic sent each other, in order) and what I do next. Then wait for my decision. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT B — Claude Code: the QA loop**

> Clean up the debate team, then create a new agent team for Part 2 of data/turning-55-brief.md, using my decision. Spawn three teammates:
> - writer, agent type content-creator: rewrite data/turning-55-draft.md into content/turning-55/email.md and content/turning-55/video-script.md.
> - qa-auditor: audit each piece with fact-check and fin-compliance; write review/turning-55-qa.md, one section per round, PASS or FAIL per check. On FAIL, message the writer directly with the lines to fix and audit again. Three rounds at most.
> - designer, agent type creative-designer: once a piece passes, ask the writer for its headline and make one thumbnail with alt text.
> - You, the Lead: never write or fix content. When everything passes, submit each piece with scripts/submit.mjs. Publish nothing. Publish the QA report as an artifact, one row per round, PASS or FAIL per check, in colour. Write for a business owner, in plain English: no codes, IDs, file names or line numbers; start with what it means and what I do next. Save a Word copy (.docx) of each result.

**PROMPT C — Claude Code: shut down**

> Ask every teammate to shut down, then clean up the team. Show me the final task list and how many QA rounds each piece needed. Publish it as an artifact.

**Ask about the result**

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Summarise the debate: the best point for, the best point against, and your verdict."
- "What failed in the first QA round, in plain English?"
- "How many rounds did each piece need, and why?"

**Check your work**

- ☐  The advocate and the critic messaged each other; every point cites a file.
- ☐  The decision has pros, cons, a verdict — and you made the call.
- ☐  Round 1 of the QA report FAILED: the FRS figure, CPF LIFE "from 55", the promised payout, the advice and the missing disclaimer.
- ☐  The auditor sent the fixes to the writer directly; a later round PASSED.
- ☐  You approved by typing in the chat; the rows show your name and a hash.
- ☐  Both teams were shut down and cleaned up.

**If it goes wrong**

- **Claude cannot find turning-55-brief.md** — Your folder is an older download. Ask: "Download turning-55-brief.md and turning-55-draft.md from https://raw.githubusercontent.com/tertiarycourses/C1034-Multi-AI-Agents-for-Content-Creation/main/labs/horizon-studio/data/ into data/." Then paste Prompt A again.
- **You got subagents, not a team** — Ask for "an agent team" by name in a new session.
- **The loop never ends** — Remind the Lead: three rounds at most, then escalate to me.
- **A task stays blocked** — Tell the Lead to check the task list and nudge the teammate who owns it.

**Stretch**

- Add a third debater, a pre-retiree persona, who argues from the customer's side.
- Run Part 2 with subagents instead and compare: how many times did the Lead have to relay a fix?

Why it matters: Use subagents when only the result matters; use a team when the agents must talk — to argue, or to send work back. Every teammate is its own Claude session, so teams cost more tokens.

## Course Summary

#### How Each Pattern Is Triggered

Five ways your team runs. The difference is what sets each one off.

- **Subagents (by delegation)** — The Lead starts them when you ask — or when a task matches an agent's description. Example: "use subagents, one per role". Where: .claude/agents/.
- **Agent teams (by the lead)** — The Lead spawns teammates who share a task list and message each other. Example: "spawn teammates using agent types…". Where: Claude Code (experimental).
- **Skills (on demand)** — Loaded when the task matches the description. Free until then. Example: campaign-brief video-render. Where: .claude/skills/.
- **Hooks (on an event)** — Run every time an event fires — before a tool runs. The model cannot skip them. Example: PreToolUse: gate-hook.mjs. Where: .claude/settings.json.
- **Scheduled tasks (on the clock)** — Run a skill on a schedule and leave the result for a person. Example: Mondays 8am: campaign-report. Where: Claude.

Who decides?  You: the approval  ·  the model: delegation and skills  ·  the system, every time: hooks and the clock

#### Horizon: One Team, Five Campaigns

Two days, one regulated business — the Claude Edition.

1. **Form** — A Lead and five agents: instructions, skills, connectors.
1. **Plan** — Campaign 1, personas, cadence and a calendar.
1. **Create** — Social week, newsletter + landing page, video.
1. **Govern** — A human gate, least privilege, a playbook.
1. **Run** — The weekly report, on a schedule, as a draft.

#### Practice Exam: Claude Certified Associate

exams.tertiaryinfotech.com/practice-exams/anthropic/anthropic-ccao-foundations

- **CCAO-F · Foundations** — For professionals who use Claude as a productivity tool.
- **What it covers** — Prompting and task execution, output evaluation, model selection, workflow integration, responsible use.
- **Try it free** — Start with the free practice teaser; exam mode is 60 questions in 120 minutes.

## Quick Command Reference

| Command | What it does |
|---|---|
| Code mode (</>) | Every lab. Left sidebar: + next to horizon-studio starts the lab's session |
| Click the session title | Rename the session after the lab: "Lab 5" |
| .claude/agents/<name>.md | An agent: name, description, tools, model, skills, instructions |
| "use the <name> subagent" · @agent-<name> | Delegate to one specialist |
| "use subagents, in parallel" | Run several specialists at once |
| "spawn teammates using the agent types …" | Start an agent team from your subagent files |
| ↑ ↓ · Enter · Ctrl+T | Agent team: select · open a teammate · task list |
| .claude/skills/<name>/SKILL.md | A skill — Claude Code reads it from your folder |
| Customize → Connectors → Discover → + | Add a connector: Google Drive, Gmail, Google Calendar, Firecrawl |
| /mcp · /status | The connectors this session can use · which account you are signed in with |
| /plugin install marketing@knowledge-work-plugins | The Marketing plugin (by Anthropic), after /plugin marketplace add anthropics/knowledge-work-plugins |
| Routines → New routine → Local | A task that runs on a schedule, e.g. Mondays 8am (Lab 13) |
| "Publish … as an artifact" · /artifacts | Publish a page; list your artifacts |
| approved <id> by <your name> | Type it in Claude Code to approve — only a person can |
| changes <id>: <what to fix> | Type it to send an item back |

## Support

Tertiary Infotech Academy Pte Ltd · enquiry@tertiaryinfotech.com · +65 6100 0613 · www.tertiarycourses.com.sg
