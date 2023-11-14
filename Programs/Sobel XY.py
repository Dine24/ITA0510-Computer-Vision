import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\Capybara.PNG", cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
abs_sobel_x = np.abs(sobel_x)
sobel_x = np.uint8(abs_sobel_x)

sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
abs_sobel_y = np.abs(sobel_y)
sobel_y = np.uint8(abs_sobel_y)

edge_image = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('Original Image', image)
cv2.imshow('Edge-Detected Image', edge_image)
cv2.imwrite('edge_detected_image.jpg', edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
