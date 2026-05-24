"""Isolate ONLY the bottle (leftmost object) from EL.jpg, which also contains the
tin. Split objects on the white vertical gap between them."""
import numpy as np
from PIL import Image

SRC = "jivo brand assets /03_products/extra-light-olive-oil/EL.jpg"
OUT = "jivo-camera-broll/extra-light-olive-oil/work/bottle-hires.png"

im = Image.open(SRC).convert("RGB")
a = np.array(im)
Hh = a.shape[0]
# Detect objects in the UPPER 72% only (avoids the base shadow that bridges the gap),
# and require real column density so a faint shadow doesn't count as object.
strong_top = a[:int(0.72 * Hh)].min(axis=2) < 215
counts = strong_top.sum(axis=0)
obj = counts > 25
xs = np.where(obj)[0]

runs, s, p = [], xs[0], xs[0]
for x in xs[1:]:
    if x - p > 14:
        runs.append((s, p)); s = x
    p = x
runs.append((s, p))
runs = [r for r in runs if r[1] - r[0] > 40]   # drop specks
bx0, bx1 = runs[0]                              # leftmost real object = bottle

# y-bbox from the bottle's own columns over the FULL height (keep its base)
strong_full = a.min(axis=2) < 225
sub = strong_full[:, bx0:bx1 + 1]
ys = np.where(sub.any(axis=1))[0]
by0, by1 = ys.min(), ys.max()
pad = 14
crop = im.crop((max(0, bx0 - pad), max(0, by0 - pad),
                min(a.shape[1], bx1 + pad), min(a.shape[0], by1 + pad)))
crop.save(OUT)
print("runs:", runs, "-> bottle crop", crop.size)
