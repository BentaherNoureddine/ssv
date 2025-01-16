import threading
from fastapi import FastAPI
from videoHandler import cap1, videoAbleToOpen, detect, cap2, cap3, cap4

app = FastAPI()


def run_detection(cap):
    detect(cap)


@app.get("/detect")
async def start_detection():
    # Start threads for each video capture
    threads = []
    for cap in [cap1, cap2, cap3, cap4]:
        thread = threading.Thread(target=run_detection, args=(cap,))
        threads.append(thread)
        thread.start()

    # Join the threads to wait for them to finish
    for thread in threads:
        thread.join()

    return {"status": "Detection started on all video streams."}
