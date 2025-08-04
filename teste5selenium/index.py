from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome()
navegador.get("https://www.saucedemo.com/v1/")

campo_usuario = navegador.find_element(By.ID, "user-name")
campo_usuario.send_keys("standard_user")

time.sleep(5)
campo_senha = navegador.find_element(By.ID, "password")
campo_senha.send_keys("secret_sauce")

time.sleep(2)
botao = navegador.find_element(By.ID, "login-button")
botao.click()

time.sleep(5)
navegador.quit()