
from PIL import Image, ImageDraw
import random
import os

def generate_gradient_wallpaper(width, height, colors, filename="gradient_wallpaper.png", gradient_type="linear"):
    """
    Generates a gradient wallpaper image and saves it to a file.

    Args:
        width:  Width of the wallpaper in pixels.
        height: Height of the wallpaper in pixels.
        colors: A list of RGB tuples representing the colors in the gradient.
                e.g., [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  (Red, Green, Blue)
        filename: The name of the file to save the wallpaper to (e.g., "wallpaper.png").
                  Defaults to "gradient_wallpaper.png".
        gradient_type:  "linear", "radial" - specifies the type of gradient. Defaults to "linear".
    """

    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    num_colors = len(colors)
    if num_colors == 0:
        print("Error: No colors provided.  Using default black and white.")
        colors = [(0, 0, 0), (255, 255, 255)]
        num_colors = 2


    if gradient_type == "linear":
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

    elif gradient_type == "radial":
        # Radial Gradient Implementation
        center_x = width // 2
        center_y = height // 2
        max_distance = ((width // 2) ** 2 + (height // 2) ** 2) ** 0.5  # Distance from center to corner

        if num_colors == 2:
            color1 = colors[0]
            color2 = colors[1]

            for x in range(width):
                for y in range(height):
                    distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                    ratio = distance / max_distance
                    ratio = min(ratio, 1.0) # Clamp to 1.0 in case distance exceeds max_distance
                    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                    img.putpixel((x, y), (r, g, b))  # putpixel is necessary for radial gradients
        else:
            print("Radial gradients only support two colors for now. Using first two colors provided.")
            color1 = colors[0]
            color2 = colors[1]

            for x in range(width):
                for y in range(height):
                    distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                    ratio = distance / max_distance
                    ratio = min(ratio, 1.0)  # Clamp to 1.0 in case distance exceeds max_distance
                    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                    img.putpixel((x, y), (r, g, b))  # putpixel is necessary for radial gradients



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

    wallpaper_dir = "wallpapers"
    create_directory_if_not_exists(wallpaper_dir)

    for i in range(1, 11):  # Generate 10 wallpapers
        random_colors = generate_random_colors(random.randint(2, 5))  # 2-5 random colors
        gradient_type = random.choice(["linear", "radial"])
        filename = os.path.join(wallpaper_dir, f"wallpaper_{i}.png")
        generate_gradient_wallpaper(width, height, random_colors, filename, gradient_type)

    print("Generated 10 wallpapers in the 'wallpapers' directory.")
