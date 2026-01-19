from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get("https://www.python.org")

    # Wait for 10 seconds
    news_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".medium-widget.blog-widget li a"))
    )

    # Print title and link for each news item
    for news in news_items:
        title = news.text
        link = news.get_attribute('href')
        print(f"{title} -> {link}")

finally:
    driver.quit()  # Ensure browser closes even if an error occurs
