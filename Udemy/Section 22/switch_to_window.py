"""
Section 22: How to switch window focus
"""
from selenium import webdriver
import time


class SwitchToWindow:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        # Find Parent handle -> Main Window
        parent_handle = driver.current_window_handle
        print("Parent Handle: " + parent_handle)

        # Find open window button and click it
        driver.find_element_by_id("openwindow").click()
        time.sleep(2)

        # Find all handles, there should be two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)


c = SwitchToWindow()
c.demo()
