# Prompts — Lab 04: Connect the Tools Each Agent Needs

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-4 (one Copy button per prompt).

## PROMPT A — Claude Code: give each agent its connectors

```
Read data/connectors-setup.md. For each
subagent in .claude/agents/, replace its tools line
with the one given there, add the disallowedTools
line where one is given, and update its
"Connectors" section: what it may use, and that
Gmail is drafts only. Change nothing else.
```

## PROMPT B — Claude Code: test each agent

```
First tell me which connectors and plugins you
can use.
Then run these five checks, each by its own subagent:
1. growth-strategist: Firecrawl — search for one
   2026 news item about financial planning in
   Singapore, scrape it and cite it.
2. growth-analyst: Google Drive — read
   firm-metrics.csv from Horizon Studio; report
   average monthly enquiries.
3. content-creator: Gmail — a DRAFT to me with the
   subject "Connector test". Do not send.
4. creative-designer: render a 1080x1080 test card
   in Horizon colours and save it in content/test/.
5. website-designer: built-in browser — open our
   own copy of the site (web/site/index.html) at
   375px wide and report any problem.
Report each result in one line. If a check fails,
say which tool was missing.
```
