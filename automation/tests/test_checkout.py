import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.remote.webdriver import WebDriver


# --- Chained Fixtures ---

# Each fixture builds on the previous end state without repeating setup
# Defined here rather than conftest.py as they are only used by this file

@pytest.fixture
def standard_user_checkout_step1(standard_user_session: WebDriver) -> WebDriver:
    inv = InventoryPage(standard_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    CartPage(standard_user_session).click_checkout()
    return standard_user_session


@pytest.fixture
def standard_user_checkout_step2(standard_user_checkout_step1: WebDriver) -> WebDriver:
    checkout = CheckoutPage(standard_user_checkout_step1)
    checkout.fill_first_name("A")
    checkout.fill_last_name("B")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    return standard_user_checkout_step1


@pytest.fixture
def standard_user_confirmation_page(standard_user_checkout_step2: WebDriver) -> WebDriver:
    CheckoutPage(standard_user_checkout_step2).click_finish()
    return standard_user_checkout_step2


# --- standard_user ---

@pytest.mark.smoke
@pytest.mark.standard_user
def test_step1_page_layout(standard_user_checkout_step1) -> None:
    checkout = CheckoutPage(standard_user_checkout_step1)
    assert checkout.get_page_title() == "Checkout: Your Information"
    assert checkout.first_name_field_is_present()
    assert checkout.last_name_field_is_present()
    assert checkout.postal_code_field_is_present()
    assert checkout.continue_button_is_present()
    assert checkout.cancel_button_is_present()


@pytest.mark.standard_user
def test_valid_data_navigates_to_step2(standard_user_checkout_step1) -> None:
    checkout = CheckoutPage(standard_user_checkout_step1)
    checkout.fill_first_name("A")
    checkout.fill_last_name("B")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    assert "checkout-step-two" in standard_user_checkout_step1.current_url


@pytest.mark.standard_user
def test_overview_item_display(standard_user_checkout_step2) -> None:
    checkout = CheckoutPage(standard_user_checkout_step2)
    assert "Sauce Labs Backpack" in checkout.get_item_names()
    assert checkout.get_item_quantities()[0] == "1"


@pytest.mark.standard_user
def test_overview_item_price(standard_user_checkout_step2) -> None:
    checkout = CheckoutPage(standard_user_checkout_step2)
    # zip pairs names and prices by position; keying by name is preferred over index access as display order may vary
    assert dict(zip(checkout.get_item_names(), checkout.get_item_prices()))["Sauce Labs Backpack"] == "$29.99"


@pytest.mark.smoke
@pytest.mark.standard_user
def test_overview_totals_display(standard_user_checkout_step2) -> None:
    checkout = CheckoutPage(standard_user_checkout_step2)
    assert checkout.get_item_total() == "Item total: $29.99"
    assert checkout.get_tax() == "Tax: $2.40"
    assert checkout.get_grand_total() == "Total: $32.39"
    assert checkout.get_payment_info() != ""
    assert checkout.get_shipping_info() != ""


@pytest.mark.smoke
@pytest.mark.standard_user
def test_finish_navigates_to_confirmation(standard_user_checkout_step2) -> None:
    CheckoutPage(standard_user_checkout_step2).click_finish()
    assert "checkout-complete" in standard_user_checkout_step2.current_url


@pytest.mark.smoke
@pytest.mark.standard_user
def test_confirmation_page_content(standard_user_confirmation_page) -> None:
    checkout = CheckoutPage(standard_user_confirmation_page)
    assert "Thank you for your order" in checkout.get_confirmation_header()
    assert checkout.back_home_button_is_present()


@pytest.mark.standard_user
def test_back_home_returns_to_inventory(standard_user_confirmation_page) -> None:
    CheckoutPage(standard_user_confirmation_page).click_back_home()
    assert "/inventory" in standard_user_confirmation_page.current_url
    assert InventoryPage(standard_user_confirmation_page).get_cart_badge_count() == 0


@pytest.mark.standard_user
def test_cancel_step1_returns_to_cart(standard_user_checkout_step1) -> None:
    CheckoutPage(standard_user_checkout_step1).click_cancel_step1()
    assert "/cart" in standard_user_checkout_step1.current_url


@pytest.mark.standard_user
def test_cancel_step2_returns_to_inventory(standard_user_checkout_step2) -> None:
    CheckoutPage(standard_user_checkout_step2).click_cancel_step2()
    assert "/inventory" in standard_user_checkout_step2.current_url


@pytest.mark.standard_user
def test_empty_first_name_error(standard_user_checkout_step1) -> None:
    checkout = CheckoutPage(standard_user_checkout_step1)
    checkout.fill_last_name("B")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    assert "First Name is required" in checkout.get_error_message()


@pytest.mark.standard_user
def test_empty_last_name_error(standard_user_checkout_step1) -> None:
    checkout = CheckoutPage(standard_user_checkout_step1)
    checkout.fill_first_name("A")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    assert "Last Name is required" in checkout.get_error_message()


@pytest.mark.standard_user
def test_empty_postal_code_error(standard_user_checkout_step1) -> None:
    checkout = CheckoutPage(standard_user_checkout_step1)
    checkout.fill_first_name("A")
    checkout.fill_last_name("B")
    checkout.click_continue()
    assert "Postal Code is required" in checkout.get_error_message()


# --- visual_user ---

@pytest.mark.visual_user
def test_visual_user_checkout_prices_correct(visual_user_session) -> None:
    inv = InventoryPage(visual_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    CartPage(visual_user_session).click_checkout()
    checkout = CheckoutPage(visual_user_session)
    checkout.fill_first_name("A")
    checkout.fill_last_name("B")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    # zip pairs names and prices by position; keying by name is preferred over index access as display order may vary
    assert dict(zip(checkout.get_item_names(), checkout.get_item_prices()))["Sauce Labs Backpack"] == "$29.99"
    assert checkout.get_item_total() == "Item total: $29.99"
    assert checkout.get_grand_total() == "Total: $32.39"


# --- problem_user ---

@pytest.mark.defect
@pytest.mark.problem_user
def test_problem_user_checkout_blocked_d023(problem_user_session) -> None:
    # Asserts buggy behaviour as expected outcome; test will fail if defect is resolved
    inv = InventoryPage(problem_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    CartPage(problem_user_session).click_checkout()
    checkout = CheckoutPage(problem_user_session)
    checkout.fill_first_name("A")
    checkout.fill_last_name("B")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    assert "Last Name is required" in checkout.get_error_message()


# --- error_user ---

@pytest.mark.defect
@pytest.mark.error_user
def test_error_user_checkout_fails_d024_d025(error_user_session) -> None:
    # Asserts buggy behaviour as expected outcome; test will fail if defect is resolved
    inv = InventoryPage(error_user_session)
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    CartPage(error_user_session).click_checkout()
    checkout = CheckoutPage(error_user_session)
    checkout.fill_first_name("A")
    checkout.fill_last_name("B")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    assert "checkout-step-two" in error_user_session.current_url
    checkout.click_finish()
    assert "checkout-step-two" in error_user_session.current_url


# --- performance_glitch_user ---

@pytest.mark.performance_glitch_user
def test_performance_glitch_user_checkout_completes(performance_glitch_user_session) -> None:
    inv = InventoryPage(performance_glitch_user_session)
    inv.wait_for_items()
    inv.click_item_button("Sauce Labs Backpack")
    inv.click_cart()
    CartPage(performance_glitch_user_session).click_checkout()
    checkout = CheckoutPage(performance_glitch_user_session)
    checkout.fill_first_name("A")
    checkout.fill_last_name("B")
    checkout.fill_postal_code("12345")
    checkout.click_continue()
    checkout.click_finish()
    assert "checkout-complete" in performance_glitch_user_session.current_url
