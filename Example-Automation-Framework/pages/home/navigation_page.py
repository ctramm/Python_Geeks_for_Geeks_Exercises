from base.base_page import BasePage
import utilities.custom_logger as cl
import logging


class NavigationPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _header_logo = "header-logo"

    def navigate_to_my_courses(self):
        self.element_click(locator=self._my_courses, locator_type="link")

    def navigate_to_all_courses(self):
        self.element_click(locator=self._all_courses, locator_type="link")

    def navigate_to_practice(self):
        self.element_click(locator=self._practice, locator_type="link")

    def navigate_to_users_settings(self):
        self.element_click(locator=self._user_settings_icon, locator_type="xpath")

    def click_header_logo(self):
        self.element_click(locator=self._header_logo, locator_type="class")

