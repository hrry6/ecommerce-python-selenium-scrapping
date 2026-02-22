from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tokopediaScraping import tokoScrap
from amazonScraping import amaScrap
from alibabaScraping import aliScrap

chrome_options = Options()
chrome_options.headless = False
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = "/usr/sbin/chromium"
service = Service("/usr/sbin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

def menu():
    print("=============================================================")
    print("Choose platform\n1.Tokopedia\n2.Amazon\n3.Alibaba\n4.Exit")
    num = input("Choose the number: ")

    if num == "1":
        print("Tokopedia")
        tokoScrap(driver, By, time)
    elif num == "2":
        print("Amazon")
        amaScrap(driver, By, time)
    elif num == "3":
        print("Alibaba")
        aliScrap(driver, By, time,wait, EC)
    elif num == "4":
        print("Exit")
        driver.close()
        exit()
    else:
        print("Unknown option")

menu()
while True:
    menu()