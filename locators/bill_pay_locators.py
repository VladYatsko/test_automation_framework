from selenium.webdriver.common.by import By


class BillPayLocators:
    URL = 'https://parabank.parasoft.com/parabank/billpay.htm'
    PAYEE_NAME = (By.XPATH, '//input[@name="payee.name"]')
    ADDRESS = (By.XPATH, '//input[@name="payee.address.street"]')
    CITY = (By.XPATH, '//input[@name="payee.address.city"]')
    STATE = (By.XPATH, '//input[@name="payee.address.state"]')
    ZIP_CODE = (By.XPATH, '//input[@name="payee.address.zipCode"]')
    PHONE_NUM = (By.XPATH, '//input[@name="payee.phoneNumber"]')
    ACCOUNT_NUM = (By.XPATH, '//input[@name="payee.accountNumber"]')
    VERIFY_ACC_NUM = (By.XPATH, '//input[@name="verifyAccount"]')
    AMOUNT = (By.XPATH, '//input[@name="amount"]')
    FROM_ACCOUNT = (By.XPATH, '//select[@name="fromAccountId"]')
    SEND_PAYMENT_BTN = (By.XPATH, '//input[@value="Send Payment"]')
    SUCCESS_PAYEE = (By.XPATH, '//span[@id="payeeName"]')
    SUCCESS_AMOUNT = (By.XPATH, '//span[@id="amount"]')
    SUCCESS_ACC_ID = (By.XPATH, '//span[@id="fromAccountId"]')
    ERROR_MSG = (By.CSS_SELECTOR, 'td > span.error')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    OPEN_ACCOUNT_TRANSITION = (By.XPATH, '//a[text()="Open New Account"]')
    ACCOUNTS_OVERVIEW_TRANSITION = (By.XPATH, '//a[text()="Accounts Overview"]')
    TRANSFER_FUNDS_TRANSITION = (By.XPATH, '//a[text()="Transfer Funds"]')
    FIND_TRANSACTIONS_TRANSITION = (By.XPATH, '//a[text()="Find Transactions"]')
    UPDATE_CONTACT_TRANSITION = (By.XPATH, '//a[text()="Update Contact Info"]')
    REQUEST_LOAN_TRANSITION = (By.XPATH, '//a[text()="Request Loan"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    