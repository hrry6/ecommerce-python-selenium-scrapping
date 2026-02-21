# 🛒 ecommerce-python-selenium-scrapping

Script sederhana berbasis **Python + Selenium** untuk melakukan scraping komentar produk dari website e-commerce.

Dengan script ini, user dapat:

- Mengambil komentar dari suatu produk
- Menampilkan seluruh komentar yang tersedia (termasuk pagination)
- Mengotomatisasi proses scroll & navigasi halaman komentar

Project ini cocok untuk:

- Belajar web scraping
- Eksperimen Selenium
- Pengolahan data komentar / review produk

---

## ⚙️ Requirements

Pastikan sudah menginstall:

- Python 3.x  
- Google Chrome / Chromium  
- ChromeDriver (sesuai versi browser)  
- Selenium  

---

## 📦 Install Selenium

```bash
pip install selenium
```
Pastikan:

- Versi ChromeDriver sesuai dengan versi Chrome / Chromium
- Path ChromeDriver sudah benar di dalam script
- Browser dapat dijalankan tanpa error

## 🚀 Cara Menjalankan

Masuk ke folder project lalu jalankan:

```bash
python main.py
```

## 🧠 Cara Kerja Singkat

Script akan:
- Membuka browser menggunakan Selenium
- Mengakses halaman produk(pastikan memberikan link halaman yang sudah terdapat komentar)
- Scroll ke bagian komentar
- Mengambil seluruh komentar yang tersedia
- Menampilkan komentar ke terminal