# ITQ-Image-Hashing
ITQ-Based Image Hashing System
Project Overview

This project implements an ITQ (Iterative Quantization) based image hashing system for efficient image retrieval. The system converts high-dimensional image feature vectors into compact binary hash codes using PCA and ITQ, enabling fast similarity searches in large-scale image datasets.

The project supports:

Image feature extraction

Dimensionality reduction using PCA

Binary hashing using ITQ

Efficient retrieval using Hamming distance

This system can be used for image search, content-based image retrieval (CBIR), and multimedia database management.

Features

High-dimensional feature handling: Extracts features from images using standard methods (e.g., raw pixel values or CNN embeddings).

Dimensionality reduction: PCA reduces feature dimensions while preserving variance.

Iterative Quantization (ITQ): Converts reduced features into binary codes with minimal quantization error.

Fast retrieval: Hamming distance allows rapid similarity comparison.

Modular design: Each component (feature extraction, PCA, ITQ, retrieval) is modular and can be replaced or enhanced.

Project Structure
ITQ-Image-Hashing/
│
├── data/                  # Image datasets for testing
├── itq/                   # ITQ algorithm implementation
│   ├── itq.py             # ITQ hashing functions
│   └── pca.py             # PCA-based dimensionality reduction
├── examples/              # Example scripts to test retrieval
│   └── test_retrieval.py
├── utils/                 # Utility functions
│   └── feature_extraction.py
├── README.md
└── requirements.txt       # Python dependencies

Installation

Clone the repository:

git clone https://github.com/yourusername/ITQ-Image-Hashing.git
cd ITQ-Image-Hashing


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows


Install required dependencies:

pip install -r requirements.txt

Usage
1. Feature Extraction

Extract features from images (e.g., flatten or CNN embeddings):

from utils.feature_extraction import extract_features

features = extract_features('data/sample_images')

2. Dimensionality Reduction with PCA

Reduce feature dimensionality:

from itq.pca import PCA_Reduction

reduced_features = PCA_Reduction(features, n_components=32)

3. ITQ Hashing

Generate binary hash codes:

from itq.itq import ITQ

binary_codes = ITQ(reduced_features, num_iterations=50)

4. Image Retrieval

Retrieve similar images using Hamming distance:

from utils.feature_extraction import compute_hamming_distance

query_code = binary_codes[0]
distances = compute_hamming_distance(query_code, binary_codes)
top_indices = distances.argsort()[:5]   # Get top 5 similar images

Dependencies

Python >= 3.8

NumPy

SciPy

scikit-learn

OpenCV (optional, if using images as input)

Install via:

pip install numpy scipy scikit-learn opencv-python

Example

To test the system on your image dataset:

python examples/test_retrieval.py


This script:

Loads the images from data/

Extracts features

Performs PCA

Generates ITQ hash codes

Retrieves top similar images for a query

References

Gong, Y., et al. “Iterative Quantization: A Procrustean Approach to Learning Binary Codes for Large-Scale Image Retrieval.” IEEE Transactions on Pattern Analysis and Machine Intelligence, 2013.

Wang, J., et al. “Hashing for Similarity Search: A Survey.” IEEE Transactions on Pattern Analysis and Machine Intelligence, 2016.

License

This project is licensed under the MIT License. See LICENSE for details.
