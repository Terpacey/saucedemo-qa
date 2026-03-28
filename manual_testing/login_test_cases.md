# Login Test Cases

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_001 |
| Title | Valid login - standard_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "standard_user" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | Page changes to the inventory page with user logged in |
| Actual Result | Page changed to inventory page, user is logged in |
| Status | Passed |
| Priority | P0 |
| Notes | Password is written on login page for all users, results in browser giving a "Change your password" warning due to a reported data breach |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_002 |
| Title | Valid login - locked_out_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "locked_out_user" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Sorry, this user has been locked out." |
| Status | Passed |
| Priority | P0 |
| Notes | Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_003 |
| Title | Valid login - problem_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "problem_user" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | Page changes to the inventory page with user logged in |
| Actual Result | Page changed to inventory page, user is logged in |
| Status | Passed |
| Priority | P0 |
| Notes | Password is written on login page for all users, results in browser giving a "Change your password" warning due to a reported data breach<br>User successfully logged in but immediately encounters a visual bug in the inventory where all product images have been replaced with a picture of a dog (pug) with a dirty tennis ball in its mouth |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_004 |
| Title | Valid login - performance_glitch_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "performance_glitch_user" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | Page changes to the inventory page with user logged in |
| Actual Result | Page changed to inventory page, user is logged in |
| Status | Passed |
| Priority | P0 |
| Notes | Password is written on login page for all users, results in browser giving a "Change your password" warning due to a reported data breach<br>User successfully logged in but experienced a noticeably longer page load time compared to other users, consistent with expected behaviour for this account type |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_005 |
| Title | Valid login - error_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "error_user" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | Page changes to the inventory page with user logged in |
| Actual Result | Page changed to inventory page, user is logged in |
| Status | Passed |
| Priority | P0 |
| Notes | Password is written on login page for all users, results in browser giving a "Change your password" warning due to a reported data breach<br>User successfully logged in but the majority of interactive functionality is broken, defects to be documented in subsequent test cases |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_006 |
| Title | Valid login - visual_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "visual_user" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | Page changes to the inventory page with user logged in |
| Actual Result | Page changed to inventory page, user is logged in |
| Status | Passed |
| Priority | P0 |
| Notes | Password is written on login page for all users, results in browser giving a "Change your password" warning due to a reported data breach<br>User successfully logged in but the Backpack product image is replaced with a pug image, defect to be documented in subsequent test cases |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_007 |
| Title | Invalid password - standard_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "standard_user" in the username field<br>2. Enter an invalid password in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | Tested with "blargh" and "invalid" as invalid passwords, both produced the same result<br>Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_008 |
| Title | Invalid password - locked_out_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "locked_out_user" in the username field<br>2. Enter an invalid password in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | Locked out status is not confirmed when credentials do not match, generic invalid credentials message is correct behaviour<br>Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_009 |
| Title | Invalid password - problem_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "problem_user" in the username field<br>2. Enter an invalid password in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_010 |
| Title | Invalid password - performance_glitch_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "performance_glitch_user" in the username field<br>2. Enter an invalid password in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_011 |
| Title | Invalid password - error_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "error_user" in the username field<br>2. Enter an invalid password in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_012 |
| Title | Invalid password - visual_user |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "visual_user" in the username field<br>2. Enter an invalid password in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_013 |
| Title | Invalid username with valid password |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "unregistered_user" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and an appropriate error message is displayed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_014 |
| Title | Special characters in username field |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "###@@" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and a validation message is displayed indicating invalid characters |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Failed |
| Priority | P1 |
| Notes | System handled input safely without crashing but did not meet user feedback standard, no guidance provided to user on invalid input, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_015 |
| Title | Special characters in password field |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "standard_user" in the username field<br>2. Enter "###@@" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and a validation message is displayed indicating invalid characters |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Failed |
| Priority | P1 |
| Notes | System handled input safely without crashing but did not meet user feedback standard, no guidance provided to user on invalid input, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_016 |
| Title | Emoji input in username field |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "😀" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and a validation message is displayed indicating invalid characters |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Failed |
| Priority | P1 |
| Notes | System handled input safely without crashing but did not meet user feedback standard, no guidance provided to user on invalid input, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_017 |
| Title | Emoji input in password field |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "standard_user" in the username field<br>2. Enter "😀" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and a validation message is displayed indicating invalid characters |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Failed |
| Priority | P1 |
| Notes | System handled input safely without crashing but did not meet user feedback standard, no guidance provided to user on invalid input, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_018 |
| Title | SQL injection attempt in username field |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "' OR '1'='1" in the username field<br>2. Enter "secret_sauce" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and authentication is not bypassed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | SQL injection attempt was not treated as a valid input, authentication was not bypassed, system is secure against this attack vector<br>Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |

| Field | Details |
|-------|---------|
| Test Case ID | TC_LOG_019 |
| Title | SQL injection attempt in password field |
| Preconditions | Browser is open<br>Saucedemo login page is loaded<br>No user is currently logged in |
| Steps | 1. Enter "standard_user" in the username field<br>2. Enter "' OR '1'='1" in the password field<br>3. Click the login button |
| Expected Result | User is denied access and authentication is not bypassed |
| Actual Result | User is denied access, error message reads "Epic sadface: Username and password do not match any user in this service" |
| Status | Passed |
| Priority | P0 |
| Notes | SQL injection attempt was not treated as a valid input, authentication was not bypassed, system is secure against this attack vector<br>Error message wording is unprofessional and not suitable for a production environment, flagged for defect report |