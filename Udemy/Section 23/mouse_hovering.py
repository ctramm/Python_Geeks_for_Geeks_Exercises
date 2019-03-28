"""
Section 23: Lecture 139 - Mouse Hover Actions
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class MouseHover:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        # Start work
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        item_to_click_locator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        mouse_hover = driver.find_element_by_id("mousehover")
        try:
            actions = ActionChains(driver)
            actions.move_to_element(mouse_hover).perform()
            print("Mouse hovered on element")
            time.sleep(2)

            top_link = driver.find_element_by_xpath(item_to_click_locator)
            actions.move_to_element(top_link).perform()
            print("Item clicked")
            time.sleep(2)
        except Exception as e:
            print("Mouse hover failed on element" + str(e))


c = MouseHover()
c.demo()
