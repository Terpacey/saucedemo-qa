# Test Plan - Saucedemo

## Overview

Saucedemo is an e-commerce platform meant for testing purposes. In line with this, the objective of this test plan is to cover all real world use cases of such a platform using standard user expectations.

## Scope
### Inclusions
This repository will focus on the following tests

Automated:

- Verify all 6 user accounts can successfully authenticate with valid credentials
- Verify complete e-commerce cycle (add to cart, remove, checkout) for all 6 user accounts
- Verify all core user flows behave correctly with valid inputs
- Verify the application handles invalid inputs and edge cases appropriately
- Verify application state is managed correctly across user sessions and actions

Manual:

- Verify all visual elements render correctly across all user accounts
- Verify user feedback mechanisms such as confirmation messages, error messages, and UI state updates are present and accurate
- Conduct exploratory testing simulating an inexperienced e-commerce user to evaluate platform usability and surface undocumented defects

### Test environment

- OS: Fedora Linux KDE 43
- Browser: Chrome
- Python 3.14.3
- Automation designed to be portable across operating systems

### Exclusions

Performance testing, load testing, and accessibility testing are out of scope as the current environment lacks the required tools and infrastructure for such testing.

## Test Strategy

### Automated

Automated test cases will use Selenium to run through all major real world use cases and will complete e-commerce cycles for all available users in the system. Each user will login, add items, remove items either from the inventory page or cart, add items back and go through the entire checkout process, some users will also abandon their carts and reopen to see if sessions can be continued without any defects.

### Manual

Manual testing cases will attempt to confirm visual and Quality of Life bugs(user feedback, confirmation, etc), as well as run through exploratory test cases simulating a user that is largely unfamiliar with these platforms to see if design is attuned to ease of use.

## Defect Reporting Procedure

Defects will be described as functionality that does not match with standard e-commerce user expectations, a standard user is assumed to be an average user that is not tech-literate but not an advanced or technical user. Defects will be reported by writing a report in the defect_reports folder as an md file, individually on a case-by-case basis. Defect reports will be grouped using sub-folders, and all reports will follow the naming convention of D_XXX, with XXX representing the number, starting with 001 to represent the Defect ID. These reports will contain the following:

- Defect ID (Repeat of file name)
- Status
- Severity
- Priority
- Defect Description
- Expected Result
- Actual Result
- Steps to Reproduce
- Date Raised
- Reference

Defect Priority will be grouped as follows:

- P0 (High, resolve immediately)
- P1 (Medium, resolve ASAP for next build)
- P2 (Low, resolve in any future version)

Severity will be grouped as follows:

- Blocker (Cannot proceed further in test cycle)
- Critical (Main function not working, breaks user flow, cannot proceed further)
- Major (Causes undesirable behaviour but still functional)
- Minor (Will not cause breakdown of flow)

## Roles/Responsibilities

All testing, documentation, and automation performed by Hari.C

## Test Deliverables

- Test case execution report, summarizing all test cases and referencing them
- Defect report summarizing all defects in main folder, referencing all defects reported in defect_reports folder

## Entry and Exit Criteria

### Entry Criteria

- Environment is set up and functional
- Site is accessible through chosen web browser(Chrome)
- Test plan has been completed and reviewed

### Exit Criteria

- All test cases have been completed
- Test cases have been marked appropriately(Pass,Fail, Blocked, etc)
- Defect reports created for bugs or defects if any
- All critical and high priority defects have been logged and documented in the defect_reports folder

## Suspension and Resumption Criteria

### Suspension Criteria

- Saucedemo crashes frequently to the point of being unusable
- Saucedemo is no longer available
- Environment causes bugs or crashes affecting test results

### Resumption Criteria

- Saucedemo is stable and accessible
- Environment issues have been resolved and verified as functional

## Tools

- Python
- Selenium WebDriver
- Pytest
- GitHub / GitHub Desktop
- VSCodium (Development Environment)

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Saucedemo becomes temporarily or permanently unavailable | Site has been publicly available and is maintained by a larger corporation, site will likely go back up in time |
| Non-standard OS causes unexpected environment behaviour | Environment has been tested independently to ensure functionality, despite it being a non-standard OS, browser features are standard |
| Flatpak sandboxing causes dependency or interpreter conflicts | Browser and all development tools were installed without Flatpak to ensure sandboxing does not create any issues |
| VSCodium extensions or dependencies behave unexpectedly | All VSCodium dependencies and extensions have been independently tested and verified |
| Linux-specific browser or driver compatibility issues | All Linux dependencies have been independently verified via Konsole to ensure best possible functionality |