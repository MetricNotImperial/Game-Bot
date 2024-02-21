"""NOTES:FOR THIS CODE TO WORK ALIGN YOURSLEF AT THE LOCATION OF THE WATER BESIDE THE BUSH AND TOP LEFT OF THE SIGN IN THE SAFARI ZONE, THE LETTER "Q"
SHOULD BE "A", THE LETTER "E" SHOULD BE "B", THE OLD ROD SHOULD BE HOT KEYED AS THE NUMBER "4", AND THE WINDOW SHOULD NOT BE FULL SCREENED
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


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


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



    elif pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png') or pyautogui.locateOnScreen('BallsZero4.png') != None:

        time.sleep(1)
        
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


def catchPokemon():


    #location of "ball" X:  392 Y:  688 RGB: (234, 234, 234)
    time.sleep(0.6)

    pyautogui.keyDown("q")
    time.sleep(np.random.uniform(0.2,0.7))
    pyautogui.keyUp("q")
       

    while True:
        
        #checks if the magikarp got caught and if it did breaks the loop
        if pyautogui.locateOnScreen('MagikarpCaught.png') != None:
            print("Karp Got In da Balls")
            time.sleep(4)
            
            #Location for where to click after the mon is caughtX: 1193 Y:  386 RGB: ( 19,  19,  19)
            win32api.SetCursorPos((1193, 386))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(np.random.uniform(0.1,0.4))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            
            #checks if balls are 0, get a refil and come back to the same place
            checkBalls()
            break;
        
        #checks if the pokeball missed by seeing if the message showed up
        elif pyautogui.locateOnScreen('1stMiss.png') or pyautogui.locateOnScreen('2ndMiss.png') or pyautogui.locateOnScreen('3rdMiss.png') or pyautogui.locateOnScreen('4thMiss.png') != None:
            print("Miss")
            time.sleep(1)
            
            #checks if the magikarp fled, and if it did it breaks the loop
            if pyautogui.locateOnScreen('FledBattle.png') != None:
                print("Fled")
                #checks if balls are 0, get a refil and come back to the same place
                checkBalls()
                break;
            
            #checks if the magikarp is still here, and if it throws another ball
            elif pyautogui.locateOnScreen('MagikarpWatching.png') != None:
                print("Still here Baby Girl")
                time.sleep(2)

                #if the count of balls is not 0 then i will throw another ball
                if pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png') or pyautogui.locateOnScreen('BallsZero4.png') or pyautogui.locateOnScreen('BallsZero5.png')  or pyautogui.locateOnScreen('BallsZero6.png') or pyautogui.locateOnScreen('BallsZero7.png') == None:

                    time.sleep(np.random.uniform(0.2,0.7))
                    #throws another ball
                    pyautogui.keyDown("q")
                    time.sleep(np.random.uniform(0.2,0.7))
                    pyautogui.keyUp("q")

                    time.sleep(np.random.uniform(0.2,0.7))
                    #throws another ball
                    pyautogui.keyDown("q")
                    time.sleep(np.random.uniform(0.2,0.7))
                    pyautogui.keyUp("q")


                time.sleep(0.5)
                #running this twice to make sre it catchs if the balls is at 0
                for zero in range(2):    
                    #if it is not 0 then i will run the checkballs function
                    if pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png') or pyautogui.locateOnScreen('BallsZero4.png') or pyautogui.locateOnScreen('BallsZero5.png')  or pyautogui.locateOnScreen('BallsZero6.png') or pyautogui.locateOnScreen('BallsZero7.png') != None:
                        checkBalls()
                        print("zero balls and it will go back")
                        #if it checked there are 0 balls it will refil and come back to the spot where I will break the code
                        break;


                
                


x = 0
time.sleep(2)

    
while keyboard.is_pressed('o') == False:
    #throws the old rod once so it doesnt spam
    if x == 0:
        time.sleep(1)
        pyautogui.keyDown("4")
        time.sleep(0.1)
        pyautogui.keyUp("4")
        x=x+1
    #checks if the fish landed
    if pyautogui.locateOnScreen('landed.png') != None:
        time.sleep(0.75)
        print("I see it landed!")
        
        #to get the white text of the screen
        pyautogui.keyDown("e")
        time.sleep(0.1)
        pyautogui.keyUp("e")
        
        #to make x = 0 so the old rod will go out again next time the code loops
        x = x - 1

        #to wait for the animation to finish of the battle
        time.sleep(7.5)

        #catchs the pokemon
        catchPokemon()
        
        time.sleep(np.random.uniform(0.1,0.5))

        
    #checks if the ting didnt land
    elif pyautogui.locateOnScreen('missed.png') != None:
        time.sleep(np.random.uniform(0.73,0.76))
        print("i see it missed")
        
        #to get the white text of the screen
        pyautogui.keyDown("e")
        time.sleep(np.random.uniform(0.1,0.3))
        pyautogui.keyUp("e")
        
        #to make x = 0 so the old rod will go out again next time the code loops
        x = x - 1

    else:
        print("I dont see shit")
        time.sleep(0.5)


