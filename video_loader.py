import cv2
import os

def extract_frames(video_path, output_folder="frames"):
    os.makedirs(output_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_folder}/frame_{frame_count}.jpg", frame)
        frame_count += 1

    cap.release()
    print(f"✅ Extracted {frame_count} frames from {video_path}")

if __name__ == "__main__":
    extract_frames("videos/sample.mp4")
