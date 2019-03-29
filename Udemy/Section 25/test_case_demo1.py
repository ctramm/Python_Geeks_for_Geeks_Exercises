"""
Section 25: Lecture 148 - Writing First Test Case
"""
import unittest


class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print("\nThe setUp method will run once before every test.")

    def test_method_a(self):
        print("\nRunning Method A")

    def test_method_b(self):
        print("\nRunning Method B")

    def tearDown(self):
        print("\nThe tearDown method will run after every test.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
