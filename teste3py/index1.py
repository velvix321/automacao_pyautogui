import pyautogui
import time

time.sleep(3)

pos = pyautogui.position()

pyautogui.moveTo(pos.x, pos.y, duration=1)
pyautogui.click()

print(pos)