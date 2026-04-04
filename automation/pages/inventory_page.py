import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import delay
from pages.base_page import BasePage


class InventoryPage(BasePage):

    # Selectors for inventory page elements

    INVENTORY_ITEM = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_IMAGE = ".inventory_item_img img"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    CART_LINK = ".shopping_cart_link"
    BURGER_MENU_BTN = "react-burger-menu-btn"
    RESET_LINK = "reset_sidebar_link"
    LOGOUT_LINK = "logout_sidebar_link"

    # Artificial delays, DELAY_ACTION for visual confirmation for user convenience
    # Avoid setting DELAY_SORT to 0; sorting re-renders the entire item list and
    # reading before the DOM settles can produce stale results on slower machines
    # Controlled via FAST_MODE in config.py; DELAY_SORT keeps a 0.3 s minimum even in FAST_MODE

    DELAY_ACTION = delay(0.5)
    DELAY_SORT = delay(1.0, minimum=0.3)

    def wait_for_items(self) -> None:

        # Block to ensure at least one item name element is present in DOM
        # Accounts for browser delays or page delays in the case of performance_glitch_user

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.ITEM_NAME))
        )

    def get_item_names(self) -> list[str]:
        return [el.text for el in self.driver.find_elements(By.CSS_SELECTOR, self.ITEM_NAME)]

    def get_item_prices(self) -> list[str]:
        return [el.text for el in self.driver.find_elements(By.CSS_SELECTOR, self.ITEM_PRICE)]

    def get_item_image_srcs(self) -> list[str | None]:
        return [el.get_attribute("src") for el in self.driver.find_elements(By.CSS_SELECTOR, self.ITEM_IMAGE)]

    def _get_item_button(self, item_name: str) -> WebElement:

        # Loop to find right container by confirming name text and fetches target element
        # Accounts for SauceDemo not having selectors that map item names
        # directly to their corresponding image or button

        for item in self.driver.find_elements(By.CSS_SELECTOR, self.INVENTORY_ITEM):
            if item.find_element(By.CSS_SELECTOR, self.ITEM_NAME).text == item_name:
                return item.find_element(By.CSS_SELECTOR, "button")
        raise ValueError(f"Item not found: {item_name}")

    def click_item_name(self, item_name: str) -> None:
        for item in self.driver.find_elements(By.CSS_SELECTOR, self.INVENTORY_ITEM):
            if item.find_element(By.CSS_SELECTOR, self.ITEM_NAME).text == item_name:
                item.find_element(By.CSS_SELECTOR, self.ITEM_NAME).click()
                time.sleep(self.DELAY_ACTION)
                return
        raise ValueError(f"Item not found: {item_name}")

    def click_item_image(self, item_name: str) -> None:
        for item in self.driver.find_elements(By.CSS_SELECTOR, self.INVENTORY_ITEM):
            if item.find_element(By.CSS_SELECTOR, self.ITEM_NAME).text == item_name:
                item.find_element(By.CSS_SELECTOR, self.ITEM_IMAGE).click()
                time.sleep(self.DELAY_ACTION)
                return
        raise ValueError(f"Item not found: {item_name}")

    def click_item_button(self, item_name: str) -> None:
        self._get_item_button(item_name).click()
        time.sleep(self.DELAY_ACTION)

    def get_button_text_for_item(self, item_name: str) -> str:
        return self._get_item_button(item_name).text

    def set_sort_order(self, value: str) -> None:

        # Raw JS execution, test previously failed despite being manually confirmed in prior test
        # SauceDemo's dropdown component appears to be a React component
        # Selenium works by changing DOM value and does not fire a browser event,
        # which does not work for React's root listener
        #
        # Execute script sets value and dispatches a native change event for React's listener

        dropdown = self.driver.find_element(By.CSS_SELECTOR, self.SORT_DROPDOWN)
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change', {bubbles: true}));",
            dropdown, value
        )
        time.sleep(self.DELAY_SORT)

    def get_sort_alert_text_and_dismiss(self) -> str | None:

        # Check for JS alert when sort is attempted, detect and dismiss
        # If nothing is detected, returns None, prevents method crash

        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return None

    def click_cart(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, self.CART_LINK).click()
        time.sleep(self.DELAY_ACTION)

    # Following methods use WebDriverWait to account for slide-open animation
    # from burger menu, elements are not interactable until animation is complete
    #
    # Uses EC.element_to_be_clickable, more reliable than fixed sleep which may not
    # account for browser delays or waste time

    def click_reset_app_state(self) -> None:
        self.driver.find_element(By.ID, self.BURGER_MENU_BTN).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, self.RESET_LINK))
        ).click()
        time.sleep(self.DELAY_ACTION)

    def click_logout(self) -> None:
        self.driver.find_element(By.ID, self.BURGER_MENU_BTN).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, self.LOGOUT_LINK))
        ).click()
        time.sleep(self.DELAY_ACTION)
