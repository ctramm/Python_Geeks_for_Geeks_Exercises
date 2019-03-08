"""
Section 15: Find Element by Class Name and Text Name
"""
from selenium import webdriver


class FindElementByClassTag:

    def find_element_by_class_name(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_by_class = driver.find_element_by_class_name("displayed-class")
        element_by_class.send_keys("Hello World")

        if element_by_class is not None:
            print("We found an element by Class Name")

        driver.close()

    def find_element_by_tag_name(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_by_tag = driver.find_element_by_tag_name("h1")
        print(element_by_tag.text)

        if element_by_tag is not None:
            print("We found an element by tag Name")

        driver.close()


ff = FindElementByClassTag()
# ff.find_element_by_class_name()
ff.find_element_by_tag_name()
