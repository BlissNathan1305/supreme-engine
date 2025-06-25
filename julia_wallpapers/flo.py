
from PIL import Image, ImageDraw
import random
import math # Import the math module

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
            angle = random.uniform(0, 2 * math.pi) # Use math.pi for PI
            distance = random.uniform(0, cluster_radius)
            flower_x = int(center_x + distance * math.cos(angle)) # Corrected to math.cos
            flower_y = int(center_y + distance * math.sin(angle)) # Corrected to math.sin

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
            ]
            petal_color = random.choice(flower_colors)

            # Center color (for the middle of the flower, usually yellow or white)
            center_color = (random.randint(200, 255), random.randint(200, 255), random.randint(50, 100)) # Yellowish-white
            if random.random() < 0.3: # Occasionally make it a bit darker yellow
                 center_color = (random.randint(180, 220), random.randint(180, 220), random.randint(0, 50))


            # Random flower size
            flower_size = random.randint(20, 60) # Diameter

            # Draw petals (simple circles around a center)
            num_petals = random.randint(4, 8)
            petal_radius = flower_size // 4
            for i in range(num_petals):
                petal_angle = (360 / num_petals) * i + random.uniform(-10, 10) # Add slight randomness to angle
                petal_dist = flower_size // 3
                petal_x = int(flower_x + petal_dist * math.cos(math.radians(petal_angle))) # Corrected to math.cos, math.radians
                petal_y = int(flower_y + petal_dist * math.sin(math.radians(petal_angle))) # Corrected to math.sin, math.radians
                draw.ellipse([petal_x - petal_radius, petal_y - petal_radius,
                              petal_x + petal_radius, petal_y + petal_radius],
                             fill=petal_color)

            # Draw flower center
            center_radius = flower_size // 6
            draw.ellipse([flower_x - center_radius, flower_y - center_radius,
                          flower_x + center_radius, flower_y + center_radius],
                         fill=center_color)

            # Occasionally draw a simple leaf
            if random.random() < 0.4: # 40% chance of drawing a leaf
                leaf_color = (random.randint(50, 150), random.randint(100, 200), random.randint(50, 100)) # Green shades
                leaf_width = random.randint(10, 30)
                leaf_height = random.randint(20, 50)
                # No need for leaf_angle if not rotating, but keeping for conceptual clarity if you want to add rotation later
                # leaf_angle = random.uniform(0, 360)

                # Simple oval leaf
                # For simplicity, just draw an unrotated ellipse and offset it slightly from flower
                offset_x = random.uniform(-leaf_width, leaf_width)
                offset_y = random.uniform(leaf_height / 2, leaf_height) # Place below or to the side
                draw.ellipse([flower_x + offset_x - leaf_width // 2, flower_y + offset_y - leaf_height // 2,
                              flower_x + offset_x + leaf_width // 2, flower_y + offset_y + leaf_height // 2],
                             fill=leaf_color)


    # Add some subtle texture or light gradients
    for i in range(500): # Draw some random small dots for subtle texture
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        dot_color_base = background_color
        # Create a subtle variation of the background color
        dot_color = (random.randint(max(0, dot_color_base[0]-20), min(255, dot_color_base[0]+20)),
                     random.randint(max(0, dot_color_base[1]-20), min(255, dot_color_base[1]+20)),
                     random.randint(max(0, dot_color_base[2]-20), min(255, dot_color_base[2]+20)))
        
        # Using a small ellipse for the "dot"
        draw.ellipse([x-1, y-1, x+1, y+1], fill=dot_color)


    # Save the generated image
    img.save(output_filename)
    print(f"Floral wallpaper generated and saved as '{output_filename}'")

if __name__ == "__main__":
    # Common mobile wallpaper resolutions:
    # Full HD: 1080x1920
    # QHD: 1440x2560
    # Higher resolutions for modern phones: 1440x3040, 1242x2688, etc.
    # Let's use a common one or slightly higher for good quality.
    mobile_width = 1080
    mobile_height = 1920
    # mobile_width = 1440
    # mobile_height = 2560

    generate_floral_wallpaper(mobile_width, mobile_height, "mobile_floral_wallpaper.png")

