import pytest


# B, A, C, E, D, F
@pytest.mark.run(order=2)
def test_run_order_method_a(one_time_setup, set_up):
    print("Running method A")


@pytest.mark.run(order=1)
def test_run_order_method_b(one_time_setup, set_up):
    print("Running method B")


@pytest.mark.run(order=3)
def test_run_order_method_c(one_time_setup, set_up):
    print("Running method C")


@pytest.mark.run(order=5)
def test_run_order_method_d(one_time_setup, set_up):
    print("Running method D")


@pytest.mark.run(order=4)
def test_run_order_method_e(one_time_setup, set_up):
    print("Running method E")


@pytest.mark.run(order=6)
def test_run_order_method_f(one_time_setup, set_up):
    print("Running method F")
