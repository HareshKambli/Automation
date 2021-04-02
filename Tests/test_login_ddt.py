import time

import pytest
from selenium import webdriver
import logging
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGenenration
from utilities import ExcelUtils


class Test_002_DDT_login:
    baseURL = ReadConfig.getURL()
    path = ".//TestData/loginCreds.xlsx"
    logger = LogGenenration.loggen()
    #logging.basicConfig(filename="automation.log",
                        #format="%(asctime)s: %(levelname)s: %(message)s")

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        logging.info(".................Test_002_DDT_login...........")
        self.logger.info("..........Verifying login............")
        self.driver = setup
        self.driver.get(self.baseURL)
        loginPage = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        self.columns = ExcelUtils.getColumnCount(self.path, 'Sheet1')
        login_status = []

        for i in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', i, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', i, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', i, 3)

            loginPage.setUsername(self.user)
            loginPage.setPassword(self.password)
            loginPage.submit()
            time.sleep(2)
            dashboard_url = self.driver.current_url

            if dashboard_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
                self.logger.info("........Successfully logged in for user " + self.user)
                if self.exp == "pass":
                    loginPage.clickLogout()
                    login_status.append("Pass")

                elif self.exp == "fail":
                    self.logger.info("........Failed logged in for user " + self.user)
                    loginPage.clickLogout()
                    login_status.append("Fail")

            else:
                if self.exp == "pass":
                    self.logger.info("........Failed logged in for user " + self.user)
                    login_status.append("Fail")

                elif self.exp == "fail":
                    self.logger.info("........Failed logged in for user " + self.user + " but tc passed")
                    login_status.append("Pass")

        if "Fail" not in login_status:
            self.logger.info("***Login DDT test passed*******")
            self.driver.close()
            assert True
        else:
            self.logger.info("***Login DDT test failed*******")
            self.driver.close()
            assert False