import os
import shutil

# Define the base directory of your dataset and the output path
base_dir = r"C:\Users\lenovo\Desktop\Dataset_parts\Gathered_Dataset"
output_path = r"C:\Users\lenovo\Desktop\Dataset_parts\Organized_dataset"

# Create the images and labels directories in the output path
images_dir = os.path.join(output_path, "images")
labels_dir = os.path.join(output_path, "labels")
os.makedirs(images_dir, exist_ok=True)
os.makedirs(labels_dir, exist_ok=True)

# Iterate through each sequence
for seq_num in range(1, 17):
    seq_folder = os.path.join(base_dir, f"seq_{seq_num}")
    
    # Define the paths for left and right frames and labels
    left_frames_dir = os.path.join(seq_folder, "left_frames")
    right_frames_dir = os.path.join(seq_folder, "right_frames")
    labels_dir_seq = os.path.join(seq_folder, "labels")
    
    # Check if the labels directory exists before proceeding
    if not os.path.exists(labels_dir_seq):
        print(f"Labels directory missing for seq_{seq_num}, skipping this sequence.")
        continue
    
    # Get the labels for both left and right frames (they are the same)
    label_files = os.listdir(labels_dir_seq)
    
    # Process left frames
    for file_name in os.listdir(left_frames_dir):
        left_file_path = os.path.join(left_frames_dir, file_name)
        if os.path.isfile(left_file_path):
            # Copy and rename left frame
            new_image_name = f"seq{seq_num}_left_{file_name}"
            shutil.copy(left_file_path, os.path.join(images_dir, new_image_name))
            
            # Copy and rename the corresponding label file
            for label_file in label_files:
                label_file_path = os.path.join(labels_dir_seq, label_file)
                if os.path.isfile(label_file_path):
                    new_label_name = f"seq{seq_num}_left_{label_file}"
                    shutil.copy(label_file_path, os.path.join(labels_dir, new_label_name))
    
    # Process right frames
    for file_name in os.listdir(right_frames_dir):
        right_file_path = os.path.join(right_frames_dir, file_name)
        if os.path.isfile(right_file_path):
            # Copy and rename right frame
            new_image_name = f"seq{seq_num}_right_{file_name}"
            shutil.copy(right_file_path, os.path.join(images_dir, new_image_name))
            
            # Copy and rename the corresponding label file
            for label_file in label_files:
                label_file_path = os.path.join(labels_dir_seq, label_file)
                if os.path.isfile(label_file_path):
                    new_label_name = f"seq{seq_num}_right_{label_file}"
                    shutil.copy(label_file_path, os.path.join(labels_dir, new_label_name))

print("Images and labels have been successfully merged and renamed.")
