import pyautogui

box = pyautogui.locateOnScreen("edit.png")
print(box)

imagem = pyautogui.center(box)
print(imagem)

pyautogui.click(imagem.x, imagem.y)