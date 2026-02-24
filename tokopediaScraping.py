import csv

def tokoScrap(driver, By, time):
    linkToped = input("Masukkan link Tokopedia: ")
    driver.get(linkToped)
    driver.implicitly_wait(4)

    print("=============================================================")
    productName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[1]/h1")
    tokoName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[7]/div[2]/div[1]/div[2]/div/div/h2")

    print("Nama Produk:", productName.text)
    print("Nama Toko:", tokoName.text)

    mid = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[12]/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)

    data_reviews = []  

    komenSection = driver.find_element(By.XPATH, "//*[@id='review-feed']")
    articles = komenSection.find_elements(By.TAG_NAME, "article")

    idx = 1

    def ambil_review(articles, idx):
        for article in articles:
            print("=============================================================")
            print("Review ke", idx)

            pembungkusKomen = article.find_element(By.TAG_NAME, "div")
            waktuReview = pembungkusKomen.find_element(By.TAG_NAME, "div")
            isiReview = pembungkusKomen.find_elements(By.TAG_NAME, "p")

            if len(isiReview) > 2:
                isi = isiReview[2].text
            else:
                isi = isiReview[1].text

            print("Waktu:", waktuReview.text)
            print("Isi:", isi)

            data_reviews.append([
                productName.text,
                tokoName.text,
                "produk",
                waktuReview.text,
                isi
            ])

            idx += 1
        return idx

    idx = ambil_review(articles, idx)

    i = 3
    while True:
        next_buttons = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[12]/div/div/section/div[3]/nav/ul/li[' + str(i) + ']/button')

        if not next_buttons:
            break

        next_buttons[0].click()
        time.sleep(2)

        komenSection = driver.find_element(By.XPATH, "//*[@id='review-feed']")
        articles = komenSection.find_elements(By.TAG_NAME, "article")

        idx = ambil_review(articles, idx)
        i += 1

    simpan = input("\nApakah anda ingin menyimpan data? (y/n): ").lower()

    if simpan == "y":
        with open("data.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow(["Nama Produk", "Nama Toko","Jenis Review","Waktu Review", "Isi Review"])

            writer.writerows(data_reviews)

        print("✅ Data berhasil disimpan ke data.csv")
    else:
        print("❌ Data tidak disimpan.")