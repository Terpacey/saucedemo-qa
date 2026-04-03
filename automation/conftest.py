import os
import sys
import time
import webbrowser
import pytest

from pathlib import Path
from selenium import webdriver
from config import delay, BROWSER
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

DELAY_PAGE_LOAD = delay(1)

# pytest calls this hook once after the full suite finishes, regardless of outcome.
# Opens the HTML report automatically in the default browser so results are immediately visible.
#
# webbrowser.open is used instead of os.startfile/xdg-open so that a single code path
# works on all platforms without OS detection. Path.as_uri() produces a correctly
# formatted file:/// URL on Windows and Linux alike.
def pytest_sessionfinish(session, exitstatus):
    report = os.path.join(session.config.rootdir, "reports", "report.html")
    webbrowser.open(Path(report).as_uri())


# The driver fixture creates a browser instance based on the BROWSER constant in config.py.
#
# Chrome branch:
#   --no-sandbox and --disable-dev-shm-usage are required for Chrome to launch on Linux;
#   they are not needed on Windows and are applied conditionally via OS detection.
#   add_experimental_option suppresses the password save/leak warning, which interferes
#   with many test flows. This API is Chrome-only and is not applied to other browsers.
#
# Firefox branch:
#   signon.rememberSignons = False suppresses the equivalent password-save prompt.
#   No platform-specific flags are required for Firefox on any OS.
#
# All browsers are maximised for headed mode so tests can be observed.

@pytest.fixture
def driver():
    if BROWSER == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.set_preference("signon.rememberSignons", False)
        if os.environ.get("CI"):
            options.add_argument("--headless")
        drv = webdriver.Firefox(options=options)
    else:
        from selenium.webdriver.chrome.options import Options
        options = Options()
        if sys.platform != "win32":
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        if os.environ.get("CI"):
            options.add_argument("--headless=new")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        drv = webdriver.Chrome(options=options)
    drv.maximize_window()
    drv.delete_all_cookies()
    drv.get("https://www.saucedemo.com")
    time.sleep(DELAY_PAGE_LOAD)
    yield drv
    drv.quit()


# Shared setup fixtures providing logged-in sessions and page-specific starting states.

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


@pytest.fixture
def standard_user_cart_page(standard_user_session):
    inv = InventoryPage(standard_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    return standard_user_session


@pytest.fixture
def standard_user_item_page(standard_user_session):
    InventoryPage(standard_user_session).click_item_name("Sauce Labs Backpack")
    return standard_user_session


@pytest.fixture
def error_user_item_page(error_user_session):
    InventoryPage(error_user_session).click_item_name("Sauce Labs Bolt T-Shirt")
    return error_user_session
