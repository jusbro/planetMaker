from PIL import Image, ImageDraw
import random
import math
import matplotlib.pyplot as plt

def generate_star_field(width, height, star_mass, star_density, noise_intensity):
    image = Image.new("L", (width, height), color=0)  # Create a new grayscale image
    draw = ImageDraw.Draw(image)

    # Define the center of the image
    center_x = width // 2
    center_y = height // 2

    # Generate stars based on density
    total_stars = int(width * height * star_density)
    for _ in range(total_stars):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        brightness = int((random.random() * 200) + (star_mass * 50))  # Adjust brightness based on mass

        # Vary the size of stars
        star_size = random.randint(1, 4)  # Vary the size of stars
        x1, y1 = x - star_size, y - star_size
        x2, y2 = x + star_size, y + star_size

        # Draw the star as a filled ellipse
        draw.ellipse([(x1, y1), (x2, y2)], fill=brightness)

    # Draw a brighter star at the center with diffraction spikes
    center_star_size = 12
    x1, y1 = center_x - center_star_size, center_y - center_star_size
    x2, y2 = center_x + center_star_size, center_y + center_star_size
    draw.ellipse([(x1, y1), (x2, y2)], fill=255)

    # Add diffraction spikes to the central star
    num_spikes = 4
    spike_length = random.randint(25, 40)
    for i in range(num_spikes):
        angle = (math.pi / 2) * i  # Angle for top, bottom, left, right
        x_end = center_x + int(math.cos(angle) * spike_length)
        y_end = center_y + int(math.sin(angle) * spike_length)
        draw.line([(center_x, center_y), (x_end, y_end)], fill=255)

    # Apply noise to the image
    for y in range(height):
        for x in range(width):
            current_brightness = image.getpixel((x, y))
            new_brightness = min(max(0, current_brightness + random.randint(-noise_intensity, noise_intensity)), 255)
            image.putpixel((x, y), new_brightness)

    return image

def main(*star_names):
    fig, axs = plt.subplots(2, 3, figsize=(10, 5))  # 2 rows, 3 columns for 6 plots
    for i in range(2):
        for j in range(3):
            star_mass = random.uniform(1, 10)  # Randomize star mass
            star_density = random.uniform(0.0005, 0.002)  # Randomize star density
            noise_intensity = random.randint(20, 80)  # Randomize noise intensity
            star_field = generate_star_field(800, 600, star_mass, star_density, noise_intensity)
            inverted_star_field = star_field.point(lambda x: 255 - x)

            # Add a thick border around the image
            bordered_image = Image.new("L", (inverted_star_field.width + 20, inverted_star_field.height + 20), color=0)
            bordered_image.paste(inverted_star_field, (10, 10))

            axs[i, j].imshow(bordered_image, cmap='gray')
            axs[i, j].axis('on')
            axs[i, j].set_title(star_names[i * 3 + j], fontsize=10, pad=5)  # Title for each image with star names

            # Add x and y grids and labels
            axs[i, j].set_xticks([0, 200, 400, 600, 800])  # Adjust ticks as needed
            axs[i, j].set_yticks([0, 200, 400, 600])  # Adjust ticks as needed
            axs[i, j].set_xlabel('Parallax (arc.hrs.)')
            axs[i, j].set_ylabel('Parallax (arc.hrs.)')

    # Save the combined image as a JPG file
    plt.tight_layout()
    plt.savefig(f"starMaker/starfield.jpg")

    # Show the combined plot (optional)
    plt.show()

if __name__ == "__main__":
    star_1_name = "Star 1"  # Replace with the actual names of your stars
    star_2_name = "Star 2"
    star_3_name = "Star 3"
    star_4_name = "Star 4"
    star_5_name = "Star 5"
    star_6_name = "Star 6"
    main(star_1_name, star_2_name, star_3_name, star_4_name, star_5_name, star_6_name)
