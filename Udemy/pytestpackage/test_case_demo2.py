# """
# Section 26: Lecture 156 - Pytest Installation and First Script
# """
# import pytest
#
#
# @pytest.fixture()
# def setup():
#     print("Demo2: Setup will run once BEFORE every test method.")
#     yield
#     print("Demo2: Post yield in setup method will run once AFTER every test method.")
#
#
# def test_method_a(setup):
#     print("Running demo2 method A")
#
#
# def test_method_b(setup):
#     print("Running demo2 method B")
