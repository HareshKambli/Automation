import pytest
from selenium import webdriver

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from utilities.customLogger import LogGenenration
from utilities.read_properties import ReadConfig


class Test_002_Home:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGenenration.loggen()

    @pytest.mark.sanity
    def test_leave(self, setup):
        self.logger.info("************* Test_002_Home ******************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.submit()
        self.logger.info("*********Login successfull *********")

        homePage = HomePage(self.driver)
        homePage.selectLeave()

        homePage.setFromDate()
        homePage.selectFromMonth(ReadConfig.getFromMonth())
        homePage.selectFromYear(ReadConfig.getFromYear())
        homePage.selectFromDate(ReadConfig.getFromDate())

        homePage.setToDate()
        homePage.selectToMonth(ReadConfig.getToMonth())
        homePage.selectToYear(ReadConfig.getToYear())
        homePage.selectToDate(ReadConfig.getToDate())
        homePage.selectRejectedLeaves()
        homePage.selectUnit(ReadConfig.getUnit())
        homePage.search()

        self.driver.quit()