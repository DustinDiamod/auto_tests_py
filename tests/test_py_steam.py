from faker import Faker
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

f = Faker()

from pages.login_page import LoginPage
from pages.main_page import MainPage

TIMEOUT = 10
MAIN_PAGE_URL = "https://store.steampowered.com/"


def test_steam_scenario1(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    wait = WebDriverWait(driver, TIMEOUT)
    main_page.driver.get(MAIN_PAGE_URL)

    wait.until(
        ec.visibility_of_element_located(main_page.UNIQUE_ELEMENT)
    ), "Unique element not found after 10 sec - smth went wrong"
    main_page.driver.find_element(*main_page.BUTTON_LOGIN).click()
    if not login_page.is_opened():
        raise AssertionError(
            f"Expected URL:{login_page.PAGE_LOGIN_URL}/ got:{driver.current_url}"
        )
    wait.until(ec.element_to_be_clickable(login_page.INPUT_LOGIN))
    login_page.input_login_send(f.email())
    wait.until(ec.element_to_be_clickable(login_page.INPUT_PASSWORD))
    login_page.input_login_password_send(f.password())
    login_page.button_submit_elem().click()
    wait.until(
        ec.visibility_of_element_located(login_page.BUTTON_SUBMIT_LOADER)
    ), "Smth went wrong - Element does not apper after timeout"
    wait.until(
        ec.invisibility_of_element_located(login_page.BUTTON_SUBMIT_LOADER)
    ), "Loader does not disappear after 10 sec"
    error_msg = wait.until(ec.visibility_of_element_located(login_page.ERROR_MSG))
    assert error_msg.is_displayed(), "Error does not display"
