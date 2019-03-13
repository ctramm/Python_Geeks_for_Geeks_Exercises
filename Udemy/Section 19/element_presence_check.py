"""
Section 19: How to check if element is present
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from Udemy.Utils.handy_wrapper import HandyWrappers
import time


class CheckElementPresence:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        hw = HandyWrappers(driver)
        driver.get(base_url)

        # id='name'
        # //*[@id='name']
        element_result = hw.is_element_present("name", By.ID)
        print(str(element_result))

        element_result2 = hw.check_elements_presence("//input[@id='name1']", By.XPATH)
        print(str(element_result2))


c = CheckElementPresence()
c.demo()
