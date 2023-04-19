from locators.account_activity_locators import AccountActivityLocators
from pages.account_overview_page import AccountOverviewPage
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class AccountActivityPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        
    def get_acc_number(self) -> str:
        return self.get_text(AccountActivityLocators.ACCOUNT_ID)
    
    def get_acc_type(self) -> str:
        return self.get_text(AccountActivityLocators.ACCOUNT_TYPE)
    
    def get_balance(self) -> str:
        return self.get_text(AccountActivityLocators.BALANCE)
    
    def get_available(self) -> str:
        return self.get_text(AccountActivityLocators.AVAILABLE_FUNDS)
    
    def select_month(self, month):
        select = Select(self.driver.find_presenting_element(AccountActivityLocators.ACTIVITY_PERIOD))
        select.select_by_value(month)
        
    def select_type(self, activity_type):
        select = Select(self.driver.find_presenting_element(AccountActivityLocators.TYPE))
        select.select_by_value(activity_type)
        
    def search_for_activity(self):
        self.click_element(AccountActivityLocators.GO_BUTTON)
        
    def select_activity(self):
        self.click_element(AccountActivityLocators.TRANSACTION_ID)

    def proceed_to_home(self):
        self.click_element(AccountActivityLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(AccountActivityLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_accounts_overview(self):
        self.click_element(AccountActivityLocators.ACCOUNTS_OVERVIEW_TRANSITION)

    def proceed_to_transfer_funds(self):
        self.click_element(AccountActivityLocators.TRANSFER_FUNDS_TRANSITION)

    def proceed_to_bill_pay(self):
        self.click_element(AccountActivityLocators.BILL_PAY_TRANSITION)

    def proceed_to_find_transactions(self):
        self.click_element(AccountActivityLocators.FIND_TRANSACTIONS_TRANSITION)

    def proceed_to_update_profile(self):
        self.click_element(AccountActivityLocators.UPDATE_CONTACT_TRANSITION)

    def proceed_to_request_loan(self):
        self.click_element(AccountActivityLocators.REQUEST_LOAN_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(AccountActivityLocators.LOG_OUT_TRANSITION)
        