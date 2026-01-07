from selenium import webdriver
import time


# Open Web browser

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()

# Navigate to webpage
driver.get("https://www.saucedemo.com/")

time.sleep(3)

#Close browser
driver.quit()