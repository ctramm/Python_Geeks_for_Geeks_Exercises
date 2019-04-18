import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class RegisterCoursesPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """
    ################
    ### Locators ###
    ################
    """

    _search_box = "search-courses"
    _search_course_icon = "search-course-button"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _zip = "postal"
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"

    """
    ############################
    ### Element Interactions ###
    ############################
    """

    def enter_course_name(self, name):
        self.send_inputs(name, locator=self._search_box)
        self.element_click(locator=self._search_course_icon)

    def select_course_to_enroll(self, full_course_name):
        self.element_click(locator=self._course.format(full_course_name), locator_type="xpath")

    def click_enroll_button(self):
        self.element_click(locator=self._enroll_button)

    def enter_card_num(self, num):
        self.switch_to_frame(name="__privateStripeFrame5")
        self.send_inputs(num, locator=self._cc_num, locator_type="xpath")
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        self.switch_to_frame(name="__privateStripeFrame6")
        self.send_inputs(exp, locator=self._cc_exp, locator_type="name")
        self.switch_to_default_content()

    def enter_card_cvv(self, cvv):
        self.switch_to_frame(name="__privateStripeFrame7")
        self.send_inputs(cvv, locator=self._cc_cvv, locator_type="name")
        self.switch_to_default_content()

    def enter_zip(self, zip_code):
        self.switch_to_frame(name="__privateStripeFrame8")
        self.send_inputs(zip_code, locator=self._zip, locator_type="name")
        self.switch_to_default_content()

    def click_agree_to_terms_checkbox(self):
        self.element_click(locator=self._agree_to_terms_checkbox)

    def click_enroll_submit_button(self):
        self.element_click(locator=self._submit_enroll, locator_type="xpath")

    def enter_cc_info(self, num, exp, cvv, zip_code):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)
        self.enter_zip(zip_code)

    def enroll_course(self, num="", exp="", cvv="", zip_code=""):
        self.click_enroll_button()
        self.scroll_page(direction="down")
        self.enter_cc_info(num, exp, cvv, zip_code)
        self.click_agree_to_terms_checkbox()

    def verify_enroll_button_is_disabled(self):
        result = self.is_enabled(locator=self._submit_enroll, locator_type="xpath",
                                 info="Enroll Button")
        return not result
