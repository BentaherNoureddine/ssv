import cv2
from fastapi import FastAPI
from starlette.responses import StreamingResponse

from videoHandler import cap1, videoAbleToOpen, detect, cap2, cap3

app = FastAPI()



# ENDPOINT TO RETURN FRAMES


#result = input("type start")

#if(result == "start"):
    #getFrames(cap1)


result = input("type start")
if result == "start":
    detect(cap3)







@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
