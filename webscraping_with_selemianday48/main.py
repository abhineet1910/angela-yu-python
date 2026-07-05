from selenium import webdriver
from selenium.webdriver.common.by import By
# keeping up the browser open after program finish
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org")
# price = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print(f"price is {price.text}")
# search = driver.find_element(By.NAME,value="field-keywords")
# print(f"search is {search.get_attribute('placeholder')}")
# print(search.size)
# # it also helps us to find through a series of element for example
# # BY.CSS_SELECTER methjod
# # for prime deal
# or_prime_id = driver.find_element(By.ID,value="nav-primeday")
# print(or_prime_id.get_attribute('href'))
# prime_deal = driver.find_element(By.CSS_SELECTOR,value=".nav-div a")
# print(prime_deal.get_attribute('href'))
# about_amazon_link = driver.find_element(By.XPATH,value='//*[@id="navFooter"]/div[1]/div/div[1]/ul/li[1]/a')
# print(f"HERES IS ABOUT AMAZON {about_amazon_link.get_attribute('href')}")

# from python.org getting all the list of upcoming event and saving them in dict

events = driver.find_elements(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
event_dict = {}

for i, event in enumerate(events):
    date = event.find_element(By.TAG_NAME, "time").text.strip()
    name = event.find_element(By.TAG_NAME, "a").text.strip()

    event_dict[i] = {
        "date": date,
        "name": name
    }

print(event_dict)



driver.quit()