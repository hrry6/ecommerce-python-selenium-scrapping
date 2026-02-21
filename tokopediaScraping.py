def tokoScrap(driver, By, time):
    linkToped = input("Masukkan link tokopedia: ")
    driver.get(linkToped)
    driver.implicitly_wait(2)
    mid = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[12]/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)
    komenSection = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[12]/div/div/section/section')
    articles = komenSection.find_elements(By.TAG_NAME, "article")
    idx = 1
    print("=============================================================")
    for article in articles:
        print("Komen ke ", idx)
        pembungkusKomen = article.find_element(By.TAG_NAME, "div")
        isiKomen = pembungkusKomen.find_elements(By.TAG_NAME, "p")
        print(isiKomen[2].text)
        idx += 1
    i = 3
    while True:
        next_buttons = driver.find_elements(
            By.XPATH,
            '/html/body/div[1]/div/div[2]/div[2]/div[12]/div/div/section/div[3]/nav/ul/li[' + str(i) + ']/button'
        )
        if not next_buttons:
            break
        next_buttons[0].click()
        time.sleep(1)
        komenSection = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[12]/div/div/section/section')
        articles = komenSection.find_elements(By.TAG_NAME, "article")
        for article in articles:
            print("Komen ke ", idx)
            pembungkusKomen = article.find_element(By.TAG_NAME, "div")
            isiKomen = pembungkusKomen.find_elements(By.TAG_NAME, "p")
            print(isiKomen[2].text)
            idx += 1
        i += 1