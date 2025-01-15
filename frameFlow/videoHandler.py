import asyncio
import cv2
from cv2 import VideoCapture
import requests

# GET THE PATHS OF THE VIDEOS

video_1_path = "videos/video1.webm"
video_2_path = "videos/video2.webm"
video_3_path = "videos/video3.webm"
video_4_path = "videos/video4.webm"


# CAPTURE THE VIDEOS

cap1 = VideoCapture(video_1_path)

cap2 = VideoCapture(video_2_path)

cap3 = VideoCapture(video_3_path)

cap4 = VideoCapture(video_4_path)



# check the ability of opening a video
def videoAbleToOpen(cap):
  if  cap.isOpened():
      return True




# send data to the process service via http
def sendData(image):
    try:
        # make the request
        response = requests.post(
            "http://127.0.0.1:8000/detect/",
            files={"file": ("image.jpg", image, "image/png")},
        )
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data: {e}")


def detect(cap):
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("End of video or error reading the frame.")
                break
            _, buffer = cv2.imencode('.png', frame)

            # call the send frame method
            sendData(frame.tobytes())

    finally:
        cap.release()
