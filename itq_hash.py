import numpy as np
from sklearn.decomposition import PCA
from itq import ITQ

class ImageHasher:
    def __init__(self):
        self.itq = ITQ(bits=32)

    def train_itq(self, frame_paths):
        """ Extract features and train ITQ hashing model. """
        features = np.random.rand(len(frame_paths), 4096)  # Simulated feature extraction

        # Fix PCA component selection
        n_components = min(32, features.shape[1])  
        pca = PCA(n_components=n_components)
        reduced_features = pca.fit_transform(features)

        print(f"✅ PCA Output Shape: {reduced_features.shape}")

        binary_codes = self.itq.fit(reduced_features)
        return {frame: binary_codes[i] for i, frame in enumerate(frame_paths)}
