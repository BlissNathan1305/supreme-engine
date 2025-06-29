
from PIL import Image, ImageDraw
import math  # Added import for math module

# Dimensions
WIDTH, HEIGHT = 1080, 1920
image = Image.new("RGB", (WIDTH, HEIGHT), "#000000")
draw = ImageDraw.Draw(image)

# Color
color = "#FF6F61"  # Coral

# Recursive Sierpinski triangle function
def draw_sierpinski(draw, x1, y1, x2, y2, x3, y3, level):
    if level == 0:
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=color, outline="#FFFFFF")
        return
    # Calculate midpoints
    mx1, my1 = (x1 + x2) / 2, (y1 + y2) / 2
    mx2, my2 = (x2 + x3) / 2, (y2 + y3) / 2
    mx3, my3 = (x1 + x3) / 2, (y1 + y3) / 2
    # Recursive calls
    draw_sierpinski(draw, x1, y1, mx1, my1, mx3, my3, level - 1)
    draw_sierpinski(draw, mx1, my1, x2, y2, mx2, my2, level - 1)
    draw_sierpinski(draw, mx3, my3, mx2, my2, x3, y3, level - 1)

# Draw large Sierpinski triangle centered
size = 800
offset_x, offset_y = (WIDTH - size) / 2, (HEIGHT - size) / 2
x1, y1 = offset_x, offset_y + size * math.sqrt(3) / 2
x2, y2 = offset_x + size / 2, offset_y
x3, y3 = offset_x + size, offset_y + size * math.sqrt(3) / 2
draw_sierpinski(draw, x1, y1, x2, y2, x3, y3, 4)

# Save
image.save("sierpinski_wallpaper.png")
print("Saved as 'sierpinski_wallpaper.png'")
