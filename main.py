import cv2
import os
import shutil

# Define the directory containing the source images
source_directory = '/path/to/images/source'
# Define the directory to move used source images
used_source_images = '/path/to/images/used/source'

# Define the coordinates and size of the templates
templates = [
    (0, 0, 10, 10),  # x, y, width, height
    (10, 10, 10, 10),
    (20, 20, 10, 10),
    (30, 30, 10, 10),
    (40, 40, 10, 10),
    # Add more templates as needed
]

# Create a directory to save the extracted templates
output_directory = '/path/to//images/templates'
os.makedirs(output_directory, exist_ok=True)

# Create the used source images directory if it doesn't exist
os.makedirs(used_source_images, exist_ok=True)

# Iterate through all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check for image file extensions
        # Load the current image
        image_path = os.path.join(source_directory, filename)
        large_image = cv2.imread(image_path)

        # Check if the image was loaded successfully
        if large_image is None:
            print(f"Error loading image: {image_path}")
            continue

        # Extract and save templates from the current image
        for i, (x, y, w, h) in enumerate(templates):
            # Crop the template from the large image
            template = large_image[y:y+h, x:x+w]
            # Save the template with a unique name
            template_filename = f'template_{os.path.splitext(filename)[0]}_{i}.jpg'
            cv2.imwrite(os.path.join(output_directory, template_filename), template)

        # Move the used source image to the specified directory
        shutil.move(image_path, os.path.join(used_source_images, filename))

print("Templates extracted and saved. Source images moved to used directory.")
