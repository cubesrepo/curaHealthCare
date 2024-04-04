import time

import test_data
from pages.base_page import BasePage


class AppointmentPage(BasePage):
    def valid_appointment(self):
        time.sleep(2)

        facility = self.wait_visibility(test_data.appointment.FACILITY)
        facility.click()

        select = self.select_by_visible_text(facility, "Seoul CURA Healthcare Center")
        self.action_click(select)
        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.READDMISSION).click()

        time.sleep(0.5)

        self.wait_clickable(test_data.appointment.MEDICAL_AID).click()

        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.DATE).click()
        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.MONT_YEAR_HEADER).click()
        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.YEAR_HEADER).click()
        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.YEAR_2025).click()
        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.MONTH_FOCUSED).click()
        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.DAY_25).click()
        time.sleep(0.5)

        self.send_keys(test_data.appointment.COMMENT, "i want to cqwpkewep my appointment to kqweowqejqwo qwoejoqwjeqwoe")
        time.sleep(0.5)

        self.wait_visibility(test_data.appointment.BOOK_APPOINTMENT).click()

        time.sleep(1)

        assert self.url_is("https://katalon-demo-cura.herokuapp.com/appointment.php#summary")