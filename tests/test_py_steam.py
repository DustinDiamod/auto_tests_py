from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

f = Faker()

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_mp_url_is_equal(driver):
    timeout = 10
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    wait = WebDriverWait(driver, timeout)

    main_page.driver.get(main_page.MAIN_PAGE_URL)
    try:
        wait.until(ec.visibility_of_element_located(MainPage.UNIQUE_ELEMENT))
    except TimeoutException:
        raise AssertionError("Unique element not found after 10 sec - smth went wrong")
    button_login_main = driver.find_element(*main_page.BUTTON_LOGIN)
    button_login_main.click()
    if not driver.current_url == LoginPage.PAGE_LOGIN_URL:
        raise AssertionError(
            f"Expected URL:{LoginPage.PAGE_LOGIN_URL}/ got:{driver.current_url}"
        )
    input_login = wait.until(ec.element_to_be_clickable(login_page.INPUT_LOGIN))
    input_login.send_keys(f.email())
    input_password = wait.until(ec.element_to_be_clickable(login_page.INPUT_PASSWORD))
    input_password.send_keys(f.password())
    button_login = driver.find_element(*login_page.BUTTON_SUBMIT)
    button_login.click()
    try:
        wait.until(ec.visibility_of_element_located(login_page.BUTTON_SUBMIT_LOADER))
    except TimeoutException:
        raise AssertionError('Smth went wrong - Element does not apper after timeout')
    try:
        wait.until(ec.invisibility_of_element_located(login_page.BUTTON_SUBMIT_LOADER))
    except TimeoutException:
        raise AssertionError('Loader does not disappear after 10 sec')
    error_msg = wait.until(ec.visibility_of_element_located(login_page.ERROR_MSG))
    assert error_msg.is_displayed(), 'Ошибка не отображается'