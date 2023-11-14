import cv2
import numpy as np

def high_boost_filter(image_path, boost_factor):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.GaussianBlur(original_image, (5, 5), 0)
    high_boost_image = original_image + boost_factor * (original_image - blurred_image)
    high_boost_image = np.clip(high_boost_image, 0, 255).astype(np.uint8)
    cv2.imshow('Original Image', original_image)
    cv2.imshow('High-Boost Image', high_boost_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    image_path = r"C:\Users\tamil\OneDrive\Documents\Computer Vision\7c40f4f9831d17c590776c8ad60ea7c0.jpg"
    boost_factor = 2.0
    high_boost_filter(image_path, boost_factor)
