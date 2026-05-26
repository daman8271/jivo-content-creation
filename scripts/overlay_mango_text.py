#!/usr/bin/env python3
"""Burn the hero tagline onto the mango reel's final beat (echoes the coke spot's
"Lleva la Magia a la Mesa" + Real Magic logo). Produces full-draft-v2-480p.mp4.

Tagline (top, ~7.6-10s): "BRING THE MAGIC / TO YOUR TABLE"
Brand line (bottom):     "JIVO HEALTHY WHEATGRASS - MANGO"
"""
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
OUTDIR = os.path.join(ROOT, "outputs", "jivo-wheatgrass-mango-reel")
DRAFT = os.path.join(OUTDIR, "drafts")
TXT = os.path.join(OUTDIR, "text")
os.makedirs(TXT, exist_ok=True)
W, H = 480, 854


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def draw_center(draw, cx, y, text, fnt, fill=(255, 255, 255, 255), tracking=0):
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, wch in zip(text, widths):
        draw.text((x + 2, y + 2), ch, font=fnt, fill=(0, 0, 0, 150))
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += wch + tracking


img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
# tagline near top
yt = int(H * 0.10)
draw_center(d, W / 2, yt, "BRING THE MAGIC", font("Poppins-Bold.ttf", 38), tracking=1)
draw_center(d, W / 2, yt + 46, "TO YOUR TABLE", font("Poppins-Bold.ttf", 38), tracking=1)
# brand line near bottom
yb = int(H * 0.88)
draw_center(d, W / 2, yb, "JIVO  HEALTHY WHEATGRASS", font("Poppins-SemiBold.ttf", 22), tracking=2)
draw_center(d, W / 2, yb + 28, "M A N G O", font("Poppins-Medium.ttf", 18), tracking=4)
img.save(os.path.join(TXT, "overlay_s4.png"))

src = os.path.join(DRAFT, "full-draft-v1-480p.mp4")
ov = os.path.join(TXT, "overlay_s4.png")
out = os.path.join(DRAFT, "full-draft-v2-480p.mp4")
fc = "[0:v][1:v]overlay=0:0:enable='between(t,7.6,10.0)'[v]"
subprocess.run([
    "ffmpeg", "-y", "-i", src, "-i", ov,
    "-filter_complex", fc, "-map", "[v]", "-an",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", out,
], check=True, capture_output=True)
print("DONE ->", out)
