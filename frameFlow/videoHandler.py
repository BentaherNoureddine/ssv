import asyncio
import cv2
from cv2 import VideoCapture
import requests

# GET THE PATHS OF THE VIDEOS

video_1_path = "videos/video1.mp4"
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
def sendData(frame,i):
    try:

        # Encode the frame as PNG
        _, image = cv2.imencode('.png', frame)

        # make the request
        response = requests.post(
            "http://127.0.0.1:8080/detect/",
            files={"file": ("image.png", image.tobytes(), "image/png")},
            params={"frame_number": i},
        )
        print(response.json(),i)
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data: {e}")


def detect(cap):
    i = 1
    try:

        while True:
            ret, frame = cap.read()
            if not ret:
                print("End of video or error reading the frame.")
                break
            # call the send frame method
            sendData(frame,i)
            i+=1

    finally:
        print("TOTAL FRAMES NUMBER: ", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
        print("FRAMES PROCESSED NUMBER = ", i)
        cap.release()
