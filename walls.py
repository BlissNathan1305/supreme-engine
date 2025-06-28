
from PIL import Image
import math

def interpolate_color(c1, c2, factor):
    """Linearly interpolate between two RGB colors based on factor (0 to 1)."""
    return tuple([
        int(c1[i] + (c2[i] - c1[i]) * factor)
        for i in range(3)
    ])

def generate_gradient(width, height, colors, direction='horizontal'):
    """
    Generate a gradient image.
    
    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        colors (list): List of RGB color tuples.
        direction (str): 'horizontal', 'vertical', 'diagonal', or 'radial'.

    Returns:
        Image: PIL Image with gradient.
    """
    image = Image.new('RGB', (width, height))
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            # Determine interpolation factor
            if direction == 'horizontal':
                factor = x / (width - 1)
            elif direction == 'vertical':
                factor = y / (height - 1)
            elif direction == 'diagonal':
                factor = (x + y) / (width + height - 2)
            elif direction == 'radial':
                cx, cy = width / 2, height / 2
                dx, dy = x - cx, y - cy
                dist = math.sqrt(dx ** 2 + dy ** 2)
                max_dist = math.sqrt(cx ** 2 + cy ** 2)
                factor = dist / max_dist
            else:
                raise ValueError("Invalid direction")

            # Clamp factor and determine color stops
            factor = min(max(factor, 0), 1)
            index = int(factor * (len(colors) - 1))
            local_factor = (factor * (len(colors) - 1)) % 1

            c1 = colors[index]
            c2 = colors[min(index + 1, len(colors) - 1)]
            color = interpolate_color(c1, c2, local_factor)
            pixels[x, y] = color

    return image

if __name__ == '__main__':
    # Wallpaper 1: Horizontal gradient (blue to green)
    img1 = generate_gradient(
        width=1080,
        height=1920,
        colors=[(0, 128, 255), (0, 255, 128)],
        direction='horizontal'
    )
    img1.save("wallpaper_horizontal.png", format="PNG")
    print("✅ Saved: wallpaper_horizontal.png")

    # Wallpaper 2: Radial gradient (red to orange to yellow)
    img2 = generate_gradient(
        width=1080,
        height=1920,
        colors=[(255, 0, 0), (255, 140, 0), (255, 255, 0)],
        direction='radial'
    )
    img2.save("wallpaper_radial.png", format="PNG")
    print("✅ Saved: wallpaper_radial.png")
