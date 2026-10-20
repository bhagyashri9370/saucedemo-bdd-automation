
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import HEADLESS, BROWSER


def create_driver():
    if BROWSER.lower() != "chrome":
        raise ValueError(f"Unsupported browser: {BROWSER}")

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1440,1000")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)
    driver.set_page_load_timeout(30)

    return driver