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


class MainPage(BasePage):
    BUTTON_LOGIN = (
        By.XPATH,
        '//*[contains(@class, "home_page_sign_in_ctn") and contains(@class, "small")]//*[contains(@class, "btn_green_white_innerfade")]//span',
    )
    UNIQUE_ELEMENT = (By.ID, "tab_preview_container")

    def wait_loading_page(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            ec.visibility_of_element_located(self.UNIQUE_ELEMENT)
        )

    def click_button_login(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()
