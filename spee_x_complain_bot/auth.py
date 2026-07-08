from selenium.webdriver.common.by import By
from time import sleep
from browser import create_driver
from config import EMAIL,PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def login(driver):
    sleep(3)
    cockie_bt = driver.find_element(By.CLASS_NAME, value= 'y-btn-primary')
    cockie_bt.click()
    sleep(1)
    login_bt= driver.find_element(By.XPATH, value= '/html/body/div/div[1]/a[4]')
    login_bt.click()
    sleep(1)
    email_input = driver.find_element(By.XPATH, value= '//*[@id="email"]')
    email_input.send_keys(EMAIL)
    password_input= driver.find_element(By.XPATH, value= '//*[@id="password"]')
    password_input.send_keys(PASSWORD)
    sleep(1)
    login_button=driver.find_element(By.XPATH,value='/html/body/div/div/form/button')
    login_button.click()