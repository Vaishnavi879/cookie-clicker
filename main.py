from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
import time

chrome_driver_path="path of 'chromedriver.exe' in your system"
service=Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID,"cookie")

def cookie_click():
  threading.Timer(0.1, cookie_click).start()
  cookie.click()

cookie_click()

def check():
    rate=driver.find_element(By.ID, "cps").text
    print(rate)

    # money=int(driver.find_element(By.ID, "money").text)
    # elder = driver.find_element(By.ID, "buyElder Pledge")
    # elder_r = int(elder.text.split(" ")[2].split("\n")[0])
    # if elder_r<=money:
    #     elder.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    time = driver.find_element(By.ID, "buyTime machine")
    time_r = int(time.text.split(" ")[3].split("\n")[0].replace(",",""))
    if time_r<=money:
        time.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    portal = driver.find_element(By.ID, "buyPortal")
    portal_r = int(portal.text.split(" ")[2].split("\n")[0].replace(",",""))
    if portal_r<=money:
        portal.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    alchemy = driver.find_element(By.ID, "buyAlchemy lab")
    alchemy_r = int(alchemy.text.split(" ")[3].split("\n")[0].replace(",",""))
    if alchemy_r<=money:
        alchemy.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    shipment = driver.find_element(By.ID, "buyShipment")
    shipment_r = int(shipment.text.split(" ")[2].split("\n")[0].replace(",",""))
    if shipment_r>=money:
        shipment.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    mine = driver.find_element(By.ID, "buyMine")
    mine_r = int(mine.text.split(" ")[2].split("\n")[0].replace(",",""))
    if mine_r<=money:
        mine.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    factory = driver.find_element(By.ID, "buyFactory")
    factory_r = int(factory.text.split(" ")[2].split("\n")[0].replace(",",""))
    if factory_r<=money:
        factory.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    grandma = driver.find_element(By.ID, "buyGrandma")
    grandma_r = int(grandma.text.split(" ")[2].split("\n")[0])
    print(grandma_r,money)
    if grandma_r<=money:
        grandma.click()

    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    cursor = driver.find_element(By.ID, "buyCursor")
    cursor_r = int(cursor.text.split(" ")[2].split("\n")[0])
    print(cursor_r,money)
    if cursor_r<=money:
        cursor.click()

for i in range(100):
    time.sleep(15)
    check()

driver.quit()

