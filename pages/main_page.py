from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    BUTTON_LOGIN = (
        By.XPATH,
        '//*[contains(@class, "home_page_sign_in_ctn") and contains(@class, "small")]//*[contains(@class, "btn_green_white_innerfade")]//span',
    )
    UNIQUE_ELEMENT = (By.ID, "tab_preview_container")

    def wait_loading_page(self):
        self.wait_visibility(self.UNIQUE_ELEMENT)

    def click_button_login(self):
        self.wait_clickable(self.BUTTON_LOGIN).click()
