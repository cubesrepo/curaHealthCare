import pytest

from pages.appointment_page import AppointmentPage
from pages.history_page import HistoryPage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class TestHistory(BaseTest):


    def test_history_with_appointment(self, driver):
        historypage = HistoryPage(driver)
        appointmentpage = AppointmentPage(driver)

        #check history of first appointment
        historypage.check_history_with_appointment()

        #perform appointemnt without comment and readmission
        appointmentpage.check_appointment_without_comment_and_readmission()

        #check history of first appointment and 2nd appointment
        historypage.check_history_with_appointment()
