from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from PySteam.pages.login_page import *
from PySteam.pages.main_page import *

# не пон исходя из задания, поч такой огромный тестовый сценарий, это атомарно? Разбил на 3, если надо переделать - ок
# первые два изи, а в третьем я чет припух писать его
# мб я чет не так понял, но мне каж чем тесты меньше тем понятнее и чище выглядит
# в логин пейдж насрал методов(просто смотрел видео, повторял за челом), если там есть откровенное г, подсвети плз

def test_mp_url_is_equal(driver):
    main_page = MainPage(driver)
    main_page.open(main_page.MAIN_PAGE_URL)
    assert MainPage.MAIN_PAGE_URL == driver.current_url


def test_login_button_from_mp(driver):
    main_page = MainPage(driver)
    main_page.open(main_page.MAIN_PAGE_URL)
    main_page.button_login_click()
    assert driver.current_url == LoginPage.PAGE_LOGIN_URL


def test_sign_in_section(driver): #тут как то странно с попапом кук, в conftest я указал опшн headless, подсвети плз что не так, упустил на каком этапе оно ушло, мб всегда инкогнито ставить?
    login_page = LoginPage(driver)
    login_page.open(login_page.PAGE_LOGIN_URL)
    wait = WebDriverWait(driver, 10)
    try:
        reject_b = wait.until(ec.element_to_be_clickable(login_page.BUTTON_REJECT_COOKIES))
        reject_b.click()
        wait.until(ec.invisibility_of_element_located(login_page.BUTTON_REJECT_COOKIES))
    except TimeoutException:
        print('Баннера нет')
    input_login = wait.until(ec.element_to_be_clickable(login_page.get_locator_input_login()))
    input_login.send_keys('DJKHALEED@UA.777')
    input_password = wait.until(ec.element_to_be_clickable(login_page.get_locator_input_login_password()))
    input_password.send_keys('777')
    login_page.button_submit_elem().click()
    loader = wait.until(ec.visibility_of_element_located(login_page.BUTTON_SUBMIT_LOADER))
    assert loader.is_displayed(), 'Лоадер не отображается'
    wait.until(ec.invisibility_of_element_located(login_page.BUTTON_SUBMIT_LOADER))
    error_msg = wait.until(ec.visibility_of_element_located(login_page.ERROR_MSG))
    assert error_msg.is_displayed(), 'Ошибка не отображается'