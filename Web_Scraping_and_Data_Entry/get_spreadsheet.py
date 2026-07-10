from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from config import google_form
class GetSpreadsheet:
    def __init__(self):
        self.driver=webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(google_form)
    def fill_address(self,address):
        sleep(2)
        address_input=self.driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address)
        sleep(1)
    def fill_price(self,price):
        price_input=self.driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(price)
        sleep(1)
    def fill_links(self,links):
        link_input=self.driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(links)
        sleep(1)
    def click_submit(self):
        click_summit=self.driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        click_summit.click()


    def submit_another_request(self):
        sleep(2)
        summit_another=self.driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        summit_another.click()











