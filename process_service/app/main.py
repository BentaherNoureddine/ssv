from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import cv2
import numpy as np

# Initialiser FastAPI
app = FastAPI()

# Charger le modèle
model = YOLO("models/yolov8n.pt")

@app.get("/")
async def root():
    return {"message": "YOLOv8 Face Detection API is running"}

@app.post("/detect/")
async def detect_faces(file: UploadFile = File(...)):
    # Lire l'image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Faire la détection
    results = model(img)

    # Extraire les coordonnées des visages détectés
    faces = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            faces.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    print("face detected")
    return {"faces_detected": faces}
