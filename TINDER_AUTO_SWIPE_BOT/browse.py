from time import sleep

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from auth import email, password

TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/2Zf_uq-Gj4--qu6qK_AOwzSlhAult1nZ"
chrome_options = webdriver.ChromeOptions()

# Keep browser open after script ends
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get(TINDOG_URL)

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(1)
facebark_button = driver.find_element(By.CLASS_NAME, value='btn-facebark')
facebark_button.click()
sleep(2)
base_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]
driver.switch_to.window(facebark_window)
print(driver.title)

sleep(2)
email_input= driver.find_element(By.ID, value='email')
password_input=driver.find_element(By.ID, value='pass')
email_input.send_keys(email)
password_input.send_keys(password)
log_in = driver.find_element(By.XPATH, value='/html/body/div[2]/div/form/button')
log_in.click()


driver.switch_to.window(base_window)
sleep(1)
allow_location=driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button')
allow_location.click()

sleep(1)
allow_notification=driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button[1]')
allow_notification.click()

sleep(1)
allow_cookies=driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button')
allow_cookies.click()

for n in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        # Match popup is in the way — dismiss it and continue
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not loaded yet OR all dogs have been swiped — wait and retry
        sleep(2)

driver.quit()


