"""
Section 14: Run Tests on IE
"""
from selenium import webdriver


class RunIETests:

    def test_method(self):
        driver = webdriver.Ie()
        driver.get("http://www.letskodeit.com")
        driver.close()


ie = RunIETests()
ie.test_method()
