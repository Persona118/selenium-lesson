import unittest
from PyRefactorTestCase import SearchText
from PyMultipleTests import HomePageTest

# TestLoader to get all tests from SearchText and HomePageTest class
search_text_test = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_text_test and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text_test])

# run the test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)

