import os
import cv2
import numpy as np

def convert_video_masks_to_yolo(input_dir, output_base_dir, min_area=200):
    """
    Converts segmentation masks for multiple videos to YOLO format, where each color in the mask corresponds to a different class.

    Parameters:
        input_dir (str): Path to the base directory containing segmentation masks.
        output_base_dir (str): Path to save YOLO label files.
        min_area (int): Minimum contour area to include (default: 200 pixels).
    """
    os.makedirs(output_base_dir, exist_ok=True)

    # Iterate over all the files in the input directory (labels in train or val)
    for mask_name in os.listdir(input_dir):
        mask_path = os.path.join(input_dir, mask_name)

        # Ensure the file is an image
        if not mask_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            print(f"Skipping non-image file: {mask_name}")
            continue

        # Load the colored mask
        mask = cv2.imread(mask_path)
        if mask is None:
            print(f"Error reading file: {mask_path}")
            continue

        # Get the height and width of the mask
        H, W, _ = mask.shape

        # Convert the mask to a list of unique colors (each color is a class)
        unique_colors = np.unique(mask.reshape(-1, mask.shape[2]), axis=0)

        # Prepare a dictionary to map colors to class IDs, skipping the background
        color_to_class = {tuple(color): idx for idx, color in enumerate(unique_colors) if tuple(color) != (0, 0, 0)}

        polygons = []

        # Iterate over each unique color (class), excluding background
        for color, class_id in color_to_class.items():
            # Create a binary mask for the current color
            color_mask = np.all(mask == color, axis=-1).astype(np.uint8) * 255

            # Find contours in the binary mask for the current color
            contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                # Filter by area
                if cv2.contourArea(cnt) > min_area:
                    polygon = []
                    for point in cnt:
                        x, y = point[0]
                        polygon.append(x / W)  # Normalize X
                        polygon.append(y / H)  # Normalize Y
                    polygons.append((class_id, polygon))

        # Generate output file name (same name as input mask, but in txt format)
        base_name = os.path.splitext(mask_name)[0]
        output_file = os.path.join(output_base_dir, f"{base_name}.txt")

        # Write the polygons and their class IDs to the YOLO label file
        with open(output_file, 'w') as f:
            for class_id, polygon in polygons:
                f.write(f"{class_id} ")  # Class ID
                f.write(' '.join(map(str, polygon)))  # Normalized polygon points
                f.write('\n')

        print(f"Processed {mask_name}, saved to {output_file}")

# Define input directories for training and validation labels
train_input_dir = r"D:\Dataset_parts\Datasplit\train\labels"
val_input_dir = r"D:\Dataset_parts\Datasplit\val\labels"

# Define output directories for YOLO label files
train_output_dir = r"D:\Dataset_parts\Datasplit\2018\train"
val_output_dir = r"D:\Dataset_parts\Datasplit\2018\val"

# Process both training and validation directories
convert_video_masks_to_yolo(train_input_dir, train_output_dir, min_area=200)
convert_video_masks_to_yolo(val_input_dir, val_output_dir, min_area=200)
