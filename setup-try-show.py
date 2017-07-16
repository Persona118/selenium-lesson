# A quick script to show Selenium and Chromedriver are properly installed

import unittest
from selenium import webdriver

class TestUbuntuHomepage(unittest.TestCase):

	def setUp(self):
		# define the web browser
		self.browser = webdriver.Chrome()

	# Test case # 1
	def testTitle(self):
		self.browser.get('https://www.ubuntu.com/')
		self.assertIn('Ubuntu', self.browser.title)

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()
