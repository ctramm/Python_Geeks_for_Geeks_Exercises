"""
Section 22: Lecture 138
"""
from selenium import webdriver
import time

class SwitchToAlert:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        driver.find_element_by_id("name").send_keys("Cameron")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(2)

        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)

        driver.find_element_by_id("name").send_keys("Cameron")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(2)

        alert2 = driver.switch_to.alert
        alert2.dismiss()

        driver.find_element_by_id("name").send_keys("Cameron")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(2)

        alert2.accept()
        time.sleep(5)


c = SwitchToAlert()
c.demo()
