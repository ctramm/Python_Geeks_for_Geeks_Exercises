"""
Section 18: Radio buttons and checkboxes
"""
from selenium import webdriver
import time


class RadioButtonsAndCheckboxes:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        rb_bmw = driver.find_element_by_id("bmwradio")
        rb_bmw.click()

        time.sleep(2)

        rb_benz = driver.find_element_by_id("benzradio")
        rb_benz.click()

        time.sleep(2)

        ck_bmw = driver.find_element_by_id("bmwcheck")
        ck_bmw.click()
        time.sleep(2)

        ck_benz = driver.find_element_by_id("benzcheck")
        ck_benz.click()
        time.sleep(2)

        # True if selected, False if unselected
        print("BMW Radio button is selected? " + str(rb_bmw.is_selected()))
        print("Benz Radio button is selected? " + str(rb_benz.is_selected()))
        print("BMW Checkbox is selected? " + str(ck_bmw.is_selected()))
        print("Benz Checkbox is selected? " + str(ck_benz.is_selected()))


c = RadioButtonsAndCheckboxes()
c.demo()
