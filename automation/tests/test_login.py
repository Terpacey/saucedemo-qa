import pytest


# --- Valid login tests ---

def test_valid_login_standard_user(standard_user_session):
    assert "/inventory" in standard_user_session.current_url


@pytest.mark.parametrize("username", [
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
])
def test_valid_login_all_users(driver, login_page, username):
    login_page.login(username, "secret_sauce")
    assert login_page.is_on_inventory_page()


# --- Locked out user ---

def test_locked_out_user(driver, login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."


# --- Invalid credential tests ---

def test_invalid_password(driver, login_page):
    login_page.login("standard_user", "wrong_password")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


def test_invalid_username(driver, login_page):
    login_page.login("not_a_user", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


def test_empty_username(driver, login_page):
    login_page.login("", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Username is required"


def test_empty_password(driver, login_page):
    login_page.login("standard_user", "")
    assert login_page.get_error_message() == "Epic sadface: Password is required"


def test_both_fields_empty(driver, login_page):
    login_page.login("", "")
    assert login_page.get_error_message() == "Epic sadface: Username is required"


# --- SQL injection tests ---

def test_sql_injection_username(driver, login_page):
    login_page.login("' OR '1'='1", "secret_sauce")
    assert not login_page.is_on_inventory_page()


def test_sql_injection_password(driver, login_page):
    login_page.login("standard_user", "' OR '1'='1")
    assert not login_page.is_on_inventory_page()
