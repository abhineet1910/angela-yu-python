import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------- SETUP ---------------- #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 120)

# ---------------- LANGUAGE ---------------- #

try:
    english = wait.until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    english.click()
except Exception:
    print("Language selection skipped.")

# ---------------- COOKIE ---------------- #

cookie = wait.until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# ---------------- TIMERS ---------------- #

check_interval = 5
end_time = time.time() + 60 * 5
next_check = time.time() + check_interval

# ---------------- MAIN LOOP ---------------- #

while time.time() < end_time:

    driver.find_element(By.ID, "bigCookie").click()

    if time.time() >= next_check:

        enabled_products = driver.find_elements(
            By.CSS_SELECTOR,
            "#products .product.unlocked.enabled"
        )

        if enabled_products:
            enabled_products[-1].click()





        next_check = time.time() + check_interval

# ---------------- RESULT ---------------- #

try:
    cookies = driver.find_element(By.ID, "cookies").text
    print(f"\nFinal Score:\n{cookies}")

except NoSuchElementException:
    print("Couldn't read final score.")