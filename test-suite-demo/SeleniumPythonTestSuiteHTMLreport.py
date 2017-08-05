import unittest
from SeleniumPythonRefactorTestCase import SearchText
from SeleniumPythonMultipleTests import HomePageTest
import os
import HtmlTestRunner

# directory to the output HTML file
file_dir = os.getcwd()

# TestLoader to get all tests from SearchText and HomePageTest class
search_text_test = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_text_test and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text_test])

# configure the HTMLtestrunner options
runner = HtmlTestRunner.HTMLTestRunner(output=file_dir)

# run the suite using HtmlTestRunner
runner.run(test_suite)
