from pages.home.navigation_page import NavigationPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.nav = NavigationPage(self.driver)
        self.ts = Status(self.driver)

    def test_my_courses_link(self):
        self.nav.navigate_to_my_courses()

    def test_all_courses_link(self):
        self.nav.navigate_to_all_courses()

    def test_practice_link(self):
        self.nav.navigate_to_practice()

    def test_user_settings_link(self):
        self.nav.navigate_to_users_settings()

    def test_header_logo_link(self):
        self.nav.click_header_logo()

