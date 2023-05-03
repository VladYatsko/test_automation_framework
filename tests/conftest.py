from datetime import datetime
import os.path
import allure
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture
def setup_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-save-password-bubble')
    if os.path.exists('/.dockerenv'):
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    return options


@pytest.fixture
def driver(setup_chrome_options):
    options = setup_chrome_options
    if os.path.exists('/.dockerenv'):
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    driver.quit()
  