from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_btn = "commit"
    _user_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _login_error = "//div[contains(text(), 'Invalid email or password')]"
    _logout = "//div[@id='navbar']//a[@href='/sign_out']"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="link")

    def enter_email(self, email):
        self.send_inputs(email, self._email_field)

    def enter_password(self, password):
        self.send_inputs(password, self._password_field)

    def click_login_btn(self):
        self.element_click(self._login_btn, locator_type="name")

    def login(self, email="", password=""):
        self.click_login_link()
        self.clear_fields()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_btn()

    def verify_login_success(self):
        self.wait_for_element(locator=self._user_icon, locator_type="xpath")
        result = self.is_element_present(locator=self._user_icon, locator_type="xpath")
        return result

    def verify_login_failure(self):
        result = self.is_element_present(self._login_error, locator_type="xpath")
        return result

    def verify_login_title(self):
        return self.verify_page_title("Let's Kode It")

    def logout(self):
        self.nav.navigate_to_users_settings()
        # self.element_click(locator=self._logout, locator_type="xpath")
        logout_link_element = self.wait_for_element(self._logout, "xpath", 10, 5.0)
        self.element_click(locator=self._logout, locator_type="xpath", element=logout_link_element)

    def clear_fields(self):
        email_field = self.get_element(locator=self._email_field)
        email_field.clear()
        password_field = self.get_element(locator=self._password_field)
        password_field.clear()
