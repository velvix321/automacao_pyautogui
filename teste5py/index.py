import pyautogui
import time

time.sleep(5)
pyautogui.write("automaçao com pyautogui", interval=0.5)
pyautogui.press("enter")

time.sleep(3)
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

time.sleep(5)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")

time.sleep(3)
pyautogui.hotkey("ctrl", "v")