"""
Section 21: How to scroll element into view
"""
from selenium import webdriver
import time


class ScrollElement:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Scroll Down
        driver.execute_script("window.scrollBy(0, 900); ")
        time.sleep(3)

        # Scroll Up
        driver.execute_script("window.scrollBy(0, -900); ")
        time.sleep(3)

        # Scroll Element into View
        element = driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150); ")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -900); ")
        time.sleep(3)

        # Native way to scroll element into view
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))



c = ScrollElement()
c.demo()
