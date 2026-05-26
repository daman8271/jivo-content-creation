#!/usr/bin/env python3
"""Add the meme caption (brand-safe, no slur) onto the golden-Jivo meme image.
White bold text with a dark top gradient for legibility, matching the reference look.

Usage: python3 scripts/caption_golden_meme.py [input.png] [output.png]
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEME = os.path.join(ROOT, "outputs", "jivo-golden-meme")
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

CAPTION = ("After hours of scrolling, you found the golden Jivo "
           "that only appears in your feed once every 67 years")

inp = sys.argv[1] if len(sys.argv) > 1 else os.path.join(MEME, "golden-meme-v2.png")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(MEME, "golden-meme-FINAL.png")

img = Image.open(inp).convert("RGB")
# upscale to 1080 wide for a crisp post
W = 1080
H = round(img.height * W / img.width)
img = img.resize((W, H), Image.LANCZOS).convert("RGBA")

# dark gradient at the top for caption legibility
barh = int(H * 0.30)
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for y in range(barh):
    a = int(205 * (1 - y / barh) ** 1.15)
    od.line([(0, y), (W, y)], fill=(0, 0, 0, a))
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FONT_PATH, 58)
margin = 46


def wrap(text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


lines = wrap(CAPTION, font, W - 2 * margin)
y = int(H * 0.022)
lh = 66
for ln in lines:
    tw = draw.textlength(ln, font=font)
    x = (W - tw) / 2
    draw.text((x + 2, y + 3), ln, font=font, fill=(0, 0, 0, 180))  # shadow
    draw.text((x, y), ln, font=font, fill=(255, 255, 255, 255))
    y += lh

img.convert("RGB").save(out, quality=95)
print("DONE ->", out, img.size, "| lines:", len(lines))
