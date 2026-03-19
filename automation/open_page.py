from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Open Web Browser


driver = webdriver.Chrome()

driver.maximize_window()

driver.delete_all_cookies()


# Navigate to webpage

driver.get("https:/www.saucedemo.com")

time.sleep(3)

#Find username and password, type in details and hit enter
username_bar = driver.find_element(By.ID, "user-name")
username_bar.send_keys("standard_user")
password_bar = driver.find_element(By.ID, "password")
password_bar.send_keys("secret_sauce")
password_bar.send_keys(Keys.RETURN)

time.sleep(3)


# Close Browser
driver.quit()