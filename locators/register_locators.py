from selenium.webdriver.common.by import By


class RegisterPageLocators:
    URL = 'https://parabank.parasoft.com/parabank/register.htm'
    FIRST_NAME = (By.XPATH, '//input[@id="customer.firstName"]')
    LAST_NAME = (By.XPATH, '//input[@id="customer.lastName"]')
    ADDRESS = (By.XPATH, '//input[@id="customer.address.street"]')
    CITY = (By.XPATH, '//input[@id="customer.address.city"]')
    STATE = (By.XPATH, '//input[@id="customer.address.state"]')
    ZIP_CODE = (By.XPATH, '//input[@id="customer.address.zipCode"]')
    PHONE_NUM = (By.XPATH, '//input[@id="customer.phoneNumber"]')
    SSN = (By.XPATH, '//input[@id="customer.ssn"]')
    USERNAME = (By.XPATH, '//input[@id="customer.username"]')
    PASSWORD = (By.XPATH, '//input[@id="customer.password"]')
    CONFIRM_PASS = (By.XPATH, '//input[@id="repeatedPassword"]')
    REGISTER_BUTTON = (By.XPATH, '//input[@value="Register"]')
    ERROR_MESSAGE = (By.XPATH, '//span[@id="customer.lastName.errors"]')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    