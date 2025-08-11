from selenium.webdriver.common.by import \
    By
from selenium.webdriver.support import \
    expected_conditions as ec
from selenium.webdriver.support.ui import \
    WebDriverWait

from config import \
    TIMEOUT
from pages.base_page import \
    BasePage


class LoginPage(BasePage):
    INPUT_LOGIN = (By.XPATH, '//*[contains(@class, "page_content")]//*[@type="text"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    BUTTON_SUBMIT_LOADER = (By.XPATH, '//button[@type="submit" and @disabled]')
    ERROR_MSG = (
        By.XPATH,
        "//*[@data-featuretarget='login']//*[contains(@class, 'G4JJ0By1qN')]",
    )
    UNIQUE_ELEMENT = (By.XPATH, '//*[contains(@style,"position")]')

    def verify_page_load(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            ec.visibility_of_element_located(self.UNIQUE_ELEMENT),
        )

    def click_button_submit(self):
        self.driver.find_element(*self.BUTTON_SUBMIT).click()

    def send_login(self, value):
        self.driver.find_element(*self.INPUT_LOGIN).send_keys(value)

    def send_login_password(self, value):
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(value)

    def check_loader_state(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            ec.visibility_of_element_located(self.BUTTON_SUBMIT_LOADER)
        ), "Smth went wrong - Element does not apper after timeout"
        WebDriverWait(self.driver, TIMEOUT).until(
            ec.invisibility_of_element_located(self.BUTTON_SUBMIT_LOADER)
        ), "Loader does not disappear after 10 sec"

    def get_error_message_text(self):
        return self.driver.find_element(*self.ERROR_MSG).text
