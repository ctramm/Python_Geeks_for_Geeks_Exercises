"""
Section 15: Find element by XPath and CSS Selectors
"""

from selenium import webdriver


class Section15:

    def find_by_xpath(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_xpath = driver.find_element_by_xpath("//*[@id='name']")

        if element_by_xpath is not None:
            print("We found an element by xpath")

        driver.close()

    def find_by_css_selector(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_css_selector = driver.find_element_by_css_selector("#displayed-text")

        if element_by_css_selector is not None:
            print("We found an element by css selector")

        driver.close()


ff = Section15()
ff.find_by_xpath()
ff.find_by_css_selector()
