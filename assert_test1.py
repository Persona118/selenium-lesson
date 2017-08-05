"""
assert_test1.py
A quick assert test on Python.org
"""

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
	def setUp(self):
		# Windows chromedriver path
		#self.chromeDriver = r"C:\Devs\Python\chromedriver.exe"
		#self.driver = webdriver.Chrome(self.chromeDriver)

		# Linux chromedriver
		self.driver = webdriver.Chrome()

	def test_search_in_python_org(self):
		browser = self.driver
		browser.get("https://www.python.org")
		self.assertIn("Python", browser.title)
		# Find search bar
		pageElem = browser.find_element_by_name("q")
		pageElem.send_keys("pycon")
		pageElem.send_keys(Keys.RETURN)
		assert "No results found." not in browser.page_source
		sleep(2)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
