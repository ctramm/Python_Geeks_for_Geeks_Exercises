"""
Section 19: Generic Method to Find Elements
"""
from selenium import webdriver
from Udemy.Utils.handy_wrapper import HandyWrappers
import time


class UsingWrappers:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)
        hw = HandyWrappers(driver)

        txt_field = hw.get_element('name')
        txt_field.send_keys("Tests")
        time.sleep(2)

        txt_field2 = hw.get_element("//input[@id='name']", locator_type="xpath")
        txt_field2.clear()


c = UsingWrappers()
c.demo()
