import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\7c40f4f9831d17c590776c8ad60ea7c0.jpg")
kernel = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]], dtype=np.float32)
sharpened_image = cv2.filter2D(image, -1, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
