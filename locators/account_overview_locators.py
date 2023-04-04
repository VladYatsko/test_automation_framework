from selenium.webdriver.common.by import By


class AccountOverviewLocators:
    URL = 'https://parabank.parasoft.com/parabank/overview.htm'
    ACCOUNT_ID = (By.CSS_SELECTOR, 'td > a')
    BALANCE = (By.CSS_SELECTOR, 'tr > td:nth-child(2)')
    AVAILABLE_AMOUNT = (By.CSS_SELECTOR, 'tr > td:nth-child(3)')
    TOTAL = (By.CSS_SELECTOR, 'tr > td:nth-child(2) > b')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    OPEN_ACCOUNT_TRANSITION = (By.XPATH, '//a[text()="Open New Account"]')
    TRANSFER_FUNDS_TRANSITION = (By.XPATH, '//a[text()="Transfer Funds"]')
    BILL_PAY_TRANSITION = (By.XPATH, '//a[text()="Bill Pay"]')
    FIND_TRANSACTIONS_TRANSITION = (By.XPATH, '//a[text()="Find Transactions"]')
    UPDATE_CONTACT_TRANSITION = (By.XPATH, '//a[text()="Update Contact Info"]')
    REQUEST_LOAN_TRANSITION = (By.XPATH, '//a[text()="Request Loan"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    