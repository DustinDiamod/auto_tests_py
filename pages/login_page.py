from selenium.webdriver.common.by import By

from pages.base_page import BasePage


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

    def wait_page_load(self):
        self.wait_visibility(self.UNIQUE_ELEMENT)

    def click_button_submit(self):
        self.click_elem(self.BUTTON_SUBMIT)

    def send_login(self, value):
        self.send_into(self.INPUT_LOGIN, value)

    def send_login_password(self, value):
        self.send_into(self.INPUT_PASSWORD, value)

    def check_loader_state(self):
        self.wait_visibility(self.BUTTON_SUBMIT_LOADER)
        self.wait_disappear(self.BUTTON_SUBMIT_LOADER)

    def get_error_message_text(self):
        return self.get_text(self.ERROR_MSG)
