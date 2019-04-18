from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, message):
        """
        Takes screenshot of the current open web page
        """
        file_name = message + "." + str(round(time.time() * 1000)) + " .png"
        screenshots_directory = "../screenshots/"
        relative_file_name = screenshots_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshots_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory -->: " + destination_file)
        except Exception as e:
            self.log.error("### EXCEPTION ERROR !!! :: " + str(e))

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported.")
            return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator + " and locatortype: " + locator_type)
        except Exception as e:
            self.log.error("Element not found with locator: " + locator + " and locatortype: " + locator_type)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))
        return element

    def get_elements(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Elements found with locator: " + locator + " and locatortype: " + locator_type)
        except Exception as e:
            self.log.error("Elements not found with locator: " + locator + " and locatortype: " + locator_type)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))
        return element

    def get_element_list(self, locator, locator_type="id"):
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        elements = self.driver.find_elements(by_type, locator)
        if len(elements) > 0:
            self.log.info("Element list FOUND with locator: " + locator +
                          " and locator_type: " + locator_type)
        else:
            self.log.error("Element list NOT FOUND with locator: " + locator +
                           " and locator_type: " + locator_type)
        return elements

    def element_click(self, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatortype: " + locator_type)
        except Exception as e:
            self.log.error("Cannot click on element with locator: " + locator + " locatortype: " + locator_type)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))

    def send_inputs(self, data, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatortype: " + locator_type)
        except Exception as e:
            self.log.error("Cannot send data on element with locator: " + locator +
                           " locatortype: " + locator_type)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))

    def clear_field(self, locator="", locator_type="id"):
        element = self.get_element(locator, locator_type)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " and locator_type: " + locator_type)

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get 'text' on an element
        Provide either element or combination of locator and locator_type
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except Exception as e:
            self.log.error("Failed to get text on an element " + info)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))
            text = None
        return text

    def is_element_present(self, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element is present with locator: " + locator +
                              " and locatortype: " + locator_type)
                return True
            else:
                return False
        except Exception as e:
            self.log.error("Element is not present with locator: " + locator +
                           " and locatortype: " + locator_type)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))
        return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.error("Element NOT displayed")
            return is_displayed
        except Exception as e:
            self.log.error("Element NOT FOUND")
            self.log.error("### EXCEPTION ERROR!!! " + str(e))
            return False

    def check_element_presence(self, locator, locator_type="id"):
        try:
            li_element = self.get_elements(locator, locator_type)
            if len(li_element) > 0:
                self.log.info("Element is present with locator: " + locator +
                              " and locatortype: " + locator_type)
                return True
            else:
                return False
        except Exception as e:
            self.log.error("Element is not present with locator: " + locator +
                           " and locatortype: " + locator_type)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))
        return False

    def wait_for_element(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency, ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ])
            element = wait.until(ec.element_to_be_clickable((by_type, locator)))

            self.log.info("Element appeared on the web page with locator: " + locator +
                          " and locatortype: " + locator_type)
        except Exception as e:
            self.log.error("Element didn't appear on the web page with locator: " + locator +
                           " and locatortype: " + locator_type)
            self.log.error("### EXCEPTION ERROR !!!" + str(e))
        return element

    def verify_title(self):
        if self.get_title() == "Let's Kode It":
            return True
        else:
            return False

    def scroll_page(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -800);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 800);")

    # noinspection PyShadowingBuiltins
    def switch_to_frame(self, id="", name="", index=None):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator="", locator_type="id"):
        if locator:
            element = self.get_element(locator, locator_type)
        value = element.get_attribute(attribute)
        return value

    def is_enabled(self, locator, locator_type="id", info=""):
        element = self.get_element(locator, locator_type)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute="class")
                self.log.info("Attribute value from application web ui ->> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is NOT enabled")
        except Exception as e:
            self.log.error("Element :: '" + info + "' state could not be found")
            self.log.error("### EXCEPTION ERROR!!! " + str(e))
        return enabled
