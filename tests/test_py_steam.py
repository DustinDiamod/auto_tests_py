from faker import Faker

f = Faker()

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_steam_scenario1(driver, base_url):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.driver.get(base_url)

    main_page.wait_loading_page(), "Unique element not found after 10 sec - smth went wrong"
    main_page.click_button_login()
    login_page.wait_page_load(), "Failed loading expected element"
    login_page.send_login(f.email())
    login_page.send_login_password(f.password())
    login_page.click_button_submit()
    login_page.check_loader_state()
    error_msg = login_page.get_error_message_text()
    assert (
        "проверьте свой пароль и имя аккаунта" in error_msg
    ), f"Current text - {error_msg}"
