#!/usr/bin/env python3
"""Synthesize a beat-synced SFX layer for the Jivo ice-shatter reel (~11.7s, no music).
Pure numpy -> 48k stereo WAV. Designed to the locked cut:

  0.0-1.75 cold ice ambience + accelerating ice CRACKLE (tension build)
  1.75     SHATTER: smash + crack cluster + low boom + whoosh   <- the hit
  1.9-3.2  debris shimmer + riser into the label
  3.0-11   warm premium pad bed
  5.2      hero settle ding
  6.9-7.4  lineup reveal whoosh + bell
  9.05     LOGO STING (bright bell cluster) on the end card
"""
import os
import wave
import numpy as np

SR = 48000
DUR = 11.7
N = int(SR * DUR)
buf = np.zeros((N, 2), dtype=np.float64)
rng = np.random.default_rng(11)
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "outputs", "jivo-wheatgrass-shatter-reel", "audio")
os.makedirs(OUT, exist_ok=True)


def add(sig, t0, pan=0.0):
    i = int(t0 * SR)
    if i >= N:
        return
    n = min(len(sig), N - i)
    lg, rg = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
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
    return np.convolve(x, np.ones(w) / w, mode="same") if w >= 2 else x


def noise(n):
    return rng.uniform(-1, 1, n)


def tone(f, n, amp=1.0):
    return amp * np.sin(2 * np.pi * f * np.arange(n) / SR)


def tick(dur, amp):
    n = int(dur * SR)
    s = noise(n)
    s = s - smooth(s, 5)
    return s * np.exp(-np.arange(n) / SR * 60) * amp


# 1) cold ice ambience (0-1.8)
n = int(1.8 * SR)
add(smooth(noise(n), 30) * 0.045 * ar(n, 0.3, 0.3), 0.0)

# 2) accelerating ice crackle build (0.3 - 1.72)
t = 0.3
while t < 1.72:
    amp = 0.05 + 0.22 * ((t - 0.3) / 1.42)
    add(tick(0.012, amp), t, pan=rng.uniform(-0.5, 0.5))
    t += rng.uniform(0.05, 0.16) * (1.72 - t + 0.2)  # accelerate toward shatter

# 3) SHATTER at 1.75
n = int(0.45 * SR)
smash = (noise(n) - smooth(noise(n), 4)) * np.exp(-np.arange(n) / SR * 9)
add(smash * 0.4, 1.75)
for k in range(10):  # crack cluster
    add(tick(0.02, 0.3), 1.75 + rng.uniform(0, 0.18), pan=rng.uniform(-0.7, 0.7))
add(tone(50, int(0.45 * SR)) * np.exp(-np.arange(int(0.45 * SR)) / SR * 11) * 0.36, 1.75)  # boom
n = int(0.55 * SR)
add(smooth(noise(n), 16) * ar(n, 0.04, 0.4) * 0.26, 1.78)  # whoosh

# 4) debris shimmer + riser (1.9 - 3.2)
for k in range(14):
    fr = rng.uniform(2200, 5200)
    nb = int(0.3 * SR)
    add(tone(fr, nb) * np.exp(-np.arange(nb) / SR * 9) * 0.05, 1.9 + rng.uniform(0, 1.0), pan=rng.uniform(-0.6, 0.6))
n = int(0.6 * SR)
tt = np.arange(n) / SR
f = 320 + 760 * (tt / tt[-1])
add(0.5 * np.sin(2 * np.pi * np.cumsum(f) / SR) * (tt / tt[-1]) ** 1.5 * 0.12, 2.6)

# 5) warm premium pad bed (3.0 - 11.0)
n = int(8.0 * SR)
tt = np.arange(n) / SR
pad = (np.sin(2 * np.pi * 196 * tt) + np.sin(2 * np.pi * 261.6 * tt) + np.sin(2 * np.pi * 392 * tt)) / 3
add(pad * np.minimum(1.0, tt / 1.5) * ar(n, 0.1, 1.5) * 0.05, 3.0)

# 6) hero settle ding (5.2)
nb = int(0.6 * SR)
add((tone(2500, nb) + 0.4 * tone(3750, nb)) * np.exp(-np.arange(nb) / SR * 6) * 0.09, 5.2)

# 7) lineup reveal whoosh + bell (6.9 - 7.4)
n = int(0.55 * SR)
add(smooth(noise(n), 18) * ar(n, 0.3, 0.25) * 0.13, 6.9, pan=0.1)
add((tone(2000, int(0.5 * SR))) * np.exp(-np.arange(int(0.5 * SR)) / SR * 7) * 0.07, 7.15)

# 8) LOGO STING (9.05) bright bell cluster + soft sub
for k, fr in enumerate([1500, 2000, 3000, 4000]):
    nb = int(1.2 * SR)
    add(tone(fr, nb) * np.exp(-np.arange(nb) / SR * 3.2) * 0.085, 9.05 + k * 0.015)
add(tone(80, int(0.8 * SR)) * np.exp(-np.arange(int(0.8 * SR)) / SR * 6) * 0.18, 9.05)

# master fade + normalize
g = np.ones(N)
g[:int(0.05 * SR)] = np.linspace(0, 1, int(0.05 * SR))
g[-int(0.6 * SR):] = np.linspace(1, 0, int(0.6 * SR))
buf *= g[:, None]
pk = np.max(np.abs(buf))
if pk > 0:
    buf *= 0.89 / pk
out = os.path.join(OUT, "shatter-sfx.wav")
with wave.open(out, "w") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((buf * 32767).astype(np.int16).tobytes())
print("DONE ->", out)
