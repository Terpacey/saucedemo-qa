import time

import pytest

DELAY_PAGE_LOAD = 0
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.saucedemo.com")
    time.sleep(DELAY_PAGE_LOAD)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def standard_user_session(driver, login_page):
    login_page.login("standard_user", "secret_sauce")
    return driver


@pytest.fixture
def problem_user_session(driver, login_page):
    login_page.login("problem_user", "secret_sauce")
    return driver


@pytest.fixture
def performance_glitch_user_session(driver, login_page):
    login_page.login("performance_glitch_user", "secret_sauce")
    return driver


@pytest.fixture
def error_user_session(driver, login_page):
    login_page.login("error_user", "secret_sauce")
    return driver


@pytest.fixture
def visual_user_session(driver, login_page):
    login_page.login("visual_user", "secret_sauce")
    return driver
