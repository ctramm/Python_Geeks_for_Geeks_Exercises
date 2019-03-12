"""
Section 18: Working with Hidden Elements Practical Example
"""
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class HiddenElements:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Find the state of the text box
        tb_element = driver.find_element_by_id("displayed-text")
        tb_state = tb_element.is_displayed()  # True if visible, False if hidden
        # Exception if not present in the DOM

        tb_element.send_keys(" ")
        tb_element.clear()

        print("Text is visible? " + str(tb_state))
        time.sleep(3)

        # Click the Hide Button
        driver.find_element_by_id("hide-textbox").click()
        # Find the state of the text box
        tb_state = tb_element.is_displayed()  # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(tb_state))
        time.sleep(3)

        # Click the show button
        driver.find_element_by_id("show-textbox").click()
        # Find the state of the text box
        tb_state = tb_element.is_displayed()  # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(tb_state))
        time.sleep(3)

        # Browser Close
        driver.quit()

    def demo_expedia(self):
        base_url = "https://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element_by_id('tab-flight-tab-hp').click()

        dd_element = driver.find_element_by_id("flight-age-select-1-hp-flight")
        print("Element visible? " + str(dd_element.is_displayed()))


c = HiddenElements()
c.demo()
c.demo_expedia()
