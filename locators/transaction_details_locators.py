from selenium.webdriver.common.by import By


class TransactionDetailsLocators:
    URL = 'https://parabank.parasoft.com/parabank/transaction.htm?id='
    TRANSACTION_ID = (By.CSS_SELECTOR, 'tr > td:nth-child(2)')
    DATE = (By.CSS_SELECTOR, 'tr:nth-child(2) > td:nth-child(2)')
    DESCRIPTION = (By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(2)')
    TYPE = (By.CSS_SELECTOR, 'tr:nth-child(4) > td:nth-child(2)')
    AMOUNT = (By.CSS_SELECTOR, 'tr:nth-child(5) > td:nth-child(2)')
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
