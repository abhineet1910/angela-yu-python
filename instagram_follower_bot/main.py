from idlelib import search

from browse import create_driver
from config import insta_url, email, password, instagram_official,target_account
from auth import *
from follow import *

for account in target_account:
    driver = create_driver()
    driver.get(insta_url)


    login_page = Login(driver)

    login_page.login(email, password)
    login_page.click_not_now()
    login_page.disable_notifications()
    search=FOLLOW(driver)

    print(account)
    search.search_profile(key=account)
    search.popup_follower()
    search.follow_everyone()




