"""
nav_test1.py
A simple script to show navigating a browser with Selenium-Python
"""

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

chromeDriver = r"C:\Devs\Python\chromedriver.exe"
driver = webdriver.Chrome(chromeDriver)

driver.get("https://www.google.co.uk")

try:
    element = driver.find_element_by_id("gb_70")
except NoSuchElementException:
    print("Elemont not found on page")
    driver.quit()

element.click()
assert "Sign in" in driver.title
driver.quit()
