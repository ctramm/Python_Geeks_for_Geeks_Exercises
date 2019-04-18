from pages.home.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.logout()
        self.lp.login("bad@email.com", "badPassword")
        result = self.lp.verify_login_failure()
        self.ts.mark_final("test_invalid_login", result, "Invalid Login passed")

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verify_title()
        self.ts.mark(result, "Verify Title passed")
        result2 = self.lp.verify_login_success()
        self.ts.mark_final("test_valid_login", result2, "Valid login passed")
