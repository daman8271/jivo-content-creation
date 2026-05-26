#!/usr/bin/env python3
"""Synthesize a beat-synced SFX layer for the Jivo Wheatgrass Mango reel (10s, no music).
Pure numpy synthesis -> 48k stereo WAV. Designed to the locked cut's hit-points:

  0.0-2.2  rising drone/tension + cap tick
  1.9-2.6  whoosh dive
  2.2-4.2  carbonation fizz
  3.5-4.78 rising swirl riser (tension into emerge)
  4.78     impact pop + splash
  4.8-5.5  bright sparkle (payoff)
  5.0-10   soft ambient bed + warm pad
  5.4,6.2  ice clinks
  6.95-7.6 tagline whoosh + sparkle
"""
import os
import wave
import numpy as np

SR = 48000
DUR = 10.0
N = int(SR * DUR)
buf = np.zeros((N, 2), dtype=np.float64)
rng = np.random.default_rng(7)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "outputs", "jivo-wheatgrass-mango-reel", "audio")
os.makedirs(OUT, exist_ok=True)


def add(sig, t0, pan=0.0):
    i = int(t0 * SR)
    n = len(sig)
    if i >= N:
        return
    n = min(n, N - i)
    l = sig[:n] * (0.5 * (1 - pan) + 0.5)
    r = sig[:n] * (0.5 * (1 + pan) + 0.5)
    # simpler constant-power-ish pan
    lg = np.cos((pan + 1) * np.pi / 4)
    rg = np.sin((pan + 1) * np.pi / 4)
    buf[i:i + n, 0] += sig[:n] * lg
    buf[i:i + n, 1] += sig[:n] * rg


def ar(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    if na:
        e[:na] = np.linspace(0, 1, na)
    if nr:
        e[-nr:] = np.linspace(1, 0, nr)
    return e


def smooth(x, w):
    if w < 2:
        return x
    k = np.ones(w) / w
    return np.convolve(x, k, mode="same")


def noise(n):
    return rng.uniform(-1, 1, n)


def tone(freq, n, amp=1.0):
    t = np.arange(n) / SR
    return amp * np.sin(2 * np.pi * freq * t)


# 1) Rising drone / tension (0 - 2.2s)
n = int(2.2 * SR)
t = np.arange(n) / SR
drone = (0.5 * np.sin(2 * np.pi * 55 * t) + 0.32 * np.sin(2 * np.pi * 82.5 * t)
         + 0.2 * np.sin(2 * np.pi * 110 * t))
shimmer = 0.12 * np.sin(2 * np.pi * (240 + 160 * (t / 2.2)) * t)
swell = (t / 2.2) ** 1.6
add((drone + shimmer) * swell * ar(n, 0.05, 0.25) * 0.22, 0.0)

# 2) Cap tick (~0.45s)
n = int(0.04 * SR)
tick = noise(n) - smooth(noise(n), 6)
add(tick * ar(n, 0.001, 0.035) * 0.18, 0.45)

# 3) Whoosh dive (1.85 - 2.6s)
n = int(0.75 * SR)
wh = smooth(noise(n), 22)
add(wh * ar(n, 0.35, 0.3) * 0.3, 1.85, pan=-0.1)

# 4) Carbonation fizz (2.2 - 4.2s)
n = int(2.0 * SR)
fz = noise(n) - smooth(noise(n), 4)          # crude highpass = crackle
crackle = smooth((rng.uniform(0, 1, n) > 0.7).astype(float), 3)
env = np.minimum(1.0, np.linspace(0, 1, n) * 3) * ar(n, 0.05, 0.5)
add(fz * crackle * env * 0.16, 2.2, pan=0.1)

# 5) Rising swirl riser (3.5 - 4.78s)
n = int(1.28 * SR)
t = np.arange(n) / SR
f = 180 + (1500 - 180) * (t / t[-1]) ** 1.3   # rising sweep
ph = 2 * np.pi * np.cumsum(f) / SR
riser = 0.6 * np.sin(ph) + 0.4 * (noise(n) - smooth(noise(n), 8))
rise_env = (t / t[-1]) ** 1.8
add(riser * rise_env * ar(n, 0.02, 0.02) * 0.26, 3.5)

# 6) Impact pop + splash (4.78s)
n = int(0.3 * SR)
thump = tone(70, n) * np.exp(-np.arange(n) / SR * 14)
add(thump * 0.34, 4.78)
n = int(0.22 * SR)
splat = smooth(noise(n), 5) * np.exp(-np.arange(n) / SR * 22)
add(splat * 0.3, 4.79)

# 7) Bright sparkle / payoff (4.85 - 5.5s)
for k, fr in enumerate([2200, 3000, 3700, 4600]):
    n = int(0.45 * SR)
    bell = tone(fr, n) * np.exp(-np.arange(n) / SR * 7)
    add(bell * 0.08, 4.85 + k * 0.07, pan=(-0.3 + 0.2 * k))

# 8) Ambient bed + warm pad (5.0 - 10s)
n = int(5.0 * SR)
amb = smooth(noise(n), 40) * 0.05 * ar(n, 0.6, 0.8)
add(amb, 5.0)
t = np.arange(n) / SR
pad = (np.sin(2 * np.pi * 196 * t) + np.sin(2 * np.pi * 261.6 * t)
       + np.sin(2 * np.pi * 329.6 * t)) / 3
padswell = np.minimum(1.0, t / 1.5) * ar(n, 0.1, 1.2)
add(pad * padswell * 0.06, 5.0)

# 9) Ice clinks (5.4, 6.2s)
for tt, fr, pn in [(5.4, 3200, 0.2), (6.2, 4200, -0.2)]:
    n = int(0.14 * SR)
    clink = (tone(fr, n) + 0.5 * tone(fr * 1.5, n)) * np.exp(-np.arange(n) / SR * 30)
    add(clink * 0.13, tt, pan=pn)

# 10) Tagline whoosh + sparkle (6.95 - 7.6s)
n = int(0.6 * SR)
tw = smooth(noise(n), 18) * ar(n, 0.3, 0.25)
add(tw * 0.16, 6.95, pan=0.1)
for k, fr in enumerate([2600, 3500]):
    n = int(0.4 * SR)
    add(tone(fr, n) * np.exp(-np.arange(n) / SR * 8) * 0.07, 7.1 + k * 0.08)

# Master: gentle global fade + normalize
g = np.ones(N)
g[:int(0.08 * SR)] = np.linspace(0, 1, int(0.08 * SR))
g[-int(0.5 * SR):] = np.linspace(1, 0, int(0.5 * SR))
buf *= g[:, None]
peak = np.max(np.abs(buf))
if peak > 0:
    buf *= 0.89 / peak

out = os.path.join(OUT, "mango-sfx.wav")
data = (buf * 32767).astype(np.int16)
with wave.open(out, "w") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(data.tobytes())
print("DONE ->", out)
