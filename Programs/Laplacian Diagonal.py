import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\jellyfish-memory-learning-neuroscience.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplacian_kernel = np.array([[1, 1, 1],
                             [1, -8, 1],
                             [1, 1, 1]], dtype=np.float32)
sharpened_image = cv2.filter2D(gray_image, -1, laplacian_kernel)
sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imwrite('sharpened_image.jpg', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
