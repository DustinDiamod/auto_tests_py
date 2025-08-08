from PySteam.pages.base_page import BasePage

class LoginPage(BasePage):

    PAGE_LOGIN_URL = 'https://store.steampowered.com/login/'
    INPUT_LOGIN = ('xpath', '//*[@class="_2v60tM463fW0V7GDe92E5f"]//*[@type="text"]')
    INPUT_PASSWORD = ('xpath', '//*[@class="_2v60tM463fW0V7GDe92E5f"]//*[@type="password"]')
    BUTTON_SUBMIT = ('xpath', '//button[@type="submit"]')
    BUTTON_SUBMIT_LOADER = ('xpath', '//*[@class = "DjSvCZoKKfoNSmarsEcTS _2NVQcOnbtdGIu9O-mB9-YE"]')
    BUTTON_REJECT_COOKIES = ('xpath', "//*[@id='rejectAllButton']//span")
    BUTTON_ACCEPT_COOKIES = ('xpath', "//*[@id='acceptAllButton']//span")
    ERROR_MSG = ('xpath', "//*[text()='Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.']")

    def __init__(self, driver):
        super().__init__(driver)

    def button_submit_elem(self):
        return self.find(self.BUTTON_SUBMIT)

    def input_login_elem(self):
        return self.find(self.INPUT_LOGIN)

    def input_login_send(self,args):
        self.input_login_elem().send_keys(*args)

    def input_login_password_elem(self):
        return self.find(self.INPUT_PASSWORD)

    def input_login_password_send(self,args):
        self.input_login_password_elem().send_keys(*args)

    def get_locator_input_login(self):
        return self.INPUT_LOGIN

    def get_locator_input_login_password(self):
        return self.INPUT_PASSWORD

    def reject_cookies_click(self):
        self.find(self.BUTTON_REJECT_COOKIES).click()