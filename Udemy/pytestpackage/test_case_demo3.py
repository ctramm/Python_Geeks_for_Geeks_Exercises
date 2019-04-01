# """
# Section 26: Lecture 157 - Multiple ways to run test cases
#
# file name should star with test
# test method name should start with test
#
# py.test test_mod.py # run tests in module
# py.test somepath # run all tests below some path
# py.test test_module.py::test_method # only run test_method in test_module
#
# -s to print statements
# -v verbose
# """
# import pytest
#
#
# @pytest.fixture()
# def setup():
#     print("Running demo3 setUp")
#     yield
#     print("Running demo3 tearDown")
#
#
# def test_method_a(setup):
#     print("Running demo3 method A")
#
#
# def test_method_b(setup):
#     print("Running demo3 method B")
