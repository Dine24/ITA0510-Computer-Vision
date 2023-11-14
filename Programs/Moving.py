import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\941898.jpg")
x = 100 
y = 100 
dx = 50  
dy = 30  
while True:
    image_copy = image.copy()
    x += dx
    y += dy
    cv2.imshow('Moving Image', image_copy)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
