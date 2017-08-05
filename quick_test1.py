"""
A quick time to show Python-Selenium working with Google Chrome driver
"""

from time import sleep
from selenium import webdriver

# Windows chromedriver path
#chromeDriver = r"C:\Devs\Python\chromedriver.exe"

# Linux chromedriver path
browser = webdriver.Chrome()

browser.get("https://www.bing.com")
sleep(2)
browser.quit()
print("test comepleted")
