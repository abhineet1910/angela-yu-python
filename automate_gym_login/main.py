from config import GYM_URL,ACCOUNT_EMAIL,ACCOUNT_PASSWORD
import browser
from auth import login
from booking import book_class
import time

import browser
from config import GYM_URL
from auth import login
from booking import book_class, get_my_bookings
from helpers import retry

driver = browser.create_driver()

driver.get(GYM_URL)

total_booked = retry(
    lambda: login(driver),
    retries=7,
    description="Login"
)

total_booked = retry(
    lambda: book_class(driver),
    retries=7,
    description="Booking Classes"
)

retry(
    lambda: get_my_bookings(driver, total_booked),
    retries=7,
    description="Verifying Bookings"
)

driver.quit()
