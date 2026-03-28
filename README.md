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
- PyTest
- GitHub Version Control

## Project Structure
- manual_testing/ → Manual test documentation
- automation/ → Automated test scripts
- automation/pages/ → Page object models
- automation/tests/ → Test implementations

## How to Run Automation Tests
```bash
pip install -r automation/requirements.txt
pytest
```
The browser set up for this project is Chrome to represent the most common user base.
To change the web browser used, navigate to 
- automation/
Open the script and find the following line of code

```bash
driver = webdriver.Chrome()
```
Change it from Chrome to the browser of your choice after ensuring all required drivers are installed.
For example, to change the browser to Edge, edit the code to match the following:

```bash
driver = webdriver.Edge()
```
