def aliScrap(driver, By, time, wait, EC):
    linkAlibaba = input("Masukkan link Alibaba: ")
    driver.implicitly_wait(10)
    driver.get(linkAlibaba)
    mid = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[2]/div[13]/div/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)

    print("=============================================================")
    productName = driver.find_element(By.CLASS_NAME, "product-title-container")
    tokoName = driver.find_element(By.CLASS_NAME, "company-name")
    print("Nama Produk:", productName.text)
    print("Nama Toko:", tokoName.text)

    numberOfProduct = driver.find_element(By.CSS_SELECTOR,'button[role="tab"][aria-controls*="content-product"]').text.replace("Product reviews (", "").replace(")", "")

    if numberOfProduct != "0":
        reviews = driver.find_elements(By.CSS_SELECTOR,'div.r-flex-1.r-overflow-hidden.r-text-ellipsis.r-whitespace-nowrap')
        for i, review in enumerate(reviews):
            print("=============================================================")
            isiReview = review.find_element(By.XPATH,".//div[contains(@class,'r-relative') and contains(@class,'r-text')]")
            waktuReview = review.find_element(By.CSS_SELECTOR,'div.r-font-Inter.r-text-left')
            print("Review produk ke", i+1)
            print("Waktu:", waktuReview.text)
            print("Isi:", isiReview.text)
    else:
        print("Produk ini tidak punya review")

    storebtn = driver.find_element(
        By.XPATH,
        "//button[@role='tab' and contains(., 'Store')]"
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", storebtn)
    storebtn.click()

    showbtn = driver.find_element(
        By.XPATH,
        "//button[@aria-haspopup='dialog' and contains(., 'Show all')]"
    )
    if showbtn:
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            showbtn
        )
        driver.execute_script("arguments[0].click();", showbtn)

    print("=============================================================")
    print("Sedang mengambil review toko...")

    dialog = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@role='dialog']")
    ))

    scroll_box = dialog.find_element(By.XPATH, ".//div[contains(@class,'overflow')]")

    collected = []
    scroll_count = 0
    max_scroll = 20
    while scroll_count < max_scroll:
        reviews = driver.find_elements(By.CSS_SELECTOR,'div.r-flex-1.r-overflow-hidden.r-text-ellipsis.r-whitespace-nowrap')
        for review in reviews:
            try:
                isiReview = review.find_element(
                    By.XPATH,
                    ".//div[contains(@class,'r-relative') and contains(@class,'r-text')]"
                ).text.strip()

                waktuReview = review.find_element(By.CSS_SELECTOR,"div.r-font-Inter.r-text-left").text.strip()

                data = (waktuReview, isiReview)

                if data not in collected:
                    collected.append(data)
            except:
                continue
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight",
            scroll_box
        )
        time.sleep(1)
        scroll_count += 1

    for i, (waktu, isi) in enumerate(collected, 1):
        print("=============================================================")
        print("Review toko ke", i)
        print("Waktu:", waktu)
        print("Isi:", isi)