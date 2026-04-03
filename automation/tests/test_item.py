from pages.inventory_page import InventoryPage
from pages.item_page import ItemPage

# Module-level constants used as expected values across tests

BACKPACK_NAME = "Sauce Labs Backpack"
BACKPACK_PRICE = "$29.99"


# --- standard_user ---

def test_navigate_via_name_standard_user(standard_user_session):
    InventoryPage(standard_user_session).click_item_name(BACKPACK_NAME)
    assert ItemPage(standard_user_session).get_item_name() == BACKPACK_NAME


def test_navigate_via_image_standard_user(standard_user_session):
    InventoryPage(standard_user_session).click_item_image(BACKPACK_NAME)
    assert "inventory-item" in standard_user_session.current_url


def test_item_name_correct_standard_user(standard_user_item_page):
    assert ItemPage(standard_user_item_page).get_item_name() == BACKPACK_NAME


def test_item_description_present_standard_user(standard_user_item_page):
    assert ItemPage(standard_user_item_page).get_item_description() != ""


def test_item_price_correct_standard_user(standard_user_item_page):
    assert ItemPage(standard_user_item_page).get_item_price() == BACKPACK_PRICE


def test_item_image_correct_standard_user(standard_user_item_page):
    assert "sl-404" not in ItemPage(standard_user_item_page).get_item_image_src()


def test_add_to_cart_increments_badge_standard_user(standard_user_item_page):
    page = ItemPage(standard_user_item_page)
    page.click_add_remove_button()
    assert page.get_cart_badge_count() == 1


def test_add_button_changes_to_remove_standard_user(standard_user_item_page):
    page = ItemPage(standard_user_item_page)
    assert page.get_button_text() == "Add to cart"
    page.click_add_remove_button()
    assert page.get_button_text() == "Remove"


def test_remove_decrements_badge_standard_user(standard_user_item_page):
    page = ItemPage(standard_user_item_page)
    page.click_add_remove_button()
    assert page.get_cart_badge_count() == 1
    page.click_add_remove_button()
    assert page.get_cart_badge_count() == 0


def test_remove_button_changes_to_add_standard_user(standard_user_item_page):
    page = ItemPage(standard_user_item_page)
    page.click_add_remove_button()
    assert page.get_button_text() == "Remove"
    page.click_add_remove_button()
    assert page.get_button_text() == "Add to cart"


def test_back_to_products_standard_user(standard_user_item_page):
    ItemPage(standard_user_item_page).click_back_to_products()
    assert "/inventory" in standard_user_item_page.current_url


# --- problem_user ---

def test_item_links_route_incorrectly_problem_user(problem_user_session):
    InventoryPage(problem_user_session).click_item_name(BACKPACK_NAME)
    assert ItemPage(problem_user_session).get_item_name() != BACKPACK_NAME


# --- visual_user ---

def test_price_mismatch_detail_vs_inventory_visual_user(visual_user_session):
    inv = InventoryPage(visual_user_session)
    # zip pairs names and prices by position; keying by name is preferred over index access as display order may vary
    inventory_price = dict(zip(inv.get_item_names(), inv.get_item_prices()))[BACKPACK_NAME]
    inv.click_item_name(BACKPACK_NAME)
    assert ItemPage(visual_user_session).get_item_price() != inventory_price


def test_detail_image_correct_visual_user(visual_user_session):
    InventoryPage(visual_user_session).click_item_name(BACKPACK_NAME)
    assert "sl-404" not in ItemPage(visual_user_session).get_item_image_src()


# --- error_user ---

def test_add_non_functional_on_detail_error_user(error_user_item_page):
    page = ItemPage(error_user_item_page)
    page.click_add_remove_button()
    assert page.get_cart_badge_count() == 0
