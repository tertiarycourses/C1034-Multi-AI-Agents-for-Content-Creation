---
name: video-render
description: Use when turning an approved scenes.json into a video. One branded card per scene, 1920x1080, under 90 seconds, ffmpeg; check with ffprobe; never change approved words.
---
# Video render
1. Input: the APPROVED content/video/<id>/scenes.json.
2. One 1920x1080 card per scene in the brand colours; last card carries
   the call to action and "General information only, not financial
   advice."
3. Join with ffmpeg (H.264 + AAC, 30 fps); optional voice-over.
4. Check with ffprobe: size, duration under 90 s, every scene present.
5. Never change the approved words.
