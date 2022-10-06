import pyautogui;
import os
import time
from PIL import ImageGrab
from functools import partial


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Bild/accept.PNG')


x = None



while x == None:
    
    #suche nach accept
    x = pyautogui.locateCenterOnScreen(filename, confidence=.7)    
    time.sleep(4)    
    print("Suche nach einem Game...")
    if x != None:
        #klickt accept
        pyautogui.click(x, button='left')
        time.sleep(5)
        x = None
