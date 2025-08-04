from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get("https://quotes.toscrape.com/")

caixa_busca = navegador.find_elements(By.CLASS_NAME, "text")

for item in caixa_busca:
    print(f"{item.text}, \n")