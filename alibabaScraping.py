import csv

def aliScrap(driver, By, time, wait, EC):
    alibabaLink = input("Enter Alibaba link: ")
    driver.implicitly_wait(10)
    driver.get(alibabaLink)

    mid = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[2]/div[13]/div/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)

    print("=============================================================")

    productNameEl = driver.find_element(By.CLASS_NAME, "product-title-container")
    shopNameEl = driver.find_element(By.CLASS_NAME, "company-name")

    productName = productNameEl.text.strip()
    shopName = shopNameEl.text.strip()

    print("Product Name:", productName)
    print("Shop Name:", shopName)

    data_reviews = []

    numberOfProduct = driver.find_element(
        By.CSS_SELECTOR,
        'button[role="tab"][aria-controls*="content-product"]'
    ).text.replace("Product reviews (", "").replace(")", "")

    if numberOfProduct != "0":

        reviews = driver.find_elements(By.CSS_SELECTOR,'div.r-flex-1.r-overflow-hidden.r-text-ellipsis.r-whitespace-nowrap')

        for i, review in enumerate(reviews, 1):
            print("=============================================================")

            reviewContains = review.find_element(By.XPATH,".//div[contains(@class,'r-relative') and contains(@class,'r-text')]").text.strip()
            reviewDate = review.find_element(By.CSS_SELECTOR,"div.r-font-Inter.r-text-left").text.strip()

            print("Product review num", i)
            print("Date:", reviewDate)
            print("Contains:", reviewContains)

            data_reviews.append([
                productName,
                shopName,
                "product",
                reviewDate,
                reviewContains
            ])
    else:
        print("This product has no review")

    storebtn = driver.find_element(By.XPATH,"//button[@role='tab' and contains(., 'Store')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", storebtn)
    storebtn.click()

    showbtn = driver.find_element(By.XPATH,"//button[@aria-haspopup='dialog' and contains(., 'Show all')]")

    if showbtn:
        driver.execute_script("arguments[0].click();", showbtn)

    print("=============================================================")
    print("Getting shop review...")

    dialog = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))

    scroll_box = dialog.find_element(By.XPATH,".//div[contains(@class,'overflow')]")

    collected = []
    scroll_count = 0
    max_scroll = 7

    while scroll_count < max_scroll:
        reviews = dialog.find_elements(By.CSS_SELECTOR,'div.r-flex-1.r-overflow-hidden.r-text-ellipsis.r-whitespace-nowrap')
        for review in reviews:
            try:
                containsEl = review.find_element(By.XPATH,".//div[contains(@class,'r-relative') and contains(@class,'r-text')]")
                dateEl = review.find_elements(By.CSS_SELECTOR,"div.r-font-Inter.r-text-left")
                reviewContains = containsEl.text.strip()
                reviewDate = dateEl[0].text.strip() if dateEl else "Tidak tersedia"
                data = (reviewDate, reviewContains)
                if reviewContains and data not in collected:
                    collected.append(data)
            except:
                continue

        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scroll_box)
        time.sleep(2)
        scroll_count += 1

    for i, (date, contains) in enumerate(collected, 1):
        print("=============================================================")
        print("Shop review num", i)
        print("Date:", date)
        print("Contains:", contains)


        data_reviews.append([
            productName,
            shopName,
            "shop",
            date,
            contains
        ])

    save = input("\nSave data in data.csv? (y/n): ").lower()

    if save == "y":
        with open("data.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow([
                    "Product Name",
                    "Shop Name",
                    "Review Type",
                    "Date Review",
                    "Review Contains"
                ])

            writer.writerows(data_reviews)

        print("✅ Data successfully saved to data.csv")
    else:
        print("❌ Data not saved")