import cv2
path=r"C:\Users\tamil\Downloads\Spider-Man_Miles_Morales.jpeg"
src = cv2.imread(path)
window_name = '180 Degrees'
window_name2='90 Degrees'
image = cv2.rotate(src, cv2.ROTATE_180)
image2=cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image)
cv2.imshow(window_name2,image2)
cv2.waitKey(0)
