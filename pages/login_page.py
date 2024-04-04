import time

import test_data
from pages.base_page import BasePage


class LoginPage(BasePage):
    def valid_login(self):
        time.sleep(2)

        assert self.title_is("CURA Healthcare Service")

        self.wait_clickable(test_data.login.MAKE_APPOINTMENT).click()

        time.sleep(1)

        assert self.url_is("https://katalon-demo-cura.herokuapp.com/profile.php#login")

        self.send_keys(test_data.login.USERNAME, test_data.username)
        time.sleep(1)
        self.send_keys(test_data.login.PASSWORD, test_data.password)
        time.sleep(1)
        self.wait_visibility(test_data.login.LOGINBTN).click()
        time.sleep(1)

        assert self.url_is("https://katalon-demo-cura.herokuapp.com/#appointment")
