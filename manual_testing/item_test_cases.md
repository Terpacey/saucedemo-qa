# Item Detail Page Test Cases

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_001 |
| Title | Navigate to item detail page via item name |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Inventory page is loaded |
| Steps | 1. Click the name "Sauce Labs Backpack" on the inventory page |
| Expected Result | Item detail page loads for Sauce Labs Backpack |
| Actual Result | Item detail page loaded for Sauce Labs Backpack |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_002 |
| Title | Navigate to item detail page via item image |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Inventory page is loaded |
| Steps | 1. Click the product image for "Sauce Labs Backpack" on the inventory page |
| Expected Result | Item detail page loads for Sauce Labs Backpack |
| Actual Result | Item detail page loaded for Sauce Labs Backpack |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_003 |
| Title | Item name displays correctly on detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Observe the product name displayed on the page |
| Expected Result | Product name reads "Sauce Labs Backpack" |
| Actual Result | Product name reads "Sauce Labs Backpack" |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_004 |
| Title | Item description displays correctly on detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Observe the product description displayed on the page |
| Expected Result | A product description is displayed and is relevant to the item |
| Actual Result | A product description was displayed and is relevant to the item |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_005 |
| Title | Item price displays correctly on detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Observe the product price displayed on the page |
| Expected Result | Price is displayed and matches the price shown on the inventory page |
| Actual Result | Price displayed as $29.99, matching the inventory page |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_006 |
| Title | Item image displays correctly on detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Observe the product image displayed on the page |
| Expected Result | The correct product image is displayed and is relevant to the item |
| Actual Result | The correct product image is displayed and is relevant to the item |
| Status | Passed |
| Priority | P0 |
| Notes | Image shows a forearm in a black sleeve (white skin) holding a backpack by the top handle |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_007 |
| Title | Add to Cart from item detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded<br>Item is not currently in the cart |
| Steps | 1. Click the "Add to cart" button |
| Expected Result | Item is added to the cart |
| Actual Result | Item was added to the cart |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_008 |
| Title | Cart badge increments when item added from detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded<br>Cart is empty |
| Steps | 1. Click the "Add to cart" button<br>2. Observe the cart icon in the top navigation |
| Expected Result | Cart badge appears and displays "1" |
| Actual Result | Cart badge appeared and displayed "1" |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_009 |
| Title | Add to Cart button changes to Remove after item is added |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded<br>Item is not currently in the cart |
| Steps | 1. Click the "Add to cart" button<br>2. Observe the button label |
| Expected Result | Button label changes from "Add to cart" to "Remove" |
| Actual Result | Button label changed from "Add to cart" to "Remove" |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_010 |
| Title | Remove item from item detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded<br>Item is currently in the cart and the Remove button is visible |
| Steps | 1. Click the "Remove" button<br>2. Observe the button label |
| Expected Result | Button label changes from "Remove" to "Add to cart" |
| Actual Result | Button label changed from "Remove" to "Add to cart" |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_011 |
| Title | Cart badge decrements when item removed from detail page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded<br>Item is currently in the cart and the cart badge displays "1" |
| Steps | 1. Click the "Remove" button<br>2. Observe the cart icon in the top navigation |
| Expected Result | Cart badge disappears |
| Actual Result | Cart badge disappeared |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_012 |
| Title | Back to Products navigates to inventory page |
| Preconditions | Browser is open<br>User is logged in as standard_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Click the "Back to products" button |
| Expected Result | Page navigates back to the inventory page |
| Actual Result | Page navigated back to the inventory page |
| Status | Passed |
| Priority | P0 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_013 |
| Title | problem_user - item image on detail page |
| Preconditions | Browser is open<br>User is logged in as problem_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Observe the product image displayed on the page |
| Expected Result | The correct product image is displayed |
| Actual Result | Could not reach Backpack detail page — item name link routed to Fleece Jacket detail page |
| Status | Blocked |
| Priority | P1 |
| Notes | All item links route to the wrong detail pages. Full mapping observed: Backpack → Fleece Jacket, Bolt T-Shirt → Onesie, Onesie → Red T-Shirt, Bike Light → Bolt T-Shirt, Test.allTheThings() T-Shirt → Backpack, Fleece Jacket → "ITEM NOT FOUND" error page. Bike Light detail page is unreachable via any route. "ITEM NOT FOUND" page displays nonsensical error text and an enlarged pug image. Detail pages that do load display correct product data (name, description, price, image). |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_014 |
| Title | visual_user - item price on detail page |
| Preconditions | Browser is open<br>User is logged in as visual_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Observe the product price displayed on the detail page<br>2. Compare to the price shown on the inventory page |
| Expected Result | Price is displayed and matches the price shown on the inventory page |
| Actual Result | Detail page displayed $29.99; inventory page displayed a different price |
| Status | Failed |
| Priority | P1 |
| Notes | — |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_015 |
| Title | visual_user - item image on detail page |
| Preconditions | Browser is open<br>User is logged in as visual_user<br>Item detail page for Sauce Labs Backpack is loaded |
| Steps | 1. Observe the product image displayed on the detail page<br>2. Compare to the image shown on the inventory page |
| Expected Result | The correct product image is displayed |
| Actual Result | Detail page displayed the correct backpack image; inventory page displayed a pug image in its place |
| Status | Failed |
| Priority | P1 |
| Notes | All other items had correct images on both inventory and detail pages |

---

| Field | Details |
|-------|---------|
| Test Case ID | TC_ITM_016 |
| Title | error_user - Add to Cart on detail page for item non-functional on inventory |
| Preconditions | Browser is open<br>User is logged in as error_user<br>Item detail page for Sauce Labs Bolt T-Shirt is loaded<br>Item is not currently in the cart |
| Steps | 1. Click the "Add to cart" button<br>2. Observe the button label and cart badge |
| Expected Result | Item is added to the cart and cart badge increments |
| Actual Result | Add to Cart button could not be clicked; button label did not change and cart badge did not increment |
| Status | Failed |
| Priority | P1 |
| Notes | Behaviour consistent with error_user Add to Cart failure observed on inventory page |
