import cv2
from ultralytics import YOLO

# Charger le modèle YOLOv8
model = YOLO("models/yolov8n.pt")

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Détection des visages
    results = model(frame)

    # Dessiner les boîtes autour des visages détectés
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Afficher le flux vidéo
    cv2.imshow("YOLOv8 Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
