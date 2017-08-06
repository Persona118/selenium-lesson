import unittest
from PyRefactorTestCase import SearchText
from PyMultipleTests import HomePageTest
import os
import HTMLTestRunner

# directory to the output HTML file
file_dir = os.getcwd()
out_file = open(file_dir + "/TestReport.html", "w")

# TestLoader to get all tests from SearchText and HomePageTest class
search_text_test = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_text_test and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text_test])

# configure the HTMLtestrunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=out_file, title="Test Report", description="Acceptance Tests")

# run the suite using HtmlTestRunner
runner.run(test_suite)
