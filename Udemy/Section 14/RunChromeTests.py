"""
Section 14: Running tests on Chrome
"""
from selenium import webdriver


class RunChromeTests:

    def test_method(self):
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")
        driver.close()


c = RunChromeTests()
c.test_method()
