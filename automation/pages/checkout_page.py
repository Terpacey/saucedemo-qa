import time

from selenium.webdriver.common.by import By
from config import delay
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # Selectors for checkout pages — covers step 1 (Your Information), step 2 (Overview), and confirmation

    TITLE = "[data-test='title']"
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE = "[data-test='continue']"
    CANCEL = "[data-test='cancel']"  # Shared between step 1 and step 2; method names distinguish which page
    ERROR = "[data-test='error']"

    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_QUANTITY = ".cart_quantity"
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    GRAND_TOTAL = ".summary_total_label"
    SUMMARY_VALUE = ".summary_value_label"  # No per-field selectors; index [0] = payment, [1] = shipping
    FINISH = "[data-test='finish']"

    COMPLETE_HEADER = ".complete-header"
    BACK_HOME = "[data-test='back-to-products']"

    # Artificial delay for visual confirmation, unnecessary for tests, can be set to 0
    # Controlled via FAST_MODE in config.py

    DELAY_ACTION = delay(0.5)

    # --- Step 1 ---

    def get_page_title(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text

    def fill_first_name(self, value: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.FIRST_NAME).send_keys(value)
        time.sleep(self.DELAY_ACTION)

    def fill_last_name(self, value: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.LAST_NAME).send_keys(value)
        time.sleep(self.DELAY_ACTION)

    def fill_postal_code(self, value: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.POSTAL_CODE).send_keys(value)
        time.sleep(self.DELAY_ACTION)

    def first_name_field_is_present(self) -> bool:
        # find_elements returns an empty list when absent; bool() converts to True/False
        return bool(self.driver.find_elements(By.CSS_SELECTOR, self.FIRST_NAME))

    def last_name_field_is_present(self) -> bool:
        return bool(self.driver.find_elements(By.CSS_SELECTOR, self.LAST_NAME))

    def postal_code_field_is_present(self) -> bool:
        return bool(self.driver.find_elements(By.CSS_SELECTOR, self.POSTAL_CODE))

    def continue_button_is_present(self) -> bool:
        return bool(self.driver.find_elements(By.CSS_SELECTOR, self.CONTINUE))

    def cancel_button_is_present(self) -> bool:
        return bool(self.driver.find_elements(By.CSS_SELECTOR, self.CANCEL))

    def click_continue(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.CONTINUE).click()
        time.sleep(self.DELAY_ACTION)

    def click_cancel_step1(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.CANCEL).click()
        time.sleep(self.DELAY_ACTION)

    def get_error_message(self) -> str:
        # Returns empty string if no error is shown, avoiding exception
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.ERROR)
        return elements[0].text if elements else ""

    # --- Step 2 ---

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

    def get_item_total(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, self.ITEM_TOTAL).text

    def get_tax(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, self.TAX).text

    def get_grand_total(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, self.GRAND_TOTAL).text

    def get_payment_info(self) -> str:
        return self.driver.find_elements(By.CSS_SELECTOR, self.SUMMARY_VALUE)[0].text

    def get_shipping_info(self) -> str:
        return self.driver.find_elements(By.CSS_SELECTOR, self.SUMMARY_VALUE)[1].text

    def click_finish(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.FINISH).click()
        time.sleep(self.DELAY_ACTION)

    def click_cancel_step2(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.CANCEL).click()
        time.sleep(self.DELAY_ACTION)

    # --- Confirmation ---

    def get_confirmation_header(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, self.COMPLETE_HEADER).text

    def back_home_button_is_present(self) -> bool:
        return bool(self.driver.find_elements(By.CSS_SELECTOR, self.BACK_HOME))

    def click_back_home(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.BACK_HOME).click()
        time.sleep(self.DELAY_ACTION)
