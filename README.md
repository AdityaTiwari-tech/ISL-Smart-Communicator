# ISL-Smart-Communicator
# ISL Smart Communicator

Lightweight Indian Sign Language (ISL) recognition and demo application.  
Uses MediaPipe for hand/keypoint detection and a TensorFlow model for classifying signs (A–Z, 0–9, delete, space).

## Features
- Real-time hand/keypoint capture (MediaPipe)
- Model inference (TensorFlow / TFLite)
- GUI demo (Tkinter + Pillow)
- Training pipeline that uses disk-based generators to avoid MemoryError

## Requirements
- Windows 10/11
- Python 3.10 or 3.11 (recommended)
- Git
- Optional: conda

Key Python packages:
- tensorflow (or tflite-runtime)
- mediapipe
- opencv-python
- Pillow
- numpy
- scikit-learn
- pyttsx3 (optional, text-to-speech)

## Setup (recommended: venv)
PowerShell (run from project root: C:\Users\Rishi\Desktop\project):

1. Install Python 3.11 from python.org, then:
```powershell
cd 'C:\Users\Rishi\Desktop\project'
C:\Path\To\Python311\python.exe -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
If using conda:
```powershell
conda create -n isl python=3.11 -y
conda activate isl
conda install -c conda-forge mediapipe opencv pillow numpy -y
python -m pip install tensorflow pyttsx3 scikit-learn
```

## Git / Large files
- Do NOT commit dataset or large model files. Add these to `.gitignore`:
```
Indian-Sign-Language-Recognition-System/data_images/
Indian-Sign-Language-Recognition-System/*.h5
models/
```
- If you need to store large model files in the repo, use Git LFS:
```powershell
git lfs install
git lfs track "*.h5"
git add .gitattributes
git commit -m "Use Git LFS for model files"
```

## Usage
- Run demo:
```powershell
# inside activated venv
python .\Indian-Sign-Language-Recognition-System\Script.py
```
- Train / evaluate: open the notebook `Indian_sign_language_Mobilenetv2.ipynb`.
  - Use disk-based generators (ImageDataGenerator or tf.data) to avoid loading all images into memory.
  - Example pattern: build a DataFrame of filepaths + labels and use flow_from_dataframe.

## Notes / Troubleshooting
- MemoryError when using in-memory arrays: switch to generators (ImageDataGenerator.flow_from_directory or image_dataset_from_directory).
- mediapipe and tensorflow may not have wheels for very new Python versions — use Python 3.10/3.11 or conda.
- If Script.py fails on imports, activate the correct venv and reinstall dependencies.

## Model distribution
Large model files are not included in repo. Upload trained models to:
- GitHub Releases, or
- Cloud storage (Google Drive / OneDrive) and add download link in README.

## License
MIT (add LICENSE file if desired)

## Contact
Project repository: https://github.com/AdityaTiwari-tech/ISL-Smart-Communicator
