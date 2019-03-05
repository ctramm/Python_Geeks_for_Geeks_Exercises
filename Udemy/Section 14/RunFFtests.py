"""
Section 14: Running Tests on Firefox
"""

from selenium import webdriver


class RunFFTests:

    def test_method(self):
        # Initiate the driver instance
        driver = webdriver.Firefox()
        driver.get('http://www.letskodeit.com')


ff = RunFFTests()
ff.test_method()
