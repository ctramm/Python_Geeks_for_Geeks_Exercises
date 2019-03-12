"""
Section 19: Get Text on element
"""
from selenium import webdriver
import time


class GetText:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        open_tab_element = driver.find_element_by_id("opentab")
        opte_text = open_tab_element.text
        print("Here is the text of the element: " + opte_text)
        time.sleep(2)

        driver.quit()


c = GetText()
c.demo()
