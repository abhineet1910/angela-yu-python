from internet_speet_check import check_speed
from browser import create_driver
from auth import login
from post_tweet import POST
from config import PROMISED_DOWN, PROMISED_UP,y_url
download_speed, upload_speed = check_speed()
print(download_speed, upload_speed)


driver = create_driver()
driver.get(y_url)
login(driver)
tweet = f"Hey Internet Provider, why is my speed {download_speed}down/{upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"

POST(driver, tweet)