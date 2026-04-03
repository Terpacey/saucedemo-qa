# Requirements Traceability Matrix

## Project: Saucedemo QA Portfolio

This matrix links all manual test cases and automated tests to their feature areas and any defects raised. Automated test function names refer to files in `automation/tests/`.

---

## Summary

| | Login | Inventory | Item | Cart | Checkout | Total |
|---|---|---|---|---|---|---|
| **Manual TCs** | 19 | 26 | 16 | 14 | 17 | **92** |
| **Passed** | 15 | 13 | 12 | 13 | 15 | **68** |
| **Failed** | 4 | 13 | 3 | 1 | 2 | **23** |
| **Blocked** | 0 | 0 | 1 | 0 | 0 | **1** |
| **Defects Raised** | 3 | 12 | 2 | 4 | 3 | **24** |

---

## Login

| TC ID | Title | Manual Status | Automated Test(s) | Defects Raised |
|---|---|---|---|---|
| TC_LOG_001 | Valid login — standard_user | Passed | `test_valid_login_standard_user` | — |
| TC_LOG_002 | Valid login — locked_out_user | Passed | `test_locked_out_user` | D_002 |
| TC_LOG_003 | Valid login — problem_user | Passed | `test_valid_login_all_users[problem_user]` | — |
| TC_LOG_004 | Valid login — performance_glitch_user | Passed | `test_valid_login_all_users[performance_glitch_user]` | — |
| TC_LOG_005 | Valid login — error_user | Passed | `test_valid_login_all_users[error_user]` | — |
| TC_LOG_006 | Valid login — visual_user | Passed | `test_valid_login_all_users[visual_user]` | — |
| TC_LOG_007 | Invalid password — standard_user | Passed | `test_invalid_password` | D_001 |
| TC_LOG_008 | Invalid password — locked_out_user | Passed | — | D_001 |
| TC_LOG_009 | Invalid password — problem_user | Passed | — | D_001 |
| TC_LOG_010 | Invalid password — performance_glitch_user | Passed | — | D_001 |
| TC_LOG_011 | Invalid password — error_user | Passed | — | D_001 |
| TC_LOG_012 | Invalid password — visual_user | Passed | — | D_001 |
| TC_LOG_013 | Invalid username with valid password | Passed | `test_invalid_username` | D_001 |
| TC_LOG_014 | Special characters in username field | Failed | — | D_003 |
| TC_LOG_015 | Special characters in password field | Failed | — | D_003 |
| TC_LOG_016 | Emoji input in username field | Failed | — | D_003 |
| TC_LOG_017 | Emoji input in password field | Failed | — | D_003 |
| TC_LOG_018 | SQL injection — username field | Passed | `test_sql_injection_username` | — |
| TC_LOG_019 | SQL injection — password field | Passed | `test_sql_injection_password` | — |

### Automation-only (Login)

These tests have no corresponding manual test case.

| Automated Test | Scenario |
|---|---|
| `test_empty_username` | Empty username field — "Username is required" error |
| `test_empty_password` | Empty password field — "Password is required" error |
| `test_both_fields_empty` | Both fields empty — "Username is required" error |

---

## Inventory

| TC ID | Title | Manual Status | Automated Test(s) | Defects Raised |
|---|---|---|---|---|
| TC_INV_001 | Sort A–Z — standard_user | Passed | `test_sort_standard_user[az]` | — |
| TC_INV_002 | Sort Z–A — standard_user | Passed | `test_sort_standard_user[za]` | — |
| TC_INV_003 | Sort price low to high — standard_user | Passed | `test_sort_standard_user[lohi]` | — |
| TC_INV_004 | Sort price high to low — standard_user | Passed | `test_sort_standard_user[hilo]` | — |
| TC_INV_005 | Sort A–Z — error_user | Failed | `test_sort_triggers_alert_error_user[az]` | D_007 |
| TC_INV_006 | Sort Z–A — error_user | Failed | `test_sort_triggers_alert_error_user[za]` | D_007 |
| TC_INV_007 | Sort price low to high — error_user | Failed | `test_sort_triggers_alert_error_user[lohi]` | D_007 |
| TC_INV_008 | Sort price high to low — error_user | Failed | `test_sort_triggers_alert_error_user[hilo]` | D_007 |
| TC_INV_009 | Sort functionality — problem_user | Failed | `test_sort_silently_broken_problem_user` | D_005 |
| TC_INV_010 | Sort functionality — visual_user | Failed | — | — |
| TC_INV_011 | Add item to cart — standard_user | Passed | `test_add_button_changes_to_remove_standard_user` | — |
| TC_INV_012 | Remove item from inventory — standard_user | Passed | `test_remove_from_inventory_decrements_badge_standard_user` | — |
| TC_INV_013 | Add item to cart — error_user | Failed | `test_only_three_items_addable_error_user` | D_008 |
| TC_INV_014 | Remove item from inventory — error_user | Failed | `test_remove_non_functional_on_inventory_error_user` | D_008 |
| TC_INV_015 | Add item to cart — problem_user | Failed | `test_only_three_items_addable_problem_user` | D_006 |
| TC_INV_016 | Remove item from inventory — problem_user | Failed | `test_remove_non_functional_on_inventory_problem_user` | D_006 |
| TC_INV_017 | Add and remove item — visual_user | Passed | `test_add_remove_functional_visual_user` | — |
| TC_INV_018 | Input registered during page load — performance_glitch_user | Failed | — | D_013, D_014 |
| TC_INV_019 | Visual verification — problem_user | Failed | `test_all_images_are_pug_problem_user` | D_004 |
| TC_INV_020 | Visual verification — visual_user | Failed | `test_prices_randomised_visual_user` | D_009, D_010, D_011, D_012 |
| TC_INV_021 | Cart icon — empty state | Passed | `test_cart_badge_absent_when_empty_standard_user` | — |
| TC_INV_022 | Cart icon counter — increments on add | Passed | `test_add_to_cart_increments_badge_standard_user` | — |
| TC_INV_023 | Cart icon counter — decrements on remove | Passed | `test_remove_from_inventory_decrements_badge_standard_user` | — |
| TC_INV_024 | Navigate to item detail page from inventory | Passed | — | — |
| TC_INV_025 | Visual verification — performance_glitch_user | Passed | `test_items_correct_after_load_performance_glitch_user` | — |
| TC_INV_026 | Navigate to empty cart | Passed | `test_cart_navigation_standard_user` | — |

### Automation-only (Inventory)

These tests have no corresponding manual test case.

| Automated Test | Scenario |
|---|---|
| `test_item_count_standard_user` | Verifies exactly 6 items are displayed on the inventory page |
| `test_item_names_standard_user` | Verifies all item names match expected values |
| `test_item_prices_standard_user` | Verifies all item prices match expected values for standard_user |

---

## Item Detail

| TC ID | Title | Manual Status | Automated Test(s) | Defects Raised |
|---|---|---|---|---|
| TC_ITM_001 | Navigate to detail page via item name | Passed | `test_navigate_via_name_standard_user` | — |
| TC_ITM_002 | Navigate to detail page via item image | Passed | `test_navigate_via_image_standard_user` | — |
| TC_ITM_003 | Item name displays correctly | Passed | `test_item_name_correct_standard_user` | — |
| TC_ITM_004 | Item description displays correctly | Passed | `test_item_description_present_standard_user` | — |
| TC_ITM_005 | Item price displays correctly | Passed | `test_item_price_correct_standard_user` | — |
| TC_ITM_006 | Item image displays correctly | Passed | `test_item_image_correct_standard_user` | — |
| TC_ITM_007 | Add to Cart from detail page | Passed | `test_add_to_cart_increments_badge_standard_user` | — |
| TC_ITM_008 | Cart badge increments when item added | Passed | `test_add_to_cart_increments_badge_standard_user` | — |
| TC_ITM_009 | Add button changes to Remove | Passed | `test_add_button_changes_to_remove_standard_user` | — |
| TC_ITM_010 | Remove item from detail page | Passed | `test_remove_button_changes_to_add_standard_user` | — |
| TC_ITM_011 | Cart badge decrements when item removed | Passed | `test_remove_decrements_badge_standard_user` | — |
| TC_ITM_012 | Back to Products navigates to inventory | Passed | `test_back_to_products_standard_user` | — |
| TC_ITM_013 | problem_user — item detail page routing | Blocked | `test_item_links_route_incorrectly_problem_user` | D_017 |
| TC_ITM_014 | visual_user — item price on detail page | Failed | `test_price_mismatch_detail_vs_inventory_visual_user` | D_010 |
| TC_ITM_015 | visual_user — item image on detail page | Failed | `test_detail_image_correct_visual_user` | D_009 |
| TC_ITM_016 | error_user — Add to Cart on detail page | Failed | `test_add_non_functional_on_detail_error_user` | D_018 |

---

## Cart

| TC ID | Title | Manual Status | Automated Test(s) | Defects Raised |
|---|---|---|---|---|
| TC_CAR_001 | Navigate to cart — empty state | Passed | `test_empty_cart_has_no_items` | D_019 |
| TC_CAR_002 | Single item — verify display | Passed | `test_single_item_name_in_cart`, `test_single_item_price_in_cart`, `test_single_item_quantity_in_cart` | D_020 |
| TC_CAR_003 | Multiple items — all display correctly | Passed | `test_multiple_items_in_cart` | — |
| TC_CAR_004 | Remove one item — remaining item unaffected | Passed | `test_remove_one_item_other_remains` | — |
| TC_CAR_005 | Remove all items — cart returns to empty state | Passed | `test_remove_all_items_cart_empty` | — |
| TC_CAR_006 | Continue Shopping — returns to inventory | Passed | `test_continue_shopping_navigates_to_inventory` | — |
| TC_CAR_007 | Checkout button — navigates to step 1 | Passed | `test_checkout_navigates_to_step_one` | — |
| TC_CAR_008 | visual_user — prices correct in cart | Passed | `test_price_correct_in_cart_visual_user` | D_011, D_022 |
| TC_CAR_009 | problem_user — cart display and Remove | Passed | `test_remove_works_in_cart_problem_user` | — |
| TC_CAR_010 | error_user — Remove works in cart | Passed | `test_remove_works_in_cart_error_user` | — |
| TC_CAR_011 | performance_glitch_user — cart accessible | Passed | `test_cart_accessible_performance_glitch_user` | — |
| TC_CAR_012 | Reset App State — cart cleared | Passed | `test_reset_clears_cart` | D_015 |
| TC_CAR_013 | Cart contents do not persist across users | Failed | — | D_016 |
| TC_CAR_014 | Unauthenticated access — redirected to login | Passed | `test_unauthenticated_access_redirects` | — |

---

## Checkout

| TC ID | Title | Manual Status | Automated Test(s) | Defects Raised |
|---|---|---|---|---|
| TC_CHK_001 | Step 1 — page layout | Passed | `test_step1_page_layout` | — |
| TC_CHK_002 | Continue with valid data — navigates to step 2 | Passed | `test_valid_data_navigates_to_step2` | — |
| TC_CHK_003 | Overview — item names and quantities | Passed | `test_overview_item_display` | — |
| TC_CHK_004 | Overview — item prices | Passed | `test_overview_item_price` | — |
| TC_CHK_005 | Overview — totals, tax, payment, shipping | Passed | `test_overview_totals_display` | — |
| TC_CHK_006 | Finish — navigates to confirmation | Passed | `test_finish_navigates_to_confirmation` | — |
| TC_CHK_007 | Confirmation page — layout and content | Passed | `test_confirmation_page_content` | — |
| TC_CHK_008 | Back Home — returns to inventory with empty cart | Passed | `test_back_home_returns_to_inventory` | — |
| TC_CHK_009 | Cancel on step 1 — returns to cart | Passed | `test_cancel_step1_returns_to_cart` | — |
| TC_CHK_010 | Cancel on step 2 — returns to inventory | Passed | `test_cancel_step2_returns_to_inventory` | — |
| TC_CHK_011 | Empty First Name — error displayed | Passed | `test_empty_first_name_error` | — |
| TC_CHK_012 | Empty Last Name — error displayed | Passed | `test_empty_last_name_error` | — |
| TC_CHK_013 | Empty Postal Code — error displayed | Passed | `test_empty_postal_code_error` | — |
| TC_CHK_014 | visual_user — prices correct at overview | Passed | `test_visual_user_checkout_prices_correct` | — |
| TC_CHK_015 | problem_user — checkout blocked at step 1 | Failed | `test_problem_user_checkout_blocked_d023` | D_023 |
| TC_CHK_016 | error_user — checkout flow fails | Failed | `test_error_user_checkout_fails_d024_d025` | D_024, D_025 |
| TC_CHK_017 | performance_glitch_user — checkout functional | Passed | `test_performance_glitch_user_checkout_completes` | — |

---

## Defect Index

| Defect ID | Area | Severity | Priority | Status | Referenced By |
|---|---|---|---|---|---|
| D_001 | Login | Minor | P1 | Open | TC_LOG_007–013 |
| D_002 | Login | Minor | P1 | Open | TC_LOG_002 |
| D_003 | Login | Minor | P1 | Open | TC_LOG_014–017 |
| D_004 | Inventory | Major | P1 | Open | TC_INV_019 |
| D_005 | Inventory | Major | P1 | Open | TC_INV_009 |
| D_006 | Inventory | Critical | P0 | Open | TC_INV_015, TC_INV_016 |
| D_007 | Inventory | Critical | P0 | Open | TC_INV_005–008 |
| D_008 | Inventory | Critical | P0 | Open | TC_INV_013, TC_INV_014 |
| D_009 | Inventory | Major | P1 | Open | TC_INV_020, TC_ITM_015 |
| D_010 | Inventory | Critical | P0 | Open | TC_INV_020, TC_ITM_014 |
| D_011 | Inventory | Minor | P2 | Open | TC_INV_020, TC_CAR_008 |
| D_012 | Inventory | Minor | P2 | Open | TC_INV_020 |
| D_013 | Inventory | Major | P1 | Open | TC_INV_018 |
| D_014 | Inventory | Major | P1 | Open | TC_INV_018 |
| D_015 | Inventory | Major | P1 | Open | TC_CAR_012 |
| D_016 | Inventory | Critical | P0 | Open | TC_CAR_013 |
| D_017 | Item | Critical | P0 | Open | TC_ITM_013 |
| D_018 | Item | Critical | P0 | Open | TC_ITM_016 |
| D_019 | Cart | Major | P1 | Open | TC_CAR_001 |
| D_020 | Cart | Minor | P2 | Open | TC_CAR_002 |
| D_022 | Cart | Minor | P2 | Open | TC_CAR_008 |
| D_023 | Checkout | Critical | P0 | Open | TC_CHK_015 |
| D_024 | Checkout | Major | P1 | Open | TC_CHK_016 |
| D_025 | Checkout | Critical | P0 | Open | TC_CHK_016 |

_D_021 was not raised; defect IDs are not fully sequential._
