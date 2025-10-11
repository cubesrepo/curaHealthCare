import pytest

from pages.login_page import LoginPage
from utilities import test_data

@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def login_page(self,driver, delay):
        loginpage= LoginPage (driver, delay)
        return loginpage

    def test_valid_login(self, login_page):
        appointment_page = login_page.login_with_valid_credentials()
        assert appointment_page.appointment_page_is_loaded(), \
            "Appointment page did not load properly"

    def test_without_username_and_password(self, login_page):
        current_result = login_page.login_without_entering_credentials()
        expected_result = test_data.login.LOGIN_FAILED_VALIDATION_MESSAGE
        assert current_result == expected_result, \
            f"Expected validation error to be {expected_result}, but got {current_result}"

    @pytest.mark.skip
    def test_invalid_login(self, login_page):
        current_result = login_page.login_with_invalid_credentials()
        expected_result = test_data.login.LOGIN_FAILED_VALIDATION_MESSAGE

        assert  current_result == expected_result, \
            f"Expected validation error to be {expected_result}, but got {current_result}"


