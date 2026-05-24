# Jivo "Flip" Carousel — Design Spec

**Date:** 2026-05-24
**Status:** Approved concept, in production (proof slide stage)
**Format:** 8-slide static Instagram carousel, 4:5 (1080×1350)

---

## 1. The concept

A relatable, witty carousel that takes a dating/relationship **red flag** and flips the
*exact same word* into a Jivo product virtue. The product becomes "the better partner."

Modeled on the viral `bakemyday.me` "men vs. dessert" carousel — same machine: one brand,
a different hero per slide, identical visual system, satisfying swipe rhythm.

- **Anchor:** brand-level (one Jivo, a different oil virtue each slide).
- **Voice:** English, witty. Setup clause + comma → lowercase flip clause (mirrors reference).
- **Closer:** the heart-health line ("he broke your heart, we're the kind that's good for it").

### Hard constraints (from the brand owner — non-negotiable)

1. **No standalone logo / watermark on the slide** — no corner mark, no logo stitched on
   the side. BUT the **real product bottle, with its actual label/logo, IS the brand
   identity and is used as-is** on the cover + closer — composited from the real product
   PNG (`jivo brand assets /03_products/canola-oil/1L Canola Oil Front New 2025.png`) for a
   pixel-perfect label, never AI-redrawn. Middle slides are pure food/oil action.
2. **Images:** Higgsfield **`gpt_image_2`** only, **2k / high quality**, generated **without text**.
3. **All typography, spacing, palette, lighting, framing are LOCKED tokens** — identical on
   every slide and reusable for future carousels. Codified in the overlay script + a fixed
   image "style block." Font files are bundled in `assets/fonts/` so they never drift.
4. **Text is added in post** by a deterministic Python/PIL script — never by the AI model.

### Compliance

Edible-oil rules: no medical/disease claims (no *cures/prevents/treats*). Keep product-led
and factual (*cold-pressed, extra light, high smoke point, low in saturated fat, rich in MUFA*).
Slide 8's "good for your heart" stays soft/product-led; final copy gets a legal pass before posting.

---

## 2. Locked visual system (the reusable template)

These values are FIXED across every slide, this carousel and all future ones.

### Canvas
- Final output: **1080 × 1350 px** (4:5).
- AI hero generated at **3:4, 2k** then cropped/fitted to 1080×1350 by the script.

### Background / palette
- **Sage-cream:** `#DDDCC4` (target). Warm muted green-cream.
- **Ink (text):** **deep Jivo forest-green `#1F3D2B`**.
- Lighting: soft top-down natural daylight, gentle center glow, one soft shadow under subject.

### Composition
- **Top ~35%:** empty negative space for text.
- **Bottom ~65%:** single hero "money-shot" (oil in action), often cropping off the bottom edge.
- Same camera height + framing logic every slide.

### Typography (Poppins, bundled in `assets/fonts/`)
- **Line 1 (the roast):** Poppins **SemiBold**, **66 px** (largest size where all 8
  headlines fit on one line at 80 px margins), ink `#1F3D2B`, centered, tracking −1,
  line-height 1.06.
- **Line 2 (the flip):** Poppins **Regular**, **40 px**, ink `#1F3D2B`, centered,
  lowercase, ~26 px gap under line 1.
- Text block **top-anchored at y = 150 px**, horizontally centered, max width **880 px** (wraps).
- Side safe margin: **80 px**.
- Optional soft top scrim (sage-cream → transparent, top 32%) — OFF by default, available
  in the script if an AI background ever drifts and text contrast needs help.

### Image "style block" (appended verbatim to every hero prompt)
> Smooth warm sage-cream seamless studio background (soft muted green-cream), soft top-down
> natural daylight, gentle center glow, one soft shadow beneath subject, clean empty
> uncluttered upper third reserved for text, single hero subject in the lower two-thirds,
> shallow depth of field, glossy appetizing highlights, commercial food photography,
> vertical 3:4, high detail, photorealistic. No text, no words, no letters, no logos,
> no labels, no packaging, no branding, no hands.

---

## 3. The 8 slides

| # | Line 1 (roast), | line 2 (flip) | Hero subject | Virtue |
|---|---|---|---|---|
| 1 · cover | He'll always let you down — | Jivo never will. *(swipe 🫒)* | luscious golden oil stream pouring/splashing mid-air, droplets | brand hook |
| 2 | He couldn't handle the heat, | we've got a high smoke point. | golden oil sizzling in a steel kadai, cumin + red chillies blooming | high smoke point |
| 3 | He was too heavy, | we're extra light. | bright golden oil drizzling over a fresh crisp salad | extra light |
| 4 | He was so fake, | we're 100% pure, cold-pressed. | extreme close-up clean oil pour, single clear droplet | cold-pressed purity |
| 5 | He gave you mixed signals, | we're consistent every time. | oil glossing/tossing vegetables in a pan, even glistening coat | reliability |
| 6 | He couldn't commit, | we've been in your kitchen for years. | warm home-kitchen scene, a finished home-cooked dish steaming | loyalty/heritage |
| 7 | His replies ran dry, | our food never does. | juicy, glistening sabzi/curry with a rich glossy sheen | richness |
| 8 · closer | He broke your heart, | we're the kind that's good for it. | a drizzle of golden oil tracing a subtle heart over a fresh dish | heart-health + CTA |

- **Slide 8 CTA (small, under line 2):** "Cook with someone good for you. — Jivo."
- Slides 1 & 8 carry the word "Jivo" (typeset, not logo). All other slides: copy only.

---

## 4. Production pipeline

1. **Generate** 8 heroes via `gpt_image_2` (3:4, 2k, high), each = `<slide subject> + style block`.
   Save raw heroes to `jivo-flip-carousel/heroes/NN-slug.png`.
2. **Overlay** type with `scripts/build_flip_carousel.py` — reads a single locked config
   (tokens above) + a slides list (the table) → outputs `jivo-flip-carousel/slides/NN-slug.png`
   at 1080×1350. One template, all 8 pixel-consistent, fully editable.
3. **Caption + legal pass**, then post as a carousel.

### Script responsibilities (`build_flip_carousel.py`)
- Single `STYLE` config block (canvas, hexes, font paths, px sizes, positions, margins).
- `SLIDES` list (line1, line2, optional cta, hero filename).
- Fit AI hero → 1080×1350 (cover-crop, anchored bottom).
- Optional top scrim toggle.
- Draw centered, wrapped line1 (SemiBold 76) + line2 (Regular 40) + optional cta.
- Deterministic: same input → identical output, every run, forever.

---

## 5. Status & open items
- ✅ Concept, look, voice, format, 66px one-line headlines, sage white-balance + scrim — locked.
- ✅ Bottle rule resolved: composite the **real** Canola PNG (pixel-perfect label) on cover + closer.
- ✅ v1 of all 8 slides built → `jivo-flip-carousel/slides/` (+ `contact-sheet.png`).
- ⏳ **Final legal/regulatory pass on copy** before posting (esp. slide 8 "good for your heart").
- ⏳ Optional: stitch slides into a fast-cut reel later (separate spec).
