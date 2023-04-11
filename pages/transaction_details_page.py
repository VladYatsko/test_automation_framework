from locators.transaction_details_locators import TransactionDetailsLocators
from pages.base_page import BasePage


class TransactionDetailsPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        
    def get_transaction_id(self):
        return self.get_text(TransactionDetailsLocators.TRANSACTION_ID)
    
    def get_date(self):
        return self.get_text(TransactionDetailsLocators.DATE)
    
    def get_description(self):
        return self.get_text(TransactionDetailsLocators.DESCRIPTION)
    
    def get_type(self):
        return self.get_text(TransactionDetailsLocators.TYPE)
    
    def get_amount(self):
        return self.get_text(TransactionDetailsLocators.AMOUNT)

    def proceed_to_home(self):
        self.click_element(TransactionDetailsLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(TransactionDetailsLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_accounts_overview(self):
        self.click_element(TransactionDetailsLocators.ACCOUNTS_OVERVIEW_TRANSITION)

    def proceed_to_transfer_funds(self):
        self.click_element(TransactionDetailsLocators.TRANSFER_FUNDS_TRANSITION)

    def proceed_to_bill_pay(self):
        self.click_element(TransactionDetailsLocators.BILL_PAY_TRANSITION)

    def proceed_to_find_transactions(self):
        self.click_element(TransactionDetailsLocators.FIND_TRANSACTIONS_TRANSITION)

    def proceed_to_update_profile(self):
        self.click_element(TransactionDetailsLocators.UPDATE_CONTACT_TRANSITION)

    def proceed_to_request_loan(self):
        self.click_element(TransactionDetailsLocators.REQUEST_LOAN_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(TransactionDetailsLocators.LOG_OUT_TRANSITION)
        