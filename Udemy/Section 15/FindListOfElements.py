"""
Section 15: How to find list of elements
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindListOfElements:

    def find_all_elements_by_classname(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_list_by_classname = driver.find_elements_by_class_name("inputs")
        length = len(element_list_by_classname)

        if element_list_by_classname is not None:
            print("Class Name -> Size of the list is: " + str(length))

        driver.close()

    def find_all_elements_by_tagname(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_list_by_tagname = driver.find_elements(By.TAG_NAME, "td")
        length = len(element_list_by_tagname)

        if element_list_by_tagname is not None:
            print("Tag Name - > Size of the list is: " + str(length))

        driver.close()


ff = FindListOfElements()
# ff.find_all_elements_by_classname()
ff.find_all_elements_by_tagname()
