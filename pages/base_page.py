from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

import test_data


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def find(self, locator):
        self.driver.find_element(locator)
    def wait_visibility(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_presence(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )

    def send_keys(self, locator, value):
        self.wait_visibility(locator).clear()
        self.wait_clickable(locator).send_keys(value)

    def hover(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()

    def url_is(self, url):
        return WebDriverWait(self.driver, 20).until(
            EC.url_to_be(url)
        )

    def title_is(self, title):
        return WebDriverWait(self.driver, 20).until(
            EC.title_is(title)
        )

    def action_click(self, locator):
        action = ActionChains(self.driver)
        action.click(locator).perform()

    def select_by_visible_text(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)
    def get_text(self, locator):
        return self.wait_visibility(locator).text
    def get_text_wait_presence(self, locator):
        return self.wait_presence(locator).text

    def get_value(self, locator):
        return self.wait_visibility(locator).get_attribute("value")

    def get_validation_message(self, locator):
        return self.wait_visibility(locator).get_attribute("validationMessage")
