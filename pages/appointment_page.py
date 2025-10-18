from utilities import test_data
from pages.base_page import BasePage
import time

class AppointmentPage(BasePage):
    def appointment_page_is_loaded(self):
        return self.wait_visibility(test_data.appointment.MAKE_APPOINTMENT_HEADER) is not None

    def select_facility(self, facility_text):
        self.select_dropdown_value(test_data.appointment.FACILITY, facility_text)

    def set_readmission(self, check=True):
        self.set_option(test_data.appointment.READDMISSION, check)

    def set_medical_aid(self):
        self.set_option(test_data.appointment.MEDICAL_AID)

    def set_none(self):
        self.set_option(test_data.appointment.NONE)

    def pick_date(self):
        locators = ['DATE',
                    'DAYS_HEADER',
                    'MONTH',
                    'DAY_25']
        for locator in locators:
            element_locator = getattr(test_data.appointment, locator)
            self.wait_clickable(element_locator).click()

    def pick_past_date(self):
        locators = ['DATE',
                    'DAYS_HEADER',
                    'MONTH_HEADER',
                    'YEAR_2024',
                    'MONTH_MARCH',
                    'DAY_1']
        for locator in locators:
            element_locator = getattr(test_data.appointment, locator)
            self.wait_clickable(element_locator).click()
            time.sleep(1)


    def add_comment(self, comment_text):
        self.action_click(test_data.appointment.COMMENT)
        self.type(test_data.appointment.COMMENT, comment_text)

    def book_appointment(self):
        self.wait_clickable(test_data.appointment.BOOK_APPOINTMENT).click()

    def get_validation_fillout_fields(self):
        return self.validation_fillout_this_field(test_data.appointment.DATE)

    def appointment_confirmation_is_loaded(self):
       return self.get_text(test_data.appointment_confirmation.TEXT_APPT_CONFIRMATION)

    def check_facility(self):
        return self.get_text(test_data.appointment_confirmation.FACILITY_LABEL)

    def check_all_fields(self):

        locators = ['FACILITY_LABEL', 'READMISSION_LABEL', 'PROGRAM_LABEL',
                    'DATE_LABEL', 'COMMENT_LABEL'
        ]

        text_values = []

        for locator in locators:
            element_locator = getattr(test_data.appointment_confirmation, locator)
            text_value = self.get_text(element_locator)

            text_values.append(text_value)

        return text_values

    def verify_valid_appointment(self):
        self.select_facility("Hongkong CURA Healthcare Center")
        self.set_readmission()
        self.set_medical_aid()
        self.pick_date()
        self.add_comment("Appointment for December 25")
        self.book_appointment()

        return self.appointment_confirmation_is_loaded()

    def verify_appointment_wihout_visitdate(self):
        self.select_facility("Hongkong CURA Healthcare Center")
        self.set_readmission()
        self.set_medical_aid()
        self.add_comment("Appointment without a date")
        self.book_appointment()

        return self.get_validation_fillout_fields(), self.appointment_confirmation_is_loaded()

    def verify_appt_past_date(self):
        self.select_facility("Seoul CURA Healthcare Center")
        self.set_readmission()
        self.set_readmission(False)
        self.pick_past_date()
        self.add_comment("Test past date")
        self.book_appointment()

        return self.appointment_confirmation_is_loaded()

    def verify_appt_confirmation_fields(self):
        self.set_readmission()
        self.set_none()
        self.pick_date()
        self.add_comment("Test appointment confirmation fields.")
        self.book_appointment()

        return self.appointment_confirmation_is_loaded(), self.check_all_fields()

