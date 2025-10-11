import pytest

from pages.appointment_page import AppointmentPage
from pages.history_page import HistoryPage
@pytest.mark.history
class TestHistory:
    @pytest.fixture
    def book_appointment(self, login_driver, delay):
        appointment_page = AppointmentPage(login_driver, delay)
        is_loaded, expected_results = appointment_page.verify_appt_confirmation_fields()
        return is_loaded, expected_results

    @pytest.fixture
    def history_page(self, login_driver, delay):
        return HistoryPage(login_driver, delay)

    def test_history_with_no_appointment(self, history_page):
        current_result = history_page.verify_history_with_no_appointment()
        expected_result = "No appointment."
        assert current_result == expected_result,\
            f"Expected result to be {expected_result}, but got {current_result}"

    def test_history_appointment_details(self, book_appointment, history_page):
        current_result_is_loaded, expected_results = book_appointment
        current_results = history_page.verify_history_appointment_details()

        assert current_result_is_loaded, \
            "Appointment confirmation is not loaded."

        for current_result, expected_result in zip(current_results, expected_results):
            assert current_result == expected_result, \
                f"Expected result to be {expected_result}, but got {current_result}"

