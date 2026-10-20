
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_product(self, product_name):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCTS)
        )

        for product in products:
            name = product.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text

            if name == product_name:
                button = product.find_element(By.TAG_NAME, "button")
                self.wait.until(
                    lambda _: button.is_enabled()
                )
                button.click()
                return

        raise AssertionError(
            f"Product '{product_name}' was not found on the Products page."
        )

    def get_cart_badge_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def contains_product(self, product_name):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )

        return any(
            item.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text == product_name
            for item in items
        )

    def proceed_to_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
