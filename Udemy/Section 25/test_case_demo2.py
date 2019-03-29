"""
Section 25: Lecture 149 - How to implement class level SetUp and TearDown methods
"""
import unittest


class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("#" * 30)
        print("This is the setUpClass running once before all tests.")
        print("#" * 30)

    def setUp(self):
        print("\nThe setUp method will run once before every test.")

    def test_method_a(self):
        print("\nRunning Method A")

    def test_method_b(self):
        print("\nRunning Method B")

    def tearDown(self):
        print("\nThe tearDown method will run after every test.")

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print("#" * 30)
        print("This is the setUpClass running once before all tests")
        print("#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
