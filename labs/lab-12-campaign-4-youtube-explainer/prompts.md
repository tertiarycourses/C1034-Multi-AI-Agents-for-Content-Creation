# Prompts — Lab 12: Campaign 4: The YouTube Explainer

**Use: Claude Code — Code mode (the </> button) in the Claude desktop app, in your horizon-studio folder.** Paste each prompt as written; change only what the lab tells you to.

**Easiest:** copy each prompt from https://tertiarycourses.github.io/C1034-Multi-AI-Agents-for-Content-Creation/prompts/claude/#lab-12 (one Copy button per prompt).

## PROMPT A — Claude Code: the video team

```
Create an agent team for YouTube episode 1 from
data/youtube-brief.md. Spawn three teammates:
growth-strategist (the angle and hook),
content-creator (content/video/ep01/scenes.json,
5-7 scenes, and ep01.md with title, tags,
description, chapters and the AI disclosure) and
creative-designer (a storyboard of the scenes and a
thumbnail, using brand-visuals).
You fact-check and fin-compliance the script, then
submit it as yt-ep01-script. Publish nothing.
Publish the storyboard as an artifact: one frame per
scene with its words, visual and timing, and the
thumbnail.
Write for a business owner, in plain English: no
codes, IDs, file names or line numbers; start with
what it means and what I do next. Save a Word copy
(.docx) of each result.
```

## PROMPTS B and C — Claude Code: render and upload

```
PROMPT B
Use the creative-designer subagent with
video-render on the approved scenes.json →
content/video/ep01/ep01.mp4 (data/video-spec.md).
Check its length and size. Do not change approved
words. Publish the checks as an artifact: length,
size, resolution and every scene, PASS or FAIL.

PROMPT C
Do a dry run of the YouTube upload for yt-ep01
(scripts/publish.mjs). If I say "go", upload it for
real — as PRIVATE. Publish the request, then the
YouTube Studio link, as an artifact.
```

## Ask about the result

Once a result opens, type any of these in the chat to get its meaning. Ask until it makes sense to you — then decide.

- "Walk me through the video scene by scene, in plain English."
- "Which figure on screen should I double-check, and against what?"
- "What does the AI disclosure say, and why do we need it?"
