"""NOTES:FOR THIS CODE TO WORK ALIGN YOURSLEF AT THE LOCATION OF THE WATER BESIDE THE BUSH AND TOP LEFT OF THE SIGN IN THE SAFARI ZONE, THE LETTER "Q"
SHOULD BE "A", THE LETTER "E" SHOULD BE "B", THE OLD ROD SHOULD BE HOT KEYED AS THE NUMBER "4", AND THE WINDOW SHOULD NOT BE FULL SCREENED, AND I HAVE TO BE SPRINTING
"""

#ADD EVERYTHING ALSO FOR DRAGONAIR BECAUSE I GOT HER


import pyautogui
from PIL import Image
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


def runFromBattle():
    #moves to bait
    pyautogui.keyDown("d")
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp("d")
    
    time.sleep(np.random.uniform(0.1,0.2))
    
    #moves to run
    pyautogui.keyDown("s")
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp("s")
    
    time.sleep(np.random.uniform(0.1,0.2))
    
    #runs from battle
    pyautogui.keyDown("q")
    time.sleep(np.random.uniform(0.1,0.3))
    pyautogui.keyUp("q")


def runBack():

    time.sleep(0.25)
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
    num = 0
    welcome_list = ['Welcome1.png','Welcome2.png','Welcome3.png','Welcome4.png','Welcome5.png','Welcome6.png','Welcome7.png','Welcome8.png','Welcome9.png']

    if pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png') or pyautogui.locateOnScreen('BallsZero4.png') or pyautogui.locateOnScreen('OutOfBalls.png', grayscale=True, confidence = 0.94)!= None:
        
        
        while True:
            if pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png') or pyautogui.locateOnScreen('BallsZero4.png') != None:
                print("da balls at 0")
                time.sleep(1)
                runFromBattle()
                time.sleep(3)
            #loops clicks through all of the dialogue while still at the fishing spot
            if pyautogui.locateOnScreen('OutOfBalls.png', grayscale=True, confidence = 0.94) != None:
                time.sleep(np.random.uniform(0.1,0.4))
                pyautogui.keyDown("q")
                time.sleep(np.random.uniform(0.1,0.3))
                pyautogui.keyUp("q")
                    
            if pyautogui.locateOnScreen('ZeroTing1.png', grayscale=True, confidence = 0.94) != None:
                time.sleep(np.random.uniform(0.1,0.4))
                pyautogui.keyDown("q")
                time.sleep(np.random.uniform(0.1,0.3))
                pyautogui.keyUp("q")
                    
            if pyautogui.locateOnScreen('ZeroTing2.png', grayscale=True, confidence = 0.94) != None:
                time.sleep(np.random.uniform(0.1,0.4))
                pyautogui.keyDown("q")
                time.sleep(np.random.uniform(0.1,0.3))
                pyautogui.keyUp("q")
                break
        #waiting for me to be sent back to the front of the safari place
        time.sleep(3)
        
        #to go infront of safari clerc to buy a ticket into the safari again
        pyautogui.keyDown("w")
        time.sleep(np.random.uniform(0.2,0.5))
        pyautogui.keyUp("w")
        
        time.sleep(0.25)
        #cycles through all the dialouge and buys the ticket into
        while True:
            for i in range(9):
                if pyautogui.locateOnScreen(welcome_list[i], grayscale=True, confidence = 0.98) != None:
                    time.sleep(np.random.uniform(0.1,0.3))
                    pyautogui.keyDown("q")
                    time.sleep(np.random.uniform(0.1,0.2))
                    pyautogui.keyUp("q")

                    if i == 8:
                        num = 1
                        break
            if num == 1:
                break
    
        #waiting for the animation of me walking into the safari to finish
        time.sleep(2.2)
    
        #to run back to the ting
        runBack()    
        
    

def catchPokemon():
    num = 0
    x = 0
    n = 0


    #location of "ball" X:  392 Y:  688 RGB: (234, 234, 234)
    time.sleep(0.3)

    pyautogui.keyDown("q")
    time.sleep(np.random.uniform(0.2,0.7))
    pyautogui.keyUp("q")
    
    print("Threw the balls")

    while keyboard.is_pressed('o') == False or pyautogui.locateOnScreen('MagikarpCaught.png', grayscale=True, confidence = 0.90) == None:

        if pyautogui.locateOnScreen('MagikarpCaught.png', grayscale=True, confidence = 0.90) != None or  x == 30:
            break
        

        print("loop: " + str(x))
        #checks if the pokeball missed by seeing if the message showed up
        if pyautogui.locateOnScreen('1stMiss.png', grayscale=True, confidence = 0.95) or pyautogui.locateOnScreen('2ndMiss.png', grayscale=True, confidence = 0.95) or pyautogui.locateOnScreen('3rdMiss.png', grayscale=True, confidence = 0.95) or pyautogui.locateOnScreen('4thMiss.png', grayscale=True, confidence = 0.95) != None or x % 10 == 0:
            print("Miss")
            if x % 10 != 0:
                x = 0
            while True:
                    
                #checks if the magikarp fled, and if it did it breaks the loop
                if pyautogui.locateOnScreen('FledBattle.png', grayscale=True, confidence = 0.95) != None:
                    print("Fled")
                    time.sleep(3)
                    #checks if balls are 0, get a refil and come back to the same place
                    checkBalls()
                    checkBalls()
                    num = num + 1
                    break
            
                #checks if the magikarp is still here, and if it throws another ball
                if pyautogui.locateOnScreen('MagikarpWatching.png', grayscale=True, confidence = 0.95) != None or n % 10 == 0:
                    print("Still here Baby Girl")
                    time.sleep(1.5)

                    #if the count of balls is not 0 then i will throw another ball
                    if pyautogui.locateOnScreen('BallsAtZero.png', grayscale=True) or pyautogui.locateOnScreen('BallsZero2.png', grayscale=True) or pyautogui.locateOnScreen('BallsZero3.png', grayscale=True) or pyautogui.locateOnScreen('BallsZero4.png',  grayscale=True) or pyautogui.locateOnScreen('BallsZero5.png', grayscale=True) or pyautogui.locateOnScreen('BallsZero6.png', grayscale=True) or pyautogui.locateOnScreen('BallsZero7.png', grayscale=True) == None:
                        print("detected there is not 0 balls left")

                        #throws another ball
                        pyautogui.keyDown("q")
                        time.sleep(np.random.uniform(0.2,0.7))
                        pyautogui.keyUp("q")

                        time.sleep(np.random.uniform(0.1,0.4))
                        #throws another ball
                        pyautogui.keyDown("q")
                        time.sleep(np.random.uniform(0.2,0.7))
                        pyautogui.keyUp("q")
                        break

                    time.sleep(0.75)    
                    #if it is not 0 then i will run the checkballs function
                    if pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png')or pyautogui.locateOnScreen('BallsZero4.png') or pyautogui.locateOnScreen('BallsZero5.png') or pyautogui.locateOnScreen('BallsZero6.png')or pyautogui.locateOnScreen('BallsZero7.png') != None:
                        num = num + 1
                        print("zero balls and it will go back")
                        #Location for where to click after the mon is caughtX: 1193 Y:  386 RGB: ( 19,  19,  19)
                        win32api.SetCursorPos((1193, 386))
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(np.random.uniform(0.1,0.3))
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        #if it checked there are 0 balls it will refil and come back to the spot where I will break the code
                        checkBalls()
                        checkBalls()
                        break
                
                n = n + 1
                
                if n != 21:
                    n = 0
                    break
                    
        #if it is not 0 then i will run the checkballs function
        if pyautogui.locateOnScreen('BallsAtZero.png') or pyautogui.locateOnScreen('BallsZero2.png') or pyautogui.locateOnScreen('BallsZero3.png') or pyautogui.locateOnScreen('BallsZero4.png') or pyautogui.locateOnScreen('BallsZero5.png')or pyautogui.locateOnScreen('BallsZero6.png') or pyautogui.locateOnScreen('BallsZero7.png') != None:
            print("zero balls and it will go back")
            #Location for where to click after the mon is caughtX: 1193 Y:  386 RGB: ( 19,  19,  19)
            win32api.SetCursorPos((1193, 386))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(np.random.uniform(0.1,0.3))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            #if it checked there are 0 balls it will refil and come back to the spot where I will break the code
            checkBalls()
            checkBalls()
            break

                        
        if num != 0:
            break
        
        x = x + 1

        
        
    #checks if the magikarp got caught and if it did breaks the loop
    print("Karp Got In da Balls")
    time.sleep(4)
            
    #Location for where to click after the mon is caughtX: 1193 Y:  386 RGB: ( 19,  19,  19)
    win32api.SetCursorPos((1193, 386))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(np.random.uniform(0.2,0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(np.random.uniform(0.2,0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            
    #checks if balls are 0, get a refil and come back to the same place
    if pyautogui.locateOnScreen('OutOfBalls.png', grayscale=True, confidence = 0.98) != None:
        checkBalls()
        checkBalls()



                
                


x = 0


number = 0


time.sleep(2)


while keyboard.is_pressed('o') == False:

    try:
        #throws the old rod once so it doesnt spam
        if x == 0:
            time.sleep(np.random.uniform(0.66,1.33))
            pyautogui.keyDown("4")
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp("4")
            x = x + 1
            number = 0

        #checks if the fish landed
        if pyautogui.locateOnScreen('landed.png') != None:
            time.sleep(0.75)
            print("I see it landed!")
            
            #to get the white text of the screen
            pyautogui.keyDown("e")
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp("e")
            
            #to make x = 0 so the old rod will go out again next time the code loops
            x = 0

            #to wait for the animation to finish of the battle
            time.sleep(6)

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
            x = 0

        else:
            print("I dont see shit")
            time.sleep(0.5)
            number = number + 1
            print(number)
            if number == 20:
                print("Ting was bugging so I had to manually throw another rod")
                x = 0
            if number % 10 == 0:
                checkBalls()

    except OSError:
        print("excepts the screen grab failure")



