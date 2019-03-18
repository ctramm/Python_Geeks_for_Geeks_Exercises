"""
Section 21: Executing JavaScript Commands
"""
from selenium import webdriver
import time

class JavaScriptExecution:

    def demo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get("https://letskodeit.teachable.com/p/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(3)
        time.sleep(10)

        # This code does not work as expected.
        # element = driver.find_element_by_id("name")
        # element = driver.execute_script("return document.getElementByID('name');")
        # element.send_keys("Test")


c = JavaScriptExecution()
c.demo()
