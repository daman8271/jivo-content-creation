#!/usr/bin/env python3
"""Render the two reference-matched text overlays (Poppins) and burn them onto the
assembled draft at the matching timestamps. Produces full-draft-v2-480p.mp4.

Overlays:
  S2 beat (~6.4-9.0s): "FROM THE FARMS OF SPAIN"  (echoes ref "American INGREDIENTS")
  S4 beat (~12.1-15s): "INDIA'S MOST / PREMIUM / EXTRA LIGHT OLIVE OIL"
                        (echoes ref "AMERICA'S MOST Premium LIGHT BEER")
"""
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
OUT = os.path.join(ROOT, "outputs", "jivo-extra-light-flying-reel")
DRAFT = os.path.join(OUT, "drafts")
TXT = os.path.join(OUT, "text")
os.makedirs(TXT, exist_ok=True)

W, H = 480, 854


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def draw_center(draw, cx, y, text, fnt, fill=(255, 255, 255, 255), tracking=0):
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, wch in zip(text, widths):
        draw.text((x + 2, y + 3), ch, font=fnt, fill=(0, 0, 0, 170))  # shadow
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += wch + tracking


# ---- S2 overlay ----
img2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d2 = ImageDraw.Draw(img2)
y2 = int(H * 0.15)
draw_center(d2, W / 2, y2, "FROM THE FARMS OF", font("Poppins-Medium.ttf", 25), tracking=2)
draw_center(d2, W / 2, y2 + 33, "SPAIN", font("Poppins-Bold.ttf", 62), tracking=2)
img2.save(os.path.join(TXT, "overlay_s2.png"))

# ---- S4 overlay ----
img4 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d4 = ImageDraw.Draw(img4)
y4 = int(H * 0.06)
draw_center(d4, W / 2, y4, "INDIA'S MOST", font("Poppins-SemiBold.ttf", 29), tracking=3)
draw_center(d4, W / 2, y4 + 33, "PREMIUM", font("Poppins-Bold.ttf", 58), tracking=1)
draw_center(d4, W / 2, y4 + 100, "EXTRA LIGHT OLIVE OIL", font("Poppins-SemiBold.ttf", 23), tracking=2)
img4.save(os.path.join(TXT, "overlay_s4.png"))

# ---- compose ----
src = os.path.join(DRAFT, "full-draft-v1-480p.mp4")
o2 = os.path.join(TXT, "overlay_s2.png")
o4 = os.path.join(TXT, "overlay_s4.png")
out = os.path.join(DRAFT, "full-draft-v2-480p.mp4")
fc = (
    "[0:v][1:v]overlay=0:0:enable='between(t,6.4,9.0)'[a];"
    "[a][2:v]overlay=0:0:enable='between(t,12.1,15.0)'[v]"
)
subprocess.run([
    "ffmpeg", "-y", "-i", src, "-i", o2, "-i", o4,
    "-filter_complex", fc, "-map", "[v]", "-an",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", out,
], check=True, capture_output=True)
print("DONE ->", out)
