# Labs — Multi AI Agents for Content Creation (Claude Edition)

C1034 · 15 labs · build an AI marketing team, then run five campaigns with it.

## The scenario

Rachel Goh founded Horizon Wealth Planning in 2010. Fifteen years and 1,200
clients later, almost every new client still comes through a referral — and
referrals are slowing. Younger Singaporeans look for money help on LinkedIn,
Facebook, YouTube and in their inbox, and Horizon is invisible there.

Rachel has a website, three planners, a part-time marketer (Jun Wei) and
S$4,000 a month. She wants 40 booked free chats a month by March 2027
— without hiring a marketing team. So you will build her one, made of AI
agents, with Claude and Claude Code:

  Marketing Team Lead  — plans, assigns, checks, hands to a person
  Growth Strategist    — research, positioning, briefs, storyboards
  Content Creator      — posts, newsletter, scripts, page copy
  Creative Designer    — images, thumbnails, the video
  Website Designer     — landing pages, published and QA-checked
  Growth Analyst       — personas, cadence, results, weekly report

First you form the team: instructions, skills and connectors for each agent.
Then the team runs five campaigns together. Financial content is regulated,
so a person approves every piece before it goes out. The data is fictitious
but consistent, and every email address resolves to your own inbox.

## The labs

| # | Lab | Day | Use | Time |
|---|---|---|---|---|
| 01 | [Build Your Marketing Agent Team](lab-01-studio-and-website/README.md) | 1 | **Claude Code** | 30 min |
| 02 | [Form the Team: Instructions for Each Agent](lab-02-agent-instructions/README.md) | 1 | **Claude Code** | 40 min |
| 03 | [Give Each Agent Its Skills](lab-03-agent-skills/README.md) | 1 | **Claude Code** | 45 min |
| 04 | [Connect the Tools Each Agent Needs](lab-04-agent-connectors/README.md) | 1 | **Claude Code** | 40 min |
| 05 | [Campaign 1: Research to Storyboard, with Subagents](lab-05-campaign-1-research-to-storyboard/README.md) | 1 | **Claude Code** | 45 min |
| 06 | [Growth Analyst: Personas from Evidence](lab-06-personas-from-evidence/README.md) | 1 | **Claude Code** | 40 min |
| 07 | [Growth Analyst and Strategist: Cadence and Calendar](lab-07-cadence-and-calendar/README.md) | 1 | **Claude Code** | 35 min |
| 08 | [Content Creator: A Quick Blog Article](lab-08-blog-article/README.md) | 1 | **Claude Code** | 40 min |
| 09 | [The Lead Magnet: a Checklist and Its Welcome Emails](lab-09-lead-magnet/README.md) | 2 | **Claude Code** | 50 min |
| 10 | [Campaign 2: Social Media Posts (Demo)](lab-10-campaign-2-social-week/README.md) | 2 | **Claude Code** | 50 min |
| 11 | [Campaign 3: Newsletter and a Landing Page](lab-11-campaign-3-newsletter-and-landing-page/README.md) | 2 | **Claude Code** | 60 min |
| 12 | [Campaign 4: The YouTube Explainer](lab-12-campaign-4-youtube-explainer/README.md) | 2 | **Claude Code** | 55 min |
| 13 | [Campaign 5: Always On — the Weekly Growth Report](lab-13-campaign-5-weekly-growth-report/README.md) | 2 | **Claude Code** | 45 min |
| 14 | [Measure, Govern and Write the Team Playbook](lab-14-team-playbook/README.md) | 2 | **Claude Code** | 50 min |
| 15 | [Agent Teams: A Strategy Debate and a QA Loop](lab-15-agent-teams-debate-and-qa-loop/README.md) | 2 | **Claude Code** | 40 min |

## Before you start

- The Claude desktop app on a Pro plan or above, signed in with your claude.ai account. Every lab says whether to use **Claude** or **Claude Code** — both are in the app.
- Installed by the trainer before class (you never type commands): Node.js, Python and ffmpeg, which run the approval gate and the video.
- A personal Google account for Drive and Gmail; optional LinkedIn, Facebook Page and YouTube accounts for live publishing.
- One working folder, `horizon-studio/`, from Lab 1 to Lab 15 — ready-made in this pack with every lab's data in `data/`. Choose it in Claude (Project or folder → Add folder); do not create one.
- `.md` files are plain text for Claude to read; each has a `.pdf` twin with the same name for you to read.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
