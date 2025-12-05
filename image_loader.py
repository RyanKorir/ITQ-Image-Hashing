import cv2

def load_image(image_path):
    """ Loads and preprocesses an image. """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return img.flatten()
