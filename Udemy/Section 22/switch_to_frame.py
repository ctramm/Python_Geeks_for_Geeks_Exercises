"""
Section 22: How to work with iFrames
"""
from selenium import webdriver
import time


class SwitchToFrame:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Switch to frame using ID

        # Switch to frame using name

        # Switch to frame using numbers

        # Search Course

        search = driver.find_element_by_id("search-courses")
        search.send_keys("python")


c = SwitchToFrame()
c.demo()
