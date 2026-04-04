import pytest

from pages.inventory_page import InventoryPage

# Module-level constants used as expected values across tests

EXPECTED_NAMES = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]

EXPECTED_PRICES = {
    "Sauce Labs Backpack": "$29.99",
    "Sauce Labs Bike Light": "$9.99",
    "Sauce Labs Bolt T-Shirt": "$15.99",
    "Sauce Labs Fleece Jacket": "$49.99",
    "Sauce Labs Onesie": "$7.99",
    "Test.allTheThings() T-Shirt (Red)": "$15.99",
}


# --- standard_user ---

@pytest.mark.smoke
@pytest.mark.standard_user
def test_item_count_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    assert len(page.get_item_names()) == 6


@pytest.mark.standard_user
def test_item_names_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    assert page.get_item_names() == EXPECTED_NAMES


@pytest.mark.standard_user
def test_item_prices_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    names = page.get_item_names()
    prices = page.get_item_prices()
    # zip pairs names and prices by position; keying by name is preferred over index access as display order may vary
    displayed = dict(zip(names, prices))
    assert displayed == EXPECTED_PRICES


@pytest.mark.standard_user
def test_cart_badge_absent_when_empty_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    assert page.get_cart_badge_count() == 0


@pytest.mark.smoke
@pytest.mark.standard_user
def test_add_to_cart_increments_badge_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 1


@pytest.mark.standard_user
def test_remove_from_inventory_decrements_badge_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 1
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 0


@pytest.mark.standard_user
def test_add_button_changes_to_remove_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    assert page.get_button_text_for_item("Sauce Labs Backpack") == "Add to cart"
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_button_text_for_item("Sauce Labs Backpack") == "Remove"


@pytest.mark.standard_user
@pytest.mark.parametrize("sort_value,expected_first,expected_last", [
    ("az",   "Sauce Labs Backpack",               "Test.allTheThings() T-Shirt (Red)"),
    ("za",   "Test.allTheThings() T-Shirt (Red)", "Sauce Labs Backpack"),
    ("lohi", "Sauce Labs Onesie",                 "Sauce Labs Fleece Jacket"),
    ("hilo", "Sauce Labs Fleece Jacket",           "Sauce Labs Onesie"),
])
def test_sort_standard_user(standard_user_session, sort_value, expected_first, expected_last) -> None:
    page = InventoryPage(standard_user_session)
    page.set_sort_order(sort_value)
    names = page.get_item_names()
    assert names[0] == expected_first
    assert names[-1] == expected_last


@pytest.mark.standard_user
def test_cart_navigation_standard_user(standard_user_session) -> None:
    page = InventoryPage(standard_user_session)
    page.click_cart()
    assert "/cart" in standard_user_session.current_url


# --- error_user ---

@pytest.mark.defect
@pytest.mark.error_user
@pytest.mark.parametrize("sort_value", ["az", "za", "lohi", "hilo"])
def test_sort_triggers_alert_error_user(error_user_session, sort_value) -> None:
    page = InventoryPage(error_user_session)
    # Page loads sorted az by default; sorting az again produces no change and no alert
    # Pre-sort to za first to ensure az triggers a real state change and fires an alert
    # Without the pre-sort, sorting az produces no alert and the assertion fails
    if sort_value == "az":
        page.set_sort_order("za")
        page.get_sort_alert_text_and_dismiss()
    page.set_sort_order(sort_value)
    alert_text = page.get_sort_alert_text_and_dismiss()
    assert alert_text == "Sorting is broken! This error has been reported to Backtrace."


@pytest.mark.defect
@pytest.mark.error_user
def test_only_three_items_addable_error_user(error_user_session) -> None:
    page = InventoryPage(error_user_session)
    for name in EXPECTED_NAMES:
        page.click_item_button(name)
    assert page.get_cart_badge_count() == 3


@pytest.mark.defect
@pytest.mark.error_user
def test_remove_non_functional_on_inventory_error_user(error_user_session) -> None:
    page = InventoryPage(error_user_session)
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 1
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 1


# --- problem_user ---

@pytest.mark.defect
@pytest.mark.problem_user
def test_sort_silently_broken_problem_user(problem_user_session) -> None:
    page = InventoryPage(problem_user_session)
    names_before = page.get_item_names()
    page.set_sort_order("za")
    names_after = page.get_item_names()
    assert names_after == names_before


@pytest.mark.defect
@pytest.mark.problem_user
def test_all_images_are_pug_problem_user(problem_user_session) -> None:
    page = InventoryPage(problem_user_session)
    srcs = page.get_item_image_srcs()
    assert len(srcs) == 6
    assert all("sl-404" in src for src in srcs)


@pytest.mark.defect
@pytest.mark.problem_user
def test_only_three_items_addable_problem_user(problem_user_session) -> None:
    page = InventoryPage(problem_user_session)
    for name in EXPECTED_NAMES:
        page.click_item_button(name)
    assert page.get_cart_badge_count() == 3


@pytest.mark.defect
@pytest.mark.problem_user
def test_remove_non_functional_on_inventory_problem_user(problem_user_session) -> None:
    page = InventoryPage(problem_user_session)
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 1
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 1


# --- visual_user ---

@pytest.mark.visual_user
def test_add_remove_functional_visual_user(visual_user_session) -> None:
    page = InventoryPage(visual_user_session)
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 1
    page.click_item_button("Sauce Labs Backpack")
    assert page.get_cart_badge_count() == 0


@pytest.mark.defect
@pytest.mark.visual_user
def test_prices_randomised_visual_user(visual_user_session) -> None:
    page = InventoryPage(visual_user_session)
    names = page.get_item_names()
    prices = page.get_item_prices()
    displayed = dict(zip(names, prices))
    # Both lists are sorted before comparing so the assertion targets value differences, not ordering
    correct_prices = sorted(EXPECTED_PRICES.values())
    displayed_prices = sorted(displayed.values())
    assert displayed_prices != correct_prices


# --- performance_glitch_user ---

@pytest.mark.performance_glitch_user
def test_items_correct_after_load_performance_glitch_user(performance_glitch_user_session) -> None:
    page = InventoryPage(performance_glitch_user_session)
    page.wait_for_items()
    assert page.get_item_names() == EXPECTED_NAMES
    names = page.get_item_names()
    prices = page.get_item_prices()
    assert dict(zip(names, prices)) == EXPECTED_PRICES
