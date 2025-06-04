from ultralytics import YOLO
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

def train_model():
    
# Load a pretrained YOLO11 model
# Load a pretrained YOLOv8-segmentation model
    model = YOLO("yolo11n-seg.yaml")  # Use a built-in segmentation model
    model.train(data="D:\Dataset_parts\config.yaml", epochs=200, imgsz=640, batch=16)    

# Evaluate the model's performance on a validation set
    model.val(data="D:\Dataset_parts\config.yaml")

# Save the trained model
    model.save("D:\Dataset_parts\2018_1.pt")
 
if __name__ == "__main__":
    train_model()