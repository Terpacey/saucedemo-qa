# Defect Summary

All defects raised during testing of the SauceDemo platform. Individual defect reports are in `defect_reports/`.

| Defect ID | Feature | Severity | Priority | Status | Description |
|-----------|---------|----------|----------|--------|-------------|
| [D_001](defect_reports/login/D_001.md) | Login | Minor | P1 | Open | All authentication error messages are prefixed with "Epic sadface:" — unprofessional and unsuitable for production |
| [D_002](defect_reports/login/D_002.md) | Login | Minor | P1 | Open | Locked-out user error message reads "Epic sadface: Sorry, this user has been locked out." — unprofessional |
| [D_003](defect_reports/login/D_003.md) | Login | Minor | P1 | Open | Special characters and emoji in credentials produce no validation feedback — login silently fails |
| [D_004](defect_reports/inventory/D_004.md) | Inventory | Major | P1 | Open | All product images replaced with pug dog image for problem_user |
| [D_005](defect_reports/inventory/D_005.md) | Inventory | Major | P1 | Open | Sort dropdown non-functional for problem_user — selecting options produces no reordering |
| [D_006](defect_reports/inventory/D_006.md) | Inventory | Critical | P0 | Open | Add to Cart broken for 3 items; Remove broken for all items for problem_user |
| [D_007](defect_reports/inventory/D_007.md) | Inventory | Critical | P0 | Open | Sort dropdown triggers a popup error for error_user; sorting completely non-functional |
| [D_008](defect_reports/inventory/D_008.md) | Inventory | Critical | P0 | Open | Add to Cart and Remove buttons non-functional for error_user on affected items |
| [D_009](defect_reports/inventory/D_009.md) | Inventory | Major | P1 | Open | Top-left inventory item randomly displays pug dog image on each load and sort for visual_user |
| [D_010](defect_reports/inventory/D_010.md) | Inventory | Critical | P0 | Open | Product prices display random incorrect values on each refresh and sort for visual_user |
| [D_011](defect_reports/inventory/D_011.md) | Inventory | Minor | P2 | Open | Cart icon button visually misaligned in navigation bar for visual_user |
| [D_012](defect_reports/inventory/D_012.md) | Inventory | Minor | P2 | Open | Add to Cart button for Test.allTheThings() T-Shirt (Red) visually misaligned for visual_user |
| [D_013](defect_reports/inventory/D_013.md) | Inventory | Major | P1 | Open | Clicks register on page elements while inventory is loading for performance_glitch_user — items added unintentionally |
| [D_014](defect_reports/inventory/D_014.md) | Inventory | Major | P1 | Open | Clicking during page load navigates to item detail pages for performance_glitch_user |
| [D_015](defect_reports/inventory/D_015.md) | Inventory | Major | P1 | Open | Reset App State clears cart data but inventory page UI does not update — Remove buttons do not revert |
| [D_016](defect_reports/inventory/D_016.md) | Inventory | Critical | P0 | Open | Cart contents persist across user sessions — different users inherit previous user's cart state |
| [D_017](defect_reports/item/D_017.md) | Item | Critical | P0 | Open | All item detail page links broken for problem_user — navigation routes to wrong pages or "ITEM NOT FOUND" |
| [D_018](defect_reports/item/D_018.md) | Item | Critical | P0 | Open | Add to Cart and Remove non-functional on item detail pages for error_user on affected items |
| [D_019](defect_reports/cart/D_019.md) | Cart | Major | P1 | Open | Checkout button active on empty cart — full checkout flow completable with $0.00 total |
| [D_020](defect_reports/cart/D_020.md) | Cart | Minor | P2 | Open | No mechanism to adjust item quantity — each item limited to 1 per session with no editable field |
| [D_021](defect_reports/cart/D_021.md) | Cart | N/A | N/A | Void | Defect ID allocated but not raised — no defect recorded under this number |
| [D_022](defect_reports/cart/D_022.md) | Cart | Minor | P2 | Open | Checkout button visually misaligned for visual_user — positioned top-right instead of bottom of page |
| [D_023](defect_reports/checkout/D_023.md) | Checkout | Critical | P0 | Open | Last Name input overwrites First Name field for problem_user on checkout step 1 |
| [D_024](defect_reports/checkout/D_024.md) | Checkout | Major | P1 | Open | Last Name field does not retain input for error_user on checkout step 1 |
| [D_025](defect_reports/checkout/D_025.md) | Checkout | Critical | P0 | Open | Finish button unresponsive for error_user on checkout step 2 — checkout cannot be completed |
