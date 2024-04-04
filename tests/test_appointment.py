import pytest

from pages.appointment_page import AppointmentPage
from tests.base_test import BaseTest


@pytest.mark.order(2)
class TestAppointment(BaseTest):
    def test_valid_appointment(self, driver):
        appointmentpage = AppointmentPage(driver)
        appointmentpage.valid_appointment()