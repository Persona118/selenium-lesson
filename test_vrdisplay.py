# A quick script to show Selenium and Chromedriver are properly installed

"""
Useful links:
https://christopher.su/2015/selenium-chromedriver-ubutnu/
http://coreygoldberg.blogspot.com/2011/07/python-getting-started-with-selenium.html
http://coreygoldberg.blogspot.com/2011/06/python-headless-selenium-webdriver.html
"""

from pyvirtualdisplay import Display
from selenium import webdriver

chromeDriver = r"C:\Devs\Python\chromedriver.exe"
display = Display(visible=0, size=(800, 600))
display.start()

# Chrome launches in virtual display
# invisible to user
driver = webdriver.Chrome(chromeDriver)
driver.get("https://www.bbc.co.uk")
print(driver.title)
dirver.quit()

display.stop()
