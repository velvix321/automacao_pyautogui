import pyautogui

pyautogui.moveTo(100, 200, duration=1)
pyautogui.click()
pyautogui.click(100, 150, clicks=2, interval=1, button='left')

pos = pyautogui.position()

print(pos)