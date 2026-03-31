import time

from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_FIELD = "user-name"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "login-button"
    ERROR_MESSAGE = "h3[data-test='error']"

    DELAY_INPUT = 0.5
    DELAY_POST_LOGIN = 1.5

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, self.USERNAME_FIELD)
        field.clear()
        field.send_keys(username)
        time.sleep(self.DELAY_INPUT)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)
        time.sleep(self.DELAY_INPUT)

    def click_login(self):
        self.driver.find_element(By.ID, self.LOGIN_BUTTON).click()
        time.sleep(self.DELAY_POST_LOGIN)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.ERROR_MESSAGE)
        if elements:
            return elements[0].text
        return ""

    def is_on_inventory_page(self):
        return "/inventory" in self.driver.current_url
