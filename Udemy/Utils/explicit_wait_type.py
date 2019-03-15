"""
Section 20 Lecture 121: Generic Method to work with explicit wait
"""
from traceback import print_stack
from Udemy.Utils.handy_wrapper import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *


class ExplicitWaitType:

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.hw.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 30, poll_frequency, ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ])
            element = wait.until(ec.element_to_be_clickable((by_type, locator)))

            print("Element appeared on the web page")
        except Exception as e:
            print("Element not appeared on the web page")
            print_stack()
            print("Exception error occurred: " + str(e))
        return element
