import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import DEFAULT_TIMEOUT


def book_class(driver):

    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "[id^='class-card-']")
        )
    )

    processed_classes = []

    booked_count = 0
    waitlist_count = 0
    already_booked_count = 0

    for card in cards:

        day_group = card.find_element(
            By.XPATH,
            "./ancestor::div[contains(@id,'day-group-')]"
        )

        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        if "Tue" not in day_title and "Thu" not in day_title:
            continue

        time_text = card.find_element(
            By.CSS_SELECTOR,
            "p[id^='class-time-']"
        ).text

        if "6:00 PM" not in time_text:
            continue

        class_name = card.find_element(
            By.CSS_SELECTOR,
            "h3[id^='class-name-']"
        ).text

        button = card.find_element(
            By.CSS_SELECTOR,
            "button[id^='book-button-']"
        )

        button_text = button.text

        class_info = f"{class_name} on {day_title}"

        if button_text == "Booked":

            already_booked_count += 1
            processed_classes.append(f"[Already Booked] {class_info}")

        elif button_text == "Waitlisted":

            already_booked_count += 1
            processed_classes.append(f"[Already Waitlisted] {class_info}")

        elif button_text == "Book Class":

            button.click()

            booked_count += 1
            processed_classes.append(f"[New Booking] {class_info}")

        elif button_text == "Join Waitlist":

            button.click()

            waitlist_count += 1
            processed_classes.append(f"[New Waitlist] {class_info}")

        else:

            print(f"Unknown state: {button_text}")

        time.sleep(0.5)

    total_booked = (
        booked_count
        + waitlist_count
        + already_booked_count
    )

    print("\n--- BOOKING SUMMARY ---")

    for item in processed_classes:
        print(f"• {item}")

    print(f"\nTotal Tue/Thu 6PM Classes: {total_booked}")

    return total_booked


def get_my_bookings(driver, total_booked):

    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    print("\n--- VERIFYING BOOKINGS ---")

    driver.find_element(
        By.ID,
        "my-bookings-link"
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.ID, "my-bookings-page")
        )
    )

    verified_count = 0

    all_cards = driver.find_elements(
        By.CSS_SELECTOR,
        "div[id*='card-']"
    )

    for card in all_cards:

        try:

            when_paragraph = card.find_element(
                By.XPATH,
                ".//p[strong[text()='When:']]"
            )

            when_text = when_paragraph.text

            if (
                ("Tue" in when_text or "Thu" in when_text)
                and "6:00 PM" in when_text
            ):

                class_name = card.find_element(
                    By.TAG_NAME,
                    "h3"
                ).text

                print(f"✓ Verified: {class_name}")

                verified_count += 1

        except NoSuchElementException:
            pass

    print("\n--- VERIFICATION RESULT ---")

    print(f"Expected: {total_booked}")

    print(f"Found: {verified_count}")

    if verified_count == total_booked:

        print("✅ SUCCESS: All bookings verified!")

    else:

        print(
            f"❌ MISMATCH: Missing {total_booked - verified_count} bookings"
        )

