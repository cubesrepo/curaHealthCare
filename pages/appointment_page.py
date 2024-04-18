import time

import test_data
from pages.base_page import BasePage


class AppointmentPage(BasePage):
    def check_appointment_without_visit_date(self):
        time.sleep(2)

        # click apply for readmission
        self.wait_clickable(test_data.appointment.READDMISSION).click()
        time.sleep(0.5)

        # add comment
        comment = "Hello, I'd like to schedule an appointment"
        self.send_keys(test_data.appointment.COMMENT, comment)
        time.sleep(1)

        # click book appointment
        book_appt_btn = self.wait_clickable(test_data.appointment.BOOK_APPOINTMENT)
        self.action_click(book_appt_btn)

        time.sleep(1)

        # assert validation message
        assert self.get_validation_message(test_data.appointment.DATE) == "Please fill out this field."


    def valid_appointment(self):
        time.sleep(2)
        #click on comment to remove the display of the date picker
        comment = self.wait_visibility(test_data.appointment.COMMENT)
        self.action_click(comment)

        time.sleep(2)
        #click facility
        facility = self.wait_visibility(test_data.appointment.FACILITY)
        facility.click()

        facility_value = "Seoul CURA Healthcare Center"
        #select Seoul CURA Healthcare Center
        select = self.select_by_visible_text(facility, facility_value)
        self.action_click(select)
        time.sleep(1)


        #click medical aid radio btn
        self.wait_clickable(test_data.appointment.MEDICAL_AID).click()
        time.sleep(0.5)

        #click date
        date = self.wait_visibility(test_data.appointment.DATE)
        date.click()
        time.sleep(0.5)

        #click month header from date picker
        month_header = self.wait_clickable(test_data.appointment.MONT_YEAR_HEADER)
        self.action_click(month_header)
        time.sleep(0.5)

        #click year header
        year_header = self.wait_clickable(test_data.appointment.YEAR_HEADER)
        self.action_click(year_header)
        time.sleep(0.5)

        #select year 2025
        year_2025 = self.wait_clickable(test_data.appointment.YEAR_2025)
        self.action_click(year_2025)
        time.sleep(0.5)

        #select month dec
        month_dec = self.wait_clickable(test_data.appointment.MONTH)
        self.action_click(month_dec)
        time.sleep(0.5)

        #select day 25
        day_25 = self.wait_clickable(test_data.appointment.DAY_25)
        self.action_click(day_25)
        time.sleep(0.5)

        #add comment
        comment = "Hello, I'd like to schedule an appointment"
        self.send_keys(test_data.appointment.COMMENT, comment)
        time.sleep(0.5)

        #retreive the date
        textdate = self.get_value(test_data.appointment.DATE)

        #click book appointment
        book_apt_btn = self.wait_clickable(test_data.appointment.BOOK_APPOINTMENT)
        self.action_click(book_apt_btn)

        time.sleep(1)
        #assertion of url page
        assert self.url_is("https://katalon-demo-cura.herokuapp.com/appointment.php#summary")
        #assertion of text confirm
        assert self.get_text(test_data.appointment.TEXT_APPT_CONFIRMATION) == "Appointment Confirmation"
        #assertion  of facility label
        assert self.get_text(test_data.appointment.FACILITY_LABEL) == facility_value
        #assertion readmission
        assert self.get_text(test_data.appointment.READMISSION_LABEL) == "Yes"
        #assertion of healthcare program
        assert self.get_text(test_data.appointment.PROGRAM_LABEL) == "Medicaid"
        #date assertion
        assert self.get_text(test_data.appointment.DATE_LABEL) == str(textdate)
        #comment assertion
        assert self.get_text(test_data.appointment.COMMENT_LABEL) == comment

    def check_appointment_without_comment_and_readmission(self):
        time.sleep(1.5)
        # checking page title
        assert self.title_is("CURA Healthcare Service")

        # click appointment button
        self.wait_clickable(test_data.login.MAKE_APPOINTMENT).click()

        time.sleep(1)
        # click none radio button
        none_radio_btn = self.wait_clickable(test_data.appointment.NONE_PROGRAMS)
        self.action_click(none_radio_btn)

        time.sleep(0.5)
        #input date without using datepicker
        date_value = "10/03/2029"
        self.send_keys(test_data.appointment.DATE, date_value)

        #click comment to remove the display of the datepicker
        comemnt = self.wait_visibility(test_data.appointment.COMMENT)
        self.action_click(comemnt)

        #click book appointment btn
        book_appt_btn = self.wait_clickable(test_data.appointment.BOOK_APPOINTMENT)
        self.action_click(book_appt_btn)

        time.sleep(1)
        # assertion of url page
        assert self.url_is("https://katalon-demo-cura.herokuapp.com/appointment.php#summary")
        # assertion of text confirm
        assert self.get_text(test_data.appointment.TEXT_APPT_CONFIRMATION) == "Appointment Confirmation"
        # assertion  of facility label
        assert self.get_text(test_data.appointment.FACILITY_LABEL) == "Tokyo CURA Healthcare Center"
        # assertion readmission
        assert self.get_text(test_data.appointment.READMISSION_LABEL) == "No"
        # assertion of healthcare program
        assert self.get_text(test_data.appointment.PROGRAM_LABEL) == "None"
        # date assertion
        assert self.get_text(test_data.appointment.DATE_LABEL) == date_value
        # comment assertion
        assert self.get_text_wait_presence(test_data.appointment.COMMENT_LABEL) == ""

