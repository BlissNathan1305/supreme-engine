
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random
import math
import colorsys
import os

# Mobile device resolution (portrait)
WIDTH = 1080
HEIGHT = 1920

def create_gradient_background(width, height, color1, color2, direction='vertical'):
    """Create a gradient background between two colors"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    if direction == 'vertical':
        for y in range(height):
            ratio = y / height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(0, y), (width, y)], fill=(r, g, b))
    else:  # horizontal
        for x in range(width):
            ratio = x / width
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(x, 0), (x, height)], fill=(r, g, b))
    
    return image

def create_radial_gradient(width, height, center_color, edge_color):
    """Create a radial gradient from center to edges"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    center_x, center_y = width // 2, height // 2
    max_radius = math.sqrt((width/2)**2 + (height/2)**2)
    
    for y in range(height):
        for x in range(width):
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            ratio = min(distance / max_radius, 1.0)
            
            r = int(center_color[0] * (1 - ratio) + edge_color[0] * ratio)
            g = int(center_color[1] * (1 - ratio) + edge_color[1] * ratio)
            b = int(center_color[2] * (1 - ratio) + edge_color[2] * ratio)
            
            draw.point((x, y), fill=(r, g, b))
    
    return image

def wallpaper_1_geometric_sunset():
    """Geometric shapes with warm sunset colors"""
    print("Generating Wallpaper 1: Geometric Sunset")
    
    # Create gradient background
    image = create_gradient_background(WIDTH, HEIGHT, (255, 94, 77), (255, 154, 0))
    draw = ImageDraw.Draw(image)
    
    # Add geometric shapes
    colors = [(255, 206, 84, 180), (255, 118, 117, 150), (162, 155, 254, 120)]
    
    # Triangles
    for _ in range(15):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(50, 200)
        color = random.choice(colors)
        
        points = [
            (x, y - size//2),
            (x - size//2, y + size//2),
            (x + size//2, y + size//2)
        ]
        
        # Create overlay for transparency
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.polygon(points, fill=color)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add circles
    for _ in range(10):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(30, 120)
        color = random.choice(colors)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Apply subtle blur
    image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    return image

def wallpaper_2_ocean_waves():
    """Flowing wave patterns in ocean colors"""
    print("Generating Wallpaper 2: Ocean Waves")
    
    # Create base gradient
    image = create_gradient_background(WIDTH, HEIGHT, (0, 119, 190), (0, 180, 216))
    draw = ImageDraw.Draw(image)
    
    # Create wave patterns
    wave_colors = [(64, 224, 208, 100), (72, 209, 204, 120), (0, 206, 209, 80)]
    
    for wave in range(8):
        points = []
        y_offset = wave * 200 + random.randint(-100, 100)
        
        for x in range(0, WIDTH + 100, 20):
            y = y_offset + int(80 * math.sin(x * 0.01 + wave * 0.5))
            points.append((x, y))
        
        # Add bottom points to close the shape
        points.extend([(WIDTH, HEIGHT), (0, HEIGHT)])
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.polygon(points, fill=random.choice(wave_colors))
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add bubble effects
    for _ in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(5, 30)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                           fill=(255, 255, 255, 60))
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    return image

def wallpaper_3_neon_grid():
    """Cyberpunk-style neon grid pattern"""
    print("Generating Wallpaper 3: Neon Grid")
    
    # Dark background
    image = Image.new('RGB', (WIDTH, HEIGHT), (20, 20, 40))
    draw = ImageDraw.Draw(image)
    
    # Grid lines
    grid_spacing = 60
    neon_colors = [(255, 0, 255), (0, 255, 255), (255, 255, 0), (0, 255, 0)]
    
    # Vertical lines
    for x in range(0, WIDTH, grid_spacing):
        color = random.choice(neon_colors)
        alpha = random.randint(100, 200)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.line([(x, 0), (x, HEIGHT)], fill=(*color, alpha), width=2)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Horizontal lines
    for y in range(0, HEIGHT, grid_spacing):
        color = random.choice(neon_colors)
        alpha = random.randint(100, 200)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.line([(0, y), (WIDTH, y)], fill=(*color, alpha), width=2)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add glowing nodes at intersections
    for x in range(0, WIDTH, grid_spacing):
        for y in range(0, HEIGHT, grid_spacing):
            if random.random() < 0.3:  # 30% chance for a node
                color = random.choice(neon_colors)
                
                overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
                overlay_draw = ImageDraw.Draw(overlay)
                
                # Draw glowing effect
                for radius in range(15, 3, -2):
                    alpha = int(150 * (15 - radius) / 12)
                    overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                                       fill=(*color, alpha))
                
                image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Apply glow effect
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    
    return image

def wallpaper_4_marble_texture():
    """Marble-like texture with elegant swirls"""
    print("Generating Wallpaper 4: Marble Texture")
    
    # Create base with noise
    image = Image.new('RGB', (WIDTH, HEIGHT), (240, 240, 245))
    
    # Create marble veins
    vein_colors = [(180, 180, 190), (160, 160, 175), (200, 195, 210)]
    
    for vein in range(20):
        points = []
        start_x = random.randint(-200, WIDTH + 200)
        start_y = random.randint(-200, HEIGHT + 200)
        
        # Create curved vein
        for i in range(100):
            angle = i * 0.1 + random.uniform(-0.3, 0.3)
            distance = i * 8
            x = start_x + int(distance * math.cos(angle))
            y = start_y + int(distance * math.sin(angle))
            points.append((x, y))
        
        # Draw vein with varying thickness
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        for i in range(len(points) - 1):
            thickness = random.randint(2, 8)
            color = random.choice(vein_colors)
            overlay_draw.line([points[i], points[i+1]], fill=(*color, 120), width=thickness)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add subtle texture
    for _ in range(1000):
        x = random.randint(0, WIDTH-1)
        y = random.randint(0, HEIGHT-1)
        brightness = random.randint(-20, 20)
        current_pixel = image.getpixel((x, y))
        new_pixel = tuple(max(0, min(255, c + brightness)) for c in current_pixel)
        image.putpixel((x, y), new_pixel)
    
    # Apply soft blur
    image = image.filter(ImageFilter.GaussianBlur(radius=1.5))
    
    return image

def wallpaper_5_abstract_flowers():
    """Abstract floral patterns with soft colors"""
    print("Generating Wallpaper 5: Abstract Flowers")
    
    # Soft gradient background
    image = create_gradient_background(WIDTH, HEIGHT, (255, 240, 245), (240, 255, 240))
    
    # Flower colors
    flower_colors = [
        (255, 182, 193, 150),  # Light pink
        (221, 160, 221, 140),  # Plum
        (255, 218, 185, 130),  # Peach
        (230, 230, 250, 120),  # Lavender
        (240, 255, 240, 110),  # Honeydew
    ]
    
    # Create abstract flowers
    for _ in range(25):
        center_x = random.randint(100, WIDTH - 100)
        center_y = random.randint(100, HEIGHT - 100)
        color = random.choice(flower_colors)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Draw petals
        num_petals = random.randint(5, 8)
        petal_size = random.randint(40, 80)
        
        for petal in range(num_petals):
            angle = (2 * math.pi * petal) / num_petals
            petal_x = center_x + int(petal_size * 0.7 * math.cos(angle))
            petal_y = center_y + int(petal_size * 0.7 * math.sin(angle))
            
            overlay_draw.ellipse([petal_x - petal_size//2, petal_y - petal_size//2,
                                petal_x + petal_size//2, petal_y + petal_size//2],
                               fill=color)
        
        # Draw center
        center_color = (255, 255, 255, 180)
        overlay_draw.ellipse([center_x - 15, center_y - 15, center_x + 15, center_y + 15],
                           fill=center_color)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add soft blur for dreamy effect
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    
    return image

def wallpaper_6_geometric_prisms():
    """3D-looking geometric prisms"""
    print("Generating Wallpaper 6: Geometric Prisms")
    
    # Dark gradient background
    image = create_gradient_background(WIDTH, HEIGHT, (30, 30, 50), (50, 30, 80))
    
    # Prism colors
    prism_colors = [
        (255, 100, 150, 200),  # Pink
        (100, 150, 255, 200),  # Blue
        (150, 255, 100, 200),  # Green
        (255, 200, 100, 200),  # Orange
        (200, 100, 255, 200),  # Purple
    ]
    
    # Create 3D-looking prisms
    for _ in range(12):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT - 100)
        size = random.randint(80, 150)
        color = random.choice(prism_colors)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Draw main face (hexagon)
        hex_points = []
        for i in range(6):
            angle = i * math.pi / 3
            hex_x = x + int(size * math.cos(angle))
            hex_y = y + int(size * math.sin(angle))
            hex_points.append((hex_x, hex_y))
        
        overlay_draw.polygon(hex_points, fill=color)
        
        # Draw top face (lighter)
        top_color = tuple(min(255, int(c * 1.3)) if i < 3 else c for i, c in enumerate(color))
        top_points = [(p[0] - 20, p[1] - 20) for p in hex_points]
        overlay_draw.polygon(top_points, fill=top_color)
        
        # Draw connecting edges
        for i in range(6):
            edge_points = [hex_points[i], top_points[i], top_points[(i+1)%6], hex_points[(i+1)%6]]
            edge_color = tuple(int(c * 0.8) if i < 3 else c for i, c in enumerate(color))
            overlay_draw.polygon(edge_points, fill=edge_color)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    return image

def wallpaper_7_particle_explosion():
    """Particle explosion effect"""
    print("Generating Wallpaper 7: Particle Explosion")
    
    # Dark radial gradient
    image = create_radial_gradient(WIDTH, HEIGHT, (80, 20, 120), (20, 20, 40))
    
    # Explosion center
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    
    # Particle colors
    particle_colors = [
        (255, 100, 100),  # Red
        (255, 200, 100),  # Orange
        (255, 255, 100),  # Yellow
        (100, 255, 100),  # Green
        (100, 100, 255),  # Blue
        (255, 100, 255),  # Magenta
    ]
    
    # Create particles
    for _ in range(300):
        # Random angle and distance from center
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(50, 800)
        
        x = center_x + int(distance * math.cos(angle))
        y = center_y + int(distance * math.sin(angle))
        
        # Only draw if within bounds
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            color = random.choice(particle_colors)
            size = random.randint(2, 12)
            alpha = max(50, int(255 * (800 - distance) / 800))
            
            overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            
            # Draw particle with glow
            for radius in range(size, 0, -1):
                particle_alpha = alpha * radius // size
                overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius],
                                   fill=(*color, particle_alpha))
            
            image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    return image

def wallpaper_8_liquid_metal():
    """Liquid metal effect with metallic colors"""
    print("Generating Wallpaper 8: Liquid Metal")
    
    # Metallic gradient background
    image = create_gradient_background(WIDTH, HEIGHT, (80, 80, 90), (120, 120, 130))
    
    # Metallic blob colors
    metal_colors = [
        (150, 150, 160, 180),  # Silver
        (180, 160, 120, 170),  # Gold
        (120, 140, 160, 160),  # Steel blue
        (160, 140, 140, 150),  # Rose gold
    ]
    
    # Create liquid metal blobs
    for _ in range(8):
        center_x = random.randint(0, WIDTH)
        center_y = random.randint(0, HEIGHT)
        base_radius = random.randint(100, 300)
        color = random.choice(metal_colors)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Create irregular blob shape
        blob_points = []
        num_points = 12
        for i in range(num_points):
            angle = (2 * math.pi * i) / num_points
            radius_variation = random.uniform(0.7, 1.3)
            radius = base_radius * radius_variation
            
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            blob_points.append((x, y))
        
        overlay_draw.polygon(blob_points, fill=color)
        
        # Add highlight
        highlight_x = center_x - base_radius // 4
        highlight_y = center_y - base_radius // 4
        highlight_radius = base_radius // 3
        highlight_color = (255, 255, 255, 100)
        
        overlay_draw.ellipse([highlight_x - highlight_radius, highlight_y - highlight_radius,
                            highlight_x + highlight_radius, highlight_y + highlight_radius],
                           fill=highlight_color)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Apply blur for smooth liquid effect
    image = image.filter(ImageFilter.GaussianBlur(radius=2))
    
    return image

def wallpaper_9_rainbow_spirals():
    """Colorful spiral patterns"""
    print("Generating Wallpaper 9: Rainbow Spirals")
    
    # Black background
    image = Image.new('RGB', (WIDTH, HEIGHT), (10, 10, 15))
    
    # Create multiple spirals
    for spiral in range(6):
        center_x = random.randint(200, WIDTH - 200)
        center_y = random.randint(200, HEIGHT - 200)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Draw spiral
        points = []
        max_radius = random.randint(150, 400)
        
        for i in range(300):
            angle = i * 0.1
            radius = (i / 300) * max_radius
            
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                # HSV to RGB for rainbow effect
                hue = (i * 2) % 360
                saturation = 1.0
                value = 1.0
                rgb = colorsys.hsv_to_rgb(hue/360, saturation, value)
                color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255), 150)
                
                # Draw small circle at each point
                overlay_draw.ellipse([x-3, y-3, x+3, y+3], fill=color)
        
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Apply glow effect
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    
    return image

def wallpaper_10_crystalline_structure():
    """Crystal-like geometric structure"""
    print("Generating Wallpaper 10: Crystalline Structure")
    
    # Gradient background
    image = create_gradient_background(WIDTH, HEIGHT, (20, 25, 40), (40, 30, 60))
    
    # Crystal colors
    crystal_colors = [
        (150, 200, 255, 120),  # Ice blue
        (200, 150, 255, 110),  # Purple
        (255, 200, 150, 100),  # Warm orange
        (150, 255, 200, 130),  # Mint
    ]
    
    # Create crystal structures
    for _ in range(20):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT - 100)
        size = random.randint(50, 150)
        color = random.choice(crystal_colors)
        
        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Draw crystal facets
        num_facets = random.randint(6, 10)
        for facet in range(num_facets):
            angle1 = (2 * math.pi * facet) / num_facets
            angle2 = (2 * math.pi * (facet + 1)) / num_facets
            
            # Inner and outer points
            inner_radius = size * 0.3
            outer_radius = size
            
            points = [
                (x, y),  # Center
                (x + int(inner_radius * math.cos(angle1)), y + int(inner_radius * math.sin(angle1))),
                (x + int(outer_radius * math.cos(angle1)), y + int(outer_radius * math.sin(angle1))),
                (x + int(outer_radius * math.cos(angle2)), y + int(outer_radius * math.sin(angle2))),
                (x + int(inner_radius * math.cos(angle2)), y + int(inner_radius * math.sin(angle2)))
            ]
            
            # Vary brightness for each facet
            brightness = random.unifor
