from selenium.webdriver.common.by import By


class CustomerCarePageLocators:
    URL = 'https://parabank.parasoft.com/parabank/contact.htm'
    NAME = (By.XPATH, '//input[@id="name"]')
    EMAIL = (By.XPATH, '//input[@id="email"]')
    PHONE = (By.XPATH, '//input[@id="phone"]')
    MESSAGE = (By.XPATH, '//textarea[@id="message"]')
    SEND_MESSAGE_BUTTON = (By.XPATH, '//input[@value="Send to Customer Care"]')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    REGISTER_TRANSITION = (By.XPATH, '//a[text()="Register"]')
    ERROR_MESSAGE = (By.XPATH, '//span[@class="error"]')
    SUCCESS_MESSAGE = (By.XPATH, '//p[text()="Thank you asd"]')
    