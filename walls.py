
from PIL import Image, ImageDraw
import math

def interpolate_color(color1, color2, factor: float):
    """Interpolates between two RGB colors with a given factor (0 to 1)."""
    return tuple([
        int(color1[i] + (color2[i] - color1[i]) * factor)
        for i in range(3)
    ])

def generate_gradient_wallpaper(width, height, colors, direction='horizontal'):
    """
    Generate a gradient wallpaper image.

    Parameters:
        width (int): Image width.
        height (int): Image height.
        colors (list): List of RGB tuples for gradient stops.
        direction (str): Gradient direction: 'horizontal', 'vertical', 'diagonal', or 'radial'.

    Returns:
        Image: PIL Image object with gradient.
    """
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    if direction == 'horizontal':
        for x in range(width):
            # Normalize x to [0, 1]
            factor = x / (width - 1)
            index = int(factor * (len(colors) - 1))
            local_factor = (factor * (len(colors) - 1)) % 1
            color = interpolate_color(colors[index], colors[min(index+1, len(colors)-1)], local_factor)
            draw.line([(x, 0), (x, height)], fill=color)

    elif direction == 'vertical':
        for y in range(height):
            factor = y / (height - 1)
            index = int(factor * (len(colors) - 1))
            local_factor = (factor * (len(colors) - 1)) % 1
            color = interpolate_color(colors[index], colors[min(index+1, len(colors)-1)], local_factor)
            draw.line([(0, y), (width, y)], fill=color)

    elif direction == 'diagonal':
        for y in range(height):
            for x in range(width):
                factor = ((x + y) / (width + height - 2))
                index = int(factor * (len(colors) - 1))
                local_factor = (factor * (len(colors) - 1)) % 1
                color = interpolate_color(colors[index], colors[min(index+1, len(colors)-1)], local_factor)
                image.putpixel((x, y), color)

    elif direction == 'radial':
        center_x, center_y = width // 2, height // 2
        max_radius = math.sqrt(center_x ** 2 + center_y ** 2)
        for y in range(height):
            for x in range(width):
                dx = x - center_x
                dy = y - center_y
                dist = math.sqrt(dx ** 2 + dy ** 2)
                factor = dist / max_radius
                factor = min(factor, 1.0)
                index = int(factor * (len(colors) - 1))
                local_factor = (factor * (len(colors) - 1)) % 1
                color = interpolate_color(colors[index], colors[min(index+1, len(colors)-1)], local_factor)
                image.putpixel((x, y), color)

    else:
        raise ValueError("Unsupported direction. Use 'horizontal', 'vertical', 'diagonal', or 'radial'.")

    return image
