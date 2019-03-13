"""
Section 19: Generic Method to Find Elements
"""
from selenium.webdriver.common.by import By


class HandyWrappers:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_by_type(locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type + " not correct/supported.")
            return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element Found: " + str(element))
        except Exception as e:
            print("Element not found" + str(e))
        return element

    def is_element_present(self, locator, by_type):
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("Element Found: ")
                return True
            else:
                return False
        except Exception as e:
            print("Element not found" + str(e))
        return False

    def check_elements_presence(self, locator, by_type):
        try:
            li_element = self.driver.find_elements(by_type, locator)
            if len(li_element) > 0:
                print("Element Found: ")
                return True
            else:
                return False
        except Exception as e:
            print("Element not found" + str(e))
        return False

