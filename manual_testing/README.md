# Manual Testing

Manual testing cases will attempt to confirm visual and Quality of Life bugs(user feedback, confirmation, etc), as well as run through exploratory test cases simulating a user that is largely unfamiliar with these platforms to see if design is attuned to ease of use.

This folder contains manual test cases for logins for all 6 users, inventory state change test cases, checkout cases and cart cases.

Cases will follow the naming convention of TC_AAA_XX, with AAA referring to a 3 letter marker to reference the type of test ,and XX referencing the number in the order that it was conducted.

Test type naming convention is as follows:

- Login: TC_LOG_XXX
- Inventory: TC_INV_XXX
- Cart: TC_CAR_XXX
- Checkout: TC_CHK_XXX
- Navigation: TC_NAV_XXX

### Defect Priority

For defect priority and severity definitions, refer to the [Test Plan](../test_plan.md)

### Status Values

Status values will be grouped as follows:

- Not Run (Test case has not yet been executed)
- Passed (Test case results in expected outcome)
- Failed (Test case does not result in expected outcome)
- Blocked (Test case cannot be run due to failed preconditions or other functional issues)