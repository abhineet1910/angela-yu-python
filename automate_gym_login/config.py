import os
from unittest.mock import DEFAULT

from dotenv import load_dotenv
load_dotenv()
USER_DATA_DIR = os.path.join(os.getcwd(), "chrome_profile")
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
GYM_URL = os.getenv("GYM_URL")
DEFAULT_TIMEOUT = 10







