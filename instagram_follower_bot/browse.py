from selenium import webdriver


def create_driver():
    """
    Creates and returns a configured Chrome WebDriver.
    """
    # USER_DATA_DIR = os.path.join(os.getcwd(), "chrome_profile")


    chrome_options = webdriver.ChromeOptions()

    # Keep browser open after script ends
    chrome_options.add_experimental_option("detach", True)

    # Use dedicated Chrome profile
    # chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    # chrome_options.add_argument("--profile-directory=Profile 6")

    driver = webdriver.Chrome(options=chrome_options)


    #
    # driver.implicitly_wait(IMPLICIT_WAIT)

    return driver