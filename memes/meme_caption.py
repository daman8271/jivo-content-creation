#!/usr/bin/env python3
"""Write meme-style caption (white fill + thick black outline) onto meme 1.png.
Matches the reference chihuahua-meme typography: bold grotesque, lower-third, centered.
"""
from PIL import Image, ImageDraw, ImageFont

SRC = "meme 1.png"
OUT = "meme-1-oil.png"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

LINES = ["Dont act innocent", "i know what type of oil u use"]

img = Image.open(SRC).convert("RGB")
W, H = img.size
draw = ImageDraw.Draw(img)

# --- auto-fit: largest font where the widest line fits in 90% of width ---
MAX_W = W * 0.90
size = 10
while size < 400:
    f = ImageFont.truetype(FONT_PATH, size + 2)
    widest = max(draw.textlength(t, font=f) for t in LINES)
    if widest > MAX_W:
        break
    size += 2
font = ImageFont.truetype(FONT_PATH, size)
stroke = max(2, round(size * 0.085))  # chunky meme outline

# --- measure block height ---
asc, desc = font.getmetrics()
line_h = asc + desc
gap = round(line_h * 0.12)
block_h = line_h * len(LINES) + gap * (len(LINES) - 1)

# vertical center of text block at ~73% of image height (over chest/paws)
block_top = int(H * 0.73 - block_h / 2)

y = block_top
for t in LINES:
    w = draw.textlength(t, font=font)
    x = (W - w) / 2
    draw.text((x, y), t, font=font, fill="white",
              stroke_width=stroke, stroke_fill="black")
    y += line_h + gap

img.save(OUT, quality=95)
print(f"Saved {OUT}  | font size={size}px  stroke={stroke}px  block_top={block_top}")
