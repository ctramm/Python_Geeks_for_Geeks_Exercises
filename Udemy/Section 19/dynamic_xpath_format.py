"""
Section 19: How to Build Dynamic XPath
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from Udemy.Utils.handy_wrapper import HandyWrappers
import time


class BuildDynamicXPath:

    def demo(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        # Login -> Lecture "How to click and type on a web element"
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Search for courses
        all_courses = driver.find_element(By.LINK_TEXT, "All Courses")
        all_courses.click()
        # search_box = driver.find_element(By.ID, "search-courses")
        # search_box.send_keys("JavaScript")

        # Select Course
        # Explicit XPath
        # //div[contains(@class, 'course-listing-title') and contains(text(),'JavaScript for beginners')]
        # Dynamic XPath
        # //div[contains(@class, 'course-listing-title') and contains(text(),'{0}')]
        course_name = "JavaScript for beginners"
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(),'{0}')]"
        _course_locator = _course.format(course_name)

        course_element = driver.find_element(By.XPATH, _course_locator)
        course_element.click()
        time.sleep(5)


c = BuildDynamicXPath()
c.demo()
