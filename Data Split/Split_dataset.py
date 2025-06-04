import os
import shutil
import random

# Define paths
base_path = r"C:\Users\lenovo\Desktop\Dataset_parts\Organized_dataset"
images_path = os.path.join(base_path, "images")
labels_path = os.path.join(base_path, "labels")

train_images_path = os.path.join(base_path, "train", "images")
train_labels_path = os.path.join(base_path, "train", "labels")
val_images_path = os.path.join(base_path, "val", "images")
val_labels_path = os.path.join(base_path, "val", "labels")

# Create directories if they don't exist
os.makedirs(train_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# Get list of all files
image_files = sorted(os.listdir(images_path))
label_files = sorted(os.listdir(labels_path))

# Ensure images and labels correspond
assert len(image_files) == len(label_files), "Number of images and labels must match."

# Shuffle and split
combined = list(zip(image_files, label_files))
random.shuffle(combined)

split_idx = int(0.8 * len(combined))
train_files = combined[:split_idx]
val_files = combined[split_idx:]

# Move files to respective directories
for img_file, lbl_file in train_files:
    shutil.move(os.path.join(images_path, img_file), train_images_path)
    shutil.move(os.path.join(labels_path, lbl_file), train_labels_path)

for img_file, lbl_file in val_files:
    shutil.move(os.path.join(images_path, img_file), val_images_path)
    shutil.move(os.path.join(labels_path, lbl_file), val_labels_path)

print("Dataset split completed successfully.")
