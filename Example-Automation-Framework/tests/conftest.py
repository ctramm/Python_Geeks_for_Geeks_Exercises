import pytest
from pages.home.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory


@pytest.fixture()
def set_up():
    # print("Running method level setUp")
    yield
    # print("Running method level tearDown")


@pytest.fixture(scope="class")
def one_time_setup(browser, request):
    # print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--osType")
