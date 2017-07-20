"""
nav_unittest1.py

A simple unit test to show interaction with www.google.co.uk
"""

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions

class GoogleSignIn(unittest.TestCase):
	def setUp(self):
		self.chromeDriver = r"C:\Devs\Python\chromedriver.exe"
		self.driver = webdriver.Chrome(self.chromeDriver)

	def test_search_in_python_org(self):
		self.driver.get("https://www.google.co.uk")

		element_ID = "gb_70"
		self.assertTrue(self.Is_element_present(By.ID, element_ID), "Element no found on page")
		element = self.driver.find_element_by_id(element_ID)
		element.click()
		#sleep(3)
		searchStr = "Sijgn in"
		self.assertIn(searchStr, self.driver.title)
		#assert (searchStr in self.driver.title), ("%s not in page title" % searchStr)
		print("GoogleSignIn test completed")

	def Is_element_present(self, findBy, findWhat):
		"""
		Determine if an element is present on current page
		findBy - how to find the element, HTML tag, string type
		findWhat - what to find in element, HTML property, string type
		"""
		try:
			self.driver.find_element(by=findBy, value=findWhat)
		except NoSuchElementException as e:
			return False
		return True

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
