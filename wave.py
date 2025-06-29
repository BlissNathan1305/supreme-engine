
from PIL import Image, ImageDraw
import math

# Dimensions
WIDTH, HEIGHT = 1080, 1920
image = Image.new("RGB", (WIDTH, HEIGHT), "#1C2526")
draw = ImageDraw.Draw(image)

# Gradient color function
def get_gradient_color(y):
    t = y / HEIGHT
    start_color = (75, 0, 130)  # Indigo
    end_color = (255, 215, 0)    # Gold
    r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
    return (r, g, b)

# Draw waves
for y in range(0, HEIGHT, 10):
    points = []
    for x in range(WIDTH):
        wave_height = 50 * math.sin(x * 0.02 + y * 0.05)
        points.append((x, y + wave_height))
    for i in range(len(points) - 1):
        draw.line(
            [points[i], points[i+1]],
            fill=get_gradient_color(y),
            width=5
        )

# Save
image.save("wave_wallpaper.png")
print("SavedਮSaved as 'wave_wallpaper.png'")
