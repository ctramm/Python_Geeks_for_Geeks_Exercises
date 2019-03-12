"""
Section 18: Working with Elements List
"""
from selenium import webdriver
import time


class WorkingWithElementsList:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        rb_cars = driver.find_elements_by_xpath("//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(rb_cars)
        print("The size of the cars button list is: " + str(size) + " items")

        for rb in rb_cars:
            selected = rb.is_selected()

            if not selected:
                rb.click()
                time.sleep(2)


c = WorkingWithElementsList()
c.demo()
