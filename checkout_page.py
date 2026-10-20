
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    ORDER_ITEMS = (By.CLASS_NAME, "cart_item")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_CONTAINER = (By.CLASS_NAME, "checkout_complete_container")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def enter_customer_details(
        self, first_name, last_name, postal_code
    ):
        fields = [
            (self.FIRST_NAME, first_name),
            (self.LAST_NAME, last_name),
            (self.POSTAL_CODE, postal_code),
        ]

        for locator, value in fields:
            field = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            field.clear()
            field.send_keys(value)

    def continue_to_overview(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def contains_product(self, product_name):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.ORDER_ITEMS)
        )

        return any(
            item.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text == product_name
            for item in items
        )

    def finish_purchase(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def is_order_complete(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.COMPLETE_CONTAINER
                )
            )
            return True
        except Exception:
            return False

    def get_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        ).text
