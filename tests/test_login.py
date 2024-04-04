import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.order(1)
class TestLogin(BaseTest):
    def test_valid_login(self, driver):
        loginpage = LoginPage(driver)
        loginpage.valid_login()