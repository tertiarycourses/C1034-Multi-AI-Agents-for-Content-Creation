# Video render spec (Lab 12)

Input: content/video/ep01/scenes.json — the APPROVED script as a list of
scenes: {"seconds": 8, "title": "...", "text": "..."}.
Output: content/video/ep01/ep01.mp4 and ep01.md (the YouTube metadata file,
with the publishing-spec frontmatter: id yt-ep01, channel youtube, title,
tags, video path; the body is the description).

- 1920x1080, 30 fps, H.264 + AAC, under 90 seconds.
- One title card per scene: sky-blue background (#EAF3FF), ink text
  (#22305B), a sun-yellow (#FFC845) accent bar, the scene's title large and
  its text below; "Horizon Wealth Planning" small at the bottom.
- Last card: the call to action and "General information only, not
  financial advice."
- Optional voice-over: on macOS, `say` can read each scene's text; or record
  your own. No voice? Captions only is fine.
- Tools: ffmpeg (and Python + Pillow, or Node) — no paid services.
