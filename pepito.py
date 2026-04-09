import ssl
import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "https://www.bcra.gob.ar" 


html = urllib.request.urlopen(url, context=ctx).read()


sopa = BeautifulSoup(html, 'html.parser')


dato = sopa.find('div', class_='cuatro-var-api-1')

dato = sopa.find('div', {'class': 'cuatro-var-api-1'})

import re
resultados = sopa.find_all('div', class_=re.compile('cuatro-var-api'))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.bcra.gob.ar")
time.sleep(3)  # esperás que cargue el JS

dato = driver.find_element(By.CLASS_NAME, 'cuatro-var-api-1')
print(dato.find_element(By.TAG_NAME, 'h1').text, "millones de pesos.")

driver.quit()