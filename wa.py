
from PIL import Image, ImageDraw
import random

# Set the dimensions for a mobile wallpaper (1080x1920 is a common mobile resolution)
WIDTH, HEIGHT = 1080, 1920

# Create a new image with a white background
image = Image.new("RGB", (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(image)

# Define a list of colors for the shapes
colors = [
    "#FF6F61",  # Coral
    "#6B728E",  # Slate Blue
    "#FFD166",  # Yellow
    "#06D6A0",  # Teal
    "#118AB2",  # Blue
]

# Function to generate random coordinates within bounds
def random_point(max_x, max_y):
    return (random.randint(0, max_x), random.randint(0, max_y))

# Function to draw a random triangle
def draw_triangle(draw, color):
    points = [random_point(WIDTH, HEIGHT) for _ in range(3)]
    draw.polygon(points, fill=color, outline="black")

# Function to draw a random circle
def draw_circle(draw, color):
    x, y = random_point(WIDTH, HEIGHT)
    radius = random.randint(20, 100)
    draw.ellipse(
        (x - radius, y - radius, x + radius, y + radius),
        fill=color,
        outline="black"
    )

# Function to draw a random rectangle
def draw_rectangle(draw, color):
    x1, y1 = random_point(WIDTH, HEIGHT)
    x2, y2 = x1 + random.randint(50, 150), y1 + random.randint(50, 150)
    draw.rectangle((x1, y1, x2, y2), fill=color, outline="black")

# Draw 50 random shapes
for _ in range(50):
    shape_type = random.choice(["triangle", "circle", "rectangle"])
    color = random.choice(colors)
    
    if shape_type == "triangle":
        draw_triangle(draw, color)
    elif shape_type == "circle":
        draw_circle(draw, color)
    else:
        draw_rectangle(draw, color)

# Save the image
image.save("geometric_wallpaper.png")
print("Wallpaper saved as 'geometric_wallpaper.png'")
