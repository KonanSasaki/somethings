import pyautogui as pg
import time
count = 0
while True:
    pg.click(491 , 1011)
    time.sleep(5)
    pg.click(476,696)
    time.sleep(180)
    pg.click(189,218)
    time.sleep(5)
    count += 1
    if(count > 90):
        break