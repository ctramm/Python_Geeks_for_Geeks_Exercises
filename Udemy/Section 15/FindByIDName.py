"""
Section 15: Find Element by ID and Name

https://letskodeit.teachable.com/pages/practice
"""
from selenium import webdriver


class FindbyIDName:

    def find_by_id(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_id = driver.find_element_by_id("name")

        if element_by_id is not None:
            print("We found an element by id")

        driver.close()

    def find_by_name(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_name = driver.find_element_by_name("show-hide")

        if element_by_name is not None:
            print("We found an element by Name")

        driver.close()

    def yahoo_example(self):
        base_url = "https://www.yahoo.com"
        driver = webdriver.Firefox()
        driver.get(base_url)
        driver.find_element_by_id("uh-signin")


ff = FindbyIDName()
# ff.find_by_id()
# ff.find_by_name()
ff.yahoo_example()
