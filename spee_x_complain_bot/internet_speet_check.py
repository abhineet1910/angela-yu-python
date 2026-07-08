from pip._internal.commands import download
from selenium.webdriver.common.by import By
from time import sleep
from browser import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def check_speed():
    driver = create_driver()
    driver.get("https://www.speedtest.net")
    sleep(5)
    comtinue_bt = driver.find_element(By.CSS_SELECTOR,value="button[id='onetrust-accept-btn-handler']")
    comtinue_bt.click()
    sleep(2)
    go_btn = driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/a')
    go_btn.click()

    # print("speed test started ....")
    sleep(45)

    download_speed= driver.find_element(By.XPATH, value= '//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    # print(f"downloading speed: {download_speed.text}")

    upload_speed= driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    # print(f"uploading speed: {upload_speed.text}")
    return download_speed.text, upload_speed.text


