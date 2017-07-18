"""
an example to quickly demonstrate Selenium-Python
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# start the webdriver
chromeDriver = r"C:\Devs\Python\chromedriver.exe"
driver = webdriver.Chrome(chromeDriver)

# navigate to a site
driver.get("https://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source
sleep(3)
driver.close()
print("test completed")
