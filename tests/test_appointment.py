import pytest

from pages.appointment_page import AppointmentPage
from tests.base_test import BaseTest


@pytest.mark.order(2)
class TestAppointment(BaseTest):
    def test_appointment_without_visit_date(self, driver):
        appointmentpage = AppointmentPage(driver)

        #testing appointemnt validation without visit date
        appointmentpage.check_appointment_without_visit_date()
    def test_valid_appointment(self, driver):
        appointmentpage = AppointmentPage(driver)

        #testing vali appointment
        appointmentpage.valid_appointment()