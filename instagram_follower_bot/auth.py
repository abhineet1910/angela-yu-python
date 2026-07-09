
from selenium.webdriver.common.by import By
from config import email,password
from time import sleep
from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(email)
        sleep(2)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        sleep(2)

        login_btn = self.driver.find_element(
            By.XPATH,
            "/html/body/div/aside/div/form/button"
        )
        login_btn.click()
        sleep(2)

    def click_not_now(self):

        not_now = self.driver.find_element(
            By.XPATH,
            '//*[@id="popup-save-login"]/div/div[2]'
        )
        not_now.click()
        sleep(2)

    def disable_notifications(self):

        notification_not_now = self.driver.find_element(
            By.XPATH,
            '//*[@id="popup-notifications"]/div/button[2]'
        )
        notification_not_now.click()
        sleep(2)





