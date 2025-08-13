import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from cfg.config_reader import ConfigReader


@pytest.fixture()
def driver():
    config = ConfigReader()
    browser_cfg = config.get_browser_config()

    service = Service(executable_path=ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    if browser_cfg.get("headless"):
        options.add_argument("--headless")
    if browser_cfg.get("window_size"):
        options.add_argument(f"--window-size={browser_cfg['window_size']}")

    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()


@pytest.fixture()
def base_url():
    return ConfigReader().get_base_url()
