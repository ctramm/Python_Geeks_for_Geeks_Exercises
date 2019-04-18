from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.status import Status
from utilities.read_data import get_csv_data
from ddt import ddt, data, unpack
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.nav = NavigationPage(self.driver)
        self.ts = Status(self.driver)

    def setUp(self):
        self.nav.click_header_logo()
        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)
    @data(*get_csv_data("C:\\Users\\Ctramm\\PycharmProjects\\ExampleAutomationFramework\\testdata.csv"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv, zip_code):
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, zip_code)
        result = self.courses.verify_enroll_button_is_disabled()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment Failed Verification")
        self.courses.take_screenshot("test_invalid_enrollment")
