"""
Section 18: How to find the state of web element (Disabled and Enabled Elements)
"""
from selenium import webdriver


class ElementState:

    def isEnabled(self):
        base_url = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        e1 = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        e1state = e1.is_enabled()  # True for Enabled and False for Disabled
        print("E1 is enabled? -> " + str(e1state))
        e1.send_keys("letskodeit")


e = ElementState()
e.isEnabled()
