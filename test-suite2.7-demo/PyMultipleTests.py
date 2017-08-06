"""
An exmaple to demonstrate running mutiple tests in one script
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):

	# use classmethod decorator to enable setting values at class level
	@classmethod
	def setUp(inst):
		# create a new Firefox session, or Chrome service
		inst.driver = webdriver.Firefox()
		inst.driver.implicitly_wait(30)
		#inst.driver.maximize_window()

		# navigate to the test home page
		inst.driver.get("https://www.google.com")

	def test_search_box(self):
		# check search box exists on home page
		self.assertTrue(self.is_element_present(By.NAME, "q"))

	def test_language_settings(self):
		# check language options on home page
		self.assertTrue(self.is_element_present(By.ID, "_eEe"))

	def test_images_link(self):
		# find and use images link on home page
		images_link = self.driver.find_element_by_link_text("Images")
		images_link.click()

		# check search field exists on Images page
		self.assertTrue(self.is_element_present(By.NAME, "q"))
		self.search_field = self.driver.find_element_by_name("q")
		# enter search keyword and submit
		self.search_field.send_keys("Miranda Kerr in bikini")
		self.search_field.submit()

	@classmethod
	def tearDown(inst):
		# close the browser window
		inst.driver.quit()

	def is_element_present(self, how, what):
		"""
		Helper function to confirm the presence of an element on page
		:param how: By locator type
		:param what: locator value
		"""
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException: return False
		return True

if __name__=="__main__":
	unittest.main(verbosity=2)

