"""
Section 21: Calendar Selection Intro
"""
from selenium import webdriver
import time


class DatePicker:

    @staticmethod
    def demo():
        base_url = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(base_url)

        time.sleep(5)

        # Check flights tab
        flight_tab = driver.find_element_by_id("tab-flight-tab-hp")
        flight_tab.click()

        # Find Departing Field
        flight_departure = driver.find_element_by_id("flight-departing-hp-flight")
        flight_departure.click()

        # Find the date to be selected
        date_to_select = driver.find_element_by_xpath(
            "//*[@id='flight-departing-wrapper-hp-flight']/div/div/div[2]/table/tbody/tr[5]/td[3]/button")
        date_to_select.click()

        time.sleep(3)
        driver.quit()


c = DatePicker()
c.demo()
