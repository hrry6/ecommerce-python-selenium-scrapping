def tokoScrap(driver, By, time):
    linkToped = input("Masukkan link tokopedia: ")
    driver.get(linkToped)
    driver.implicitly_wait(4)
    
    print("=============================================================")
    productName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[1]/h1")
    tokoName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[7]/div[2]/div[1]/div[2]/div/div/h2")
    print("Nama Produk:", productName.text)
    print("Nama Toko:", tokoName.text)
    
    mid = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[12]/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)
    

    komenSection = driver.find_element(By.XPATH, "//*[@id='review-feed']")
    articles = komenSection.find_elements(By.TAG_NAME, "article")
    
    idx = 1
    for article in articles:
        print("=============================================================")
        print("Review ke ", idx)
        pembungkusKomen = article.find_element(By.TAG_NAME, "div")
        waktuReview = pembungkusKomen.find_element(By.TAG_NAME, "div")
        isiReview = pembungkusKomen.find_elements(By.TAG_NAME, "p")
        print("Waktu:", waktuReview.text)
        print("Isi:", isiReview[2].text)
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
        komenSection = driver.find_element(By.XPATH, "//*[@id='review-feed']")
        articles = komenSection.find_elements(By.TAG_NAME, "article")
        for article in articles:
            print("=============================================================")
            print("Review ke ", idx)
            pembungkusKomen = article.find_element(By.TAG_NAME, "div")
            waktuReview = pembungkusKomen.find_element(By.TAG_NAME, "div")
            isiReview = pembungkusKomen.find_elements(By.TAG_NAME, "p")
            print("Waktu:", waktuReview.text)

            if len(isiReview) > 2:
                print("Isi:", isiReview[2].text)
            else:
                print("Isi:", isiReview[1].text)
            idx += 1
        i += 1


        
