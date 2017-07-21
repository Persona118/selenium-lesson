"""
exwait_test1.py
A test on explicit wait with expected condition in Selenium webdriver
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

chromeDriver = r"C:\Devs\Python\chromedriver.exe"
driver = webdriver.Chrome(chromeDriver)

