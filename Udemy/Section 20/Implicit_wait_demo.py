"""
Section 20: Implicit Wait ***Practice Example***
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class ImplicitWaitDemo:

    def demo(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        login_link = driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a")
        login_link.click()

        email_field = driver.find_element_by_id("user_email")
        email_field.send_keys("test")


c = ImplicitWaitDemo()
c.demo()
