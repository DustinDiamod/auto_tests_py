from pages.base_page import BasePage

class MainPage(BasePage):
    BUTTON_MAIN_PAGE_LOGO = ('xpath', '//*[contains(@alt, "Ссылка")]')
    BUTTON_LOGIN = ('xpath',
                    '//*[@class= "home_page_sign_in_ctn small"]//*[contains(@class, "btn_green_white_innerfade")]//span')
    MAIN_PAGE_URL = 'https://store.steampowered.com/'
    UNIQUE_ELEMENT = ('xpath', '//*[@class = "steamdeck_banner_desktop"]')