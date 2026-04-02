

# Cart Page Test Cases

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_001 |
| Title | Navigate to cart page — empty cart state |
| Preconditions | Browser is open<br>User is logged in as standard_user (password: secret_sauce)<br>No items have been added to the cart<br>Inventory page is loaded |
| Steps | 1. Click the cart icon in the top-right corner of the page |
| Expected Result | Cart page loads; page header reads "Your Cart"; no items are listed; "Continue Shopping" and "Checkout" buttons are visible; cart badge is not shown |
| Actual Result | Cart page loaded; header reads "Your Cart"; QTY and Description column headers shown; no items listed; no placeholder text; "Continue Shopping" and "Checkout" buttons present; no cart badge shown |
| Status | Passed |
| Priority | P0 |
| Notes | Checkout button is active on an empty cart; proceeding through checkout with no items results in a $0.00 order being accepted — see D_019 |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_002 |
| Title | Single item in cart — verify item display |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Backpack has been added to the cart<br>Cart page is loaded |
| Steps | 1. Observe the contents of the cart page |
| Expected Result | Sauce Labs Backpack is listed with its name, a short description, price "$29.99", and quantity "1"; a Remove button is present for the item |
| Actual Result | Sauce Labs Backpack listed with full product description matching the inventory page; price "$29.99"; quantity "1" shown in a non-editable box to the left of the item name; Remove button present; no product image displayed; no subtotal shown on the page |
| Status | Passed |
| Priority | P0 |
| Notes | No product image displayed in cart; quantity field is non-editable — see D_020 |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_003 |
| Title | Multiple items in cart — all items display correctly |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Backpack and Sauce Labs Bike Light have been added to the cart<br>Cart page is loaded |
| Steps | 1. Observe the contents of the cart page |
| Expected Result | Both items are listed, each with name, description, price, and quantity "1"; Remove buttons are present for each item; cart badge on the icon shows 2 |
| Actual Result | Sauce Labs Backpack and Sauce Labs Bike Light both listed; items appeared in the order they were added (most recently added appears last); each item showed name, full description, price, and quantity "1"; Remove buttons present; cart badge showed 2 |
| Status | Passed |
| Priority | P0 |
| Notes | Consistent ordering confirmed: items always appear in the order they were added to the cart |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_004 |
| Title | Remove one item — remaining item is unaffected |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Backpack and Sauce Labs Bike Light are in the cart<br>Cart page is loaded |
| Steps | 1. Click the Remove button for Sauce Labs Backpack |
| Expected Result | Sauce Labs Backpack is removed from the cart; Sauce Labs Bike Light remains listed; cart badge decrements to 1 |
| Actual Result | Sauce Labs Backpack removed; Sauce Labs Bike Light remained listed; cart badge decremented to 1 immediately with no delay |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_005 |
| Title | Remove all items — cart returns to empty state |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Backpack is in the cart<br>Cart page is loaded |
| Steps | 1. Click the Remove button for Sauce Labs Backpack |
| Expected Result | Cart is empty; no items are listed; cart badge is not shown or shows 0 |
| Actual Result | Cart returned to empty state; no items listed; no cart badge shown; appearance consistent with TC_CAR_001 |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_006 |
| Title | Continue Shopping — returns to inventory page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Cart page is loaded |
| Steps | 1. Click the "Continue Shopping" button |
| Expected Result | Inventory page loads |
| Actual Result | Inventory page loaded |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_007 |
| Title | Checkout button — navigates to checkout step 1 |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>At least one item is in the cart<br>Cart page is loaded |
| Steps | 1. Click the "Checkout" button |
| Expected Result | Checkout step 1 page loads (URL contains "checkout-step-one") |
| Actual Result | Checkout step 1 page loaded; URL: https://www.saucedemo.com/checkout-step-one.html |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_008 |
| Title | visual_user — item prices display correctly in cart |
| Preconditions | Browser is open<br>User is logged in as visual_user (password: secret_sauce)<br>Sauce Labs Backpack has been added to the cart from the inventory page<br>Cart page is loaded |
| Steps | 1. Observe the price displayed for Sauce Labs Backpack in the cart |
| Expected Result | Price displays as "$29.99" |
| Actual Result | Price displayed as "$29.99"; cart icon misaligned (D_011); Checkout button displayed in the top-right of the page near the Swag Labs heading rather than at the bottom of the page (D_022) |
| Status | Passed |
| Priority | P0 |
| Notes | Price correct and unaffected by visual_user's inventory-layer price randomisation bug; see D_011 for cart icon misalignment; see D_022 for Checkout button misalignment on the cart page |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_009 |
| Title | problem_user — cart display and Remove functionality |
| Preconditions | Browser is open<br>User is logged in as problem_user (password: secret_sauce)<br>Sauce Labs Backpack has been added to the cart from the inventory page<br>Cart page is loaded |
| Steps | 1. Observe the item displayed in the cart<br>2. Click the Remove button for Sauce Labs Backpack |
| Expected Result | Step 1: Sauce Labs Backpack is listed with name, description, price, and quantity 1<br>Step 2: Item is removed from the cart; cart returns to empty state |
| Actual Result | No product image shown in cart (consistent with all users); item name, description, and price correct; Remove button removed the item and cleared the cart badge |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_010 |
| Title | error_user — Remove functionality works in cart |
| Preconditions | Browser is open<br>User is logged in as error_user (password: secret_sauce)<br>Sauce Labs Backpack has been added to the cart from the inventory page<br>Cart page is loaded |
| Steps | 1. Click the Remove button for Sauce Labs Backpack |
| Expected Result | Sauce Labs Backpack is removed from the cart; cart returns to empty state |
| Actual Result | Remove button removed the item and cleared the cart badge |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_011 |
| Title | performance_glitch_user — cart page is accessible and functional |
| Preconditions | Browser is open<br>User is logged in as performance_glitch_user (password: secret_sauce)<br>Sauce Labs Backpack has been added to the cart<br>Inventory page load has fully completed |
| Steps | 1. Click the cart icon<br>2. Observe the cart page<br>3. Click Remove for Sauce Labs Backpack |
| Expected Result | Cart page loads; item is displayed correctly; Remove button successfully removes the item |
| Actual Result | Cart page loaded without delay; item displayed correctly; performance glitch did not extend beyond the inventory page; navigating back to inventory from the cart via the Continue Shopping button or browser back button re-triggered the performance glitch |
| Status | Passed |
| Priority | P1 |
| Notes | Performance delay is isolated to the inventory page; re-entering inventory from the cart re-triggers the glitch — consistent with existing performance_glitch_user inventory behaviour |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_012 |
| Title | Reset App State — cart badge and cart page reflect cleared state |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Backpack has been added to the cart<br>Inventory page is loaded |
| Steps | 1. Open the burger menu (top-left)<br>2. Click "Reset App State"<br>3. Close the burger menu<br>4. Observe the cart icon badge<br>5. Click the cart icon and observe the cart page |
| Expected Result | Step 4: Cart badge shows 0 or is no longer visible<br>Step 5: Cart page shows no items |
| Actual Result | Cart badge disappeared immediately after Reset App State; cart page was empty; Remove buttons on the inventory page remained active and clickable after reset |
| Status | Passed |
| Priority | P1 |
| Notes | See D_015 — Remove buttons on inventory page are not reverted to Add to Cart after Reset App State; clicking Remove on the inventory page post-reset produced no visible change |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_013 |
| Title | Cart contents do not persist across user sessions |
| Preconditions | Browser is open |
| Steps | 1. Log in as standard_user (password: secret_sauce)<br>2. Add Sauce Labs Backpack to the cart<br>3. Log out via the burger menu<br>4. Log in as problem_user (password: secret_sauce)<br>5. Click the cart icon |
| Expected Result | Cart is empty; no items from the previous session are present |
| Actual Result | Sauce Labs Backpack added by standard_user was present in problem_user's cart on login |
| Status | Failed |
| Priority | P0 |
| Notes | Formally reproduces D_016 during cart testing |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_CAR_014 |
| Title | Unauthenticated access to cart page is blocked |
| Preconditions | Browser is open<br>No user is logged in (or user has logged out) |
| Steps | 1. Navigate directly to https://www.saucedemo.com/cart.html |
| Expected Result | User is redirected to the login page and cannot access the cart |
| Actual Result | Redirected to the login page; error message displayed: "Epic sadface: You can only access '/cart.html' when you are logged in." |
| Status | Passed |
| Priority | P1 |
| Notes | Error message uses "Epic sadface:" prefix, consistent with login error format |
