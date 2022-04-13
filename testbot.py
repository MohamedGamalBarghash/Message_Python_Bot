import pyautogui as pg
import time as t

t.sleep(10)

txt = open("animals.txt", 'r')

for i in txt:
    pg.write("This is a "+i)
    pg.press("Enter")