# Lab 08 — Content Creator: A Quick Blog Article

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 1 · Topic 2 · about 40 minutes · slides 86–90**\
**Surface:** Claude Code (Firecrawl, your Horizon skills) → your copy of Horizon's website\
**Features:** one prompt runs the whole job: research · draft · fact-check and fin-compliance · fix · post to the blog on your copy of the website · a person reads it last

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-8 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

Jun Wei has the storyboard and the personas. Rachel wants the first real piece today: a blog article that people searching for CPF top-ups will find — and that every post can link to.

## Your goal

The storyboard is the plan; now make the first piece, fast. A blog article is the hub every post, email and video links to — and one prompt can take it from research to a checked post.

## You'll build

a 500-700-word blog article with dated sources, checked and fixed and posted on your own copy of Horizon's website, opened in your browser, with a Word copy

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/facts-2026.md`
- `assets/brand.md`
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 8". Run all of this lab's prompts in it.
2. **Write and post it** — Copy and paste the prompt. Claude researches, writes, checks and fixes the article, then posts it to your copy of Horizon's website.
3. **Read it on the site** — Your copy of the website opens in your browser: your article is first under "From our blog". Say what to change, if anything.

## The prompts

### PROMPT — Claude Code: a quick blog

> Write a quick blog article for Horizon and post it
> to the website. Use the blog-post, sunny-voice,
> fact-check and fin-compliance skills.
> 1. Pick one topic from strategy/storyboard.md that
>    a Singaporean would search for. Use Firecrawl to
>    find two current sources (CPF Board, MAS or
>    MoneySense), each with its date.
> 2. Write 500-700 words: a title under 60
>    characters, every figure from data/facts-2026.md,
>    one call to action (book a free 30-minute
>    chat) and the full disclaimer →
>    content/blog/<slug>.md.
> 3. Run fact-check and fin-compliance; fix every
>    issue and list each fix in one line.
> 4. Add it to the blog in web/site/index.html as one
>    new post, built like the posts already there.
>    Change nothing else on the site. Then start my
>    website if it is not running, and open it.
> Write for a business owner, in plain English. Save
> a Word copy (.docx) of the article.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Summarise the article in three sentences. Who is it for?"
- "Why did you pick this topic, and who will search for it?"
- "What did the checks find, and how did you fix it?"

## Check your work

- [ ] Two sources, each with a date and a link.
- [ ] The title is under 60 characters.
- [ ] Every figure is from Horizon's 2026 facts.
- [ ] The fixes are listed; no Critical or High issue is left.
- [ ] One call to action and the full disclaimer at the end.
- [ ] Your article is first under "From our blog" on your copy of the website.

## If it goes wrong

- **Firecrawl finds nothing** — Type /mcp: Firecrawl must be connected — or say "use web search instead".
- **The site looks unchanged** — Refresh the browser page. Or say: "open my website again".
- **The browser does not open** — Say: "Start my website again."

## Stretch

- Ask for two LinkedIn posts and one Facebook post that link to the article, with linkedin-post and facebook-post.

> **Why it matters:** One prompt can run the whole job — research, writing and checks. A person still reads the result before it goes anywhere.

## Next

Lab 9 — The Lead Magnet: a Checklist and Its Welcome Emails. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
