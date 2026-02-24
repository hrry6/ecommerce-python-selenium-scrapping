import csv

def amaScrap(driver, By, time):
    linkAmazon = input("Masukkan link Amazon: ")
    driver.get(linkAmazon)
    driver.implicitly_wait(3)

    mid = driver.find_element(By.CSS_SELECTOR, "h3[data-testid='heading']")
    driver.execute_script("arguments[0].scrollIntoView();", mid)

    reviews = driver.find_elements(By.XPATH,'.//div[starts-with(@id,"customer_review")]')

    print("=============================================================")

    productName = driver.find_element(By.ID, "title")
    tokoName = driver.find_element(By.XPATH, '//a[@id="bylineInfo"]')

    nama_produk = productName.text.strip()
    nama_toko = tokoName.text.replace("Visit the ", "").replace(" Store", "").strip()

    print("Nama Produk:", nama_produk)
    print("Nama Toko:", nama_toko)

    data_reviews = []

    i = 1
    for review in reviews:
        print("=============================================================")

        reviewDate = review.find_element(By.CSS_SELECTOR,'span[data-hook="review-date"]')

        reviewIsi = review.find_element(By.CSS_SELECTOR,'span[data-hook="review-body"]')

        tanggal = reviewDate.text.split(" on ")[-1].strip()
        isi = reviewIsi.text.strip()

        print("Review ke", i)
        print("Waktu:", tanggal)
        print("Isi:", isi)

        data_reviews.append([
            nama_produk,
            nama_toko,
            "produk",
            tanggal,
            isi
        ])
        i += 1

    simpan = input("\nApakah anda ingin menyimpan data? (y/n): ").lower()

    if simpan == "y":
        with open("data.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow(["Nama Produk", "Nama Toko","Jenis Review", "Waktu Review", "Isi Review"])
            writer.writerows(data_reviews)

        print("✅ Data berhasil disimpan ke data.csv")
    else:
        print("❌ Data tidak disimpan.")