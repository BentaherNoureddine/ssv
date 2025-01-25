from fastapi import FastAPI, UploadFile, File, Query
from ultralytics import YOLO
import cv2
import numpy as np


app = FastAPI()

# Load the YOLO model
model = YOLO("models/yolov8n.pt")



@app.post("/detect/")
async def detect_faces(file: UploadFile = File(...),videoName:str=Query(...)):
    # Read the contents of the uploaded file asynchronously
    contents = await file.read()

    # Convert the binary content of the file into a NumPy array
    nparr = np.frombuffer(contents, np.uint8)

    # Decode the NumPy array into an image (OpenCV format)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Run the YOLO model on the image to detect objects
    results = model(img)

    # Initialize an empty list to store the bounding box coordinates of detected objects
    objects = []

    # Loop through each result of the detected objects (bounding boxes and their properties)
    for result in results:
        # Loop through all the detected bounding boxes in the result
        for box in result.boxes:
            # Extract the coordinates (x1, y1, x2, y2) of the bounding box and convert them to integers
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            print({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

            # Append the coordinates of the bounding box to the 'objects' list in dictionary format
            objects.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    print("object detected")


    if len(objects) > 0:
        return {"video_name":videoName,"object(s) detected": objects}
    else:
        return {}
