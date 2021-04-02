from selenium import webdriver


class LoginPage:
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_login_xpath = "//input[@name='Submit']"
    user_id = "welcome"
    logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def getUser(self):
        return self.driver.find_element_by_id(self.user_id).text

    def clickLogout(self):
        self.driver.find_element_by_id(self.user_id).click()
        self.driver.find_element_by_link_text(self.logout_link_text).click()
