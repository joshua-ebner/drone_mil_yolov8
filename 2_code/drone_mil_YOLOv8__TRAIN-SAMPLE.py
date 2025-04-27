from ultralytics import YOLO
import os

# Move working directory up one level
os.chdir("..")

# Load YOLOv8n and start training
model = YOLO("yolov8n.pt")

model.train(
    data="1_data/z_SAMPLE/data_sample_500.yaml",  # correct relative path from project root
    epochs=5,
    imgsz=640,
    batch=16,
    name="drone-yolov8n-sample"
)