from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v147.fed_cm import click_dialog_button


class FOLLOW:
    def __init__(self, driver):
        self.driver = driver

    def search_profile(self,key):
        sleep(1)
        search_profile = self.driver.find_element(By.XPATH, value='/html/body/div[1]/nav/button')
        search_profile.click()
        sleep(1)
        profile_input=self.driver.find_element(By.CLASS_NAME,value='naan-search-input')
        profile_input.send_keys(key)
        sleep(2)
        click_result=self.driver.find_element(By.XPATH,value='/html/body/aside/div[4]/a')
        click_result.click()



    def popup_follower(self):
        sleep(1)
        click__followers=self.driver.find_element(By.XPATH,value='/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a')
        click__followers.click()

    from time import sleep
    from selenium.webdriver.common.by import By

    def follow_everyone(self):

        # Replace this with the actual scrollable div
        modal = self.driver.find_element(
            By.CSS_SELECTOR,
            ".followers-scroll"
        )

        # processed = set()
        for _ in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight;",
                modal
            )

            sleep(1)

            # Get every follower row
        followers = self.driver.find_elements(
            By.CLASS_NAME,
            "naan-follower-row"
        )

        print(f"Found {len(followers)} followers")
        for row in followers:

            try:

                button = row.find_element(
                    By.TAG_NAME,
                    "button"
                )

                status = button.get_attribute("data-following")

                if status == "false":

                    button.click()

                    print("Followed")

                    sleep(1)

                else:

                    print("Already Following")

            except Exception as e:

                print(e)
    # def follow_everyone(self):
    #     sleep(2)
    #     followers = self.driver.find_elements(
    #         By.CLASS_NAME,
    #         "naan-follower-row"
    #     )
