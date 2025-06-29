
from PIL import Image, ImageDraw
import math

# Set the dimensions for a mobile wallpaper (1080x1920)
WIDTH, HEIGHT = 1080, 1920

# Create a new image with a dark background
image = Image.new("RGB", (WIDTH, HEIGHT), "#1C2526")
draw = ImageDraw.Draw(image)

# Hexagon parameters
HEX_SIZE = 50  # Radius of each hexagon (distance from center to vertex)
HEX_SPACING = HEX_SIZE * 1.5  # Vertical spacing between hexagons
HEX_WIDTH = HEX_SIZE * math.sqrt(3)  # Width of a hexagon (side to side)

# Function to generate a gradient color based on position
def get_gradient_color(x, y):
    # Gradient from blue (#118AB2) to coral (#FF6F61) based on y-position
    t = y / HEIGHT  # Normalize y to [0, 1]
    start_color = (17, 138, 178)  # RGB for #118AB2
    end_color = (255, 111, 97)    # RGB for #FF6F61
    r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
    return (r, g, b)

# Function to draw a hexagon at (center_x, center_y)
def draw_hexagon(draw, center_x, center_y, size, color):
    points = []
    for i in range(6):
        angle = math.pi / 3 * i  # 60 degrees in radians
        x = center_x + size * math.cos(angle)
        y = center_y + size * math.sin(angle)
        points.append((x, y))
    draw.polygon(points, fill=color, outline="#FFFFFF")

# Draw a hexagonal grid
for row in range(-1, int(HEIGHT / HEX_SPACING) + 1):
    for col in range(-1, int(WIDTH / HEX_WIDTH) + 1):
        # Calculate center of hexagon
        x = col * HEX_WIDTH
        y = row * HEX_SPACING
        if row % 2 == 1:  # Offset every other row for honeycomb pattern
            x += HEX_WIDTH / 2
        # Ensure hexagon is within bounds
        if 0 <= x <= WIDTH and 0 <= y <= HEIGHT:
            color = get_gradient_color(x, y)
            draw_hexagon(draw, x, y, HEX_SIZE, color)

# Save the image
image.save("hexagonal_wallpaper.png")
print("Wallpaper saved as 'hexagonal_wallpaper.png'")
