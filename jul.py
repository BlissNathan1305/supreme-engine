
from PIL import Image, ImageDraw
import numpy as np
import colorsys
import os

# Mobile resolution
WIDTH, HEIGHT = 1080, 1920
MAX_ITER = 300

# Create output directory
os.makedirs("julia_wallpapers", exist_ok=True)

# Generate 10 different Julia sets with varying constants
constants = [
    complex(-0.7, 0.27015),
    complex(0.355, 0.355),
    complex(-0.4, 0.6),
    complex(0.37, -0.1),
    complex(-0.835, -0.2321),
    complex(0.45, 0.1428),
    complex(-0.8, 0.156),
    complex(0.285, 0.01),
    complex(-0.70176, -0.3842),
    complex(0.3, 0.5),
]

def generate_julia(c, filename):
    img = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = img.load()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            zx = 3.0 * (x - WIDTH / 2) / (WIDTH / 2)
            zy = 2.0 * (y - HEIGHT / 2) / (HEIGHT / 2)
            z = complex(zx, zy)

            iteration = 0
            while abs(z) < 4 and iteration < MAX_ITER:
                z = z * z + c
                iteration += 1

            hue = int(255 * iteration / MAX_ITER)
            saturation = 255
            value = 255 if iteration < MAX_ITER else 0

            r, g, b = [int(x * 255) for x in colorsys.hsv_to_rgb(hue / 255.0, saturation / 255.0, value / 255.0)]
            pixels[x, y] = (r, g, b)

    img.save(f"julia_wallpapers/{filename}.png", "PNG")

# Generate 10 images
for i, c in enumerate(constants):
    print(f"Generating wallpaper {i+1}...")
    generate_julia(c, f"julia_set_{i+1}")

print("✅ Done. Check the 'julia_wallpapers' folder.")
