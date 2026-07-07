import time


def retry(func, retries=7, description="Operation"):

    for attempt in range(1, retries + 1):

        try:

            print(f"\n[{attempt}/{retries}] {description}")

            result = func()

            print(f"✅ {description} successful")

            return result

        except Exception as e:

            print(f"❌ {description} failed")

            print(e)

            if attempt == retries:

                print("❌ Maximum retries reached.")

                raise

            print("Retrying in 2 seconds...\n")

            time.sleep(2)