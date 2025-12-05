import shutil
import os

frames_folder = "frames"

if os.path.exists(frames_folder):
    shutil.rmtree(frames_folder)
    print(f"✅ Deleted folder: {frames_folder}")
else:
    print("❌ No frames folder found.")
