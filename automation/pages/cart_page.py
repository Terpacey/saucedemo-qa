import time

from selenium.webdriver.common.by import By
from config import delay
from pages.base_page import BasePage


class CartPage(BasePage):

    # Selectors for cart page elements

    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_QUANTITY = ".cart_quantity"
    CONTINUE_SHOPPING = "[data-test='continue-shopping']"
    CHECKOUT = "[data-test='checkout']"

    # Artificial delay for visual confirmation, unnecessary for tests, can be set to 0
    # Controlled via FAST_MODE in config.py

    DELAY_ACTION = delay(0.5)

    def get_item_names(self) -> list[str]:
        return [
            item.find_element(By.CSS_SELECTOR, self.ITEM_NAME).text
            for item in self.driver.find_elements(By.CSS_SELECTOR, self.CART_ITEM)
        ]

    def get_item_prices(self) -> list[str]:
        return [
            item.find_element(By.CSS_SELECTOR, self.ITEM_PRICE).text
            for item in self.driver.find_elements(By.CSS_SELECTOR, self.CART_ITEM)
        ]

    def get_item_quantities(self) -> list[str]:
        return [
            item.find_element(By.CSS_SELECTOR, self.ITEM_QUANTITY).text
            for item in self.driver.find_elements(By.CSS_SELECTOR, self.CART_ITEM)
        ]

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(By.CSS_SELECTOR, self.CART_ITEM))

    def click_remove(self, item_name: str) -> None:

        # Loop to find right container by confirming name text and clicks its Remove button
        # Accounts for cart holding multiple items with no selector linking name directly to button

        for item in self.driver.find_elements(By.CSS_SELECTOR, self.CART_ITEM):
            if item.find_element(By.CSS_SELECTOR, self.ITEM_NAME).text == item_name:
                item.find_element(By.CSS_SELECTOR, "button").click()
                time.sleep(self.DELAY_ACTION)
                return
        raise ValueError(f"Item not found in cart: {item_name}")

    def click_continue_shopping(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.CONTINUE_SHOPPING).click()
        time.sleep(self.DELAY_ACTION)

    def click_checkout(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.CHECKOUT).click()
        time.sleep(self.DELAY_ACTION)
