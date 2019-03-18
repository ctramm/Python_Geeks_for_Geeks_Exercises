"""
Section 21: How to find the size of the window
"""
from selenium import webdriver


class WindowSize:

    def demo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))


c = WindowSize()
c.demo()
