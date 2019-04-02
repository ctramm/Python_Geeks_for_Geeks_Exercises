import pytest


@pytest.fixture()
def set_up():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def one_time_setup(browser, request):
    print("Running one time setUp")
    if browser == 'firefox':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on Chrome")

    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--platform", help="Enter OS ID")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")
