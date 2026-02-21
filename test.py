from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.headless = False
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = "/usr/sbin/chromium"
service = Service("/usr/sbin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

linkAlibaba = input("Masukkan link Alibaba: ")
driver.implicitly_wait(10)
driver.get(linkAlibaba)
mid = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[2]/div[13]/div/div/h2")
driver.execute_script("arguments[0].scrollIntoView();", mid)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[2]/div[13]/div/div/div[1]/div[3]/div/button").click()

print(driver.find_element(By.XPATH, "/html/body/div[8]/h2").text)

# comments = driver.find_elements(By.XPATH, "/html/body/div[8]/div/div[3]/div[13]/div/div[2]/div[3]/div/div[2]")
# for comment in comments:
#     print(comment.text)


input()