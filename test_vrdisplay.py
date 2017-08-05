# A quick script to show Selenium and Chromedriver are properly installed

"""
Useful links:
https://christopher.su/2015/selenium-chromedriver-ubutnu/
http://coreygoldberg.blogspot.com/2011/07/python-getting-started-with-selenium.html
http://coreygoldberg.blogspot.com/2011/06/python-headless-selenium-webdriver.html
"""

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

display = Display(visible=0, size=(800, 600))
display.start()

# Chrome launches in virtual display
# invisible to user

driver.get("https://www.bbc.co.uk")
try:
	element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "bbccom_native_1_2_3_4")))
	print(driver.title)
	#driver.save_screenshot("~/Documents/selenium-scrncap/bbc.jpeg")
finally:
	driver.quit()

display.stop()
