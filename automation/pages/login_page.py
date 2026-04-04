import time

from selenium.webdriver.common.by import By
from config import delay
from pages.base_page import BasePage


class LoginPage(BasePage):

    # Selectors for login page elements

    USERNAME_FIELD = "user-name"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "login-button"
    ERROR_MESSAGE = "h3[data-test='error']"

    # Artificial delays for visual confirmation, unnecessary for tests, can be set to 0
    # Controlled via FAST_MODE in config.py

    DELAY_INPUT = delay(0.5)
    DELAY_POST_LOGIN = delay(1.5)

    def enter_username(self, username: str) -> None:
        field = self.driver.find_element(By.ID, self.USERNAME_FIELD)
        field.clear()
        field.send_keys(username)
        time.sleep(self.DELAY_INPUT)

    def enter_password(self, password: str) -> None:
        field = self.driver.find_element(By.ID, self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)
        time.sleep(self.DELAY_INPUT)

    def click_login(self) -> None:
        self.driver.find_element(By.ID, self.LOGIN_BUTTON).click()
        time.sleep(self.DELAY_POST_LOGIN)

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        # Returns empty string if no error is shown, avoiding exception
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.ERROR_MESSAGE)
        if elements:
            return elements[0].text
        return ""

    def is_on_inventory_page(self) -> bool:
        # URL check to confirm successful login
        return "/inventory" in self.driver.current_url
