from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

time.sleep(4)

im1 = pyautogui.screenshot(region=(547,128,248,35))
im1.save(r"C:\Users\Shubh\OneDrive\Desktop\Coding\Safari Magikarp\testing files\savedimage.png")


#top left X:  547 Y:  120 RGB: (253, 253, 253)
#top right X:  795 Y:  120 RGB: (253, 253, 253)
#bottem right X:  800 Y:  155 RGB: (253, 253, 253)
