"""
Section 17: Advanced locators exercise
"""
from selenium import webdriver
import time


class Exercise:

    def first(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)

        explicit_element = driver.find_element_by_xpath('//*[@id="product"]/tbody/tr[3]/td[3]')

        if explicit_element is not None:
            print("I have found the element explicitly")
            print("The price for the Python Programming Language is: " + str(explicit_element.text))
        else:
            print("The element was not found, please try again.")

        driver.close()

    def second(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)

        parent_element = driver.find_element_by_xpath('//*[@id="product"]/tbody/tr[1]')

        if parent_element is not None:
            print("I have found the parent element.")
            print("The text value for this element is " + str(parent_element.text))
        else:
            print("The element was not found, please try again.")

        driver.close()

    def greenmile(self):
        base_url = "https://dhtmlx.com/docs/products/dhtmlxGrid/samples/08_filtering/02_pro_filter_combo.html"
        driver = webdriver.Chrome()
        driver.get(base_url)
        time.sleep(10)
        stephen_king = driver.find_element_by_xpath('//*[@id="gridbox"]/div[2]/table/tbody/tr[5]/td[3]')
        green_mile = driver.find_element_by_xpath('//*[@id="gridbox"]/div[2]/table/tbody/tr[5]/td[3]')
        specific_row = driver.find_element_by_xpath('//*[@id="gridbox"]/div[2]/table/tbody/tr[5]')

        if stephen_king is not None:
            print("I have found the stephen king element.")
            print("The text value for this element is " + str(stephen_king.text))
        else:
            print("The element was not found, please try again.")

        if green_mile is not None:
            print("I have found the green mile element.")
            print("The text value for this element is " + str(green_mile.))
        else:
            print("The element was not found, please try again.")

        driver.close()

        if specific_row is not None:
            print("I have found the parent element.")
        else:
            print("The element was not found, please try again.")


c = Exercise()
# c.first()
# c.second()
c.greenmile()
