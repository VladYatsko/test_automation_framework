from selenium.webdriver.common.by import By


class OpenAccountLocators:
    URL = 'https://parabank.parasoft.com/parabank/openaccount.htm'
    ACCOUNT_TYPE = (By.XPATH, '//select[@id="type"]')
    ACCOUNT_TO_TAKE = (By.XPATH, '//select[@id="fromAccountId"]')
    OPEN_ACC_BTN = (By.XPATH, '//input[@value="Open New Account"]')
    NEW_ACC_ID = (By.XPATH, '//a[@id="newAccountId"]')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    ACCOUNTS_OVERVIEW_TRANSITION = (By.XPATH, '//a[text()="Accounts Overview"]')
    TRANSFER_FUNDS_TRANSITION = (By.XPATH, '//a[text()="Transfer Funds"]')
    BILL_PAY_TRANSITION = (By.XPATH, '//a[text()="Bill Pay"]')
    FIND_TRANSACTIONS_TRANSITION = (By.XPATH, '//a[text()="Find Transactions"]')
    UPDATE_CONTACT_TRANSITION = (By.XPATH, '//a[text()="Update Contact Info"]')
    REQUEST_LOAN_TRANSITION = (By.XPATH, '//a[text()="Request Loan"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    