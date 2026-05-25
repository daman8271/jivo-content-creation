#!/usr/bin/env python3
"""Render a top-band meme caption (bold black on transparent) sized for the
white space above the clip in meme 4.mp4, scaled to 1080x1920."""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1080, 1920
TOP_BAND = 603                      # detected white band height
PAD_TOP, PAD_BOT = 46, 34           # breathing room inside the band
MAX_W = W * 0.90                     # text wrap width
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
TEXT = 'every premium "heart oil" brand the second you flip the bottle and actually read the ingredients'

usable_h = TOP_BAND - PAD_TOP - PAD_BOT
canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(canvas)


def wrap(font):
    words, lines, cur = TEXT.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= MAX_W:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


# auto-fit: largest size whose wrapped block fits the usable band height
best = None
for size in range(72, 28, -2):
    font = ImageFont.truetype(FONT_PATH, size)
    lines = wrap(font)
    asc, desc = font.getmetrics()
    line_h = asc + desc
    gap = round(line_h * 0.10)
    block_h = line_h * len(lines) + gap * (len(lines) - 1)
    if block_h <= usable_h:
        best = (size, font, lines, line_h, gap, block_h)
        break
if best is None:                      # fallback to smallest
    size = 30; font = ImageFont.truetype(FONT_PATH, size)
    lines = wrap(font); asc, desc = font.getmetrics(); line_h = asc + desc
    gap = round(line_h * 0.10); block_h = line_h * len(lines) + gap * (len(lines) - 1)
    best = (size, font, lines, line_h, gap, block_h)

size, font, lines, line_h, gap, block_h = best
y = PAD_TOP + (usable_h - block_h) // 2          # vertical-center in band
for ln in lines:
    w = draw.textlength(ln, font=font)
    draw.text(((W - w) / 2, y), ln, font=font, fill=(0, 0, 0, 255))
    y += line_h + gap

canvas.save("caption4.png")
print(f"caption4.png | size={size}px lines={len(lines)} block_h={block_h}px / usable={usable_h}px")
print("lines:", lines)

# preview: composite over a real bright frame
base = Image.open(".work/f_07.png").convert("RGBA")
Image.alpha_composite(base, canvas).convert("RGB").save("caption4_preview.png", quality=92)
print("wrote caption4_preview.png")
