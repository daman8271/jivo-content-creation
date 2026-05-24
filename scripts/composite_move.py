"""Composite the real Jivo bottle into a modern GPT background and render the
6 keyframes of a simple LEFT->RIGHT camera truck. Bottle + counter pan together
(stays grounded); subtle contact shadow only, no dramatic cinematic shadows.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BG = "jivo-camera-broll/extra-light-olive-oil/work/modern-bg-A.png"
BOTTLE = "jivo-camera-broll/extra-light-olive-oil/work/bottle-cutout.png"
OUTDIR = "jivo-camera-broll/extra-light-olive-oil/shot01-modern"
os.makedirs(OUTDIR, exist_ok=True)

bg = Image.open(BG).convert("RGB")
W, H = bg.size

bottle = Image.open(BOTTLE).convert("RGBA")
bw, bh = bottle.size

# ---- placement (tweakable) ----
BOTTLE_H = int(0.52 * H)
scale = BOTTLE_H / bh
BOTTLE_W = int(bw * scale)
bottle_r = bottle.resize((BOTTLE_W, BOTTLE_H), Image.LANCZOS)

center_x = W // 2
base_y = int(0.84 * H)
left = center_x - BOTTLE_W // 2
top = base_y - BOTTLE_H

# ---- subtle contact shadow ----
scene = bg.convert("RGBA")
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sw, sh = int(BOTTLE_W * 1.5), int(BOTTLE_H * 0.10)
cx, cy = center_x + int(0.06 * BOTTLE_W), base_y
sd.ellipse([cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2], fill=(0, 0, 0, 95))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
scene = Image.alpha_composite(scene, shadow)

# ---- place bottle ----
scene.alpha_composite(bottle_r, (left, top))
scene = scene.convert("RGB")
scene.save(f"{OUTDIR}/_composite-wide.png")

# ---- 6 keyframes: left->right camera truck ----
vw, vh = round(H * 9 / 16), H
PAN_X0, PAN_X1 = 202, 435
xs = np.linspace(PAN_X0, PAN_X1, 6).round().astype(int)
FW, FH = 540, 960
frames = []
for i, x in enumerate(xs, 1):
    x = int(max(0, min(W - vw, x)))
    fr = scene.crop((x, 0, x + vw, vh)).resize((FW, FH), Image.LANCZOS)
    fr.save(f"{OUTDIR}/frame-{i:02d}.png")
    frames.append(fr)
frames[0].save(f"{OUTDIR}/START-frame.png")
frames[-1].save(f"{OUTDIR}/END-frame.png")

# ---- contact sheet ----
gap = 12
sheet = Image.new("RGB", (FW * 6 + gap * 7, FH + gap * 2), (245, 245, 245))
for i, fr in enumerate(frames):
    sheet.paste(fr, (gap + i * (FW + gap), gap))
sheet.save(f"{OUTDIR}/contact-sheet.png")
print("saved ->", OUTDIR)
print("bg", (W, H), "viewport", (vw, vh), "pan_x", list(xs),
      "bottle", (BOTTLE_W, BOTTLE_H), "at", (left, top))
