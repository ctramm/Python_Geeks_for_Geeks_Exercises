"""
Section 21: Generic Method to take screenshots
"""
from selenium import webdriver
import time


class Screenshot:

    def demo(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys("abc@email.com")
        driver.find_element_by_id("user_password").send_keys("abc")
        driver.find_element_by_name("commit").click()

        self.take_screenshot(driver)

        driver.quit()

    @staticmethod
    def take_screenshot(driver):
        """
        Takes screenshot of the current open web page
        :param driver:
        :return:
        """
        file_name = str(round(time.time() * 1000)) + " .png"
        directory = "C:\\Users\\Ctramm\\PycharmProjects\\Python_Training\\Udemy\\Utils\\Screenshots\\"
        dest_file = directory + file_name

        try:
            driver.save_screenshot(dest_file)
            print("Screenshot saved to directory -->: " + dest_file)
        except NotADirectoryError as e:
            print("Not a directory: " + str(e))


c = Screenshot()
c.demo()
