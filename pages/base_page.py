from selenium.webdriver.support import \
    expected_conditions as ec
from selenium.webdriver.support.ui import \
    WebDriverWait

from config import \
    TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_visibility(self, locator):
        return WebDriverWait(self.driver, TIMEOUT).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, TIMEOUT).until(
            ec.element_to_be_clickable(locator)
        )

    def wait_disappear(self, locator):
        return WebDriverWait(self.driver, TIMEOUT).until(
            ec.invisibility_of_element_located(locator)
        )

    def click_elem(self, locator):
        self.wait_visibility(locator).click()

    def send_into(self, locator, value):
        self.wait_clickable(locator).send_keys(value)

    def get_text(self, locator):
        return self.wait_visibility(locator).text
