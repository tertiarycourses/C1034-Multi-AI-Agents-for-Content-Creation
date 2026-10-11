# Connectors for each agent (Claude edition)

## 1. Connect the tools — no code

In the Claude desktop app: Customize → Connectors → Discover. Search for each
tool below, click +, and sign in with your PERSONAL account. Customize →
Connectors → Yours then lists all four. Claude Code uses the same connectors:
type /mcp in a Code mode session to see them.

- Google Drive, Gmail, Google Calendar (your personal Google account)
- Firecrawl — web search and clean page scraping for research (free account)

The Website Designer checks pages with the desktop app's built-in browser —
nothing to install.

## Plugin — Marketing (by Anthropic)

In a Code mode session, type these two lines, one at a time:
  /plugin marketplace add anthropics/knowledge-work-plugins
  /plugin install marketing@knowledge-work-plugins
Then start a new session; /plugin lists Marketing as installed.
It gives the team general marketing know-how — skills for content
creation, campaign planning, brand voice, competitive analysis and
performance analytics — and commands you can type: /draft-content,
/campaign-plan, /brand-review, /competitive-brief, /performance-report,
/seo-audit and /email-sequence.

Do not connect its optional connectors (HubSpot, Ahrefs, Similarweb,
Klaviyo and others) — the course does not need them. Horizon's own skills
(sunny-voice, fact-check, fin-compliance and the channel skills) still set
the voice, the facts and the rules.

## 2. Who may use what

| Agent | May use | Limit |
|---|---|---|
| Marketing Team Lead | Google Drive (read), Gmail, Google Calendar | Gmail: drafts only, except one review email to the approver |
| Growth Strategist | web search, Firecrawl, Google Drive (read) | cite every source |
| Content Creator | Google Drive (docs), Gmail | Gmail: drafts only (sending is blocked) |
| Creative Designer | Bash: Pillow for images, ffmpeg for video | no real or synthetic "clients" |
| Website Designer | Artifacts; built-in browser | publish only after approval |
| Growth Analyst | Google Drive and Sheets (read) | no personal data in reports |

## 3. The tools line for each agent

An agent can use only what its `tools:` line names — a connector that is not
named is invisible to it, even when it is connected. Lab 4 Prompt A asks
Claude to put these lines into each agent file for you.

**growth-strategist**

    tools: Read, Write, Grep, Glob, WebSearch, WebFetch, mcp__claude_ai_Firecrawl, mcp__claude_ai_Google_Drive

**content-creator**

    tools: Read, Write, Edit, Grep, Glob, mcp__claude_ai_Google_Drive, mcp__claude_ai_Gmail
    disallowedTools: mcp__claude_ai_Gmail__send_message, mcp__claude_ai_Gmail__reply, mcp__claude_ai_Gmail__forward

**creative-designer**

    tools: Read, Write, Edit, Bash, Glob

**website-designer**

    tools: Read, Write, Edit, Bash, Glob, mcp__Claude_Browser, mcp__claude-in-chrome

**growth-analyst**

    tools: Read, Write, Bash, Grep, Glob, mcp__claude_ai_Google_Drive

The Lead (your main session) can use every connected tool. The approval rule
(Lab 10) stops every agent from approving or publishing.
