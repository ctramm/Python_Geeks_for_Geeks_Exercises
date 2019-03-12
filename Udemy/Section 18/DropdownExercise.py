"""
Section 18: Dropdown Practice Example
"""
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class DropdownSelect:

    @staticmethod
    def demo():
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        dropdown = driver.find_element_by_id("carselect")
        sel = Select(dropdown)

        sel.select_by_value("benz")
        print("Select Benz by Value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by Index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by Index")


c = DropdownSelect()
c.demo()
