from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import ACCOUNT_EMAIL, ACCOUNT_PASSWORD, DEFAULT_TIMEOUT


def login(driver):
    """Logs into the gym website."""

    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    # Click Login button
    login_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_btn.click()

    # Enter email
    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "email-input"))
    )
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    # Enter password
    password_input = wait.until(
        EC.presence_of_element_located((By.ID, "password-input"))
    )
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    # Click Sign In button
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    submit_btn.click()
