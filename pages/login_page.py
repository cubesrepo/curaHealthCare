import time

import test_data
from pages.base_page import BasePage


class LoginPage(BasePage):
    def check_login_without_username_and_password(self):
        time.sleep(1)
        # checking page title
        assert self.title_is("CURA Healthcare Service")

        # click appointment button
        self.wait_clickable(test_data.login.MAKE_APPOINTMENT).click()

        #assert page url
        assert self.url_is("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        #assert page title
        assert self.title_is("CURA Healthcare Service")

        #click login btn without username and password
        self.wait_clickable(test_data.login.LOGINBTN).click()

        time.sleep(1)
        #assertion of validation
        assert self.get_text(
            test_data.login.LOGIN_FAILED_VALIDATION) == "Login failed! Please ensure the username and password are valid."

    def check_login_without_username(self):
        time.sleep(2)

        # input password
        self.send_keys(test_data.login.PASSWORD, test_data.password)
        time.sleep(1)
        # click login btn
        self.wait_clickable(test_data.login.LOGINBTN).click()

        time.sleep(1)
        # assertion of validation
        assert self.get_text(
            test_data.login.LOGIN_FAILED_VALIDATION) == "Login failed! Please ensure the username and password are valid."
    def check_login_without_password(self):
        time.sleep(2)
        # input username
        self.send_keys(test_data.login.USERNAME, test_data.username)
        time.sleep(1)
        # click login btn
        self.wait_clickable(test_data.login.LOGINBTN).click()

        time.sleep(1)
        # assertion of validation
        assert self.get_text(
            test_data.login.LOGIN_FAILED_VALIDATION) == "Login failed! Please ensure the username and password are valid."

    def valid_login(self):
        time.sleep(2)

        #input username
        self.send_keys(test_data.login.USERNAME, test_data.username)
        time.sleep(1)
        #input password
        self.send_keys(test_data.login.PASSWORD, test_data.password)
        time.sleep(1)
        #click login btn
        self.wait_clickable(test_data.login.LOGINBTN).click()
        time.sleep(1)

        #check page url
        assert self.url_is("https://katalon-demo-cura.herokuapp.com/#appointment")
