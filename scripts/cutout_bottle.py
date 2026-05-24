"""Clean white-background cutout for the Jivo packshot.

Keeps interior whites (cap highlights, label whites, veg mark) by only removing
near-white pixels that are connected to the image border (true background).
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

SRC = sys.argv[1] if len(sys.argv) > 1 else \
    "jivo-camera-broll/extra-light-olive-oil/work/bottle-front.webp"
OUT = sys.argv[2] if len(sys.argv) > 2 else \
    "jivo-camera-broll/extra-light-olive-oil/work/bottle-cutout.png"
THRESH = 232

_src = Image.open(SRC)
# If the source already carries transparency, trust it instead of white-keying.
if _src.mode in ("RGBA", "LA") or "transparency" in _src.info:
    rgba0 = _src.convert("RGBA")
    a0 = np.array(rgba0.split()[-1])
    if (a0 < 250).mean() > 0.02:  # genuinely has cut-out alpha
        ys, xs = np.where(a0 > 12)
        res = rgba0.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
        res.save(OUT)
        print(f"[existing-alpha] cutout saved {OUT} size={res.size}")
        sys.exit(0)

img = _src.convert("RGB")
arr = np.array(img).astype(np.int16)
h, w = arr.shape[:2]

near_white = (arr[:, :, 0] > THRESH) & (arr[:, :, 1] > THRESH) & (arr[:, :, 2] > THRESH)

# border-connected flood fill -> background only
try:
    from scipy import ndimage
    lbl, _ = ndimage.label(near_white)
    border = set(lbl[0, :]) | set(lbl[-1, :]) | set(lbl[:, 0]) | set(lbl[:, -1])
    border.discard(0)
    bg = np.isin(lbl, list(border))
    method = "scipy"
except Exception:
    bg = np.zeros((h, w), bool)
    bg[0, :] |= near_white[0, :]
    bg[-1, :] |= near_white[-1, :]
    bg[:, 0] |= near_white[:, 0]
    bg[:, -1] |= near_white[:, -1]
    while True:
        up = np.zeros_like(bg); up[1:, :] = bg[:-1, :]
        dn = np.zeros_like(bg); dn[:-1, :] = bg[1:, :]
        lf = np.zeros_like(bg); lf[:, 1:] = bg[:, :-1]
        rt = np.zeros_like(bg); rt[:, :-1] = bg[:, 1:]
        nxt = bg | ((up | dn | lf | rt) & near_white)
        if nxt.sum() == bg.sum():
            break
        bg = nxt
    method = "numpy"

alpha = np.where(bg, 0, 255).astype(np.uint8)
alpha_img = Image.fromarray(alpha, "L")
# erode 1px to kill the white anti-alias fringe, then soften
alpha_img = alpha_img.filter(ImageFilter.MinFilter(3))
alpha_img = alpha_img.filter(ImageFilter.GaussianBlur(0.7))

rgba = np.dstack([np.array(img).astype(np.uint8), np.array(alpha_img)])
res = Image.fromarray(rgba, "RGBA")

# crop to content
a = np.array(alpha_img)
ys, xs = np.where(a > 12)
res = res.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
res.save(OUT)
print(f"[{method}] cutout saved {OUT} size={res.size}")
