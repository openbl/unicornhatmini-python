#!/usr/bin/env python3

import time
from colorsys import hsv_to_rgb
from minicorn import Minicorn


print("""Minicorn: fps.py

Attempts to refresh the Minicorn display as fast as possible
with a horizontal rainbow and displays the frames per second
refresh rate.

Press Ctrl+C to exit!

""")

minicorn = Minicorn()
minicorn.set_brightness(0.1)
minicorn.set_rotation(0)
width, height = minicorn.get_shape()

frames = 0
t_start = time.time()

t_report = time.time()
report_freq = 5.0

print("Please wait...")

while True:
    for y in range(height):
        for x in range(width):
            hue = (time.time() / 10.0) + (x / float(width * 2))
            r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
            minicorn.set_pixel(x, y, r, g, b)
    minicorn.show()

    frames += 1

    if time.time() - t_report > report_freq:
        t_report = time.time()
        t = time.time() - t_start
        fps = frames / t
        print("FPS: {:05.3f} ({} frames in {:.1f} seconds)".format(fps, frames, t))