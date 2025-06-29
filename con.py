
from PIL import Image, ImageDraw
import random

# Dimensions for mobile
WIDTH, HEIGHT = 1080, 1920
image = Image.new("RGB", (WIDTH, HEIGHT), "#1C2526")
draw = ImageDraw.Draw(image)

# Gradient color function
def get_gradient_color(t):
    start_color = (255, 111, 97)  # Coral
    end_color = (17, 138, 178)    # Blue
    r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
    return (r, g, b)

# Draw 10 sets of concentric circles
for _ in range(10):
    center_x, center_y = random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)
    max_radius = random.randint(50, 150)
    for r in range(10, max_radius, 10):
        t = r / max_radius  # Normalize for gradient
        color = get_gradient_color(t)
        draw.ellipse(
            (center_x - r, center_y - r, center_x + r, center_y + r),
            fill=color,
            outline="#FFFFFF"
        )

# Save
image.save("concentric_circles_wallpaper.png")
print("Saved as 'concentric_circles_wallpaper.png'")
