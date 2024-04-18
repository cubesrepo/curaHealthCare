import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.order(1)
class TestLogin(BaseTest):
    def test_login_without_username_password(self, driver):
        loginpage = LoginPage(driver)
        loginpage.check_login_without_username_and_password()
    def test_login_without_username(self, driver):
        loginpage = LoginPage(driver)
        loginpage.check_login_without_username()
    def test_login_without_password(self, driver):
        loginpage = LoginPage(driver)
        loginpage.check_login_without_password()
    def test_valid_login(self, driver):
        loginpage = LoginPage(driver)
        loginpage.valid_login()