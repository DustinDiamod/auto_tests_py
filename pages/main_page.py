from PySteam.pages.base_page import BasePage

BUTTON_LOGIN = ('xpath','//*[@class= "home_page_sign_in_ctn small"]//*[contains(@class, "btn_green_white_innerfade")]//span')
BUTTON_MAIN_PAGE_LOGO = ('xpath', '//*[contains(@alt, "Ссылка")]')

class MainPage(BasePage):

    MAIN_PAGE_URL = 'https://store.steampowered.com/'

    def __init__(self, driver):
        super().__init__(driver)

    def button_login(self):
        return self.find(BUTTON_LOGIN)

    def button_mp_logo(self):
        return self.find(BUTTON_MAIN_PAGE_LOGO)

    def button_login_click(self):
        self.button_login().click()

    def button_mp_logo_click(self):
        self.button_mp_logo().click()