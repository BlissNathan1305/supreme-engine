
from PIL import Image, ImageDraw
import math
import random
import colorsys

# Set dimensions for HD mobile (1080x1920)
WIDTH = 1080
HEIGHT = 1920

# Create a new image with gradient background
img = Image.new('RGB', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

# Create a cosmic gradient background
for y in range(HEIGHT):
    # Interpolate between deep blue and purple
    r = int(10 + 100 * (y/HEIGHT))
    g = int(20 + 50 * (y/HEIGHT))
    b = int(100 + 100 * (y/HEIGHT))
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

# Function to draw a 3D sphere with proper lighting
def draw_sphere(draw, center, radius, color):
    x0, y0 = center
    light_dir = (0.5, 0.5, -0.707)  # Light coming from top-left
    
    for y in range(int(y0 - radius), int(y0 + radius) + 1):
        if y < 0 or y >= HEIGHT:
            continue
            
        chord_length = math.sqrt(radius**2 - (y - y0)**2)
        
        for x in range(int(x0 - chord_length), int(x0 + chord_length) + 1):
            if x < 0 or x >= WIDTH:
                continue
                
            # Calculate normal vector
            nx = (x - x0) / radius
            ny = (y - y0) / radius
            nz_squared = 1 - nx*nx - ny*ny
            
            # Skip if outside the sphere
            if nz_squared <= 0:
                continue
                
            nz = math.sqrt(nz_squared)
            
            # Calculate lighting
            light = max(0.2, nx*light_dir[0] + ny*light_dir[1] + nz*light_dir[2])
            
            # Apply lighting to color
            r = int(color[0] * light)
            g = int(color[1] * light)
            b = int(color[2] * light)
            
            # Add specular highlight
            if light > 0.9:
                r = min(255, r + 50)
                g = min(255, g + 50)
                b = min(255, b + 50)
                
            draw.point((x, y), fill=(r, g, b))

# Draw main 3D spheres
for _ in range(5):
    x = random.randint(200, WIDTH-200)
    y = random.randint(200, HEIGHT-200)
    radius = random.randint(80, 180)
    
    # Generate vibrant color
    h = random.uniform(0.6, 0.9)  # Blues and purples
    s = 0.8 + random.random() * 0.2
    v = 0.7 + random.random() * 0.3
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v)]
    
    draw_sphere(draw, (x, y), radius, (r, g, b))

# Add glowing particles
for _ in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(1, 4)
    brightness = random.randint(150, 255)
    draw.ellipse([x-size, y-size, x+size, y+size], fill=(brightness, brightness, brightness))

# Add subtle lens flare effect
flare_positions = [(WIDTH//4, HEIGHT//4), (WIDTH*3//4, HEIGHT//3)]
for x, y in flare_positions:
    for size in range(50, 10, -10):
        alpha = size / 50
        color = (int(255*alpha), int(255*alpha), int(200*alpha))
        draw.ellipse([x-size, y-size, x+size, y+size], outline=color, width=2)

# Save the final image
img.save('3d_mobile_wallpaper.jpg', quality=95)
print("3D mobile wallpaper generated successfully!")
