"""
Section 15: Understanding "By" class
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementBy:

    @staticmethod
    def find_element_by():
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_by_id = driver.find_element(By.ID, "name")

        if element_by_id is not None:
            print("We found an element by Id")

        element_by_Xpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if element_by_Xpath is not None:
            print("We found an element by XPAth")

        element_by_link_text = driver.find_element(By.LINK_TEXT, "Login")

        if element_by_link_text is not None:
            print("We found an element by Link Text")

        driver.close()


ff = FindElementBy()
ff.find_element_by()
