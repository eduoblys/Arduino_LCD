
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import serial
import sys
import time
import requests
import json

options = Options()
options.headless = True
arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10) # 10seconds
uRL = "https://www.realitymod.com/prspy/prbf2/17c498c4f8ba9879c9f13084bfe725133f6a77b1"     #=HOG= Mixed Maps

driver.get(uRL)

print(driver.title)

playersPath="/html/body/div[1]/div[2]/section[3]/div/div[1]/div[2]/div[2]/div[3]/span[1]"
mapPath="/html/body/div[1]/div[2]/section[3]/div/div[1]/div[2]/div[2]/div[1]"
gmodePath="/html/body/div[1]/div[2]/section[3]/div/div[1]/div[2]/div[2]/div[2]"

numplayers = driver.find_element(by=By.XPATH, value=playersPath)
mapname = driver.find_element(by=By.XPATH, value=mapPath)
gmode = driver.find_element(by=By.XPATH, value=gmodePath)
simtas = "/100"

print(numplayers.text)
print(mapname.text)
print(gmode.text)

nmplayers = numplayers.text
mname = mapname.text
gode = gmode.text

array = [nmplayers,mname,gode]
newLine = "\n"

while True:
    arduino.write(nmplayers.encode() + simtas.encode() +newLine.encode())
    arduino.write(mname.encode()+newLine.encode())
    arduino.write(gode.encode())
    time.sleep(8.5)
    driver.quit()
    exit()