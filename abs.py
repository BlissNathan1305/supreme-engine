
from PIL import Image, ImageDraw
n_abstract_circles.py
from PIL import Image, ImageDraw
import random

def create_abstract_circles_wallpaper(width, height, num_circles, output_filename="abstract_circles.png"):
    """
    Creates a wallpaper with abstract random circles.

    Args:
        width (int): Width of the wallpaper in pixels.
        height (int): Height of the wallpaper in pixels.
        num_circles (int): Number of circles to draw.
        output_filename (str): Name of the output image file.
    """
    # Create a blank image with a dark background
    img = Image.new('RGB', (width, height), color=(20, 20, 30))
    draw = ImageDraw.Draw(img)

    for _ in range(num_circles):
        # Random position
        x = random.randint(0, width)
        y = random.randint(0, height)

        # Random radius
        radius = random.randint(20, min(width, height) // 8) # Max radius relative to smallest dimension

        # Random color with transparency (RGBA)
        # Using a range of blue/purple tones for a cohesive look
        r = random.randint(50, 150)
        g = random.randint(50, 100)
        b = random.randint(150, 255)
        alpha = random.randint(50, 180) # Transparency (0-255)

        fill_color = (r, g, b, alpha)
        
        # Draw ellipse (circle is a special case of ellipse)
        # Bounding box (x1, y1, x2, y2)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill_color)

    # Save the image
    img.save(output_filename)
    print(f"Generated {output_filename} ({width}x{height})")

if __name__ == "__main__":
    # Example Usage:
    create_abstract_circles_wallpaper(1920, 1080, 500, "abstract_circles_hd.png")
    create_abstract_circles_wallpaper(3840, 2160, 1500, "abstract_circles_4k.png")
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
