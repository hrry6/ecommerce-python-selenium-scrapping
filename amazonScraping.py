def amaScrap(driver, By, time):
    linkAmazon = input("Masukkan link Amazon: ")
    driver.get(linkAmazon)
    driver.implicitly_wait(3)
    mid = driver.find_element(By.CSS_SELECTOR, "h3[data-testid='heading']")
    driver.execute_script("arguments[0].scrollIntoView();", mid)
    reviews = driver.find_elements(By.XPATH,'.//div[starts-with(@id,"customer_review")]')

    print("=============================================================")    
    productName = driver.find_element(By.ID, "title")
    print("Nama Produk:", productName.text)
    tokoName = driver.find_element(By.XPATH, '//a[@id="bylineInfo"]')
    print("Nama Toko:", tokoName.text.replace("Visit the ", "").replace(" Store", ""))

    i = 1
    for review in reviews:
        print("=============================================================")
        reviewDate = review.find_element(By.CSS_SELECTOR, 'span[data-hook="review-date"]')
        reviewIsi = review.find_element(By.CSS_SELECTOR, 'span[data-hook="review-body"]')
        print("Review ke", i)
        print("Waktu:", reviewDate.text.split(" on ")[-1])
        print("Isi:",reviewIsi.text)
        i += 1

