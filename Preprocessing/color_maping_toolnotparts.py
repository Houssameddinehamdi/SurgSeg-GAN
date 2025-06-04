import os
from PIL import Image

# Define the class colors to convert to white
convert_to_white_colors = [
    (0, 255, 0),   # instrument-shaft
    (0, 255, 255), # instrument-clasper
    (125, 255, 12) # instrument-wrist
]

# Input folders
input_folders = {
    "train": r"D:\Dataset_parts\Datasplit\train\labels",
    "val": r"D:\Dataset_parts\Datasplit\val\labels"
}

# Output folder
output_base_folder = r"D:\Processed_Labels_White"
os.makedirs(output_base_folder, exist_ok=True)

def process_image(input_path, output_path, convert_to_white_colors):
    # Open the image
    img = Image.open(input_path)
    img = img.convert("RGB")  # Ensure it's in RGB format
    
    # Create a new image to store the processed data
    processed_img = Image.new("RGB", img.size, (0, 0, 0))
    pixels = img.load()
    processed_pixels = processed_img.load()

    # Iterate over all pixels
    for y in range(img.height):
        for x in range(img.width):
            if pixels[x, y] in convert_to_white_colors:
                processed_pixels[x, y] = (255, 255, 255)  # Convert to white
            else:
                processed_pixels[x, y] = (0, 0, 0)  # Set to black

    # Save the processed image
    processed_img.save(output_path)

# Process each folder
for folder_type, folder_path in input_folders.items():
    output_folder = os.path.join(output_base_folder, folder_type)
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):  # Process only PNG images
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)

            # Process the image
            process_image(input_path, output_path, convert_to_white_colors)

print(f"Processing complete. Processed images saved in '{output_base_folder}'.")
