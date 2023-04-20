from selenium.webdriver.common.by import By


class AccountActivityLocators:
    URL = 'https://parabank.parasoft.com/parabank/activity.htm?id='
    ACCOUNT_ID = (By.XPATH, '//td[@id="accountId"]')
    ACCOUNT_TYPE = (By.XPATH, '//td[@id="accountType"]')
    BALANCE = (By.XPATH, '//td[@id="balance"]')
    AVAILABLE_FUNDS = (By.XPATH, '//td[@id="availableBalance"]')
    ACTIVITY_PERIOD = (By.XPATH, '//select[@id="month"]')
    TYPE = (By.XPATH, '//select[@id="transactionType"]')
    GO_BUTTON = (By.XPATH, '//input[@value="Go"]')
    NO_TRANSACTION = (By.XPATH, '//b[text()="No transactions found."]')
    TRANSACTION_ID = (By.CSS_SELECTOR, 'tr td:nth-child(2) > a')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    OPEN_ACCOUNT_TRANSITION = (By.XPATH, '//a[text()="Open New Account"]')
    ACCOUNTS_OVERVIEW_TRANSITION = (By.XPATH, '//a[text()="Accounts Overview"]')
    TRANSFER_FUNDS_TRANSITION = (By.XPATH, '//a[text()="Transfer Funds"]')
    BILL_PAY_TRANSITION = (By.XPATH, '//a[text()="Bill Pay"]')
    FIND_TRANSACTIONS_TRANSITION = (By.XPATH, '//a[text()="Find Transactions"]')
    UPDATE_CONTACT_TRANSITION = (By.XPATH, '//a[text()="Update Contact Info"]')
    REQUEST_LOAN_TRANSITION = (By.XPATH, '//a[text()="Request Loan"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    