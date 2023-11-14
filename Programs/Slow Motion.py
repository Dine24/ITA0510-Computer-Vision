import cv2
import numpy as np
cap = cv2.VideoCapture(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\WhatsApp Video 2023-11-14 at 13.13.57_6b4ff839.mp4")
if (cap.isOpened()== False):
          Print("Error opening video file")
while(cap.isOpened()):
          ret, frame = cap.read()
          if ret == True:
              cv2.imshow('Frame', frame)
              if cv2.waitKey(250) & 0xFF == ord('q'):
                         break
          else:
                 break
cap.release()
cv2.destroyAllWindows()
