Drone-mil YOLOv8

Light-weight drone detection pipeline trained on the public drone_mil dataset and optimized for real-time inference (< 20 ms) on edge hardware (e.g., NVIDIA Jetson).


PROJECT STRUCTURE

1_data/         # dataset + YAML
2_code/         # training & utilities 
3_scripts/      # runnable shell entry-points 
4_logs/         # training logs, curves 
5_predictions/  # sample inference outputs 
.gitignore 
README.md


DATASET
The project uses the drone_mil dataset (Roboflow CC BY 4.0 license).

7,261 images (640x640 resolution)
1 class: drone
A smaller 500-image sample is also provided under 1_data/z_SAMPLE/ for quick experiments.


QUICK START
Set up environment:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

TRAIN MODEL
bash 3_scripts/train-full.sh # Train on full dataset
bash 3_scripts/train-sample.sh # Train on sample dataset


RUN INFERENCE
bash 3_scripts/predict-image.sh path/to/image.jpg # Predict single image
bash 3_scripts/predict-image.sh path/to/images/ # Predict folder of images

Predicted images will be saved into runs/detect/predict/.


RESULTS (YOLOv8 as of April 27, 2025)
Validation Set (1345 images):
 Precision: 0.978
 Recall: 0.961
 mAP@50: 0.984
 mAP@50-95: 0.719

Test Set (678 images):
 Precision: 0.962
 Recall: 0.961
 mAP@50: 0.979
 mAP@50-95: 0.722
 
Training curves and metrics are available in 4_logs/.


LICENSE
Code: Copyright 2025 Josh E.
Dataset: Roboflow CC BY 4.0 License (see 1_data/README.roboflow.txt)