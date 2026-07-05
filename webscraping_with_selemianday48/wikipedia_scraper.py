from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# keeping up the browser open after program finish
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
# no_of_en_articles = driver.find_element(By.CSS_SELECTOR,value="#mwDg")
# # no_of_en_articles.click()
# _by_linktext = driver.find_element(By.LINK_TEXT,value="Keiko Fujimori")
# _by_linktext.click()
#
# #  to give inpiuty to the specific web page like scearch etc
# search = driver.find_element(By.XPATH,value='//*[@id="p-search"]/a')
# search.click()
# to_search= driver.find_element(By.NAME,value='search')
# to_search.send_keys("Elon Musk")
# to_search.send_keys(Keys.ENTER)
first_name = driver.find_element(By.NAME,value='fName')
first_name.send_keys("ABHINEET")
last_name = driver.find_element(By.NAME,value='lName')
last_name.send_keys("MITRA")
email = driver.find_element(By.NAME,value='email')
email.send_keys("testingmail19@gmail.com")
signup = driver.find_element(By.XPATH,value='//*[@id="signup-form"]/button')
signup.click()


# driver.quit()