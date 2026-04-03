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

Pass a `BROWSER` environment variable — no file editing required:

```bash
# Linux / macOS
BROWSER=firefox pytest
BROWSER=edge pytest

# Windows (PowerShell)
$env:BROWSER = "firefox"; pytest
```

Supported values: `chrome` (default), `firefox`, `edge`. Firefox requires [geckodriver](https://github.com/mozilla/geckodriver/releases) on PATH; Edge requires msedgedriver. These are driver executables that act as the bridge between Selenium and the browser, the same role ChromeDriver plays for Chrome.

To change the default permanently, edit `BROWSER` in `automation/config.py`. Linux-specific Chrome flags are applied automatically and only when Chrome is selected.

**Changing run speed**

All delay constants are controlled by `FAST_MODE`. Pass it as an environment variable:

```bash
# Linux / macOS
FAST_MODE=true pytest    # near-zero delays (~2 minutes)

# Windows (PowerShell)
$env:FAST_MODE = "true"; pytest
```

`FAST_MODE` defaults to `false` locally and is set automatically to `true` in CI. To change the local default, edit `FAST_MODE` in `automation/config.py`.

Note: `DELAY_SORT` in `InventoryPage` keeps a minimum of 0.3 s even when `FAST_MODE` is on. Sorting triggers a full DOM re-render; removing all delay here produces stale-element failures.

