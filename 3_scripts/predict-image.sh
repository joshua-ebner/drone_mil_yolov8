#!/bin/bash

# === CONFIG ===
MODEL_PATH="runs/detect/drone-yolov8n/weights/best.pt"
SOURCE_PATH="$1"    # Input command line argument (image OR folder)
CONFIDENCE=0.25

# === Input Validation ===
if [ -z "$1" ]; then
  echo "Error: No source path provided."
  echo "Usage: bash predict-image.sh path/to/image.jpg OR path/to/folder/"
  exit 1
fi

# === RUN YOLO PREDICT ===
yolo predict model=$MODEL_PATH source="$SOURCE_PATH" conf=$CONFIDENCE save=True