"""NOTES:
Landed a Pokémon!
Not even a nibble...

"""
import pyautogui
from PIL import Image
from pytesseract import *
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con




time.sleep(2)



time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def catchPokemon():

    #STILL HAVE SETUP THE NUMBER OF POKEBALLS TING IF I REACH 0 BALLS THE BALLS
    #JUST DONT THROW SO I HAVE TO RUN
    #THEN THE PERSON DOES THE RING DING TING AND I HAVE TO GO BACK TO MY SPOT


    #location of "ball" X:  392 Y:  688 RGB: (234, 234, 234)
    time.sleep(1)

    pyautogui.keyDown("q")
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp("q")
       

    while True:
        
        #checks if the magikarp got caught and if it did breas the loop
        if pyautogui.locateOnScreen('MagikarpCaught.png') != None:
            print("Karp Got In da Balls")
            time.sleep(4)
            break;
        
        #checks if the pokeball missed by seeing if the message showed up
        elif pyautogui.locateOnScreen('1stMiss.png') or pyautogui.locateOnScreen('2ndMiss.png') or pyautogui.locateOnScreen('3rdMiss.png') or pyautogui.locateOnScreen('4thMiss.png') != None:
            print("Miss")
            time.sleep(1)
            
            #checks if the magikarp fled, and if it did it breaks the loop
            if pyautogui.locateOnScreen('FledBattle.png') != None:
                print("Fled")
                break;
            
            #checks if the magikarp is still here, and if it throws another ball
            elif pyautogui.locateOnScreen('MagikarpWatching.png') != None:
                print("Still here Baby Girl")
                time.sleep(2)
                
                #throws another ball
                pyautogui.keyDown("q")
                time.sleep(np.random.uniform(0.1,0.5))
                pyautogui.keyUp("q")



def runBack():

    #goes forward until bush
    pyautogui.keyDown("w")
    time.sleep(1.65)
    pyautogui.keyUp("w")
    print("Reachs Bush")

    #goes left until its inbetween sign and bushs
    pyautogui.keyDown("d")
    time.sleep(1)
    pyautogui.keyUp("d")
    print("Inbetween Sign And Bushes")

    #goes forward until i am in position
    pyautogui.keyDown("w")
    time.sleep(0.75)
    pyautogui.keyUp("w")
    print("reached the spot")



def checkBalls():
    
    #checks if the safari person says ring ding meaning the balls are gone
    if pyautogui.locateOnScreen('OutOfBalls.png') != None:
        
        #loops clicks through all of the dialogue while still at the fishing spot
        for i in range(3):
            time.sleep(np.random.uniform(0.1,0.4))
            pyautogui.keyDown("q")
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp("q")

        #waiting for me to be sent back to the front of the safari place
        time.sleep(2.5)

        #to go infront of safari clerc to buy a ticket into the safari again
        pyautogui.keyDown("w")
        time.sleep(np.random.uniform(0.1,0.5))
        pyautogui.keyUp("w")

        #cycles through all the dialouge and buys the ticket into
        for i in range(8):
            time.sleep(np.random.uniform(0.1,0.4))
            pyautogui.keyDown("q")
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp("q")

        #waiting for the animation of me walking into the safari to finish
        time.sleep(2.5)

        #to run back to the ting
        runBack()

    elif pyautogui.locateOnScreen('BallsAtZero.png') != None:

        #moves to bait
        pyautogui.keyDown("d")
        time.sleep(np.random.uniform(0.1,0.3))
        pyautogui.keyUp("d")

        #moves to run
        pyautogui.keyDown("s")
        time.sleep(np.random.uniform(0.1,0.3))
        pyautogui.keyUp("s")

        #runs from battle
        pyautogui.keyDown("q")
        time.sleep(np.random.uniform(0.1,0.3))
        pyautogui.keyUp("q")

        time.sleep(0.5)

        #loops clicks through all of the dialogue while still at the fishing spot
        for i in range(3):
            time.sleep(np.random.uniform(0.1,0.4))
            pyautogui.keyDown("q")
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp("q")

        #waiting for me to be sent back to the front of the safari place
        time.sleep(2.5)

        #to go infront of safari clerc to buy a ticket into the safari again
        pyautogui.keyDown("w")
        time.sleep(np.random.uniform(0.1,0.5))
        pyautogui.keyUp("w")

        #cycles through all the dialouge and buys the ticket into
        for i in range(8):
            time.sleep(np.random.uniform(0.1,0.4))
            pyautogui.keyDown("q")
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp("q")

        #waiting for the animation of me walking into the safari to finish
        time.sleep(2.5)

        #to run back to the ting
        runBack()


if pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png') or pyautogui.locateOnScreen('BallsZero4.png') != None:

    #moves to bait
    pyautogui.keyDown("d")
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp("d")

    #moves to run
    pyautogui.keyDown("s")
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp("s")

    #runs from battle
    pyautogui.keyDown("q")
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp("q")

    time.sleep(0.5)

    #loops clicks through all of the dialogue while still at the fishing spot
    for i in range(3):
        time.sleep(np.random.uniform(0.1,0.4))
        pyautogui.keyDown("q")
        time.sleep(np.random.uniform(0.1,0.3))
        pyautogui.keyUp("q")

    #waiting for me to be sent back to the front of the safari place
    time.sleep(2.5)

    #to go infront of safari clerc to buy a ticket into the safari again
    pyautogui.keyDown("w")
    time.sleep(np.random.uniform(0.1,0.5))
    pyautogui.keyUp("w")

    #cycles through all the dialouge and buys the ticket into
    for i in range(8):
        time.sleep(np.random.uniform(0.1,0.4))
        pyautogui.keyDown("q")
        time.sleep(np.random.uniform(0.1,0.3))
        pyautogui.keyUp("q")

    #waiting for the animation of me walking into the safari to finish
    time.sleep(2.5)

    #to run back to the ting
    runBack()

