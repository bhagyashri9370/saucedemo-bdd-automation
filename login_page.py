
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def is_products_page_displayed(self):
        try:
            title = self.wait.until(
                EC.visibility_of_element_located(self.PRODUCTS_TITLE)
            )
            return (
                title.text == "Products"
                and "/inventory.html" in self.driver.current_url
            )
        except Exception:
            return False
