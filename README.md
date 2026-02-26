# 🛒 ecommerce-python-selenium-scrapping

A simple Python + Selenium-based script for scraping product comments from e-commerce websites.

With this script, users can:

- Retrieve comments from a product
- Display all available comments (including pagination)
- Automate the scrolling and navigation process of the comment page

This project is suitable for:

- Learning web scraping
- Selenium experiments
- Processing product comment/review data

## ⚙️ Requirements

Make sure you have installed:

- Python 3.x
- Google Chrome / Chromium
- ChromeDriver (depending on your browser version)
- Selenium

## 📦 Install Selenium

```bash
pip install selenium
```

Make sure:

- ChromeDriver version matches your Chrome/Chromium version
- ChromeDriver path is correct in the script
- Browser runs without errors

## 🚀 How to Run

Go to the project folder and run:

```bash
python main.py
```

## 🧠 How It Works in Brief

The script will:
- Open a browser using Selenium
- Access the product page (make sure to provide a link to the page that already has comments)
- Scroll to the comments section
- Fetch all available comments
- Display the comments in the terminal