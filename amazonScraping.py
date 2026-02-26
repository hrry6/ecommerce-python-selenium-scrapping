import csv

def amaScrap(driver, By, time):
    amazonLink = input("Enter Amazon Link: ")
    driver.get(amazonLink)
    driver.implicitly_wait(3)

    mid = driver.find_element(By.CSS_SELECTOR, "h3[data-testid='heading']")
    driver.execute_script("arguments[0].scrollIntoView();", mid)

    reviews = driver.find_elements(By.XPATH,'.//div[starts-with(@id,"customer_review")]')

    print("=============================================================")

    productNameEl = driver.find_element(By.ID, "title")
    shopNameEl = driver.find_element(By.XPATH, '//a[@id="bylineInfo"]')

    productName = productNameEl.text.strip()
    shopName = shopNameEl.text.replace("Visit the ", "").replace(" Store", "").strip()

    print("Product Name:", productName)
    print("Shop Name:", shopName)

    data_reviews = []

    i = 1
    for review in reviews:
        print("=============================================================")
        reviewDate = review.find_element(By.CSS_SELECTOR,'span[data-hook="review-date"]')
        reviewContains = review.find_element(By.CSS_SELECTOR,'span[data-hook="review-body"]')
        date = reviewDate.text.split(" on ")[-1].strip()
        contains = reviewContains.text.strip()

        print("Product review num", i)
        print("Date:", date)
        print("Contains:", contains)

        data_reviews.append([
            productName,
            shopName,
            "product",
            date,
            contains
        ])
        i += 1

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