"""
Section 21: AutoComplete Intro and Practical Example
"""
from selenium import webdriver
import time


class AutoComplete:

    def demo(self):
        base_url = "http://www.southwest.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        time.sleep(10)

        # Send Partial Data
        city_field = driver.find_element_by_id("LandingPageAirSearchForm_originationAirportCode")
        city_field.send_keys("New York")

        time.sleep(10)

        # Find the item and click
        desc = driver.find_element_by_id("LandingPageAirSearchForm_originationAirportCode--menu")
        item_to_click = desc.find_element_by_id("LandingPageAirSearchForm_originationAirportCode--item-2")
        item_to_click.click()

        time.sleep(3)
        driver.quit()


c = AutoComplete()
c.demo()
