from selenium.webdriver.common.by import By


class TransferFundsLocators:
    URL = 'https://parabank.parasoft.com/parabank/transfer.htm'
    AMOUNT = (By.XPATH, '//input[@id="amount"]')
    FROM_ACCOUNT = (By.XPATH, '//select[@id="fromAccountId"]')
    TO_ACCOUNT = (By.XPATH, '//select[@id="toAccountId"]')
    TRANSFER_BUTTON = (By.XPATH, '//input[@value="Transfer"]')
    SUCCESS_FROM_ACC = (By.XPATH, '//span[@id="fromAccountId"]')
    SUCCESS_TO_ACC = (By.XPATH, '//span[@id="toAccountId"]')
    SUCCESS_AMOUNT = (By.XPATH, '//span[@id="amount"]')
    ERROR_MSG = (By.XPATH, '//p[@class="error"]')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    OPEN_ACCOUNT_TRANSITION = (By.XPATH, '//a[text()="Open New Account"]')
    ACCOUNTS_OVERVIEW_TRANSITION = (By.XPATH, '//a[text()="Accounts Overview"]')
    BILL_PAY_TRANSITION = (By.XPATH, '//a[text()="Bill Pay"]')
    FIND_TRANSACTIONS_TRANSITION = (By.XPATH, '//a[text()="Find Transactions"]')
    UPDATE_CONTACT_TRANSITION = (By.XPATH, '//a[text()="Update Contact Info"]')
    REQUEST_LOAN_TRANSITION = (By.XPATH, '//a[text()="Request Loan"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    