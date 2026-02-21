def amaScrap(driver, By, time):
    linkAmazon = input("Masukkan link Amazon: ")
    driver.get(linkAmazon)
    driver.implicitly_wait(3)
    mid = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[35]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/h3")
    driver.execute_script("arguments[0].scrollIntoView();", mid)
    comments = driver.find_elements(By.CLASS_NAME, "review-data")
    i = 1
    print("=============================================================")
    for comment in comments:
        print("Komen ke", i)
        print(comment.text)
        i += 1

