from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    CART_BADGE = ".shopping_cart_badge"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def get_cart_badge_count(self) -> int:
        # Returns 0 if badge element is absent; SauceDemo removes it from DOM when cart is empty
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.CART_BADGE)
        return int(elements[0].text) if elements else 0
