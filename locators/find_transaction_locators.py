from selenium.webdriver.common.by import By


class FindTransactionLocators:
    URL = 'https://parabank.parasoft.com/parabank/findtrans.htm'
    SELECT_ACCOUNT = (By.XPATH, '//select[@id="accountId"]')
    TRANSACTION_ID = (By.XPATH, '//input[@id="criteria.transactionId"]')
    FIND_BY_ID_BTN = (By.XPATH, '//button[@ng-click="criteria.searchType = \'ID\'"]')
    FIND_BY_DATE = (By.XPATH, '//input[@id="criteria.onDate"]')
    FIND_BY_DATE_BTN = (By.XPATH, '//button[@ng-click="criteria.searchType = \'DATE\'"]')
    FIND_BY_START_DATE = (By.XPATH, '//input[@id="criteria.fromDate"]')
    FIND_BY_END_DATE = (By.XPATH, '//input[@id="criteria.toDate"]')
    RANGE_SEARCH_BTN = (By.XPATH, '//button[@ng-click="criteria.searchType = \'DATE_RANGE\'"]')
    AMOUNT = (By.XPATH, '//input[@id="criteria.amount"]')
    AMOUNT_SEARCH_BTN = (By.XPATH, '//button[@ng-click="criteria.searchType = \'AMOUNT\'"]')
    HOME_TRANSITION = (By.XPATH, '//a[@text()="home"]')
    CUSTOMER_CARE_TRANSITION = (By.XPATH, '//a[text()="contact"]')
    OPEN_ACCOUNT_TRANSITION = (By.XPATH, '//a[text()="Open New Account"]')
    ACCOUNTS_OVERVIEW_TRANSITION = (By.XPATH, '//a[text()="Accounts Overview"]')
    TRANSFER_FUNDS_TRANSITION = (By.XPATH, '//a[text()="Transfer Funds"]')
    BILL_PAY_TRANSITION = (By.XPATH, '//a[text()="Bill Pay"]')
    UPDATE_CONTACT_TRANSITION = (By.XPATH, '//a[text()="Update Contact Info"]')
    REQUEST_LOAN_TRANSITION = (By.XPATH, '//a[text()="Request Loan"]')
    LOG_OUT_TRANSITION = (By.XPATH, '//a[text()="Log Out"]')
    