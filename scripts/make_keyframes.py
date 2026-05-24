"""Build two extreme-wide keyframes (KF1 left, KF2 right) of the real Jivo bottle
floating on a clean premium background. Same cutout in both -> identical bottle.
Feed KF1 (start) + KF2 (end) into Kling 3.0 for the left->right move.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

CUT = "jivo-camera-broll/extra-light-olive-oil/work/bottle-cutout-hires.png"
OUT = "jivo-camera-broll/extra-light-olive-oil/shot01-keyframes"
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920

# ---- clean premium radial-gradient background ----
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
cx0, cy0 = 0.50 * W, 0.40 * H
d = np.sqrt(((xx - cx0) / (0.78 * W)) ** 2 + ((yy - cy0) / (0.88 * H)) ** 2)
d = np.clip(d, 0, 1)
c_center = np.array([250, 250, 248], np.float32)
c_edge = np.array([228, 227, 223], np.float32)
bg = (c_center[None, None] * (1 - d[..., None]) + c_edge[None, None] * d[..., None]).astype(np.uint8)
bg_img = Image.fromarray(bg, "RGB")

bottle = Image.open(CUT).convert("RGBA")
BH = int(0.48 * H)
scale = BH / bottle.height
BW = int(bottle.width * scale)
b = bottle.resize((BW, BH), Image.LANCZOS)


def make(cx_frac, name):
    cx = int(cx_frac * W)
    base_y = int(0.72 * H)          # bottle bottom (floating)
    top = base_y - BH
    left = cx - BW // 2
    scene = bg_img.convert("RGBA")
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sy, sw, shh = int(0.82 * H), int(BW * 1.6), int(BW * 0.32)
    sd.ellipse([cx - sw // 2, sy - shh // 2, cx + sw // 2, sy + shh // 2], fill=(0, 0, 0, 55))
    sh = sh.filter(ImageFilter.GaussianBlur(36))
    scene = Image.alpha_composite(scene, sh)
    scene.alpha_composite(b, (left, top))
    out = scene.convert("RGB")
    out.save(f"{OUT}/{name}.png")
    return out


kf1 = make(0.26, "KF1-left")
kf2 = make(0.74, "KF2-right")

cmp = Image.new("RGB", (W * 2 + 40, H), (255, 255, 255))
cmp.paste(kf1, (0, 0))
cmp.paste(kf2, (W + 40, 0))
cmp = cmp.resize((int((W * 2 + 40) * 0.42), int(H * 0.42)))
cmp.save(f"{OUT}/KF-compare.png")
print("keyframes saved ->", OUT, "| bottle", (BW, BH))
