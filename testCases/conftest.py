import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
        print("Launching Chrome browser.......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser.......")
    else:
        driver = webdriver.Chrome(options=options)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser vlue to setup method
    return request.config.getoption('--browser')


############################# pyTest THML Report ############################

# Tt is hook for Adding Environmental info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['tester'] = 'Lukesh Ade'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
