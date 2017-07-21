"""
exwait_test1.py
A test on explicit wait with expected condition in Selenium webdriver
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeDriver = r"C:\Devs\Python\chromedriver.exe"
driver = webdriver.Chrome(chromeDriver)

driver.get("https://www.bbc.co.uk")
searchID = "orb-nav-links"
try:
	# await up to 10 sec before a TimeoutException error
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, searchID)))
	print("element %s %s located" % ("ID", searchID))
finally:
	driver.quit()
