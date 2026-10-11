"""Render an approved scenes.json into a 1920x1080 explainer (Lab 11).

    python3 scripts/render-video.py content/video/ep01/scenes.json [--voice]

One branded title card per scene (Pillow), joined with ffmpeg. --voice adds
a voice-over with macOS `say`; without it the video has a silent track, so
it uploads like any other MP4. Never changes the approved words.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
INK, SKY, SUN, SUN_DEEP = '#22305B', '#EAF3FF', '#FFC845', '#F5A524'
FONTS = ['/System/Library/Fonts/Supplemental/Arial Bold.ttf',
         '/System/Library/Fonts/Supplemental/Arial.ttf',
         '/Library/Fonts/Arial.ttf', 'C:/Windows/Fonts/arialbd.ttf',
         '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']


def font(size):
    for f in FONTS:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default(size)


def sunny(d, cx, cy, r):
    for i in range(12):                      # rays
        import math
        a = i * math.pi / 6
        x1, y1 = cx + (r + 18) * math.cos(a), cy + (r + 18) * math.sin(a)
        x2, y2 = cx + (r + 48) * math.cos(a), cy + (r + 48) * math.sin(a)
        d.line([(x1, y1), (x2, y2)], fill=SUN_DEEP, width=12)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SUN, outline=INK, width=8)
    d.ellipse([cx - 38, cy - 30, cx - 18, cy - 6], fill=INK)
    d.ellipse([cx + 18, cy - 30, cx + 38, cy - 6], fill=INK)
    d.arc([cx - 44, cy - 20, cx + 44, cy + 48], 20, 160, fill=INK, width=8)


def card(scene, n, total, out):
    im = Image.new('RGB', (W, H), SKY)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 28, H], fill=SUN)
    sunny(d, W - 260, 250, 110)
    d.text((140, 150), f'{n} / {total}', font=font(40), fill=SUN_DEEP)
    y = 230
    for line in textwrap.wrap(scene['title'], 26):
        d.text((140, y), line, font=font(104), fill=INK)
        y += 124
    y += 40
    for line in textwrap.wrap(scene['text'], 48):
        d.text((140, y), line, font=font(56), fill=INK)
        y += 76
    d.line([(140, H - 150), (W - 140, H - 150)], fill=INK, width=4)
    d.text((140, H - 120), 'Horizon Wealth Planning', font=font(40), fill=INK)
    d.text((W - 140, H - 120), 'General information only, not financial advice',
           font=font(32), fill=INK, anchor='ra')
    im.save(out)


def main():
    if not shutil.which('ffmpeg'):
        sys.exit('ffmpeg is not installed (brew install ffmpeg / winget install ffmpeg)')
    src = Path(sys.argv[1])
    voice = '--voice' in sys.argv and shutil.which('say')
    out = Path(sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv \
        else src.with_name(src.parent.name + '.mp4')
    scenes = json.loads(src.read_text())
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        parts = []
        for i, s in enumerate(scenes, 1):
            png, mp4 = t / f'{i:02d}.png', t / f'{i:02d}.mp4'
            card(s, i, len(scenes), png)
            audio = ['-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo']
            if voice:
                aiff = t / f'{i:02d}.aiff'
                subprocess.run(['say', '-o', str(aiff), s['text']], check=True)
                audio = ['-i', str(aiff)]
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1',
                            '-i', str(png), *audio, '-t', str(s['seconds']),
                            '-r', '30', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                            '-c:a', 'aac', '-af', 'apad', '-shortest', str(mp4)],
                           check=True)
            parts.append(mp4)
        lst = t / 'list.txt'
        lst.write_text(''.join(f"file '{p}'\n" for p in parts))
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat',
                        '-safe', '0', '-i', str(lst), '-c', 'copy', str(out)],
                       check=True)
    print(f'{out}  ({sum(s["seconds"] for s in scenes)} s, {len(scenes)} scenes)')


if __name__ == '__main__':
    main()
