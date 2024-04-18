import pytest

from pages.profile_page import ProfilePage
from tests.base_test import BaseTest

@pytest.mark.order(4)
class TestProfile(BaseTest):


    def test_navigate_to_profile_and_click_logout(self, driver):
        profilepage = ProfilePage(driver)

        #perform navigation to profile page and click logout
        profilepage.navigate_to_profile_then_click_logout()