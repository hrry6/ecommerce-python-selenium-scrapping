import csv

def aliScrap(driver, By, time, wait, EC):
    linkAlibaba = input("Masukkan link Alibaba: ")
    driver.implicitly_wait(10)
    driver.get(linkAlibaba)

    mid = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[2]/div[13]/div/div/h2")
    driver.execute_script("arguments[0].scrollIntoView();", mid)

    print("=============================================================")

    productName = driver.find_element(By.CLASS_NAME, "product-title-container")
    tokoName = driver.find_element(By.CLASS_NAME, "company-name")

    nama_produk = productName.text.strip()
    nama_toko = tokoName.text.strip()

    print("Nama Produk:", nama_produk)
    print("Nama Toko:", nama_toko)

    data_reviews = []

    numberOfProduct = driver.find_element(
        By.CSS_SELECTOR,
        'button[role="tab"][aria-controls*="content-product"]'
    ).text.replace("Product reviews (", "").replace(")", "")

    if numberOfProduct != "0":

        reviews = driver.find_elements(By.CSS_SELECTOR,'div.r-flex-1.r-overflow-hidden.r-text-ellipsis.r-whitespace-nowrap')

        for i, review in enumerate(reviews, 1):
            print("=============================================================")

            isiReview = review.find_element(By.XPATH,".//div[contains(@class,'r-relative') and contains(@class,'r-text')]").text.strip()

            waktuReview = review.find_element(By.CSS_SELECTOR,"div.r-font-Inter.r-text-left").text.strip()

            print("Review produk ke", i)
            print("Waktu:", waktuReview)
            print("Isi:", isiReview)

            data_reviews.append([
                nama_produk,
                nama_toko,
                "produk",
                waktuReview,
                isiReview
            ])
    else:
        print("Produk ini tidak punya review")

    storebtn = driver.find_element(By.XPATH,"//button[@role='tab' and contains(., 'Store')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", storebtn)
    storebtn.click()

    showbtn = driver.find_element(By.XPATH,"//button[@aria-haspopup='dialog' and contains(., 'Show all')]")

    if showbtn:
        driver.execute_script("arguments[0].click();", showbtn)

    print("=============================================================")
    print("Sedang mengambil review toko...")

    dialog = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))

    scroll_box = dialog.find_element(By.XPATH,".//div[contains(@class,'overflow')]")

    collected = []
    scroll_count = 0
    max_scroll = 7

    while scroll_count < max_scroll:
        reviews = dialog.find_elements(By.CSS_SELECTOR,'div.r-flex-1.r-overflow-hidden.r-text-ellipsis.r-whitespace-nowrap')
        for review in reviews:
            try:
                isi_elem = review.find_element(By.XPATH,".//div[contains(@class,'r-relative') and contains(@class,'r-text')]")
                waktu_elems = review.find_elements(By.CSS_SELECTOR,"div.r-font-Inter.r-text-left")
                isiReview = isi_elem.text.strip()
                waktuReview = waktu_elems[0].text.strip() if waktu_elems else "Tidak tersedia"
                data = (waktuReview, isiReview)
                if isiReview and data not in collected:
                    collected.append(data)
            except:
                continue

        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scroll_box)
        time.sleep(2)
        scroll_count += 1

    for i, (waktu, isi) in enumerate(collected, 1):
        print("=============================================================")
        print("Review toko ke", i)
        print("Waktu:", waktu)
        print("Isi:", isi)

        data_reviews.append([
            nama_produk,
            nama_toko,
            "toko",
            waktu,
            isi
        ])

    simpan = input("\nApakah anda ingin menyimpan data? (y/n): ").lower()

    if simpan == "y":
        with open("data.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow([
                    "Nama Produk",
                    "Nama Toko",
                    "Jenis Review",
                    "Waktu Review",
                    "Isi Review"
                ])

            writer.writerows(data_reviews)

        print("✅ Data berhasil disimpan ke data.csv")
    else:
        print("❌ Data tidak disimpan.")