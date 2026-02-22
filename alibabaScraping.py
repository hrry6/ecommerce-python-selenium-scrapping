def aliScrap(driver, By, time, wait, EC):
    linkAlibaba = input("Masukkan link Alibaba: ")
    # linkAlibaba = "https://www.alibaba.com/product-detail/Havit-H628BT-Wireless-Headphone-Stereo-Foldable_1600967787750.html?spm=a2700.prosearch.normal_offer.d_image.3c9467afknUxpW&priceId=d35dcc8853d0465f9325df8e3c881940"
    driver.implicitly_wait(10)
    driver.get(linkAlibaba)
    mid = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[2]/div[13]/div/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)
    print("Berhasil scroll to elemen")

    print("=============================================================")
    comments = driver.find_elements(By.XPATH,"//div[contains(@class,'r-relative') and contains(@class,'r-text')]")
    for i, comment in enumerate(comments):
        print("Komen ke", i+1)
        print(comment.text)

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
    print("Sedang mengambil data...")

    dialog = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@role='dialog']")
    ))

    scroll_box = dialog.find_element(By.XPATH, ".//div[contains(@class,'overflow')]")

    collected = set()
    scroll_count = 0
    max_scroll = 20

    while scroll_count < max_scroll:
        comments = dialog.find_elements(
            By.XPATH,
            ".//div[contains(@class,'r-relative') and contains(@class,'r-text')]"
        )
        for c in comments:
            text = c.text.strip()
            if text:
                collected.add(text)
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight",
            scroll_box
        )
        time.sleep(1)
        scroll_count += 1

    for i, text in enumerate(collected, 1):
        print("Komen ke", i+1)
        print(text)
