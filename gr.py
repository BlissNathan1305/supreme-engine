
from PIL import Image, ImageDraw
import random
import os

def generate_gradient_wallpaper(width, height, colors, filename="gradient_wallpaper.png"):
    """
    Generates a gradient wallpaper image and saves it to a file.

    Args:
        width:  Width of the wallpaper in pixels.
        height: Height of the wallpaper in pixels.
        colors: A list of RGB tuples representing the colors in the gradient.
                e.g., [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  (Red, Green, Blue)
        filename: The name of the file to save the wallpaper to (e.g., "wallpaper.png").
                  Defaults to "gradient_wallpaper.png".
    """

    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    num_colors = len(colors)
    if num_colors == 0:
        print("Error: No colors provided.  Using default black and white.")
        colors = [(0, 0, 0), (255, 255, 255)]
        num_colors = 2


    # Linear Gradient
    if num_colors == 2:
        color1 = colors[0]
        color2 = colors[1]

        for i in range(height):
            # Calculate the ratio (0.0 to 1.0) based on the height
            ratio = float(i) / height

            # Interpolate the RGB values
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)

            # Draw a line
            draw.line((0, i, width, i), fill=(r, g, b))


    # Multi-color Gradient
    else:
        color_stops = [(i / (num_colors - 1)) for i in range(num_colors)]  # Position of each color

        for i in range(height):
            # Calculate the ratio (0.0 to 1.0) based on the height
            ratio = float(i) / height

            # Find the two color stops that the ratio falls between
            for j in range(len(color_stops) - 1):
                if color_stops[j] <= ratio <= color_stops[j + 1]:
                    stop1 = color_stops[j]
                    stop2 = color_stops[j + 1]
                    color1 = colors[j]
                    color2 = colors[j + 1]
                    break
            else:  # Handle case where ratio might be exactly 1.0
                stop1 = color_stops[-2]
                stop2 = color_stops[-1]
                color1 = colors[-2]
                color2 = colors[-1]

            # Interpolate between the two colors
            local_ratio = (ratio - stop1) / (stop2 - stop1)
            r = int(color1[0] * (1 - local_ratio) + color2[0] * local_ratio)
            g = int(color1[1] * (1 - local_ratio) + color2[1] * local_ratio)
            b = int(color1[2] * (1 - local_ratio) + color2[2] * local_ratio)

            # Draw a line
            draw.line((0, i, width, i), fill=(r, g, b))



    img.save(filename)
    print(f"Wallpaper saved to {filename}")


def generate_random_colors(num_colors=3):
    """Generates a list of random RGB color tuples."""
    return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_colors)]


def create_directory_if_not_exists(directory):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)



if __name__ == "__main__":
    #  Recommended Mobile Resolutions (adjust as needed):
    #  *  1080x1920 (Full HD)
    #  *  1440x2560 (Quad HD)
    #  *  2160x3840 (4K Ultra HD)
    #
    #  Example usage:

    width = 1080
    height = 1920

    # Example 1: Generate a simple blue-to-green gradient
    generate_gradient_wallpaper(width, height, [(0, 0, 255), (0, 255, 0)], "blue_to_green.png")

    # Example 2: Generate a red-yellow-orange gradient
    generate_gradient_wallpaper(width, height, [(255, 0, 0), (255, 255, 0), (255, 165, 0)], "red_yellow_orange.png")

    # Example 3: Generate a random gradient
    random_colors = generate_random_colors(5)  # 5 random colors
    generate_gradient_wallpaper(width, height, random_colors, "random_gradient.png")

    # Example 4: Create a directory for wallpapers and save there
    wallpaper_dir = "wallpapers"
    create_directory_if_not_exists(wallpaper_dir)
    generate_gradient_wallpaper(width, height, [(255, 0, 255), (0, 255, 255)], os.path.join(wallpaper_dir, "magenta_cyan.png"))

    print("Done!")
