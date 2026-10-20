import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
WAIT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "10"))
