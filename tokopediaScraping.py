import csv

def tokoScrap(driver, By, time):
    tokopediaLink = input("Enter Tokopedia Link: ")
    driver.get(tokopediaLink)
    driver.implicitly_wait(4)

    print("=============================================================")
    productName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[1]/h1")
    shopName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[7]/div[2]/div[1]/div[2]/div/div/h2")

    print("Product Name:", productName.text)
    print("Shop Name:", shopName.text)

    mid = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[12]/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)

    data_reviews = []  

    reviewSection = driver.find_element(By.XPATH, "//*[@id='review-feed']")
    articles = reviewSection.find_elements(By.TAG_NAME, "article")

    idx = 1

    def get_review(articles, idx):
        for article in articles:
            print("=============================================================")
            print("Product review num", idx)

            commentWrap = article.find_element(By.TAG_NAME, "div")
            reviewDate = commentWrap.find_element(By.TAG_NAME, "div")
            reviewContains = commentWrap.find_elements(By.TAG_NAME, "p")

            if len(reviewContains) > 2:
                contains = reviewContains[2].text
            else:
                contains = reviewContains[1].text

            print("Date:", reviewDate.text)
            print("Contains:", contains)

            data_reviews.append([
                productName.text,
                shopName.text,
                "product",
                reviewDate.text,
                contains
            ])

            idx += 1
        return idx

    idx = get_review(articles, idx)

    i = 3
    while True:
        next_buttons = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[12]/div/div/section/div[3]/nav/ul/li[' + str(i) + ']/button')

        if not next_buttons:
            break

        next_buttons[0].click()
        time.sleep(2)

        reviewSection = driver.find_element(By.XPATH, "//*[@id='review-feed']")
        articles = reviewSection.find_elements(By.TAG_NAME, "article")

        idx = get_review(articles, idx)
        i += 1

    simpan = input("\nSave data in data.csv? (y/n): ").lower()

    if simpan == "y":
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