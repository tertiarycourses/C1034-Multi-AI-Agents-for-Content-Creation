# Lab 12 — Campaign 4: The YouTube Explainer

> **USE: CLAUDE CODE** — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder

**Course:** Multi AI Agents for Content Creation (Claude Edition) (C1034)\
**Day 2 · Topic 3 · about 55 minutes · slides 126–131**\
**Surface:** Claude Code (agent team, render, upload)\
**Features:** strategist angle · creator script · designer storyboard, thumbnail and render · approve twice · private upload

> **Copy the prompts:** https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-12 — click **Copy** next to each prompt, then paste it into the chat.

## The story so far

Pre-retirees say they would rather watch than read. Rachel wants the first 'Money in Plain English' video, uploaded privately until she has watched it.

## Your goal

Pre-retirees would rather watch than read. The team makes "Your CPF retirement sums in 60 seconds" — and it goes up privately until a person has watched it.

## You'll build

the script, storyboard and thumbnail, the video, and a private YouTube upload (or dry run) — shown as artifacts, with a Word copy of each

## What is in this folder

> **.md or .pdf?** A `.md` file (Markdown) is plain text that Claude reads. Every `.md` here has a `.pdf` twin with the same name — open the PDF to read it yourself.

- `assets/youtube-brief.md`
- `assets/video-spec.md`
- `assets/sample-explainer.mp4`
- `solution/` — reference files from the verified build (each `.md` with its `.pdf`)
- `prompts.md` / `prompts.pdf` — every prompt, ready to paste
- `evidence/checklist.md` / `checklist.pdf` — what to capture as proof

## Step by step

1. **New session** — Left sidebar: click + next to horizon-studio. Click the session title at the top and rename it "Lab 12". Run all of this lab's prompts in it.
2. **Script it as a team** — Copy and paste Prompt A.
3. **Approve the script** — Read the scenes, title and description in the storyboard artifact; type: approved yt-ep01-script by <your name>.
4. **Render it** — After you approve the script, copy and paste Prompt B. The designer runs video-render.
5. **Approve the video** — Ask the Lead to submit the video, watch ep01.mp4 to the end, then approve yt-ep01.
6. **Upload** — After you approve the video, copy and paste Prompt C. It goes up as private.
7. **Disclose** — In YouTube Studio, answer the altered or synthetic content question before making it public.

## The prompts

### PROMPT A — Claude Code: the video team

> Create an agent team for YouTube episode 1 from
> data/youtube-brief.md. Spawn three teammates:
> growth-strategist (the angle and hook),
> content-creator (content/video/ep01/scenes.json,
> 5-7 scenes, and ep01.md with title, tags,
> description, chapters and the AI disclosure) and
> creative-designer (a storyboard of the scenes and a
> thumbnail, using brand-visuals).
> You fact-check and fin-compliance the script, then
> submit it as yt-ep01-script. Publish nothing.
> Publish the storyboard as an artifact: one frame per
> scene with its words, visual and timing, and the
> thumbnail.
> Write for a business owner, in plain English: no
> codes, IDs, file names or line numbers; start with
> what it means and what I do next. Save a Word copy
> (.docx) of each result.

### PROMPTS B and C — Claude Code: render and upload

> PROMPT B
> Use the creative-designer subagent with
> video-render on the approved scenes.json →
> content/video/ep01/ep01.mp4 (data/video-spec.md).
> Check its length and size. Do not change approved
> words. Publish the checks as an artifact: length,
> size, resolution and every scene, PASS or FAIL.
>
> PROMPT C
> Do a dry run of the YouTube upload for yt-ep01
> (scripts/publish.mjs). If I say "go", upload it for
> real — as PRIVATE. Publish the request, then the
> YouTube Studio link, as an artifact.

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Walk me through the video scene by scene, in plain English."
- "Which figure on screen should I double-check, and against what?"
- "What does the AI disclosure say, and why do we need it?"

## Check your work

- [ ] The strategist, creator and designer each delivered their part.
- [ ] You approved the script, then the finished video.
- [ ] ep01.mp4 is 1920x1080, under 90 seconds, every scene present.
- [ ] Every figure on screen matches Horizon's 2026 facts.
- [ ] The description has chapters, link, disclaimer and AI disclosure.
- [ ] The upload is private (or the dry run printed the request).

## If it goes wrong

- **The video will not render** — Ask the trainer, or use sample-explainer.mp4 to test the upload.

## Stretch

- Ask the designer for a 30-second vertical Short from the same scenes.

> **Why it matters:** Approve twice: once for the words, once for the finished video. Rendering can break what the script got right.

## Next

Lab 13 — Campaign 5: Always On — the Weekly Growth Report. Keep what you built — the next lab starts from it.

## Safety

Use only this lab's synthetic data and your own accounts. Never paste a real API key, password, token or client data into a prompt or a file. Every email address in the data must resolve to your own inbox. Nothing is published or sent without a person approving that exact version.
