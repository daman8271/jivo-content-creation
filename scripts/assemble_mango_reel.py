#!/usr/bin/env python3
"""Assemble the Jivo Wheatgrass Mango "cola-clone" reel from 480p Seedance segments.
Normalize to one spec (480x854 @ 24fps, no audio), trim to the reference's beat timings,
concat losslessly. Audio dropped (clone is silent; add a track later).

Run: python3 scripts/assemble_mango_reel.py [out_name.mp4]
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "outputs", "jivo-wheatgrass-mango-reel")
SEG = os.path.join(OUTDIR, "segments")
DRAFT = os.path.join(OUTDIR, "drafts")
os.makedirs(DRAFT, exist_ok=True)

W, H, FPS = 480, 854, 24

# (filename, trim-to seconds) — beats matched to the 10s coke reference.
SEGMENTS = [
    ("S1-cap-dive-480p.mp4", 2.0),       # 0.0 - 2.0  cap macro -> dive into bottle
    ("S2-juice-rush-480p.mp4", 1.5),     # 2.0 - 3.5  travel through fizzing juice
    ("S2b-emerge-480p.mp4", 3.5),        # 3.5 - 7.0  rise + warm swirl vortex + emerge to table
    ("S4-hero-sunny-480p.mp4", 3.0),     # 7.0 - 10.0 sunny hero + tagline
]

VF = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
      f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},setsar=1,format=yuv420p")


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    out_name = sys.argv[1] if len(sys.argv) > 1 else "full-draft-v1-480p.mp4"
    missing = [f for f, _ in SEGMENTS if not os.path.exists(os.path.join(SEG, f))]
    if missing:
        sys.exit(f"Missing segments: {missing}")
    tmp = []
    for i, (fname, dur) in enumerate(SEGMENTS):
        dst = os.path.join(DRAFT, f"_norm_{i}.mp4")
        run(["ffmpeg", "-y", "-i", os.path.join(SEG, fname), "-t", f"{dur}",
             "-vf", VF, "-an", "-c:v", "libx264", "-preset", "veryfast",
             "-crf", "20", "-pix_fmt", "yuv420p", dst])
        tmp.append(dst)
    listfile = os.path.join(DRAFT, "_concat.txt")
    with open(listfile, "w") as f:
        for t in tmp:
            f.write(f"file '{t}'\n")
    out = os.path.join(DRAFT, out_name)
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listfile, "-c", "copy", out])
    for t in tmp:
        os.remove(t)
    os.remove(listfile)
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=noprint_wrappers=1:nokey=1", out],
                         capture_output=True, text=True).stdout.strip()
    print(f"DONE -> {out}  duration: {dur}s")


if __name__ == "__main__":
    main()
