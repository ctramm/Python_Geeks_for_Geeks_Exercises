"""
Section 25: Lecture 152 - How to run code from terminal
"""
import unittest


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("#" * 30)
        print("Class 1 -> class level setUp")
        print("#" * 30)

    def setUp(self):
        print("Class 1 -> setUp")

    def test_class1_method_a(self):
        print("Running class 1 -> method a")

    def test_class1_method_b(self):
        print("Running class 1 -> method b")

    def tearDown(self):
        print("Class 1 -> tearDown")

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print("#" * 30)
        print("Class 1 -> class level tearDown")
        print("#" * 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
