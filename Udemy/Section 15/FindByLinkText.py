"""
Section 15: Find Element by Link Text
"""

from selenium import webdriver


class FindByLinkText:

    @staticmethod
    def find_element_by_link_text():
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_by_link_text = driver.find_element_by_link_text("Login")

        if element_by_link_text is not None:
            print("We found an element by Link Text")

        driver.close()

    @staticmethod
    def find_element_by_partial_link_text():
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_partial_link_text = driver.find_element_by_partial_link_text("Pract")

        if element_by_partial_link_text is not None:
            print("We found an element by Partial Link Text")

        driver.close()



ff = FindByLinkText()
ff.find_element_by_link_text()
ff.find_element_by_partial_link_text()
