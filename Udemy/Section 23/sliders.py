"""
Section 23: Lecture 141 - Working with Sliders Actions
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Slider:

    def demo(self):
        base_url = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        element = driver.find_element_by_xpath("//div[@id='slider']//span")
        time.sleep(2)

        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding element successful")
            time.sleep(2)
        except Exception as e:
            print("sliding failed as element: " + str(e))


c = Slider()
c.demo()
