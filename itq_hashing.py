import argparse
from retrieval import find_matching_video

parser = argparse.ArgumentParser()
parser.add_argument("--image", required=True, help="Path to the query image")
parser.add_argument("--compare", required=True, help="Path to the frames folder")
args = parser.parse_args()

best_match, distance = find_matching_video(args.image, args.compare)
print(f"✅ Closest frame: {best_match} (Distance: {distance})")
