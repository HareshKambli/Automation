import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="Drivers\\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="Drivers\\geckodriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="Drivers\\chromedriver.exe")


    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# def pytest_configure(config):
#     config._metadata['Project Name'] = 'HR website'
#     config._metadata['Module Name'] = 'Employees'
#     config._metadata['Tester'] = 'Haresh'
#
#
# # It is hook for delete/modify environment info to html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)