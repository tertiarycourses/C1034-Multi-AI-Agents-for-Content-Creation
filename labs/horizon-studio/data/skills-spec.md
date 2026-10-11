# The team's twenty skills

Each skill is a folder with a SKILL.md: a name, a "Use when…" description (the trigger), then the steps. Under 80 lines each. Keep the master copy in skills/ and copy it where each tool looks:

| Tool | Where skills live |
|---|---|
| Claude Code (every subagent and teammate) | .claude/skills/<name>/SKILL.md |
| Claude (desktop and web) | Customize -> Skills (via /skill-creator) |

| Owner | Skill | Use when… |
|---|---|---|
| Growth Strategist | competitor-scan | Use when researching Horizon's market or competitors. Six named Singapore competitors across planning firms, robo-advisers, bank advisers and finfluencers: offer, pricing model, channels, content themes, gaps. Every figure cited with a date, or UNKNOWN. |
| Growth Strategist | campaign-brief | Use when planning a Horizon campaign. Objective, audience, core message, proof from facts-2026.md, channels, one call to action, measures, and a five-beat storyboard (hook, tension, proof, resolution, action). |
| Growth Strategist | content-marketing | Use when planning what Horizon publishes and why. Three content pillars, each idea tagged to a funnel stage (aware, consider, book), one call to action per stage, and how one idea is repurposed across blog, LinkedIn, Facebook, email and video. |
| Content Creator | sunny-voice | Use when writing anything Horizon will publish. Plain English, warm and calm; banned words; explain acronyms once; no sentence over 25 words; the Sunny sign-off on social posts. |
| Content Creator | copywriting | Use when writing a headline, hook, subject line or call to action for Horizon. Problem-agitate-solve or AIDA; one reader, one promise, one action; three options with a reason for the best; no hype and no promise of returns. |
| Content Creator | channel-formats | Use when writing a LinkedIn post, Facebook post, newsletter issue, YouTube script or page copy. The shape of each channel, UTM links, the short disclaimer and the content-file frontmatter. |
| Content Creator | linkedin-post | Use when writing a Horizon LinkedIn post. A first line that stands alone, short paragraphs, one idea backed by facts-2026.md, a question or one call to action, a UTM link, three hashtags and the short disclaimer. |
| Content Creator | facebook-post | Use when writing a Horizon Facebook post. Warm and local, 60-150 words, ends with a question, an image brief with alt text, a UTM link and the short disclaimer. |
| Content Creator | blog-post | Use when writing a Horizon blog article. One search intent and keyword, a title under 60 characters, a meta description under 155, H2 sections, a FAQ, sources cited, 700-1,000 words, one call to action and the full disclaimer. |
| Content Creator | newsletter | Use when writing a Sunny Sunday email. Subject under 50 characters, preview under 90, one tip, one nudge, one call to action, plain-text twin, unsubscribe, address and disclaimer; consent-only recipients. |
| Creative Designer | brand-visuals | Use when making any Horizon image, carousel, thumbnail or video frame. Colours (ink #22305B, sun #FFC845, sky #EAF3FF), Sunny, thick outlines, readable text at thumbnail size, alt text, and an AI-disclosure note. No real or synthetic "clients". |
| Creative Designer | video-render | Use when turning an approved scenes.json into a video. One branded card per scene, 1920x1080, under 90 seconds, ffmpeg; check with ffprobe; never change approved words. |
| Website Designer | web-design | Use when designing or restyling any Horizon page. Brand tokens, type scale, one column on mobile, 44px tap targets, contrast AA, one primary button per screen, and a layout that leads to the call to action. |
| Website Designer | landing-page | Use when building a Horizon campaign or lead-magnet page. One self-contained page in the brand tokens: hero, proof, the offer, a form with a required PDPA consent box, the footer disclaimer word for word; ready to publish as a Claude artifact. |
| Website Designer | lead-magnet | Use when creating or promoting a Horizon lead magnet such as the Money Check-up Checklist. The reader's problem, one promise, the format, the items from checklist-items.md, the opt-in page with PDPA consent, the delivery email, and the measure (downloads to chats). |
| Website Designer | page-qa | Use before any Horizon page is published or shared. Check 1440px and 375px, keyboard focus, alt text, links, the calculator test (S$693,138), the consent box and the disclaimer; report PASS or FAIL. |
| Growth Analyst | audience-insights | Use when analysing Horizon's survey, enquiries or checklists. Count with code; every claim carries n and the file; label INFERENCE and LOW CONFIDENCE (n < 20); quote enquiries verbatim with ids. |
| Growth Analyst | campaign-report | Use when reporting Horizon's marketing results. Per channel: clicks, checklist downloads, chats booked, cost per chat; the best and worst channel; next month's budget split with reasons; one page. |
| Marketing Team Lead | fact-check | Use when a draft contains a number, age, rate, date or rule. Match every claim to facts-2026.md: VERIFIED or UNVERIFIED. Never fix a figure from memory. |
| Marketing Team Lead | fin-compliance | Use before any Horizon content goes to a person for approval. Apply compliance-checklist.md C1-C12; a table of issues with severity; PASS only with no Critical or High issue; the right disclaimer. |
