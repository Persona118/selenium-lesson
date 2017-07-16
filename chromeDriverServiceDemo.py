"""
Use ChromeDriverService to control ChromeDriver's lifetime for large test suites

ChromeDriverService allows start/stop ChromeDriver server
"""

import time
from selenium import webdriver
import selenium.webdriver.chrome.service as cDriverService

chromeDriver = r"C:\Devs\Python\chromedriver.exe"
cDriverService = cDriverService.Service(chromeDriver)
cDriverService.start()
cDriverCapability = {"chrome.binary":"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"}

driver = webdriver.Remote(cDriverService.service_url, cDriverCapability)
driver.get("https://www.google.co.uk/xhtml")
time.sleep(5)
driver.quit()
