
from fastapi import FastAPI


from videoHandler import cap1, videoAbleToOpen, detect, cap2, cap3

app = FastAPI()






result = input("type start")
if result == "start":
    detect(cap3)





