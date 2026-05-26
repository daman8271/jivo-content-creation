# Jivo Extra Light Olive Oil — "Flying Reel" (clone of `copy the video.mp4`)

Reference: Samuel Adams American Light, 15.0s, 9:16, ~24fps, 720x1280. Continuous piece with quick
match-cuts at ~4.5s and ~9s. **Audio ignored** (per user). Iterate at **480p**, upscale once locked.

Product: **Jivo Extra Light Olive Oil**, 1L clear PET bottle, golden-yellow oil, navy cap, JIVO smile
logo. Clean cutout asset: `outputs/copy-reel-recreate/jivo-extra-light-packshot.png` (real label →
composite, never AI-redraw).

## Locked creative decisions (Checkpoint 1, approved)
- **Beats 3 & 4 → "drizzle over food"**: golden oil drizzles over a fresh dish; hero = Jivo bottle + the
  dish. (Exact dish chosen at S3/S4 stage.)
- **Pilot = S2 (olive-bed reveal)**.
- Text overlays rendered in **post** (PIL, deterministic) — never AI-typed.

## Reference breakdown → Olive-oil translation
| # | Time | Reference | Jivo version |
|---|------|-----------|--------------|
| 1a | 0–1s | Macro neck + crown cap, droplet, amber bokeh | Macro Jivo cap/spout, golden oil droplet, warm bokeh |
| 1b | 1–2s | Carbonation bubbles rising in golden beer | Golden oil droplets/bubbles suspended, light refraction |
| 1c | 2–3s | Golden bubble burst (radial blur) | Golden oil swirl/burst (radial blur) |
| 1d | 3–4.5s | Track across wet "SAMUEL ADAMS" label | Track across glossy "JIVO EXTRA LIGHT OLIVE OIL" label |
| 2 | 4.5–9s | REVEAL: bottle in barley + green hops bed, flying | REVEAL: bottle in green & dark olives + olive leaves/branches bed, flying |
| txt | 7–9s | "American INGREDIENTS" | "FROM THE FARMS OF SPAIN" |
| 3 | 9–12s | Beer poured into branded glass, foam | Golden oil drizzled over a fresh dish |
| 4 | 12–15s | Hero: bottle + foamy glass, "AMERICA'S MOST Premium LIGHT BEER" | Hero: Jivo bottle + dish, "INDIA'S MOST PREMIUM EXTRA LIGHT OLIVE OIL" |

## Reveal mechanics (S2, observed 4.5–9s)
Bottle stays **static, centered, upright, front-facing** (label always legible). Camera ~overhead.
Snap-reveal at ~5s, then **ingredients fly/tumble** around the bottle and settle. Text fades in ~7–8s.
→ Front-lock the Jivo bottle; put all motion into the flying olives + leaves.

## Segmentation (shared boundary frames)
| Seg | Span | Content | Anchors | Model |
|-----|------|---------|---------|-------|
| S1 | 0–4.5s | Sensory dive (cap→oil→burst→label) | A0 → (A0.5 burst) → A1 label | Seedance 2.0 (may split) |
| S2 | 4.5–9s | Olive-bed reveal + flying ingredients (PILOT) | A1 → A2 | Seedance 2.0 (Kling 3.0 backup) |
| S3 | 9–12s | Oil drizzle over food | A2/cut → A3 → A4 | Kling 3.0 |
| S4 | 12–15s | Hero beauty + headline | A4 → A5 | Seedance 2.0 |

Generate at 480p; cap 3 iterations/segment; verify each vs reference beat with claude-video-vision.
Higgsfield balance at start: 4,111 credits (Ultra).
