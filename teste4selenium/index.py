from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome()
navegador.get("https://google.com")

caixa_busca = navegador.find_element(By.NAME, "q")
caixa_busca.send_keys("python selenium")
caixa_busca.send_keys(Keys.ENTER)

time.sleep(5)
navegador.quit()