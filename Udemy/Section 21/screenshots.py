"""
Section 21: How to take screenshots
"""
from selenium import webdriver


class Screenshots:

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

        dest_file_name = "C:\\Users\\Ctramm\\PycharmProjects\\Python_Training\\Udemy\\Utils\\Screenshots"

        try:
            driver.save_screenshot(dest_file_name)
            print("Screenshot saved to test.png")
        except NotADirectoryError:
            print("Not a directory issue")


c = Screenshots()
c.demo()
