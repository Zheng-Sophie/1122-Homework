import cv2
import datetime
import time

def capture_photos(num_photos):
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Loop to capture specified number of photos
    for i in range(num_photos):
        # Capture a frame
        ret, frame = cap.read()

        if ret:
            # Generate a timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            # Save the captured frame with a date-based name
            filename = f"captured_photo_{timestamp}.jpg"
            cv2.imshow("Captured Photo", frame)
            cv2.imwrite(filename, frame)
            print(f"Photo {i+1} saved as {filename}")
        time.sleep(1)
    # Release the webcam
    cap.release()

if __name__ == "__main__":
    # Specify the number of photos to capture
    num_photos = 3
    capture_photos(num_photos)