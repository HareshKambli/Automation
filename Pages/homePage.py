from selenium import webdriver
import pytest
from selenium.webdriver.support.select import Select


class HomePage:
    leave_option_id = "menu_leave_viewLeaveModule"
    from_date_name = "leaveList[calFromDate]"
    to_date_name = "leaveList[calToDate]"
    from_month_class = "ui-datepicker-month"
    from_year_class = "ui-datepicker-year"
    to_month_class = "ui-datepicker-month"
    to_year_class = "ui-datepicker-year"
    rejected_checkbox_id = "leaveList_chkSearchFilter_-1"
    unit_dropdown_id = "leaveList_cmbSubunit"
    search_button_name = "btnSearch"

    def __init__(self, driver):
        self.driver = driver

    def selectLeave(self):
        self.driver.find_element_by_id(self.leave_option_id).click()

    def setFromDate(self):
        self.driver.find_element_by_name(self.from_date_name).click()

    def selectFromMonth(self, month):
        from_month_select = Select(self.driver.find_element_by_class_name(self.from_month_class))
        from_month_select.select_by_visible_text(month)

    def selectFromYear(self, year):
        from_year_select = Select(self.driver.find_element_by_class_name(self.from_year_class))
        from_year_select.select_by_visible_text(year)

    def selectFromDate(self, date):
        self.driver.find_element_by_xpath("//a[text()="+date+"]").click()

    def setToDate(self):
        self.driver.find_element_by_name(self.to_date_name).click()

    def selectToMonth(self, month):
        to_month_select = Select(self.driver.find_element_by_class_name(self.to_month_class))
        to_month_select.select_by_visible_text(month)

    def selectToYear(self, year):
        to_year_select = Select(self.driver.find_element_by_class_name(self.to_year_class))
        to_year_select.select_by_visible_text(year)

    def selectToDate(self, date):
        self.driver.find_element_by_xpath("//a[text()="+date+"]").click()

    def selectRejectedLeaves(self):
        self.driver.find_element_by_id(self.rejected_checkbox_id).click()

    def selectUnit(self, unit):
        select_unit = Select(self.driver.find_element_by_id(self.unit_dropdown_id))
        select_unit.select_by_visible_text(unit)

    def search(self):
        self.driver.find_element_by_name(self.search_button_name).click()