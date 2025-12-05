from itq_hash import ImageHasher

def find_matching_video(frames_folder):
    """ Finds the best matching frame for a query image. """
    hasher = ImageHasher()
    
    frame_paths = [f"{frames_folder}/frame_{i}.jpg" for i in range(2300)]  # Simulated frame paths
    binary_codes = hasher.train_itq(frame_paths)
    
    best_match = min(binary_codes, key=lambda x: sum(binary_codes[x]))  # Find closest match
    return best_match
