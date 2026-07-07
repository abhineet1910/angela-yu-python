import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from config import (
    USER_DATA_DIR,

)


def create_driver():
    """
    Creates and returns a configured Chrome WebDriver.
    """

    chrome_options = webdriver.ChromeOptions()

    # Keep browser open after script ends
    chrome_options.add_experimental_option("detach", True)

    # Use dedicated Chrome profile
    chrome_options.add_argument(
        f"--user-data-dir={USER_DATA_DIR}"
    )

    # Run without opening browser (future use)
    # if HEADLESS_MODE:
    #     chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)


    #
    # driver.implicitly_wait(IMPLICIT_WAIT)

    return driver
