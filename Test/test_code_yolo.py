from ultralytics import YOLO

model_best = YOLO(r"C:\Users\lenovo\runs\segment\train36\weights\best.pt")

# Perform inference on the test dataset
test_results = model_best.predict(source=r"D:\Dataset_parts\test_data-20250106T080124Z-001\test_data\seq_2\left_frames", save=True)