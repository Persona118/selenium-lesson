"""
A quick time to show Python-Selenium working with Google Chrome driver
"""

from time import sleep
from selenium import webdriver

chromeDriver = r"C:\Devs\Python\chromedriver.exe"
browser = webdriver.Chrome(chromeDriver)
browser.get("https://www.bing.com")
sleep(3)
browser.quit()
print("test comepleted")
