from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

driver.get("https://shopee.co.id/PLAYSTATION-5-PS5-DISC-DIGITAL-VERSION-GARANSI-GARANSI-INDO-BONUS-500-GAME-ORIGINAL-TERBARU-2025-FULL-REQUEST-i.179131318.6283645095?extraParams=%7B%22display_model_id%22%3A212116369667%2C%22model_selection_logic%22%3A3%7D&sp_atk=b0345fbf-6f7e-4d83-aa88-4a1d5266c443&xptdk=b0345fbf-6f7e-4d83-aa88-4a1d5266c443")

# time.sleep(5)
# commentBtn = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Comments')]")))
# commentBtn.click()

# time.sleep(5)
# elements = driver.find_elements(
#     By.XPATH,
#     "//span[contains(@class,'TUXText')]"
# )
# for e in elements:
#     print(e.text)

# time.sleep(2)
# captchaClose = driver.find_element(By.ID, "captcha_close_button")
# captchaClose.click()

input("end")