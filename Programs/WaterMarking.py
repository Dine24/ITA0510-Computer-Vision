import cv2  
logo = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\Capybara.PNG") 
img = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\images.jpeg")  
h_logo, w_logo, _ = logo.shape 
h_img, w_img, _ = img.shape 

center_y = int(h_img/2) 
center_x = int(w_img/2) 

top_y = center_y - int(h_logo/2) 
left_x = center_x - int(w_logo/2) 
bottom_y = top_y + h_logo 
right_x = left_x + w_logo 
destination = img[top_y:bottom_y, left_x:right_x] 
result = cv2.addWeighted(destination, 1, logo, 1, 0)

img[top_y:bottom_y, left_x:right_x] = result 
cv2.imwrite("watermarked.jpg", img) 
cv2.imshow("Watermarked Image", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
