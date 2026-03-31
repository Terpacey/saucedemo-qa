# Inventory Test Cases

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_001 |
| Title | Sort A-Z - standard_user |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Name (A to Z)" from the sort dropdown |
| Expected Result | Items are sorted alphabetically from A to Z |
| Actual Result | Items sorted correctly from A to Z |
| Status | Passed |
| Priority | P1 |
| Notes | |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_002 |
| Title | Sort Z-A - standard_user |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Name (Z to A)" from the sort dropdown |
| Expected Result | Items are sorted alphabetically from Z to A |
| Actual Result | Items sorted correctly from Z to A |
| Status | Passed |
| Priority | P1 |
| Notes | |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_003 |
| Title | Sort price low to high - standard_user |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Price (low to high)" from the sort dropdown |
| Expected Result | Items are sorted by price from lowest to highest |
| Actual Result | Items sorted correctly by price from lowest to highest |
| Status | Passed |
| Priority | P1 |
| Notes | Sauce Labs Onesie is cheapest, Sauce Labs Fleece Jacket is most expensive |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_004 |
| Title | Sort price high to low - standard_user |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Price (high to low)" from the sort dropdown |
| Expected Result | Items are sorted by price from highest to lowest |
| Actual Result | Items sorted correctly by price from highest to lowest |
| Status | Passed |
| Priority | P1 |
| Notes | |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_005 |
| Title | Sort A-Z - error_user |
| Preconditions | Browser is open<br>error_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Name (A to Z)" from the sort dropdown |
| Expected Result | Items are sorted alphabetically from A to Z |
| Actual Result | Popup displayed reading "Sorting is broken! This error has been reported to Backtrace." |
| Status | Failed |
| Priority | P0 |
| Notes | Sort functionality is completely non-functional for error_user, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_006 |
| Title | Sort Z-A - error_user |
| Preconditions | Browser is open<br>error_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Name (Z to A)" from the sort dropdown |
| Expected Result | Items are sorted alphabetically from Z to A |
| Actual Result | Popup displayed reading "Sorting is broken! This error has been reported to Backtrace." |
| Status | Failed |
| Priority | P0 |
| Notes | Sort functionality is completely non-functional for error_user, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_007 |
| Title | Sort price low to high - error_user |
| Preconditions | Browser is open<br>error_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Price (low to high)" from the sort dropdown |
| Expected Result | Items are sorted by price from lowest to highest |
| Actual Result | Popup displayed reading "Sorting is broken! This error has been reported to Backtrace." |
| Status | Failed |
| Priority | P0 |
| Notes | Sort functionality is completely non-functional for error_user, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_008 |
| Title | Sort price high to low - error_user |
| Preconditions | Browser is open<br>error_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select "Price (high to low)" from the sort dropdown |
| Expected Result | Items are sorted by price from highest to lowest |
| Actual Result | Popup displayed reading "Sorting is broken! This error has been reported to Backtrace." |
| Status | Failed |
| Priority | P0 |
| Notes | Sort functionality is completely non-functional for error_user, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_009 |
| Title | Sort functionality - problem_user |
| Preconditions | Browser is open<br>problem_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select each sort option from the sort dropdown |
| Expected Result | Items are sorted according to selected option |
| Actual Result | Sort options can be selected without error popup but items do not reorder |
| Status | Failed |
| Priority | P0 |
| Notes | Sort is silently broken for problem_user, no error is shown to the user, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_010 |
| Title | Sort functionality - visual_user |
| Preconditions | Browser is open<br>visual_user is logged in<br>Inventory page is loaded |
| Steps | 1. Select each sort option from the sort dropdown |
| Expected Result | Items are sorted according to selected option with correct prices displayed |
| Actual Result | Sort operates on displayed prices but prices change to random values on each sort and page refresh, sort order is technically applied but results are unreliable |
| Status | Failed |
| Priority | P1 |
| Notes | Prices are unstable and change on every sort action and page refresh, top left item randomly assigned pug image on each change, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_011 |
| Title | Add item to cart - standard_user |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded<br>Cart is empty |
| Steps | 1. Click "Add to cart" on any item |
| Expected Result | Item is added to cart, button changes to "Remove", cart icon updates with item count |
| Actual Result | Item added to cart, button changed to "Remove", cart icon updated correctly |
| Status | Passed |
| Priority | P0 |
| Notes | Tested with multiple items, all behaved correctly |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_012 |
| Title | Remove item from inventory page - standard_user |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded<br>At least one item is in the cart |
| Steps | 1. Click "Remove" on an item that has been added to the cart |
| Expected Result | Item is removed from cart, button reverts to "Add to cart", cart icon count decrements |
| Actual Result | Item removed from cart, button reverted to "Add to cart", cart icon decremented correctly |
| Status | Passed |
| Priority | P0 |
| Notes | Tested with multiple items, all behaved correctly |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_013 |
| Title | Add item to cart - error_user |
| Preconditions | Browser is open<br>error_user is logged in<br>Inventory page is loaded<br>Cart is empty |
| Steps | 1. Attempt to click "Add to cart" on each of the 6 items |
| Expected Result | All items can be added to cart |
| Actual Result | Only Sauce Labs Backpack, Sauce Labs Bike Light, and Sauce Labs Onesie can be added, remaining items cannot be added |
| Status | Failed |
| Priority | P0 |
| Notes | Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket and Test.allTheThings() T-Shirt (Red) add buttons are non-functional, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_014 |
| Title | Remove item from inventory page - error_user |
| Preconditions | Browser is open<br>error_user is logged in<br>Inventory page is loaded<br>At least one item is in the cart |
| Steps | 1. Attempt to click "Remove" on an item that has been added to the cart |
| Expected Result | Item is removed from cart, button reverts to "Add to cart", cart icon count decrements |
| Actual Result | Remove button is non-functional on inventory page for all items |
| Status | Failed |
| Priority | P0 |
| Notes | Items can still be removed from the cart page directly, inventory page remove is completely non-functional for error_user, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_015 |
| Title | Add item to cart - problem_user |
| Preconditions | Browser is open<br>problem_user is logged in<br>Inventory page is loaded<br>Cart is empty |
| Steps | 1. Attempt to click "Add to cart" on each of the 6 items |
| Expected Result | All items can be added to cart |
| Actual Result | Only Sauce Labs Backpack, Sauce Labs Bike Light, and Sauce Labs Onesie can be added, remaining items cannot be added |
| Status | Failed |
| Priority | P0 |
| Notes | Same add/remove issues as error_user, Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket and Test.allTheThings() T-Shirt (Red) add buttons are non-functional, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_016 |
| Title | Remove item from inventory page - problem_user |
| Preconditions | Browser is open<br>problem_user is logged in<br>Inventory page is loaded<br>At least one item is in the cart |
| Steps | 1. Attempt to click "Remove" on an item that has been added to the cart |
| Expected Result | Item is removed from cart, button reverts to "Add to cart", cart icon count decrements |
| Actual Result | Remove button is non-functional on inventory page for all items |
| Status | Failed |
| Priority | P0 |
| Notes | Items can still be removed from the cart page directly, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_017 |
| Title | Add and remove item - visual_user |
| Preconditions | Browser is open<br>visual_user is logged in<br>Inventory page is loaded<br>Cart is empty |
| Steps | 1. Click "Add to cart" on any item<br>2. Click "Remove" on the same item |
| Expected Result | Item is added and removed correctly, cart icon updates accordingly |
| Actual Result | Add and remove functionality works correctly despite visual bugs |
| Status | Passed |
| Priority | P1 |
| Notes | Core functionality is intact but visual bugs are present on the page, flagged for separate defect reports |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_018 |
| Title | Input registered during page load - performance_glitch_user |
| Preconditions | Browser is open<br>performance_glitch_user is logged in<br>Inventory page is loading |
| Steps | 1. Click anywhere on the inventory page while it is still loading |
| Expected Result | No input should be registered until the page has fully loaded |
| Actual Result | Clicks register on whichever element loads under the cursor, items can be accidentally added or product pages opened during load |
| Status | Failed |
| Priority | P1 |
| Notes | Clicks register on whichever element loads under the cursor during the extended load time, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_019 |
| Title | Visual verification - problem_user |
| Preconditions | Browser is open<br>problem_user is logged in<br>Inventory page is loaded |
| Steps | 1. Visually inspect all product images on the inventory page |
| Expected Result | All product images display correctly |
| Actual Result | All product images replaced with a pug dog holding a dirty tennis ball |
| Status | Failed |
| Priority | P0 |
| Notes | All 6 product images are replaced with the pug image for problem_user, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_020 |
| Title | Visual verification - visual_user |
| Preconditions | Browser is open<br>visual_user is logged in<br>Inventory page is loaded |
| Steps | 1. Visually inspect all product images, prices, buttons and cart icon on the inventory page |
| Expected Result | All visual elements display correctly and consistently |
| Actual Result | Sauce Labs Backpack image randomly replaced with pug image, all prices display random incorrect values that change on refresh and sort, cart button is misaligned, Add to cart button on Test.allTheThings() T-Shirt (Red) is misaligned |
| Status | Failed |
| Priority | P1 |
| Notes | Multiple visual defects present, prices are unstable and change on every interaction, product page shows correct price and image for all items, flagged for defect reports |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_021 |
| Title | Cart icon empty state |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded<br>Cart is empty |
| Steps | 1. Visually inspect the cart icon with no items added |
| Expected Result | Cart icon displays with no count indicator |
| Actual Result | Cart icon displays correctly with no count indicator when cart is empty |
| Status | Passed |
| Priority | P2 |
| Notes | |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_022 |
| Title | Cart icon counter increments on add |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded<br>Cart is empty |
| Steps | 1. Add items to cart one at a time<br>2. Observe cart icon after each addition |
| Expected Result | Cart icon count increments by 1 for each item added |
| Actual Result | Cart icon incremented correctly with each item added, tested with all 6 items |
| Status | Passed |
| Priority | P0 |
| Notes | |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_023 |
| Title | Cart icon counter decrements on remove |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded<br>At least one item is in the cart |
| Steps | 1. Remove items from cart one at a time<br>2. Observe cart icon after each removal |
| Expected Result | Cart icon count decrements by 1 for each item removed |
| Actual Result | Cart icon decremented correctly with each item removed, tested with all 6 items |
| Status | Passed |
| Priority | P0 |
| Notes | |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_024 |
| Title | Navigate to item detail page from inventory |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded |
| Steps | 1. Click on any item heading on the inventory page |
| Expected Result | Item detail page opens showing correct product information |
| Actual Result | Item detail page opened with correct name, description, price, image and add to cart button, back to products link present |
| Status | Passed |
| Priority | P1 |
| Notes | Social media links to Saucelabs Facebook, X and LinkedIn present on item detail page |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_025 |
| Title | Visual verification - performance_glitch_user |
| Preconditions | Browser is open<br>performance_glitch_user is logged in<br>Inventory page is fully loaded |
| Steps | 1. Visually inspect all product images, prices and buttons once page has fully loaded |
| Expected Result | All visual elements display correctly |
| Actual Result | All visual elements display correctly once page has fully loaded |
| Status | Passed |
| Priority | P1 |
| Notes | Page takes noticeably longer to load than other users, all elements are correct once loading is complete |

| Field | Details |
|-------|---------|
| Test Case ID | TC_INV_026 |
| Title | Navigate to empty cart |
| Preconditions | Browser is open<br>standard_user is logged in<br>Inventory page is loaded<br>Cart is empty |
| Steps | 1. Click the cart icon |
| Expected Result | Cart page loads and displays an empty cart state |
| Actual Result | Cart page loaded correctly and displayed empty cart state |
| Status | Passed |
| Priority | P1 |
| Notes | |