import time

from selenium.webdriver.common.by import By
from config import delay


class ItemPage:

    # Selectors for item detail page elements

    ITEM_NAME = ".inventory_details_name"
    ITEM_DESC = ".inventory_details_desc"
    ITEM_PRICE = ".inventory_details_price"
    ITEM_IMAGE = "img.inventory_details_img"  # Class is on the <img> element itself, not a parent container
    ADD_REMOVE_BUTTON = ".btn_inventory"  # Same selector covers both Add and Remove states; button text determines current state
    BACK_BUTTON = "[data-test='back-to-products']"
    CART_BADGE = ".shopping_cart_badge"

    # Artificial delay for visual confirmation, unnecessary for tests, can be set to 0
    # Controlled via FAST_MODE in config.py

    DELAY_ACTION = delay(0.5)

    def __init__(self, driver):
        self.driver = driver

    def get_item_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ITEM_NAME).text

    def get_item_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ITEM_DESC).text

    def get_item_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ITEM_PRICE).text

    def get_item_image_src(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ITEM_IMAGE).get_attribute("src")

    def click_add_remove_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ADD_REMOVE_BUTTON).click()
        time.sleep(self.DELAY_ACTION)

    def get_button_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ADD_REMOVE_BUTTON).text

    def click_back_to_products(self):
        self.driver.find_element(By.CSS_SELECTOR, self.BACK_BUTTON).click()
        time.sleep(self.DELAY_ACTION)

    def get_cart_badge_count(self):
        # Returns 0 if badge element is absent; SauceDemo removes it from DOM when cart is empty
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.CART_BADGE)
        return int(elements[0].text) if elements else 0
