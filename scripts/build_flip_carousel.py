#!/usr/bin/env python3
"""
Jivo "Flip" Carousel — deterministic type/layout engine.

Takes AI-generated hero shots (oil/food, NO text, NO logo) and stamps the locked
typography onto them. One template, every slide pixel-consistent, this carousel and
every future one. See docs/superpowers/specs/2026-05-24-jivo-flip-carousel-design.md.

Usage:
    python3 scripts/build_flip_carousel.py            # build every slide that has a hero
    python3 scripts/build_flip_carousel.py 02         # build only slide 02
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
HEROES = ROOT / "jivo-flip-carousel" / "heroes"
SLIDES_OUT = ROOT / "jivo-flip-carousel" / "slides"

# ----------------------------------------------------------------------------
# LOCKED STYLE TOKENS  — do not edit casually; these define the series' identity
# ----------------------------------------------------------------------------
STYLE = {
    "canvas_w": 1080,
    "canvas_h": 1350,            # 4:5
    "bg": (221, 220, 196),       # #DDDCC4 sage-cream (fallback / scrim color)
    "ink": (31, 61, 43),         # #1F3D2B deep Jivo forest-green
    "margin": 80,                # side safe margin
    "top_y": 150,                # y where the text block starts
    "l1_font": "Poppins-SemiBold.ttf",
    "l1_size": 66,
    "l1_tracking": -1,           # px between glyphs
    "l1_line_spacing": 1.06,
    "l2_font": "Poppins-Regular.ttf",
    "l2_size": 40,
    "l2_tracking": 0,
    "l2_gap": 26,                # gap between line1 block and line2
    "cta_font": "Poppins-Medium.ttf",
    "cta_size": 30,
    "cta_gap": 40,               # gap above CTA
    "top_scrim": True,           # soft sage-cream->transparent scrim over top 32%
    "scrim_frac": 0.32,
}

# ----------------------------------------------------------------------------
# SLIDES  — (id, line1, line2, cta)   hero file = heroes/<id>-*.png
# ----------------------------------------------------------------------------
SLIDES = [
    ("01", "He'll always let you down —", "Jivo never will.   (keep swiping)", None),
    ("02", "He couldn't handle the heat,", "we've got a high smoke point.", None),
    ("03", "He was too heavy,", "we're extra light.", None),
    ("04", "He was so fake,", "we're 100% pure, cold-pressed.", None),
    ("05", "He gave you mixed signals,", "we're consistent every time.", None),
    ("06", "He couldn't commit,", "we've been in your kitchen for years.", None),
    ("07", "His replies ran dry,", "our food never does.", None),
    ("08", "He broke your heart,", "we're the kind that's good for it.",
     "Cook with someone good for you. — Jivo"),
]


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def line_width(draw, text, fnt, tracking):
    w = draw.textlength(text, font=fnt)
    if tracking and len(text) > 1:
        w += tracking * (len(text) - 1)
    return w


def wrap(draw, text, fnt, tracking, max_w):
    words = text.split(" ")
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if line_width(draw, trial, fnt, tracking) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, text, fnt, tracking, cx, y, fill):
    """Draw one line centered on cx at top-y=y, honoring per-glyph tracking."""
    total = line_width(draw, text, fnt, tracking)
    x = cx - total / 2
    if not tracking:
        draw.text((x, y), text, font=fnt, fill=fill)
        return
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking


def fit_hero(hero_path, w, h):
    """Cover-crop the hero to w x h, anchored to the BOTTOM (keep the food)."""
    img = Image.open(hero_path).convert("RGB")
    scale = max(w / img.width, h / img.height)
    nw, nh = round(img.width * scale), round(img.height * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    left = (nw - w) // 2
    top = nh - h                      # bottom-anchored
    return img.crop((left, top, left + w, top + h))


def add_scrim(img):
    w, h = img.size
    band = int(h * STYLE["scrim_frac"])
    scrim = Image.new("RGBA", (w, band), (0, 0, 0, 0))
    sd = scrim.load()
    r, g, b = STYLE["bg"]
    for y in range(band):
        a = int(255 * (1 - y / band))   # opaque at top -> transparent
        for x in range(w):
            sd[x, y] = (r, g, b, a)
    base = img.convert("RGBA")
    base.alpha_composite(scrim, (0, 0))
    return base.convert("RGB")


def build(slide):
    sid, l1, l2, cta = slide
    matches = list(HEROES.glob(f"{sid}-*.png")) + list(HEROES.glob(f"{sid}-*.jpg"))
    W, H, M = STYLE["canvas_w"], STYLE["canvas_h"], STYLE["margin"]
    cx = W / 2
    max_w = W - 2 * M

    if matches:
        canvas = fit_hero(matches[0], W, H)
    else:
        canvas = Image.new("RGB", (W, H), STYLE["bg"])   # placeholder if no hero yet

    if STYLE["top_scrim"]:
        canvas = add_scrim(canvas)

    draw = ImageDraw.Draw(canvas)
    f1 = font(STYLE["l1_font"], STYLE["l1_size"])
    f2 = font(STYLE["l2_font"], STYLE["l2_size"])

    y = STYLE["top_y"]
    for line in wrap(draw, l1, f1, STYLE["l1_tracking"], max_w):
        draw_centered(draw, line, f1, STYLE["l1_tracking"], cx, y, STYLE["ink"])
        y += int(STYLE["l1_size"] * STYLE["l1_line_spacing"])

    y += STYLE["l2_gap"]
    for line in wrap(draw, l2, f2, STYLE["l2_tracking"], max_w):
        draw_centered(draw, line, f2, STYLE["l2_tracking"], cx, y, STYLE["ink"])
        y += int(STYLE["l2_size"] * 1.18)

    if cta:
        fc = font(STYLE["cta_font"], STYLE["cta_size"])
        y += STYLE["cta_gap"]
        for line in wrap(draw, cta, fc, 0, max_w):
            draw_centered(draw, line, fc, 0, cx, y, STYLE["ink"])
            y += int(STYLE["cta_size"] * 1.18)

    SLIDES_OUT.mkdir(parents=True, exist_ok=True)
    out = SLIDES_OUT / f"{sid}-slide.png"
    canvas.save(out, "PNG")
    tag = "" if matches else "  (placeholder bg — no hero yet)"
    print(f"built {out.relative_to(ROOT)}{tag}")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for slide in SLIDES:
        if only and slide[0] != only:
            continue
        build(slide)


if __name__ == "__main__":
    main()
