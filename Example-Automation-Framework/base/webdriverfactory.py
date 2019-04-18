"""
@package base

WebDriver Factor Class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        base_url = "https://letskodeit.teachable.com/"
        if self.browser == "ie":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()

        # Settings and Open URL
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)

        return driver
