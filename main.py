"""

Portfolio: T-RexBot Project
#100DaysOfCode with Python
Day: 92
Date: 2023-07-26
Author: MC

"""

import pyautogui
import time
import keyboard


while True:

    im = pyautogui.screenshot()
    screen = im.getpixel((550, 1070))

    x1 = im.getpixel((551, 1071))

    if screen[0] == 255:
        if x1[0] != 255:
            pyautogui.press('space')
    else:
        if x1[0] == 255:
            pyautogui.press('space')
    time.sleep(0.001)

    if keyboard.is_pressed('s'):
         break
    else:
        pass
