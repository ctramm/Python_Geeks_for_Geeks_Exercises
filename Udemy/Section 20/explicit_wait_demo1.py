"""
Section 20: Explicit Wait ***Practical Example***
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import time


class ExplicitWait:

    @staticmethod
    def demo():
        base_url = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(base_url)

        wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ])

        time.sleep(5)

        flight_tab = driver.find_element_by_id("tab-flight-tab-hp")
        flight_tab.click()

        flight_origin = driver.find_element_by_id("flight-origin-hp-flight")
        flight_origin.click()
        time.sleep(1)
        flight_origin.send_keys("SFO")

        flight_destination = driver.find_element_by_id("flight-destination-hp-flight")
        flight_destination.click()
        time.sleep(1)
        flight_destination.send_keys("NYC")

        flight_departure = driver.find_element_by_id("flight-departing-hp-flight")
        flight_departure.send_keys("3/24/2019")

        return_date = driver.find_element_by_id("flight-returning-hp-flight")

        for x in range(1, 11):
            return_date.send_keys(Keys.BACKSPACE)
            x += x

        return_date.send_keys("3/26/2019")

        btn_submit = driver.find_element_by_class_name("gcw-submit")
        btn_submit.click()

        element = wait.until(ec.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

        driver.quit()


c = ExplicitWait()
c.demo()
