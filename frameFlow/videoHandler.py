import cv2
from cv2 import VideoCapture
import requests


# GET THE PATHS OF THE VIDEOS

video_1_path = "videos/video1.mp4"
video_2_path = "videos/video2.webm"
video_3_path = "videos/video3.webm"
video_4_path = "videos/video4.webm"


# CAPTURED VIDEO SCHEMA
class Cap:
    def __init__(self, videoCapture, videoName):
        self.videoCapture = videoCapture
        self.videoName = videoName



# CAPTURE THE VIDEOS

cap1 = Cap(VideoCapture(video_1_path), videoName="video1.mp4")
cap2 = Cap(VideoCapture(video_2_path), videoName="video2.webm")
cap3 = Cap(VideoCapture(video_3_path), videoName="video3.webm")
cap4=  Cap(VideoCapture(video_4_path), videoName="video4.webm")



# check the ability of opening a video
def videoAbleToOpen(cap):
  if  cap.isOpened():
      return True




# send data to the process service via http
def sendData(frame,video_name, i):
    try:
        # Encode the frame as PNG
        _, image = cv2.imencode('.jpg', frame)

        # make the request
        response = requests.post(
            "http://127.0.0.1:8080/detect/",
            files={"file": ("image.jpg", image.tobytes(), "image/jpeg")},
            params={"frame_number": i,"videoName": video_name},
        )

        # Increment i and return the updated value
        if response.status_code == 200:
            i+=1
        print(response.json(), i)
        return i
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data: {e}")
        return i

# READ VIDEO PASSED IN THE PARAMETERS THEN SEND EACH FRAME USING SEND DATA METHOD
def detect(stCap):
    i = 0
    try:
        while True:
            ret, frame = stCap.videoCapture.read()
            if not ret:
                print("End of video or error reading the frame.")
                break
            # Call sendData and update i with the return value
            i = sendData(frame, stCap.videoName, i)

    finally:
        print("VIDEO NAME " + stCap.videoName)
        print("TOTAL FRAMES NUMBER: ", int(stCap.videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)))
        print("FRAMES PROCESSED NUMBER = ", i)
        stCap.videoCapture.release()
