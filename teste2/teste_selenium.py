from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
driver = webdriver.Chrome(service=servico)

driver.get("http://google.com")
time.sleep(3)

driver.quit()