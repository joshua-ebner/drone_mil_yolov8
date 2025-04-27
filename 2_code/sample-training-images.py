import os
import random
import shutil



# === CONFIG ===
PROJECT_DIRECTORY = "/Users/je/Documents/1_work/3_side-projects/1_computer-vision/drone_mil_yolov8"
SOURCE_IMAGES_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "1_data/train/images")
SOURCE_LABELS_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "1_data/train/labels")
DEST_IMAGES_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "1_data_small/train/images")
DEST_LABELS_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "1_data_small/train/labels")
SAMPLE_SIZE = 500  # adjust as needed

# === Setup target dirs ===
os.makedirs(DEST_IMAGES_DIRECTORY, exist_ok=True)
os.makedirs(DEST_LABELS_DIRECTORY, exist_ok=True)

# === Get list of all image files ===
images = []
for f in os.listdir(SOURCE_IMAGES_DIRECTORY):
    if f.endswith(".jpg"):
        images.append(f)


# SAMPLE IMAGES
sampled = random.sample(images, SAMPLE_SIZE)

for img_file in sampled:
    label_file = img_file.replace(".jpg", ".txt")

    # Copy image
    shutil.copy2(os.path.join(SOURCE_IMAGES_DIRECTORY, img_file)
                 ,os.path.join(DEST_IMAGES_DIRECTORY, img_file)
                 )

    # Copy label
    shutil.copy2(os.path.join(SOURCE_LABELS_DIRECTORY, label_file)
                 ,os.path.join(DEST_LABELS_DIRECTORY, label_file)
                 )


print(f"✅ Copied {SAMPLE_SIZE} images and labels to {DEST_IMAGES_DIRECTORY} and {DEST_LABELS_DIRECTORY}")