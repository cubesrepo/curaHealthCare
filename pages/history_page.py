import time

import pytest

from pages.base_page import BasePage
from utilities import test_data


class HistoryPage(BasePage):

    def click_menu(self):
        self.wait_clickable(test_data.history.MENU_TOGGLE).click()

    def click_history(self):
        self.wait_clickable(test_data.history.HISTORY).click()

    def get_no_appointment_message(self):
        return  self.get_text(test_data.history.NO_APPOINTMENT)

    def get_history_details(self):
        locators = [
                    'FACILITY_HISTORY',
                    'READMISSIOM_HISTORY',
                    'PROGRAM_HISTORY',
                    'DATE_HISTORY',
                    'COMMENT_HISTORY']
        history_fields_value = []
        for locator in locators:
            element_locator = getattr(test_data.history, locator)
            text_value = self.get_text(element_locator)
            history_fields_value.append(text_value)
        return history_fields_value

    def verify_history_with_no_appointment(self):
        self.click_menu()
        self.click_history()
        no_appointment_message = self.get_no_appointment_message()
        return no_appointment_message

    def verify_history_appointment_details(self):
        self.click_menu()
        self.click_history()
        history_details = self.get_history_details()
        return history_details