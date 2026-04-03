# Saucedemo QA Project

## Overview
This project demonstrates manual and automated quality assurance testing using Python Selenium and PyTest on the SauceDemo platform.

## Purpose
The goal of this project is to showcase QA testing skills including:
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

**Changing the browser**

Set the `BROWSER` constant to your chosen browser:

```python
BROWSER = "chrome"    # default
BROWSER = "firefox"   # requires geckodriver on PATH
BROWSER = "edge"      # requires msedgedriver on PATH
```

Geckodriver (Firefox) and msedgedriver (Edge) are separate executables that act as the bridge between Selenium and their respective browsers. They must be installed and available on your system PATH before switching.

Linux-specific Chrome flags are applied automatically and only when Chrome is selected. No other manual changes are needed when switching browsers.

**Changing run speed**

All delay constants across every page object and `conftest.py` are controlled by the `FAST_MODE` flag:

```python
FAST_MODE = False    # default — runs at human-visible speed (~10 minutes)
FAST_MODE = True     # near-zero delays (~2 minutes)
```

Note: `DELAY_SORT` in `InventoryPage` keeps a minimum of 0.3 s even in `FAST_MODE`. Sorting triggers a full DOM re-render; removing all delay here produces stale-element failures.

