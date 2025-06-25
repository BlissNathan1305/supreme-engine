
from PIL import Image, ImageDraw
import random
import math

def get_random_pastel_color():
    """Generates a random pastel RGB color."""
    return (random.randint(180, 255), random.randint(180, 255), random.randint(180, 255))

def get_random_vibrant_color():
    """Generates a random vibrant RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def generate_wallpaper_1_expanding_circles(width, height, output_filename="geometric_wallpaper_1_expanding_circles.png"):
    """
    Generates a wallpaper with circles expanding from the center in a geometric sequence.
    """
    img = Image.new('RGB', (width, height), color=get_random_pastel_color())
    draw = ImageDraw.Draw(img)

    center_x, center_y = width // 2, height // 2

    # Geometric sequence parameters
    initial_radius = random.randint(10, 30) # Smallest circle radius
    common_ratio = random.uniform(1.1, 1.5) # How much each successive circle grows
    num_circles = random.randint(15, 25) # Number of circles to draw

    for i in range(num_circles):
        radius = int(initial_radius * (common_ratio ** i))
        if radius > max(width, height) * 0.7: # Prevent circles from getting too large
            break

        # Random vibrant color for each circle
        circle_color = get_random_vibrant_color()

        # Draw the circle
        draw.ellipse([center_x - radius, center_y - radius,
                      center_x + radius, center_y + radius],
                     outline=circle_color, width=random.randint(1, 5))

    img.save(output_filename)
    print(f"Generated {output_filename}")


def generate_wallpaper_2_geometric_grid_squares(width, height, output_filename="geometric_wallpaper_2_geometric_grid_squares.png"):
    """
    Generates a wallpaper with a grid of squares, where sizes scale geometrically.
    """
    img = Image.new('RGB', (width, height), color=get_random_pastel_color())
    draw = ImageDraw.Draw(img)

    grid_cols = random.randint(5, 10)
    grid_rows = random.randint(8, 15)

    cell_width = width / grid_cols
    cell_height = height / grid_rows

    # Geometric sequence for scaling squares
    initial_scale = random.uniform(0.1, 0.3) # Initial square size as a fraction of cell size
    common_ratio = random.uniform(1.05, 1.2) # How much the scale increases per row/column

    for r in range(grid_rows):
        for c in range(grid_cols):
            # Calculate square size based on geometric sequence (example: scale by row)
            scale = initial_scale * (common_ratio ** r)
            square_size = min(cell_width, cell_height) * scale

            # Center the square in its grid cell
            square_x1 = c * cell_width + (cell_width - square_size) / 2
            square_y1 = r * cell_height + (cell_height - square_size) / 2
            square_x2 = square_x1 + square_size
            square_y2 = square_y1 + square_size

            # Random color for the square
            square_color = get_random_vibrant_color()

            draw.rectangle([square_x1, square_y1, square_x2, square_y2],
                           fill=square_color)

    img.save(output_filename)
    print(f"Generated {output_filename}")


def generate_wallpaper_3_spiral_dots(width, height, output_filename="geometric_wallpaper_3_spiral_dots.png"):
    """
    Generates a wallpaper with dots arranged in a spiral, with sizes scaling geometrically.
    """
    img = Image.new('RGB', (width, height), color=get_random_pastel_color())
    draw = ImageDraw.Draw(img)

    center_x, center_y = width // 2, height // 2

    # Spiral parameters
    initial_angle = random.uniform(0, 2 * math.pi)
    angle_step = random.uniform(0.1, 0.3) # How much the angle increases per dot
    initial_radius_step = random.uniform(2, 5) # How much the radius increases per dot initially
    radius_ratio = random.uniform(1.01, 1.05) # Geometric growth of radius step

    # Dot size parameters
    initial_dot_radius = random.randint(5, 15)
    dot_size_ratio = random.uniform(0.9, 1.1) # Can grow or shrink

    current_radius = 0
    current_angle = initial_angle

    max_dist = math.sqrt(center_x**2 + center_y**2) * 1.2 # Max distance for dots

    dot_count = 0
    while current_radius < max_dist and dot_count < 500: # Limit dot count to prevent infinite loop
        dot_count += 1
        x = center_x + current_radius * math.cos(current_angle)
        y = center_y + current_radius * math.sin(current_angle)

        dot_radius = int(initial_dot_radius * (dot_size_ratio ** dot_count))
        if dot_radius < 1: dot_radius = 1 # Minimum dot size
        if dot_radius > 50: dot_radius = 50 # Maximum dot size

        dot_color = get_random_vibrant_color()

        draw.ellipse([x - dot_radius, y - dot_radius,
                      x + dot_radius, y + dot_radius],
                     fill=dot_color)

        current_angle += angle_step
        current_radius += initial_radius_step * (radius_ratio ** dot_count) # Geometric increase in radius step

    img.save(output_filename)
    print(f"Generated {output_filename}")


def generate_wallpaper_4_layered_shapes(width, height, output_filename="geometric_wallpaper_4_layered_shapes.png"):
    """
    Generates a wallpaper with layered, geometrically scaled shapes (e.g., rectangles or triangles).
    """
    img = Image.new('RGB', (width, height), color=get_random_pastel_color())
    draw = ImageDraw.Draw(img)

    # Choose a random primary shape to layer
    shape_type = random.choice(['rectangle', 'ellipse'])

    num_layers = random.randint(5, 15)
    initial_size_factor = random.uniform(0.8, 1.0) # How large the outermost shape is relative to screen
    scaling_ratio = random.uniform(0.7, 0.9) # How much each inner shape scales down

    # Determine initial shape dimensions
    current_width = width * initial_size_factor
    current_height = height * initial_size_factor

    for i in range(num_layers):
        # Center the shape
        x1 = (width - current_width) / 2
        y1 = (height - current_height) / 2
        x2 = x1 + current_width
        y2 = y1 + current_height

        shape_color = get_random_vibrant_color()

        if shape_type == 'rectangle':
            draw.rectangle([x1, y1, x2, y2], fill=shape_color)
        elif shape_type == 'ellipse':
            draw.ellipse([x1, y1, x2, y2], fill=shape_color)

        current_width *= scaling_ratio
        current_height *= scaling_ratio

        if current_width < 10 or current_height < 10: # Stop if shapes get too small
            break

    img.save(output_filename)
    print(f"Generated {output_filename}")


def generate_wallpaper_5_geometric_lines(width, height, output_filename="geometric_wallpaper_5_geometric_lines.png"):
    """
    Generates a wallpaper with parallel lines where either thickness or spacing scales geometrically.
    """
    img = Image.new('RGB', (width, height), color=get_random_pastel_color())
    draw = ImageDraw.Draw(img)

    # Randomly choose horizontal or vertical lines
    is_horizontal = random.choice([True, False])

    # Parameters for line thickness/spacing
    initial_value = random.randint(5, 20) # Initial thickness or spacing
    common_ratio = random.uniform(1.05, 1.2) # How much it grows
    max_lines = 50 # Maximum number of lines to draw

    current_pos = 0
    line_idx = 0

    while True:
        line_idx += 1
        if line_idx > max_lines:
            break

        # Calculate thickness or spacing based on geometric sequence
        line_thickness = int(initial_value * (common_ratio ** line_idx))
        if line_thickness < 1: line_thickness = 1
        if line_thickness > max(width, height) / 5: line_thickness = int(max(width, height) / 5) # Cap max thickness

        line_color = get_random_vibrant_color()

        if is_horizontal:
            start_y = current_pos
            end_y = current_pos + line_thickness
            if start_y >= height: break
            draw.line([(0, start_y), (width, start_y)], fill=line_color, width=line_thickness)
            current_pos = end_y + random.randint(1, 10) # Add a small random gap
        else: # Vertical lines
            start_x = current_pos
            end_x = current_pos + line_thickness
            if start_x >= width: break
            draw.line([(start_x, 0), (start_x, height)], fill=line_color, width=line_thickness)
            current_pos = end_x + random.randint(1, 10) # Add a small random gap

    img.save(output_filename)
    print(f"Generated {output_filename}")


if __name__ == "__main__":
    # Common mobile wallpaper resolutions
    mobile_width = 1080
    mobile_height = 1920

    print("Generating 5 geometric sequence wallpapers...")
    generate_wallpaper_1_expanding_circles(mobile_width, mobile_height)
    generate_wallpaper_2_geometric_grid_squares(mobile_width, mobile_height)
    generate_wallpaper_3_spiral_dots(mobile_width, mobile_height)
    generate_wallpaper_4_layered_shapes(mobile_width, mobile_height)
    generate_wallpaper_5_geometric_lines(mobile_width, mobile_height)
    print("All wallpapers generated!")


