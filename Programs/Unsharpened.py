import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\7c40f4f9831d17c590776c8ad60ea7c0.jpg")
image_float = np.float32(image)

blur = cv2.GaussianBlur(image_float, (0, 0), sigmaX=5)
unsharp_mask = cv2.addWeighted(image_float, 2.5, blur, -1.5, 0)
sharpened_image = cv2.convertScaleAbs(unsharp_mask)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image (Unsharp Masking)', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
