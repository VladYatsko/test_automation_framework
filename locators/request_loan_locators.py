from selenium.webdriver.common.by import By


class RequestLoanLocators:
    URL = 'https://parabank.parasoft.com/parabank/requestloan.htm'
    LOAN_AMOUNT = (By.XPATH, '//input[@id="amount"]')
    DOWN_PAYMENT = (By.XPATH, '//input[@id="downPayment"]')
    FROM_ACC_ID = (By.XPATH, '//select[@id="fromAccountId"]')
    APPLY_BUTTON = (By.XPATH, '//input[@value="Apply Now"]')
    NOT_APPROVED = (By.XPATH, '//p[@class="error ng-scope"]')
    ERROR_MSG = (By.XPATH, '//p[@class="error"]')
    APPROVED = (By.CSS_SELECTOR, 'div.ng-scope > p')
    NEW_ACCOUNT_ID = (By.XPATH, '//a[@id="newAccountId"]')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    OPEN_ACCOUNT_TRANSITION = (By.XPATH, '//a[text()="Open New Account"]')
    ACCOUNTS_OVERVIEW_TRANSITION = (By.XPATH, '//a[text()="Accounts Overview"]')
    TRANSFER_FUNDS_TRANSITION = (By.XPATH, '//a[text()="Transfer Funds"]')
    BILL_PAY_TRANSITION = (By.XPATH, '//a[text()="Bill Pay"]')
    FIND_TRANSACTIONS_TRANSITION = (By.XPATH, '//a[text()="Find Transactions"]')
    UPDATE_CONTACT_TRANSITION = (By.XPATH, '//a[text()="Update Contact Info"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    