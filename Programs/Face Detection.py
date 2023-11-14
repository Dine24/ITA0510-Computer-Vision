import cv2
img = cv2.imread(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\WhatsApp Image 2023-11-14 at 14.22.17_ec694523.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade =cv2.CascadeClassifier(r"C:\Users\tamil\Downloads\haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Faces Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
