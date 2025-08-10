from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    BUTTON_MAIN_PAGE_LOGO = (By.XPATH, '//*[contains(@alt, "Ссылка")]')
    BUTTON_LOGIN = (
        By.XPATH,
        '//*[contains(@class, "home_page_sign_in_ctn") and contains(@class, "small")]//*[contains(@class, "btn_green_white_innerfade")]//span'
    )
    UNIQUE_ELEMENT = (By.XPATH, '//*[@class = "steamdeck_banner_desktop"]')