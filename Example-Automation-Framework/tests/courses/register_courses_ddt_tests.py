from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
from ddt import ddt, data, unpack
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "10", "1220", "10", "76710"),
          ("Learn Python 3 from scratch", "20", "1221", "20", "90210"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv, zip_code):
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, zip_code)
        result = self.courses.verify_enroll_button_is_disabled()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment Failed Verification")
        self.driver.get("https://letskodeit.teachable.com/courses")
