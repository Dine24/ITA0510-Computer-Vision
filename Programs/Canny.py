import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\shutterstock_509463667.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 100, 200)  
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imwrite('edges_detected.jpg', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
