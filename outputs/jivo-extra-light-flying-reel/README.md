# Jivo Extra Light Olive Oil — "Flying Reel"

A 1:1 recreation of the reference `copy the video.mp4` (Samuel Adams American Light, 15s 9:16)
with **Jivo Extra Light Olive Oil** swapped in as the hero and all ingredients contextually
re-mapped to the olive-oil world. Built with the segmented keyframe → i2v → stitch pipeline.

## ▶️ Deliverable
- **`final/jivo-extra-light-flying-reel-FINAL-1080p.mp4`** — 1080×1920, 24fps, 15.0s, silent.
- `drafts/full-draft-v2-480p.mp4` — approved 480p cut (with text).
- `drafts/full-draft-v1-480p.mp4` — 480p cut, no text.

Silent by design (per brief) — drop a music track on top.

## Reference → Jivo translation
| Beat | Reference | Jivo version |
|---|---|---|
| 0–4.5s | macro cap droplet → carbonation bubbles → wet label | macro Jivo cap + oil drop → **golden oil bubbles** → wet JIVO label |
| 4.5–9s | reveal: bottle in barley + hops, flying | reveal: bottle in **olives + olive leaves**, flying; text **"FROM THE FARMS OF SPAIN"** |
| 9–12s | beer poured into glass | golden oil **drizzled over a fresh salad** |
| 12–15s | hero + "AMERICA'S MOST Premium LIGHT BEER" | hero (bottle + salad) + **"INDIA'S MOST PREMIUM EXTRA LIGHT OLIVE OIL"** |

## Pipeline (how to regenerate / extend)
1. **Keyframes** (`keyframes/`): Nano Banana Pro (`nano_banana_pro`) with the real packshot
   `outputs/copy-reel-recreate/jivo-extra-light-packshot.png` as the `image` reference → pixel-faithful
   label, never AI-redrawn. JSON prompts (json-prompter-image).
2. **Motion clips** (`segments/`): Seedance 2.0 (`seedance_2_0`), 480p, start (+end) keyframes + packshot
   as identity reference. Front-locked bottle = label never drifts. JSON prompts (json-prompter-video).
   Decline the "IN THE DARK" preset (`declined_preset_id`) to generate literally.
3. **Assemble**: `scripts/assemble_flying_reel.py` — normalize to 480×854/24fps, trim to beat timings, concat.
4. **Text**: `scripts/overlay_flying_reel_text.py` — Poppins headlines rendered + burned at the beat timestamps.
5. **Upscale**: ffmpeg lanczos + light unsharp → 1080×1920 (preserves the approved motion; no AI re-roll).

## Notes / lessons
- **Cost driver = 2K keyframe images (~100 cr each), not the 480p Seedance clips (~15 cr each).**
  Use 1k keyframes while iterating; reserve 2k for locked frames.
- Higgsfield (this MCP) has **no standalone video upscaler** — finalize via ffmpeg resolution pass, or
  re-render segments at 1080p (fresh motion roll) if true AI detail is required.
- Reference watched/compared with claude-video-vision (local, free).
