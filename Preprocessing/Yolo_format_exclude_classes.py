import os
import cv2
import numpy as np

def convert_video_masks_to_yolo(input_dir, output_base_dir, min_area=200):
    """
    Converts segmentation masks for multiple videos to YOLO format, where ignored classes are treated as background.
    
    Parameters:
        input_dir (str): Path to the base directory containing segmentation masks.
        output_base_dir (str): Path to save YOLO label files.
        min_area (int): Minimum contour area to include (default: 200 pixels).
    """
    os.makedirs(output_base_dir, exist_ok=True)

    # Define colors for the classes to ignore
    colors_to_ignore = [
        [0, 255, 0],        # Instrument-Shaft
        [24, 55, 125],      # Covered-Kidney
        [123, 15, 175],     # Suction-Instrument
        [124, 155, 5],      # Small-Intestine
        [12, 255, 141]      # Ultrasound-Probe
    ]

    # Background class ID
    background_class_id = 0

    # Iterate over all the files in the input directory
    for mask_name in os.listdir(input_dir):
        mask_path = os.path.join(input_dir, mask_name)

        if not mask_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            print(f"Skipping non-image file: {mask_name}")
            continue

        # Load the colored mask
        mask = cv2.imread(mask_path)
        if mask is None:
            print(f"Error reading file: {mask_path}")
            continue

        H, W, _ = mask.shape

        # Get the unique colors in the mask
        unique_colors = np.unique(mask.reshape(-1, mask.shape[2]), axis=0)

        # Map colors to class IDs
        color_to_class = {}
        class_id = 1  # Start from 1, reserving 0 for the background
        for color in unique_colors:
            color_list = color.tolist()
            if color_list in colors_to_ignore:
                color_to_class[tuple(color)] = background_class_id  # Assign ignored colors to background
            else:
                color_to_class[tuple(color)] = class_id
                class_id += 1

        polygons = []

        # Process each unique color
        for color, class_id in color_to_class.items():
            color_mask = np.all(mask == color, axis=-1).astype(np.uint8) * 255
            contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                if cv2.contourArea(cnt) > min_area:
                    polygon = []
                    for point in cnt:
                        x, y = point[0]
                        polygon.append(x / W)  # Normalize X
                        polygon.append(y / H)  # Normalize Y
                    polygons.append((class_id, polygon))

        # Write YOLO label file
        base_name = os.path.splitext(mask_name)[0]
        output_file = os.path.join(output_base_dir, f"{base_name}.txt")

        with open(output_file, 'w') as f:
            for class_id, polygon in polygons:
                f.write(f"{class_id} ")
                f.write(' '.join(map(str, polygon)))
                f.write('\n')

        print(f"Processed {mask_name}, saved to {output_file}")

# Define input directories for training and validation labels
train_input_dir = r"D:\Dataset_parts\Datasplit\train\labels"
val_input_dir = r"D:\Dataset_parts\Datasplit\val\labels"

# Define output directories for YOLO label files
train_output_dir = r"D:\Dataset_parts\YOLO_Converted_Masks_new\train"
val_output_dir = r"D:\Dataset_parts\YOLO_Converted_Masks_new\val"

# Process both training and validation directories
convert_video_masks_to_yolo(train_input_dir, train_output_dir, min_area=200)
convert_video_masks_to_yolo(val_input_dir, val_output_dir, min_area=200)
