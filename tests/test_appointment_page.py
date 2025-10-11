import pytest
from pages.appointment_page import AppointmentPage
from tests.conftest import login_driver
from utilities import test_data

@pytest.mark.appointment
class TestAppointmentPage:
    @pytest.fixture
    def appointment_page(self, login_driver, delay):
        return  AppointmentPage(login_driver, delay)

    def test_valid_appointment(self, appointment_page):
        current_result = appointment_page.verify_valid_appointment()
        expected_result = test_data.appointment_confirmation.APPT_CONFIRMATION_MESSAGE
        assert current_result == expected_result, \
            f"Expected message to be {expected_result}, but got {current_result}"

    def test_appointment_without_visit_date(self, appointment_page):
        current_result_fill_out_this_field, current_result_is_loaded = appointment_page.verify_appointment_wihout_visitdate()
        expected_result_fill_out_this_field = "Please fill out this field."

        assert current_result_fill_out_this_field == expected_result_fill_out_this_field, \
            f"Expected result to be {expected_result_fill_out_this_field}, but got {current_result_fill_out_this_field}"

        assert current_result_is_loaded is None, "Appointment Confirmation is Loaded"

    def test_appt_past_date(self, appointment_page):
        current_result_is_loaded = appointment_page.verify_appt_past_date()

        assert current_result_is_loaded, f"Appointment Confirmation is not loaded"

    def test_appt_confirmation_fields(self, appointment_page):
        is_loaded, current_values = appointment_page.verify_appt_confirmation_fields()
        expected_values = ["Tokyo CURA Healthcare Center", "Yes", "None",
                          "25/12/2025", "Test appointment confirmation fields."]

        assert is_loaded
        for current_value, expected_value in zip(current_values, expected_values):
            assert current_value == expected_value, \
                f"Expected value to be {expected_value}, but got {current_value}"





