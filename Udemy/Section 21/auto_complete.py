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
        driver.implicitly_wait(5)

        # Send Partial Data
        city_field = driver.find_element_by_id("LandingPageAirSearchForm_originationAirportCode")
        city_field.send_keys("New York")
        time.sleep(3)

        # # Find the item and click
        # item_to_select = driver.find_element_by_xpath(
        #     "//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        # item_to_select.click()

        time.sleep(3)
        driver.quit()


c = AutoComplete()
c.demo()
