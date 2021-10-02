

import pyautogui
import time
# time.sleep(2)
pyautogui.click()
# distance=500
# while distance>0:
#     pyautogui.dragRel(distance,0,duration=0.2)
#     distance-=5
#     pyautogui.dragRel(0,distance,  duration=0.2)
#     pyautogui.dragRel(-distance, 0, duration=0.2)
#     distance -= 5
#     pyautogui.dragRel(0, -distance,  duration=0.2)

for _ in range(3):
    pyautogui.typewrite("hello world")
    #pyautogui.hotkey('shift','1')
    # pyautogui.hotkey('ctrl', '\n')
    pyautogui.click(pyautogui.center((pyautogui.locateOnScreen('submit.png'))))
    pyautogui.moveRel(-388,-80,duration=0.1)
