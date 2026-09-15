#from PIL import ImageGrab
#from functools import partial
import pyautogui as pg
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, 'img.png')

print(pg.size())

while(1):
    # print("position: ", str(pg.position()))

    try:
        center = pg.locateOnScreen(img_path, confidence=0.8)
    except pg.ImageNotFoundException:
        center = None
    if center is not None:
        point = pg.center(center)
        print("center: " + str(center))
        pg.click(point.x, point.y)
    time.sleep(2)
    

