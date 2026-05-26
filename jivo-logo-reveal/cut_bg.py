#!/usr/bin/env python3
"""Controlled white/shadow key for the hand-drawn JIVO badge.

Keeps the greenish mint circle + dark-green doodle, drops the pure-white
field and the soft grey drop-shadow, with a feathered (anti-aliased) edge.
"""
import numpy as np
from PIL import Image

src = Image.open("logo.png").convert("RGB")
a = np.asarray(src).astype(np.float32)
R, G, B = a[..., 0], a[..., 1], a[..., 2]

mn = np.minimum(np.minimum(R, G), B)   # brightness floor (white ~255)
mx = np.maximum(np.maximum(R, G), B)
sat = mx - mn                           # 0 = neutral/grey, high = colored

# "background-ness": bright AND nearly neutral (white field + grey shadow).
# mint interior ~ (216,245,227): sat ~29 -> stays foreground.
# Feather the alpha between mn=225 (fully keep) and mn=252 (fully remove),
# but only treat a pixel as removable when it's near-neutral (sat < 32).
lo, hi = 225.0, 252.0
bright_ramp = np.clip((mn - lo) / (hi - lo), 0.0, 1.0)   # 0 keep .. 1 remove
neutral = np.clip((32.0 - sat) / 32.0, 0.0, 1.0)         # 1 neutral .. 0 colored
removal = bright_ramp * neutral
alpha = (1.0 - removal) * 255.0

out = np.dstack([a, alpha]).astype(np.uint8)
img = Image.fromarray(out, mode="RGBA")

# Tight-crop to opaque bounds, then re-center on a square padded canvas so
# the badge sits clean in the composition.
bbox = img.getchannel("A").point(lambda p: 255 if p > 12 else 0).getbbox()
if bbox:
    cropped = img.crop(bbox)
    s = max(cropped.size)
    pad = int(s * 0.06)
    canvas = Image.new("RGBA", (s + 2 * pad, s + 2 * pad), (0, 0, 0, 0))
    canvas.paste(cropped, ((canvas.size[0] - cropped.size[0]) // 2,
                           (canvas.size[1] - cropped.size[1]) // 2))
    img = canvas

img.save("logo-cut.png")
print("wrote logo-cut.png", img.size,
      "opaque px:", int((np.asarray(img)[..., 3] > 12).sum()))
