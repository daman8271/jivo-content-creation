#!/usr/bin/env python3
"""Assemble the Jivo Extra Light "flying reel" clone from 480p Seedance segments.

Normalizes every segment to one spec (480x854 @ 24fps, no audio), trims each to its
target beat duration (mirroring the reference's pacing), then concatenates losslessly.
Audio is intentionally dropped (per brief).

Run:  python3 scripts/assemble_flying_reel.py [output_name.mp4]
"""
import os
import subprocess
import sys

# Project root = parent of this script's dir (robust to spaces in path).
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "outputs", "jivo-extra-light-flying-reel")
SEG = os.path.join(OUTDIR, "segments")
DRAFT = os.path.join(OUTDIR, "drafts")
os.makedirs(DRAFT, exist_ok=True)

W, H, FPS = 480, 854, 24

# (filename in segments/, trim-to seconds) — beat timings matched to the reference.
SEGMENTS = [
    ("S1-sensory-dive-480p.mp4", 4.5),   # 0.0 - 4.5  macro dive -> label
    ("S2-olivebed-reveal-480p.mp4", 4.5),  # 4.5 - 9.0  olive-bed reveal + flying
    ("S3-drizzle-salad-480p.mp4", 3.0),  # 9.0 - 12.0 oil drizzle over salad
    ("S4-hero-480p.mp4", 3.0),           # 12.0 - 15.0 hero + headline
]

VF = (
    f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
    f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},setsar=1,format=yuv420p"
)


def run(cmd):
    print("+", " ".join(cmd[:6]), "...")
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    out_name = sys.argv[1] if len(sys.argv) > 1 else "full-draft-v1-480p.mp4"
    tmp = []
    missing = [f for f, _ in SEGMENTS if not os.path.exists(os.path.join(SEG, f))]
    if missing:
        sys.exit(f"Missing segments: {missing}")

    for i, (fname, dur) in enumerate(SEGMENTS):
        src = os.path.join(SEG, fname)
        dst = os.path.join(DRAFT, f"_norm_{i}.mp4")
        run([
            "ffmpeg", "-y", "-i", src, "-t", f"{dur}",
            "-vf", VF, "-an",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
            "-pix_fmt", "yuv420p", dst,
        ])
        tmp.append(dst)

    listfile = os.path.join(DRAFT, "_concat.txt")
    with open(listfile, "w") as f:
        for t in tmp:
            f.write(f"file '{t}'\n")

    out = os.path.join(DRAFT, out_name)
    run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listfile,
        "-c", "copy", out,
    ])

    # cleanup temps
    for t in tmp:
        os.remove(t)
    os.remove(listfile)

    dur = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", out],
        capture_output=True, text=True,
    ).stdout.strip()
    print(f"\nDONE -> {out}\nduration: {dur}s")


if __name__ == "__main__":
    main()
