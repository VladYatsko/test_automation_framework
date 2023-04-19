import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-save-password-bubble')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
