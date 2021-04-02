import pytest
from selenium import webdriver
import logging
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGenenration

class Test_001_login:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGenenration.loggen()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info(".................Test_001_home...........")
        self.logger.info("..........Verifying login............")
        self.driver = setup
        self.driver.get(self.baseURL)
        loginPage = LoginPage(self.driver)

        loginPage.setUsername(self.username)
        loginPage.setPassword(self.password)
        loginPage.submit()
        user = loginPage.getUser()
        print("user is.........."+user)
        if user == "Welcome haresh":
            self.logger.info("........Successfully logged in..............")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.error("............login failed..............")
            self.driver.close()
            assert False

