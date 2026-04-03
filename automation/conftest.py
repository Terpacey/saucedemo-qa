import os
import subprocess
import sys
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

DELAY_PAGE_LOAD = 1

# pytest calls this hook once after the full suite finishes, regardless of outcome.
# Opens the HTML report automatically in the default browser so results are immediately visible.
#
# Popen is used instead of run so the browser launch does not block pytest from returning
# control to the terminal.
#
# OS detection selects the appropriate file-opener:
# Windows uses os.startfile (built-in, no subprocess needed);
# Linux uses xdg-open.
# session.config.rootdir resolves to the automation/ directory (where pytest.ini lives),
# keeping the path consistent with the --html setting in pytest.ini.
def pytest_sessionfinish(session, exitstatus):
    report = os.path.join(session.config.rootdir, "reports", "report.html")
    if sys.platform == "win32":
        os.startfile(report)
    else:
        subprocess.Popen(["xdg-open", report])


# --no-sandbox and --disable-dev-shm-usage are required for Chrome to launch on Linux;
# they are not needed on Windows and are applied conditionally via OS detection.
#
# Additional option to suppress the password save/leak warning, as it interferes with many test flows.
#
# Chrome is maximised for headed mode so tests can be observed.

@pytest.fixture
def driver():
    options = Options()
    if sys.platform != "win32":
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
