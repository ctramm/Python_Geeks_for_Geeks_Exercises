import pytest


class SomeClassToTest:

    def __init__(self, value):
        self.value = value

    def sum_of_numbers(self, a, b):
        return a + b + self.value


@pytest.mark.usefixtures("one_time_setup", "set_up")
class TestClassDemo:

    @pytest.fixture(autouse=True)
    def class_set_up(self):
        self.abc = SomeClassToTest(10)

    def test_method_a(self, class_set_up):
        result = self.abc.sum_of_numbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_method_b(self, class_set_up):
        print("Running method B")
