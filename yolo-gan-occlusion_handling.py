from ultralytics import YOLO

model_best = YOLO(r"D:\Dataset_parts\gan_yolo11n_seg1.pt")

# Perform inference on the test dataset
test_results = model_best.predict(source=r"D:\Dataset_parts\test_data-20250106T080124Z-001\test_data\seq_3\left_frames", save=True, save_dir = r"D:\Dataset_parts\results")