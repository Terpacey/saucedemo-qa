from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# --- standard_user ---

def test_empty_cart_has_no_items(standard_user_session):
    InventoryPage(standard_user_session).click_cart()
    assert CartPage(standard_user_session).get_item_count() == 0


def test_single_item_name_in_cart(standard_user_cart_page):
    assert "Sauce Labs Backpack" in CartPage(standard_user_cart_page).get_item_names()


def test_single_item_price_in_cart(standard_user_cart_page):
    cart = CartPage(standard_user_cart_page)
    # zip pairs names and prices by position; keying by name is preferred over index access as display order may vary
    assert dict(zip(cart.get_item_names(), cart.get_item_prices()))["Sauce Labs Backpack"] == "$29.99"


def test_single_item_quantity_in_cart(standard_user_cart_page):
    assert CartPage(standard_user_cart_page).get_item_quantities()[0] == "1"


def test_multiple_items_in_cart(standard_user_session):
    inv = InventoryPage(standard_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_item_button("Sauce Labs Bike Light")
    inv.click_cart()
    assert CartPage(standard_user_session).get_item_count() == 2


def test_remove_one_item_other_remains(standard_user_session):
    inv = InventoryPage(standard_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_item_button("Sauce Labs Bike Light")
    inv.click_cart()
    cart = CartPage(standard_user_session)
    cart.click_remove("Sauce Labs Backpack")
    assert cart.get_item_count() == 1
    assert cart.get_item_names() == ["Sauce Labs Bike Light"]
    assert cart.get_cart_badge_count() == 1


def test_remove_all_items_cart_empty(standard_user_cart_page):
    cart = CartPage(standard_user_cart_page)
    cart.click_remove("Sauce Labs Backpack")
    assert cart.get_item_count() == 0
    assert cart.get_cart_badge_count() == 0


def test_continue_shopping_navigates_to_inventory(standard_user_cart_page):
    CartPage(standard_user_cart_page).click_continue_shopping()
    assert "/inventory" in standard_user_cart_page.current_url


def test_checkout_navigates_to_step_one(standard_user_cart_page):
    CartPage(standard_user_cart_page).click_checkout()
    assert "checkout-step-one" in standard_user_cart_page.current_url


def test_reset_clears_cart(standard_user_session):
    inv = InventoryPage(standard_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_reset_app_state()
    # Navigate directly to cart URL; reset leaves user on inventory page with no UI path to verify cart state
    standard_user_session.get("https://www.saucedemo.com/cart.html")
    assert CartPage(standard_user_session).get_item_count() == 0


# --- visual_user ---

def test_price_correct_in_cart_visual_user(visual_user_session):
    inv = InventoryPage(visual_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    cart = CartPage(visual_user_session)
    # zip pairs names and prices by position; keying by name is preferred over index access as display order may vary
    assert dict(zip(cart.get_item_names(), cart.get_item_prices()))["Sauce Labs Backpack"] == "$29.99"


# --- problem_user ---

def test_remove_works_in_cart_problem_user(problem_user_session):
    inv = InventoryPage(problem_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    cart = CartPage(problem_user_session)
    cart.click_remove("Sauce Labs Backpack")
    assert cart.get_item_count() == 0
    assert cart.get_cart_badge_count() == 0


# --- error_user ---

def test_remove_works_in_cart_error_user(error_user_session):
    inv = InventoryPage(error_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    cart = CartPage(error_user_session)
    cart.click_remove("Sauce Labs Backpack")
    assert cart.get_item_count() == 0
    assert cart.get_cart_badge_count() == 0


# --- performance_glitch_user ---

def test_cart_accessible_performance_glitch_user(performance_glitch_user_session):
    inv = InventoryPage(performance_glitch_user_session)
    inv.wait_for_items()
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    cart = CartPage(performance_glitch_user_session)
    assert cart.get_item_count() == 1
    cart.click_remove("Sauce Labs Backpack")
    assert cart.get_cart_badge_count() == 0


# --- unauthenticated access (TC_CAR_014) ---

def test_unauthenticated_access_redirects(driver):
    # No session fixture; navigates directly to cart URL without logging in
    driver.get("https://www.saucedemo.com/cart.html")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
    assert LoginPage(driver).get_error_message() != ""
