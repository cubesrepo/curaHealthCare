from pages.appointment_page import AppointmentPage
from utilities import test_data
from pages.base_page import BasePage

class LoginPage(BasePage):
    def click_appointment(self):
        appointment = self.wait_clickable(test_data.login.MAKE_APPOINTMENT)
        appointment.click()

    def enter_username_password(self, username, password):
        self.type(test_data.login.USERNAME, username)
        self.type(test_data.login.PASSWORD, password)

    def login(self):
        self.wait_clickable(test_data.login.LOGINBTN).click()

    def get_login_validation_error(self):
        return self.get_text(test_data.login.LOGIN_FAILED_VALIDATION)

    def login_with_valid_credentials(self):
        self.click_appointment()
        self.enter_username_password(test_data.USER_CREDENTIALS["valid_username"],
                                     test_data.USER_CREDENTIALS["valid_password"])
        self.login()
        return AppointmentPage(self.driver)

    def login_without_entering_credentials(self):
        self.click_appointment()
        self.login()
        login_validation_error = self.get_login_validation_error()

        return login_validation_error

    def login_with_invalid_credentials(self):
        self.click_appointment()
        self.enter_username_password(test_data.USER_CREDENTIALS["invalid_username"],
                                     test_data.USER_CREDENTIALS["invalid_password"])
        self.login()
        login_validation_error = self.get_login_validation_error()

        return login_validation_error


