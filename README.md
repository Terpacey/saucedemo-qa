# Saucedemo QA Project

## Overview
This project demonstrates manual and automated quality assurance testing using Python Selenium and PyTest on the SauceDemo platform.

## Purpose
The goal of this project is to showcase junior QA testing skills including:
- Test planning
- Manual test documentation
- Basic automation testing
- Page Object Model structure

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- GitHub Version Control

## Project Structure
- test_plan.md → Test plan
- rtm.md → Requirements Traceability Matrix
- manual_testing/ → Manual test cases
- defect_reports/ → Individual defect reports logged during testing
- automation/ → Automated test scripts
- automation/pages/ → Page object models
- automation/tests/ → Test implementations

## How to Run Automation Tests

```bash
pip install -r automation/requirements.txt
cd automation
pytest
```

An HTML report is generated automatically at `automation/reports/report.html` and will open in your default browser when the run completes. Each run overwrites the previous report.

Each page object in `automation/pages/` contains delay constants (e.g. `DELAY_ACTION`, `DELAY_SORT`, `DELAY_POST_LOGIN`) and `automation/conftest.py` contains `DELAY_PAGE_LOAD`. These are set to non-zero values to make test execution visible at human speed. With delays enabled, the full suite takes approximately 10 minutes. Setting all delay constants to `0` reduces this to approximately 2 minutes.

The browser used for this project is Chrome. To change the browser, open `automation/conftest.py` and locate the `driver` fixture. Find the following line:

```python
driver = webdriver.Chrome(options=options)
```

Replace it with the driver for your chosen browser, ensuring the relevant driver is installed. For example, to use Edge:

```python
driver = webdriver.Edge(options=options)
```
Note: Current config settings only work for Chromium-based browsers, please ensure that you run these automation tests accordingly.

Linux-specific Chrome flags and the post-run report opener are applied automatically based on the detected OS. No manual changes are needed when switching between Linux and Windows.
