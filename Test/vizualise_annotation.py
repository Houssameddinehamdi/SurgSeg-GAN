import os
import cv2
import numpy as np

def visualize_yolo_annotations(image_dir, label_dir, output_dir):
    """
    Visualizes YOLO format annotations by overlaying polygons on images.
    
    Parameters:
        image_dir (str): Path to the directory containing the original images.
        label_dir (str): Path to the directory containing YOLO label files.
        output_dir (str): Path to save the visualization images.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all label files
    for label_name in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_name)

        if not label_name.endswith('.txt'):
            print(f"Skipping non-label file: {label_name}")
            continue

        # Find the corresponding image
        base_name = os.path.splitext(label_name)[0]
        image_path = os.path.join(image_dir, f"{base_name}.png")  # Change extension if necessary
        if not os.path.exists(image_path):
            print(f"Image not found for label: {label_name}")
            continue

        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error reading image: {image_path}")
            continue

        H, W, _ = image.shape

        # Read the label file
        with open(label_path, 'r') as f:
            lines = f.readlines()

        # Overlay polygons
        for line in lines:
            data = line.strip().split()
            class_id = int(data[0])
            points = np.array(data[1:], dtype=np.float32).reshape(-1, 2)  # (x, y) pairs

            # Convert normalized points back to image coordinates
            points[:, 0] *= W  # Denormalize X
            points[:, 1] *= H  # Denormalize Y
            points = points.astype(np.int32)

            # Draw the polygon
            color = (0, 255, 0) if class_id == 0 else (0, 0, 255)  # Green for background, Red for other classes
            cv2.polylines(image, [points], isClosed=True, color=color, thickness=2)
            cv2.putText(image, f"Class {class_id}", tuple(points[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        # Save the visualization
        output_path = os.path.join(output_dir, f"{base_name}_viz.png")
        cv2.imwrite(output_path, image)
        print(f"Saved visualization: {output_path}")

# Define paths
image_dir = r"D:\Dataset_parts\Dataset_cls_exclude\images\val"  # Path to images
label_dir = r"D:\Dataset_parts\Dataset_cls_exclude\labels\val"  # Path to YOLO labels
output_dir = r"D:\Dataset_parts\Visualized_Masks2\val"  # Path to save visualizations

# Visualize the YOLO annotations
visualize_yolo_annotations(image_dir, label_dir, output_dir)
