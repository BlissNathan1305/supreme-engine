
from PIL import Image, ImageDraw
n_perlin_wallpaper.py
import noise # Make sure you 'pip install noise'
from PIL import Image
import numpy as np
import random

def create_perlin_noise_wallpaper(width, height, scale, octaves, persistence, lacunarity, output_filename="perlin_wallpaper.png"):
    """
    Creates a wallpaper using Perlin noise.

    Args:
        width (int): Width of the wallpaper in pixels.
        height (int): Height of the wallpaper in pixels.
        scale (float): Determines the "zoom" level of the noise. Lower values zoom in.
        octaves (int): Number of noise layers to combine (for detail).
        persistence (float): How much each octave contributes (amplitude).
        lacunarity (float): How much the frequency changes per octave.
        output_filename (str): Name of the output image file.
    """
    # Create an empty NumPy array for grayscale pixels
    pixels = np.zeros((height, width), dtype=np.float64) # Use float for noise values

    seed = random.randint(0, 1000000) # Random base for different noise patterns

    # Generate Perlin noise for each pixel
    for y in range(height):
        for x in range(width):
            # pnoise2 generates 2D Perlin noise
            # (x/scale, y/scale) gives coordinates for the noise function
            # octaves, persistence, lacunarity control the detail and texture
            # repeatx, repeaty can make the noise tileable (useful for game textures, less for wallpapers)
            # base gives a unique pattern for each seed
            pixels[y, x] = noise.pnoise2(x / scale,
                                         y / scale,
                                         octaves=octaves,
                                         persistence=persistence,
                                         lacunarity=lacunarity,
                                         repeatx=width,
                                         repeaty=height, # Can set to 0 for non-repeating
                                         base=seed)
    
    # Normalize noise values from their current range to 0-255 (for image pixels)
    # The noise library returns values typically in a range like -1 to 1 or -0.5 to 0.5.
    # np.interp maps values from one range to another.
    normalized_pixels = np.interp(pixels, (pixels.min(), pixels.max()), (0, 255)).astype(np.uint8)

    # --- Apply a simple color map for a "stunning" look ---
    # Convert grayscale values to RGB using a custom gradient
    rgb_pixels = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            val = normalized_pixels[y, x]
            # Example: Blueish cloud effect (dark blue to light blue/white)
            r = int(np.interp(val, [0, 255], [0, 255]))
            g = int(np.interp(val, [0, 255], [0, 200]))
            b = int(np.interp(val, [0, 255], [50, 255]))
            rgb_pixels[y, x] = [r, g, b]

    img = Image.fromarray(rgb_pixels, 'RGB')
    img.save(output_filename)
    print(f"Generated {output_filename} ({width}x{height})")

if __name__ == "__main__":
    # Example Usage:
    # Experiment with scale, octaves, persistence, and lacunarity for different effects
    # Scale: larger values zoom in (more detail), smaller values zoom out (smoother)
    # Octaves: more layers of noise = more detail/complexity
    # Persistence: how much each octave contributes to the overall shape
    # Lacunarity: how quickly the frequency increases for each octave

    create_perlin_noise_wallpaper(
        width=1920, height=1080, 
        scale=100.0, octaves=6, persistence=0.5, lacunarity=2.0,
        output_filename="perlin_clouds_hd.png"
    )

    create_perlin_noise_wallpaper(
        width=3840, height=2160, 
        scale=200.0, octaves=8, persistence=0.55, lacunarity=2.2,
        output_filename="perlin_abstract_4k.png"
    )
import random

def generate_floral_wallpaper(width, height, output_filename="floral_wallpaper.png"):
    """
    Generates a floral-themed wallpaper using Python PIL.

    Args:
        width (int): The width of the wallpaper in pixels.
        height (int): The height of the wallpaper in pixels.
        output_filename (str): The name of the file to save the wallpaper to.
    """
    # Create a new image with a light background color
    # Using a soft pastel color for the background
    background_color = (random.randint(220, 250), random.randint(220, 250), random.randint(220, 250))
    img = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Number of floral clusters to draw
    num_clusters = random.randint(15, 30)

    for _ in range(num_clusters):
        # Random position for the center of the cluster
        center_x = random.randint(0, width)
        center_y = random.randint(0, height)

        # Random size for the cluster (determines how spread out the flowers are)
        cluster_radius = random.randint(50, 200)

        # Number of flowers in this cluster
        num_flowers_in_cluster = random.randint(3, 8)

        for _ in range(num_flowers_in_cluster):
            # Random position for each flower within the cluster radius
            angle = random.uniform(0, 2 * 3.14159)
            distance = random.uniform(0, cluster_radius)
            flower_x = int(center_x + distance * random.cos(angle))
            flower_y = int(center_y + distance * random.sin(angle))

            # Ensure flower position is within image bounds
            flower_x = max(0, min(width - 1, flower_x))
            flower_y = max(0, min(height - 1, flower_y))

            # Random flower colors (various shades of pink, purple, red, orange, yellow)
            flower_colors = [
                (255, random.randint(150, 200), random.randint(150, 200)), # Pinks/Reds
                (random.randint(150, 200), 0, random.randint(150, 255)), # Purples
                (random.randint(200, 255), random.randint(100, 150), 0), # Oranges
                (random.randint(200, 255), random.randint(200, 255), 0), # Yellows
                (random.randint(250, 255), random.randint(150, 200), random.randint(150, 255)), # Lavender/Light purples
