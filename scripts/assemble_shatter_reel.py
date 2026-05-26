#!/usr/bin/env python3
"""Assemble the Jivo Wheatgrass Mango ice-shatter reel (clone of deeptest.mp4 / UPTIME).
Normalize to 480x854 @ 24fps, trim to beats, concat. Last beat is a STATIC logo card
(image held). Audio dropped (added separately). Total ~11.7s.

Run: python3 scripts/assemble_shatter_reel.py [out_name.mp4]
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "outputs", "jivo-wheatgrass-shatter-reel")
SEG = os.path.join(OUTDIR, "segments")
KF = os.path.join(OUTDIR, "keyframes")
DRAFT = os.path.join(OUTDIR, "drafts")
os.makedirs(DRAFT, exist_ok=True)
W, H, FPS = 480, 854, 24

# (path, dur, is_image, pad_color)
SEGMENTS = [
    (os.path.join(SEG, "S1-shatter-480p.mp4"), 2.0, False, "black"),     # 0.0-2.0 ice -> shatter reveal
    (os.path.join(SEG, "S2-label-track-480p.mp4"), 3.2, False, "black"), # 2.0-5.2 reveal -> label track up
    (os.path.join(SEG, "S3-pull-hero-480p.mp4"), 1.8, False, "black"),   # 5.2-7.0 pull to single hero
    (os.path.join(SEG, "S4-lineup-480p.mp4"), 2.0, False, "black"),      # 7.0-9.0 pull to 3-bottle lineup
    (os.path.join(KF, "KF6-logo.png"), 2.7, True, "white"),              # 9.0-11.7 logo end card (static)
]


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def vf(pad):
    return (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
            f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:{pad},fps={FPS},setsar=1,format=yuv420p")


def main():
    out_name = sys.argv[1] if len(sys.argv) > 1 else "full-draft-v1-480p.mp4"
    missing = [p for p, _, _, _ in SEGMENTS if not os.path.exists(p)]
    if missing:
        sys.exit(f"Missing: {missing}")
    tmp = []
    for i, (path, dur, is_img, pad) in enumerate(SEGMENTS):
        dst = os.path.join(DRAFT, f"_norm_{i}.mp4")
        if is_img:
            cmd = ["ffmpeg", "-y", "-loop", "1", "-t", f"{dur}", "-i", path,
                   "-vf", vf(pad), "-an", "-c:v", "libx264", "-preset", "veryfast",
                   "-crf", "20", "-pix_fmt", "yuv420p", dst]
        else:
            cmd = ["ffmpeg", "-y", "-i", path, "-t", f"{dur}",
                   "-vf", vf(pad), "-an", "-c:v", "libx264", "-preset", "veryfast",
                   "-crf", "20", "-pix_fmt", "yuv420p", dst]
        run(cmd)
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
