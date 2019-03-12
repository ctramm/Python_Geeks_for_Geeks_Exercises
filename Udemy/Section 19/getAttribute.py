"""
Section 19: Get Value of Element Attribute
"""
from selenium import webdriver
import time


class GetAttribute:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")

        print("Value of attribute is: " + result)
        time.sleep(2)
        driver.quit()


c = GetAttribute()
c.demo()
