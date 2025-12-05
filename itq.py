import numpy as np

class ITQ:
    def __init__(self, bits=32, iterations=50):
        self.bits = bits
        self.iterations = iterations
        self.R = None  

    def fit(self, data):
        """ Performs ITQ optimization for hashing. """
        num_samples, num_features = data.shape

        if num_samples < self.bits:
            raise ValueError(f"❌ Not enough samples for PCA. At least {self.bits} needed, but got {num_samples}.")

        # Initialize random rotation matrix
        self.R = np.random.randn(self.bits, self.bits)
        U, _, Vt = np.linalg.svd(self.R)
        self.R = U[:, :self.bits]

        for _ in range(self.iterations):
            Z = data @ self.R  # Ensure correct multiplication (2300, 32) @ (32, 32)
            UX = np.sign(Z)
            U, _, Vt = np.linalg.svd(UX.T @ data)
            self.R = U @ Vt

        return np.sign(data @ self.R)  # Return binary hash
