# Checkout Test Cases

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_001 |
| Title | Checkout step 1 — page layout |
| Preconditions | Browser is open<br>User is logged in as standard_user (password: secret_sauce)<br>At least one item is in the cart<br>Checkout step 1 page is loaded |
| Steps | 1. Observe the page layout, fields, and buttons |
| Expected Result | Page header reads "Checkout: Your Information"; First Name, Last Name, and Zip/Postal Code fields are present; Cancel and Continue buttons are present |
| Actual Result | Header reads "Checkout: Your Information"; First Name, Last Name, and Zip/Postal Code fields present; Cancel and Continue buttons present; no step indicator shown |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_002 |
| Title | Continue with valid data — navigates to step 2 |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>At least one item is in the cart<br>Checkout step 1 page is loaded |
| Steps | 1. Enter a value in First Name<br>2. Enter a value in Last Name<br>3. Enter a value in Zip/Postal Code<br>4. Click Continue |
| Expected Result | Checkout step 2 (overview) page loads |
| Actual Result | Checkout step 2 page loaded; URL: https://www.saucedemo.com/checkout-step-two.html |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_003 |
| Title | Checkout overview — item names and quantities display correctly |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Bike Light is in the cart<br>Checkout step 2 page is loaded |
| Steps | 1. Observe the items listed on the overview page |
| Expected Result | Sauce Labs Bike Light is listed with its name, full description, and quantity 1 |
| Actual Result | Sauce Labs Bike Light listed with full description and quantity 1 |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_004 |
| Title | Checkout overview — item prices display correctly |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Bike Light is in the cart<br>Checkout step 2 page is loaded |
| Steps | 1. Observe the price shown for Sauce Labs Bike Light |
| Expected Result | Price displays as "$9.99" |
| Actual Result | Price displayed as "$9.99" |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_005 |
| Title | Checkout overview — totals, tax, payment, and shipping display correctly |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Sauce Labs Bike Light is in the cart<br>Checkout step 2 page is loaded |
| Steps | 1. Observe the payment information, shipping information, and price total section |
| Expected Result | Payment information, shipping information, item total, tax, and grand total are all shown |
| Actual Result | Payment Information: "SauceCard #31337"; Shipping Information: "Free Pony Express Delivery!"; Item total: $9.99; Tax: $0.80; Total: $10.79 |
| Status | Passed |
| Priority | P0 |
| Notes | Tax is shown as a dollar amount only — no percentage label displayed |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_006 |
| Title | Finish — navigates to order confirmation page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Checkout step 2 page is loaded |
| Steps | 1. Click the Finish button |
| Expected Result | Order confirmation page loads |
| Actual Result | Order confirmation page loaded; URL: https://www.saucedemo.com/checkout-complete.html |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_007 |
| Title | Order confirmation page — layout and content |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Order confirmation page is loaded |
| Steps | 1. Observe the page content |
| Expected Result | A confirmation message is displayed along with a Back Home button |
| Actual Result | Header reads "Checkout: Complete!"; pony graphic labelled "Pony Express" shown; body text reads "Thank you for your order!" and "Your order has been dispatched, and will arrive just as fast as the pony can get there!"; Back Home button present |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_008 |
| Title | Back Home — returns to inventory with empty cart |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Order confirmation page is loaded |
| Steps | 1. Click the Back Home button |
| Expected Result | Inventory page loads; cart badge is not shown |
| Actual Result | Inventory page loaded; cart badge not shown |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_009 |
| Title | Cancel on step 1 — returns to cart |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Checkout step 1 page is loaded |
| Steps | 1. Click the Cancel button |
| Expected Result | Cart page loads |
| Actual Result | Cart page loaded |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_010 |
| Title | Cancel on step 2 — returns to inventory |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Checkout step 2 page is loaded |
| Steps | 1. Click the Cancel button |
| Expected Result | Inventory page loads |
| Actual Result | Inventory page loaded |
| Status | Passed |
| Priority | P0 |
| Notes | Cancel on step 2 returns to inventory rather than back to step 1 or the cart — checkout progress is abandoned |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_011 |
| Title | Continue with empty First Name — error displayed |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Checkout step 1 page is loaded<br>Last Name and Zip/Postal Code fields are populated |
| Steps | 1. Leave First Name empty<br>2. Click Continue |
| Expected Result | An error message is displayed indicating First Name is required; user remains on step 1 |
| Actual Result | Error displayed: "Error: First Name is required"; user remained on step 1 |
| Status | Passed |
| Priority | P0 |
| Notes | Error message format is "Error: X is required" — no "Epic sadface:" prefix; different format from login error messages (see D_001) |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_012 |
| Title | Continue with empty Last Name — error displayed |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Checkout step 1 page is loaded<br>First Name and Zip/Postal Code fields are populated |
| Steps | 1. Leave Last Name empty<br>2. Click Continue |
| Expected Result | An error message is displayed indicating Last Name is required; user remains on step 1 |
| Actual Result | Error displayed: "Error: Last Name is required"; user remained on step 1 |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_013 |
| Title | Continue with empty Postal Code — error displayed |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Checkout step 1 page is loaded<br>First Name and Last Name fields are populated |
| Steps | 1. Leave Zip/Postal Code empty<br>2. Click Continue |
| Expected Result | An error message is displayed indicating Postal Code is required; user remains on step 1 |
| Actual Result | Error displayed: "Error: Postal Code is required"; user remained on step 1 |
| Status | Passed |
| Priority | P0 |
| Notes | — |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_014 |
| Title | visual_user — prices on checkout overview are correct |
| Preconditions | Browser is open<br>User is logged in as visual_user (password: secret_sauce)<br>At least one item is in the cart<br>Checkout step 2 page is loaded |
| Steps | 1. Observe the item prices and totals on the overview page |
| Expected Result | Item prices match the correct catalogue prices and are not randomly altered |
| Actual Result | Sauce Labs Backpack price displayed as "$29.99"; item total $29.99; tax $2.40; total $32.39 — all consistent with correct catalogue prices |
| Status | Passed |
| Priority | P0 |
| Notes | Prices are correct and unaffected by visual_user's inventory-layer price randomisation bug |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_015 |
| Title | problem_user — full checkout flow completes |
| Preconditions | Browser is open<br>User is logged in as problem_user (password: secret_sauce)<br>Sauce Labs Backpack has been added to the cart (Add to Cart works for Backpack as problem_user)<br>Checkout step 1 page is loaded |
| Steps | 1. Enter values in First Name, Last Name, and Zip/Postal Code<br>2. Click Continue<br>3. Observe step 2<br>4. Click Finish |
| Expected Result | Full checkout flow completes; order confirmation page loads |
| Actual Result | First Name field accepted input; input directed at the Last Name field instead overwrote the First Name field — a single keypress overwrote with the last character typed, a pasted or autofilled value overwrote with the full string; Last Name field remained empty; Postal Code accepted input; clicking Continue produced "Error: Last Name is required"; checkout blocked |
| Status | Failed |
| Priority | P0 |
| Notes | See D_023 — Last Name field input is routed to the First Name field for problem_user; checkout cannot be completed |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_016 |
| Title | error_user — checkout flow completes with addable items |
| Preconditions | Browser is open<br>User is logged in as error_user (password: secret_sauce)<br>Sauce Labs Backpack has been added to the cart (one of the three items that can be added)<br>Checkout step 1 page is loaded |
| Steps | 1. Enter values in First Name, Last Name, and Zip/Postal Code<br>2. Click Continue<br>3. Observe step 2<br>4. Click Finish |
| Expected Result | Full checkout flow completes; order confirmation page loads |
| Actual Result | First Name and Postal Code accepted input; Last Name field did not retain input — characters did not appear or cleared instantly; continuing without Last Name produced errors for First Name and Postal Code only, not Last Name, and allowed progression to step 2; Finish button on step 2 was unresponsive — clicking produced no action and checkout could not be completed |
| Status | Failed |
| Priority | P0 |
| Notes | See D_024 — Last Name field non-functional for error_user; see D_025 — Finish button unresponsive for error_user |

| Field | Details |
|-------|---------|
| Test Case ID | TC_CHK_017 |
| Title | performance_glitch_user — checkout flow is accessible and functional |
| Preconditions | Browser is open<br>User is logged in as performance_glitch_user (password: secret_sauce)<br>At least one item is in the cart<br>Inventory page load has fully completed |
| Steps | 1. Navigate to the cart and click Checkout<br>2. Complete step 1 with valid data<br>3. Click Finish on step 2 |
| Expected Result | Full checkout flow completes; order confirmation page loads |
| Actual Result | Checkout flow completed without delay from the cart page onwards; all checkout steps and confirmation page loaded normally; performance glitch isolated to the inventory page |
| Status | Passed |
| Priority | P1 |
| Notes | Performance delay does not extend into the checkout flow; navigating back to inventory re-triggers the glitch via any route — Continue Shopping button, browser back, or Back Home from the confirmation page — consistent with existing performance_glitch_user inventory behaviour |
