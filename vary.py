
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import random
import colorsys
import os

# Create output directory
os.makedirs('wallpapers', exist_ok=True)

# Dimensions for HD mobile
WIDTH = 1080
HEIGHT = 1920

# Default font for text (used in Digital Rain)
font = ImageFont.load_default()

def generate_wallpaper(design_number):
    img = Image.new('RGB', (WIDTH, HEIGHT), color='black')
    draw = ImageDraw.Draw(img)
    
    # Select design
    designs = {
        1: create_cosmic_nebula,
        2: create_geometric_prisms,
        3: create_liquid_metal,
        4: create_cyber_grid,
        5: create_organic_bubbles,
        6: create_sunset_mountains,
        7: create_digital_rain,
        8: create_crystal_cave,
        9: create_abstract_waves,
        10: create_fractal_universe
    }
    
    if design_number in designs:
        designs[design_number](draw)
    else:
        print(f"Design number {design_number} not found!")
        return
    
    # Apply effects and save
    img = apply_final_effects(img, design_number)
    img.save(f'wallpapers/wallpaper_{design_number}.jpg', quality=95)

# Design 1: Cosmic Nebula
def create_cosmic_nebula(draw):
    # Starfield
    for _ in range(1000):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(1, 3)
        brightness = random.randint(200, 255)
        draw.ellipse([x-size, y-size, x+size, y+size], fill=(brightness, brightness, brightness))
    
    # Nebula clouds
    for _ in range(10):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(200, 500)
        h = random.random()
        r, g, b = colorsys.hsv_to_rgb(h, 0.7, 0.8)
        for r2 in range(radius, 0, -20):
            alpha = r2 / radius
            color = (int(r*255*alpha), int(g*255*alpha), int(b*255*alpha))
            draw.ellipse([x-r2, y-r2, x+r2, y+r2], outline=color, width=3)

# Design 2: Geometric Prisms
def create_geometric_prisms(draw):
    for i in range(HEIGHT):
        r = int(50 + 100 * abs(math.sin(i * 0.01)))
        g = int(50 + 100 * abs(math.sin(i * 0.015 + 1)))
        b = int(50 + 100 * abs(math.sin(i * 0.02 + 2)))
        draw.line([(0, i), (WIDTH, i)], fill=(r, g, b))
    
    for _ in range(7):
        size = random.randint(150, 300)
        x = random.randint(size, WIDTH-size)
        y = random.randint(size, HEIGHT-size)
        points = []
        for j in range(3):
            angle = j * (2 * math.pi / 3) + random.uniform(-0.2, 0.2)
            points.append((x + size * math.cos(angle), y + size * math.sin(angle)))
        h = random.random()
        r, g, b = colorsys.hsv_to_rgb(h, 0.8, 0.8)
        draw.polygon(points, fill=(int(r*255), int(g*255), int(b*255)), outline=(255, 255, 255))

# Design 3: Liquid Metal
def create_liquid_metal(draw):
    for i in range(HEIGHT):
        shade = int(50 + 150 * abs(math.sin(i * 0.005)))
        draw.line([(0, i), (WIDTH, i)], fill=(shade, shade, shade))
    
    for _ in range(5):
        x, y = random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)
        radius = random.randint(80, 200)
        for r in range(radius, 0, -5):
            shade = min(255, 150 + int(100 * (r/radius)))
            draw.ellipse([x-r, y-r, x+r, y+r], outline=(shade, shade, shade), width=2)

# Design 4: Cyber Grid
def create_cyber_grid(draw):
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=(10, 20, 30))
    
    for i in range(0, WIDTH, 50):
        draw.line([(i, 0), (i, HEIGHT)], fill=(0, 50, 100), width=1)
    for i in range(0, HEIGHT, 50):
        draw.line([(0, i), (WIDTH, i)], fill=(0, 50, 100), width=1)
    
    for _ in range(20):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        r, g, b = colorsys.hsv_to_rgb(random.uniform(0.5, 0.7), 0.9, 0.9)
        draw.ellipse([x-10, y-10, x+10, y+10], fill=(int(r*255), int(g*255), int(b*255)))

# Design 5: Organic Bubbles
def create_organic_bubbles(draw):
    for i in range(HEIGHT):
        r = int(50 + 50 * math.sin(i * 0.01))
        g = int(100 + 50 * math.sin(i * 0.015))
        b = int(150 + 50 * math.sin(i * 0.02))
        draw.line([(0, i), (WIDTH, i)], fill=(r, g, b))
    
    for _ in range(15):
        x, y = random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)
        radius = random.randint(40, 150)
        h = random.uniform(0.4, 0.6)
        r, g, b = colorsys.hsv_to_rgb(h, 0.4, 0.9)
        for r2 in range(radius, 0, -5):
            alpha = 0.2 + 0.8 * (r2/radius)
            color = (int(r*255*alpha), int(g*255*alpha), int(b*255*alpha))
            draw.ellipse([x-r2, y-r2, x+r2, y+r2], outline=color, width=2)

# Design 6: Sunset Mountains
def create_sunset_mountains(draw):
    for i in range(HEIGHT):
        r = int(200 - 150 * (i/HEIGHT))
        g = int(100 - 80 * (i/HEIGHT))
        b = int(50 + 50 * (i/HEIGHT))
        draw.line([(0, i), (WIDTH, i)], fill=(r, g, b))
    
    for _ in range(3):
        base_y = random.randint(HEIGHT//2, HEIGHT-100)
        points = [(0, HEIGHT)]
        for x in range(0, WIDTH+1, 50):
            y = base_y - random.randint(50, 200)
            points.append((x, y))
        points.append((WIDTH, HEIGHT))
        draw.polygon(points, fill=(20, 30, 40))

# Design 7: Digital Rain
def create_digital_rain(draw):
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=(0, 20, 10))
    
    for _ in range(50):
        x = random.randint(0, WIDTH)
        length = random.randint(10, 30)
        for i in range(length):
            y = random.randint(0, HEIGHT)
            char = chr(random.randint(0x30A0, 0x30FF))
            brightness = random.randint(100, 200)
            draw.text((x, y + i*20), char, fill=(0, brightness, 0), font=font)

# Design 8: Crystal Cave
def create_crystal_cave(draw):
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=(10, 20, 40))
    
    for _ in range(10):
        x, y = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)
        size = random.randint(30, 100)
        points = []
        for i in range(6):
            angle = i * (math.pi / 3) + random.uniform(-0.2, 0.2)
            points.append((x + size * math.cos(angle), y + size * math.sin(angle)))
        r, g, b = colorsys.hsv_to_rgb(random.uniform(0.55, 0.65), 0.7, 0.9)
        draw.polygon(points, fill=(int(r*255), int(g*255), int(b*255)))

# Design 9: Abstract Waves
def create_abstract_waves(draw):
    for i in range(HEIGHT):
        r = int(50 + 50 * math.sin(i * 0.01))
        g = int(100 + 50 * math.cos(i * 0.015))
        b = int(150 + 50 * math.sin(i * 0.02))
        draw.line([(0, i), (WIDTH, i)], fill=(r, g, b))
    
    for _ in range(5):
        y_base = random.randint(100, HEIGHT-100)
        amplitude = random.randint(50, 150)
        frequency = random.uniform(0.01, 0.03)
        for x in range(0, WIDTH, 2):
            y = y_base + amplitude * math.sin(x * frequency)
            r, g, b = colorsys.hsv_to_rgb(random.uniform(0.4, 0.6), 0.7, 0.9)
            draw.line([(x, y), (x, y+10)], fill=(int(r*255), int(g*255), int(b*255)), width=2)

# Design 10: Fractal Universe
def create_fractal_universe(draw):
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=(0, 0, 0))
    
    for _ in range(5000):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        if (x * y) % (x + y + 1) < 10:
            size = random.randint(1, 3)
            h = (x + y) / (WIDTH + HEIGHT)
            r, g, b = colorsys.hsv_to_rgb(h, 0.9, 0.9)
            draw.ellipse([x-size, y-size, x+size, y+size], fill=(int(r*255), int(g*255), int(b*255)))

def apply_final_effects(img, design_number):
    filters = {
        1: ImageFilter.GaussianBlur(1),
        2: ImageFilter.SMOOTH,
        3: ImageFilter.EDGE_ENHANCE,
        4: ImageFilter.SHARPEN,
        5: ImageFilter.SMOOTH,
        6: ImageFilter.GaussianBlur(0.5),
        7: ImageFilter.EDGE_ENHANCE,
        8: ImageFilter.SHARPEN,
        9: ImageFilter.SMOOTH,
        10: ImageFilter.GaussianBlur(1)
    }
    return img.filter(filters.get(design_number, ImageFilter.SMOOTH))

# Generate all wallpapers
for i in range(1, 11):
    generate_wallpaper(i)
    print(f"Generated wallpaper {i}")

print("All 10 wallpapers created successfully in the 'wallpapers' folder!")
