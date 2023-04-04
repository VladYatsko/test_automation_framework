from selenium.webdriver.common.by import By


class HomePageLocators:
    URL = 'https://parabank.parasoft.com/parabank/index.htm'
    USER_NAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOG_IN = (By.XPATH, '//input[@type="submit"]')
    REGISTER_TRANSITION = (By.XPATH, '//a[text()="Register"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    