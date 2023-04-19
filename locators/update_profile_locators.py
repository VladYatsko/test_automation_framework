from selenium.webdriver.common.by import By


class UpdatedProfileLocators:
    URL = 'https://parabank.parasoft.com/parabank/updateprofile.htm'
    FIRST_NAME = (By.XPATH, '//input[@id="customer.firstName"]')
    LAST_NAME = (By.XPATH, '//input[@id="customer.lastName"]')
    ADDRESS = (By.XPATH, '//input[@id="customer.address.street"]')
    CITY = (By.XPATH, '//input[@id="customer.address.city"]')
    STATE = (By.XPATH, '//input[@id="customer.address.state"]')
    ZIP_CODE = (By.XPATH, '//input[@id="customer.address.zipCode"]')
    PHONE_NUM = (By.XPATH, '//input[@id="customer.phoneNumber"]')
    UPDATE_PROFILE_BTN = (By.XPATH, '//value[@id="Update Profile"]')
    SUCCESS_MSG = (By.XPATH, '//div//h1')
    ERROR_MSG = (By.XPATH, '//span[@class="error ng-scope"]')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    OPEN_ACCOUNT_TRANSITION = (By.XPATH, '//a[text()="Open New Account"]')
    ACCOUNTS_OVERVIEW_TRANSITION = (By.XPATH, '//a[text()="Accounts Overview"]')
    TRANSFER_FUNDS_TRANSITION = (By.XPATH, '//a[text()="Transfer Funds"]')
    BILL_PAY_TRANSITION = (By.XPATH, '//a[text()="Bill Pay"]')
    FIND_TRANSACTIONS_TRANSITION = (By.XPATH, '//a[text()="Find Transactions"]')
    REQUEST_LOAN_TRANSITION = (By.XPATH, '//a[text()="Request Loan"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    