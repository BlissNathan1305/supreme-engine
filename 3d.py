
from PIL import Image, ImageDraw
import math
import random
import colorsys

# Set the dimensions for HD mobile (1080x1920)
WIDTH = 1080
HEIGHT = 1920

# Create a new image with black background
img = Image.new('RGB', (WIDTH, HEIGHT), color='black')
draw = ImageDraw.Draw(img)

# Generate a smooth gradient background
def create_gradient(width, height, color1, color2):
    for y in range(height):
        # Interpolate between color1 and color2 based on y position
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

# Choose two vibrant colors for the gradient
color1 = (random.randint(0, 100), random.randint(0, 100), random.randint(100, 255))
color2 = (random.randint(100, 255), random.randint(0, 100), random.randint(0, 100))
create_gradient(WIDTH, HEIGHT, color1, color2)

# Function to draw a 3D sphere (fixed version)
def draw_sphere(draw, center, radius, color, light_dir=(1, 1, -1)):
    x0, y0 = center
    # Normalize light direction
    light_dir = [x / math.sqrt(sum(x*x for x in light_dir)) for x in light_dir]
    
    for y in range(int(y0 - radius), int(y0 + radius) + 1):
        if y < 0 or y >= HEIGHT:
            continue
            
        chord_length = math.sqrt(radius**2 - (y - y0)**2)
        
        for x in range(int(x0 - chord_length), int(x0 + chord_length) + 1):
            if x < 0 or x >= WIDTH:
                continue
                
            # Calculate normal vector components
            nx = (x - x0) / radius
            ny = (y - y0) / radius
            nz_squared = 1 - nx*nx - ny*ny
            
            # Skip if outside the sphere
            if nz_squared <= 0:
                continue
                
            nz = math.sqrt(nz_squared)
            
            # Calculate lighting (dot product of normal and light direction)
            light = max(0, nx*light_dir[0] + ny*light_dir[1] + nz*light_dir[2])
            
            # Apply lighting to color
            r = int(color[0] * (0.3 + 0.7*light))
            g = int(color[1] * (0.3 + 0.7*light))
            b = int(color[2] * (0.3 + 0.7*light))
            
            # Add some specular highlight
            if light > 0.8:
                r = min(255, r + 50)
                g = min(255, g + 50)
                b = min(255, b + 50)
                
            draw.point((x, y), fill=(r, g, b))

# Draw multiple 3D spheres with random positions and colors
for _ in range(8):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    radius = random.randint(50, 200)
    
    # Generate a random vibrant color
    h = random.random()
    s = 0.7 + random.random() * 0.3
    v = 0.7 + random.random() * 0.3
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v)]
    
    draw_sphere(draw, (x, y), radius, (r, g, b))

# Add some glow effect by drawing blurred circles
for _ in range(15):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    radius = random.randint(50, 300)
    h = random.random()
    s = 0.3 + random.random() * 0.2
    v = 0.8 + random.random() * 0.2
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v)]
    
    for r2 in range(radius, radius - 20, -1):
        alpha = int(30 * (r2 / radius))
        color_with_alpha = (r, g, b, alpha)
        draw.ellipse([x - r2, y - r2, x + r2, y + r2], 
                    outline=color_with_alpha, 
                    width=2)

# Add some abstract lines for depth
for _ in range(5):
    x1 = random.randint(0, WIDTH)
    y1 = random.randint(0, HEIGHT)
    x2 = random.randint(0, WIDTH)
    y2 = random.randint(0, HEIGHT)
    width = random.randint(1, 5)
    h = random.random()
    s = 0.7 + random.random() * 0.3
    v = 0.7 + random.random() * 0.3
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v)]
    draw.line([x1, y1, x2, y2], fill=(r, g, b), width=width)

# Save the image
img.save('3d_wallpaper.jpg', quality=95)
print("3D wallpaper generated successfully!")
