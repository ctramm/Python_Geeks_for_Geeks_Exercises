from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_enrollment(self):
        self.courses.enter_course_name("JavaScript")
        self.courses.select_course_to_enroll("JavaScript for beginners")
        self.courses.enroll_course(num="10", exp="1220", cvv="10", zip_code="76710")
        result = self.courses.verify_enroll_button_is_disabled()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment Failed Verification")
