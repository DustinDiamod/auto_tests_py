from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    PAGE_LOGIN_URL = "https://store.steampowered.com/login/"
    INPUT_LOGIN = (By.XPATH, '//*[@class="page_content"]//*[@type="text"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    BUTTON_SUBMIT_LOADER = (By.XPATH, '//button[@type="submit" and @disabled]')
    ERROR_MSG = ("xpath", "//*[@class='_1W_6HXiG4JJ0By1qN_0fGZ']")
    UNIQUE_ELEMENT = ("xpath", '//*[contains(@style,"position")]')

    def is_opened(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.UNIQUE_ELEMENT),
            "Login page is not loaded",
        )
        return True

    def button_submit_elem(self):
        return self.driver.find_element(*self.BUTTON_SUBMIT)

    def input_login_elem(self):
        return self.driver.find_element(*self.INPUT_LOGIN)

    def input_login_send(self, value):
        self.input_login_elem().send_keys(value)

    def input_login_password_elem(self):
        return self.driver.find_element(*self.INPUT_PASSWORD)

    def input_login_password_send(self, value):
        self.input_login_password_elem().send_keys(value)
