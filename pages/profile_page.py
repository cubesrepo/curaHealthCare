import time

import test_data
from pages.base_page import BasePage


class ProfilePage(BasePage):

    def navigate_to_profile_then_click_logout(self):
        time.sleep(2)

        #click the menu
        menu_toggle = self.wait_clickable(test_data.history.MENU_TOGGLE)
        self.action_click(menu_toggle)

        time.sleep(0.5)

        #click profile
        profile = self.wait_clickable(test_data.profile.PROFILE)
        self.action_click(profile)

        time.sleep(1)

        #check the page url
        assert self.url_is("https://katalon-demo-cura.herokuapp.com/profile.php#profile")

        #click logout
        logout_btn = self.wait_clickable(test_data.profile.LOG_OUT_BTN)
        self.action_click(logout_btn)

        time.sleep(1)

        #assert the page url is equal to base_Url after clicking the logout
        assert self.url_is(test_data.BASE_URL)