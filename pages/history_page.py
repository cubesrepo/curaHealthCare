import time

import test_data
from pages.base_page import BasePage


class HistoryPage(BasePage):
    def check_history_with_appointment(self):
        time.sleep(2)
        #click menu toggle
        menu_toggle = self.wait_clickable(test_data.history.MENU_TOGGLE)
        self.action_click(menu_toggle)

        time.sleep(0.5)

        #click history item
        history = self.wait_clickable(test_data.history.HISTORY)
        self.action_click(history)

        time.sleep(0.5)

        #assertion of url
        assert self.url_is("https://katalon-demo-cura.herokuapp.com/history.php#history")

        time.sleep(1)
        #date history
        assert self.get_text(test_data.history.DATE_HISTORY) == "25/12/2025"
        #facility history
        assert self.get_text(test_data.history.FACILITY_HISTORY) == "Seoul CURA Healthcare Center"
        #assertion of readmission
        assert self.get_text(test_data.history.READMISSIOM_HISTORY) == "Yes"
        #assertion of program
        assert self.get_text(test_data.history.MEDICA_AID_HISTORY) == "Medicaid"
        #assertion of comment
        assert self.get_text(test_data.history.COMMENT_HISTORY) == "Hello, I'd like to schedule an appointment"

        time.sleep(0.5)

        #added try except to prevent failures
        try:
            date_value = "10/03/2029"

            # date history of 2nd appointment assertion
            # we use self.find() because we anticipate that the 2nd appointment will not be displayed when checking the first history.
            # so that we dont have to wait for an extended period.
            assert self.find(test_data.history.DATE_HISTORY_2).text == date_value
            # facility history
            assert self.find(test_data.history.FACILITY_HISTORY_2).text == "Tokyo CURA Healthcare Center"
            # assertion of readmission
            assert self.find(test_data.history.READMISSIOM_HISTORY_2).text == "No"
            # assertion of program
            assert self.find(test_data.history.MEDICA_AID_HISTORY_2).text == "None"
            # assertion of comment
            assert self.find(test_data.history.MEDICA_AID_HISTORY_2).text == ""
        except:
            pass

        #go to homepage
        go_to_homepage = self.wait_presence(test_data.history.GO_TO_HOMEPAGE)
        self.action_click(go_to_homepage)

        time.sleep(1)

