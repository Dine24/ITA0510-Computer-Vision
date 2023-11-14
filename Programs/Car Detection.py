import cv2

def detect_cars_cascade_video(video_path):
    car_cascade = cv2.CascadeClassifier(r"C:\Users\tamil\OneDrive\Documents\Computer Vision\cars.xml")
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(10, 25))

        # Draw bounding boxes around detected cars
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow("Car Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Example usage:
if __name__ == "__main__":
    video_path=r"C:\Users\tamil\OneDrive\Documents\Computer Vision\WhatsApp Video 2023-11-14 at 14.32.41_06f42d27.mp4"
    detect_cars_cascade_video(video_path)
