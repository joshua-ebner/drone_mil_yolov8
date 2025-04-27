from ultralytics import YOLO
import os

# Move working directory up one level
os.chdir("..")

# Load YOLOv8n and start training
model = YOLO("yolov8n.pt")

model.train(
    data="1_data/data.yaml",  # correct relative path from project root
    epochs=50,
    imgsz=640,
    batch=16,
    name="drone-yolov8n"
)