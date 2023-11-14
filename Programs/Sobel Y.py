import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\Capybara.PNG", cv2.IMREAD_GRAYSCALE)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = np.abs(sobel_y)
sobel_y = np.uint8(sobel_y)
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
