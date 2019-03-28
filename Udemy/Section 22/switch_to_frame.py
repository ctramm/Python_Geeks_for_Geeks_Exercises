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
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using ID
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name

        # Switch to frame using numbers

        time.sleep(5)
        # Search Course
        search = driver.find_element_by_id("search-courses")
        search.send_keys("python")
        time.sleep(5)

        # Switch back to the parent handle/frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(5)
        driver.find_element_by_id("name").send_keys("Test Successful")
        time.sleep(5)


c = SwitchToFrame()
c.demo()
