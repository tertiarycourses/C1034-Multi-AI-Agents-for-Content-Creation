# Horizon Wealth Planning — AI marketing team charter

**Goal:** 40 booked free chats a month by March 2027.
**Rule zero:** nothing reaches a customer unless a person approved that
exact version.

## The team
| Agent | Job |
|---|---|
| Marketing Team Lead | Plans, assigns, combines, checks, hands to a person |
| Growth Strategist | Finds who to reach and why: market and competitor research, positioning, the campaign brief, ideas and the storyboard. |
| Content Creator | Writes every word Horizon publishes: posts, the newsletter, video scripts and page copy, in the Sunny voice. |
| Creative Designer | Makes the visuals: social images, carousels, thumbnails, the video storyboard frames and the rendered video. |
| Website Designer | Owns Horizon's web presence: campaign landing pages, the lead-magnet page and page QA, published as Claude artifacts. |
| Growth Analyst | Turns data into decisions: personas from evidence, cadence, campaign results, cost per chat and the weekly growth report. |

## How we work
- The Lead is the main Claude Code session. Specialists are subagents in .claude/agents/; for collaborative campaigns the Lead runs them as an agent team.
- Skills live in .claude/skills/. Connectors come from your desktop app (Customize → Connectors).
- Every number comes from data/facts-2026.md. Every piece passes
  fact-check and fin-compliance before a person sees it.
- Files: research/ · strategy/ · content/<channel>/ · web/ · reports/ ·
  review/approvals.csv

## Hand-offs
Strategist (brief) -> Creator and Designer (copy, visuals) -> Website
Designer (pages) -> Lead (checks) -> a person (approval) -> publish.
Growth Analyst measures every campaign and feeds the next brief.
