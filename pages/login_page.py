from pages.base_page import BasePage

class LoginPage(BasePage):

    PAGE_LOGIN_URL = 'https://store.steampowered.com/login/'
    INPUT_LOGIN = ('xpath', '//*[@class="_2GBWeup5cttgbTw8FM3tfx" and @type="text"]')
    INPUT_PASSWORD = ('xpath', '//*[@type="password"]')
    BUTTON_SUBMIT = ('xpath', '//button[@type="submit"]')
    BUTTON_SUBMIT_LOADER = ('xpath', '//*[contains(@class, "DjSvCZoKKfoNSmarsEcTS") and contains(@class, " _2NVQcOnbtdGIu9O-mB9-YE")]')
    ERROR_MSG = ('xpath', "//*[@class='_1W_6HXiG4JJ0By1qN_0fGZ']")