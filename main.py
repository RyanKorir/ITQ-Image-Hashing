from retrieval import find_matching_video

frames_folder = "frames"

print("✅ Running ITQ-based Video Retrieval...")
matches = find_matching_video(frames_folder)

print(f"✅ Best match found: {matches}")
