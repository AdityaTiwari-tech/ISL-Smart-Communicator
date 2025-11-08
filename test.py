# python
import os
DATA_PATH = "C:/Users/Rishi/Desktop/project/Indian-Sign-Language-Recognition-System/data_images"
for cls in sorted(os.listdir(DATA_PATH)):
    cls_path = os.path.join(DATA_PATH, cls)
    if os.path.isdir(cls_path):
        print(cls, len([f for f in os.listdir(cls_path) if os.path.isfile(os.path.join(cls_path, f))]))