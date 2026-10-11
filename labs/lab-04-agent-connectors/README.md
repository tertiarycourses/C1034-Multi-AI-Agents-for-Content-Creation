# Lab 04 — Connect the Tools Each Agent Needs

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 1 · Topic 1 · about 40 minutes · slides 53–57**\
**Surface:** Claude desktop app (Customize → Connectors), Claude Code\
**Features:** Customize → Connectors: Google Drive · Gmail (drafts) · Google Calendar · Firecrawl · /plugin: Marketing (by Anthropic) · built-in browser · least privilege per agent

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-4 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

The analyst cannot read the data, the designer has no design tool and the creator cannot draft an email. Connect each agent to what its job needs — and nothing more.

## Your goal

An agent can only do the job if it can reach the tools — and a regulated firm only lets each agent reach the tools its job needs. Connect them, then test each one.

## You'll build

every specialist tested on its own connector, with its limits written into its instructions

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/connectors-setup.md`
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 4". Run all of this lab's prompts in it.
2. **Add the connectors** — Desktop app: Customize → Connectors → Discover. Add (+) Google Drive, Gmail, Google Calendar and Firecrawl; sign in to each.
3. **Add the plugin** — In the chat type /plugin marketplace add anthropics/knowledge-work-plugins, then /plugin install marketing@knowledge-work-plugins.
4. **Check** — Start a new session. Type /mcp: the four connectors are listed. Type /plugin: Marketing is installed.
5. **Put the data on Drive** — Ask: "Create a Google Drive folder named Horizon Studio and upload every file in data/ to it as plain files — do not convert them."
6. **Give each agent its connectors** — Copy and paste Prompt A, then start a new session so the agents reload.
7. **Test each agent** — After the new session opens, copy and paste Prompt B — one small job per agent, each on its own connector.

## The prompts

### PROMPT A — Claude Code: give each agent its connectors

> Read data/connectors-setup.md. For each
> subagent in .claude/agents/, replace its tools line
> with the one given there, add the disallowedTools
> line where one is given, and update its
> "Connectors" section: what it may use, and that
> Gmail is drafts only. Change nothing else.

### PROMPT B — Claude Code: test each agent

> First tell me which connectors and plugins you
> can use.
> Then run these five checks, each by its own subagent:
> 1. growth-strategist: Firecrawl — search for one
>    2026 news item about financial planning in
>    Singapore, scrape it and cite it.
> 2. growth-analyst: Google Drive — read
>    firm-metrics.csv from Horizon Studio; report
>    average monthly enquiries.
> 3. content-creator: Gmail — a DRAFT to me with the
>    subject "Connector test". Do not send.
> 4. creative-designer: render a 1080x1080 test card
>    in Horizon colours and save it in content/test/.
> 5. website-designer: built-in browser — open our
>    own copy of the site (web/site/index.html) at
>    375px wide and report any problem.
> Report each result in one line. If a check fails,
> say which tool was missing.

## Check your work

- [ ] /mcp lists Google Drive, Gmail, Google Calendar and Firecrawl; /plugin shows Marketing.
- [ ] Five checks ran, each by its own agent.
- [ ] The Gmail test is a draft in your inbox — nothing was sent.
- [ ] The analyst read the CSV from Drive, not from the local folder.
- [ ] Each agent's tools line names only the connectors its job needs.

## If it goes wrong

- **Insufficient scope** — Reconnect and grant read access to the Horizon Studio folder.
- **Claude cannot upload to Drive** — Check Google Drive is in /mcp. Or upload the files yourself: drive.google.com → New → New folder "Horizon Studio", open it → New → File upload.
- **An agent says it has no Drive or Gmail tools** — Its tools line does not name the connector, or the session is old. Paste Prompt A again, then start a new session.
- **A connector is missing from /mcp** — Customize → Connectors → Yours: it must be there and signed in — if not, find it under Discover and click +. Then start a new session.
- **/mcp shows no connectors at all** — Type /status: you must be signed in with your claude.ai account, not an API key.
- **The Marketing plugin is not listed** — Type /plugin: it must be installed and enabled. Start a new session. Its optional connectors (HubSpot, Ahrefs and others) are not needed.
- **The browser check fails** — Skip check 5 and open the site on your phone instead.

## Stretch

- Give Google Calendar to the Lead only, for review deadlines.

> **Why it matters:** Least privilege is a design decision, not a setting. Ask of each connector: does this agent's job need it?

## Next

Lab 5 — Campaign 1: Research to Storyboard, with Subagents. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
