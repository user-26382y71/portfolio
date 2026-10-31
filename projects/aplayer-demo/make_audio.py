"""生成一段五声音阶的小样，用于 APlayer 本地演示。
只用标准库，不装任何依赖。
"""
import math
import struct
import wave

RATE = 22050
DUR = 1.1          # 每个音持续秒数
NOTES = [440.00, 523.25, 587.33, 659.25, 783.99, 659.25, 587.33, 523.25]

frames = bytearray()
for f in NOTES:
    n = int(RATE * DUR)
    for i in range(n):
        t = i / RATE
        # 指数衰减包络，听起来像拨弦
        env = math.exp(-3.2 * t / DUR)
        v = 0.45 * env * math.sin(2 * math.pi * f * t)
        v += 0.15 * env * math.sin(2 * math.pi * f * 2 * t)   # 泛音
        frames += struct.pack("<h", int(max(-1.0, min(1.0, v)) * 32767))

with wave.open("demo.wav", "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(RATE)
    w.writeframes(bytes(frames))

print("demo.wav generated:", len(frames) // 2 / RATE, "seconds")
