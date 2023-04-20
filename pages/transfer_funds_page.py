from locators.transfer_funds_locators import TransferFundsLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class TransferFundsPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def transfer_funds_page_is_expected(self):
        assert self.get_url() == TransferFundsLocators.URL
        
    def specify_amount(self, value):
        self.send_text(TransferFundsLocators.AMOUNT, value)
        
    def select_from_account(self, index):
        try:
            select = Select(self.driver.find_element(*TransferFundsLocators.FROM_ACCOUNT))
            select.select_by_index(index)
        except IndexError:
            select = Select(self.driver.find_element(*TransferFundsLocators.FROM_ACCOUNT))
            select.select_by_index(0)
        
    def select_to_account(self, index):
        try:
            select = Select(self.driver.find_element(*TransferFundsLocators.TO_ACCOUNT))
            select.select_by_index(index)
        except IndexError:
            select = Select(self.driver.find_element(*TransferFundsLocators.FROM_ACCOUNT))
            select.select_by_index(0)
        
    def submit_transfer(self):
        self.click_element(TransferFundsLocators.TRANSFER_BUTTON)
        
    def is_successful(self):
        assert self.find_visible_element(TransferFundsLocators.SUCCESS_FROM_ACC).is_displayed() is True
        assert self.find_visible_element(TransferFundsLocators.SUCCESS_TO_ACC).is_displayed() is True
        assert self.find_visible_element(TransferFundsLocators.SUCCESS_AMOUNT).is_displayed() is True
        
    def is_not_successful(self):
        assert self.find_visible_element(TransferFundsLocators.AMOUNT_ERROR).is_displayed() is True
        
    def proceed_to_home(self):
        self.click_element(TransferFundsLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(TransferFundsLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_accounts_overview(self):
        self.click_element(TransferFundsLocators.ACCOUNTS_OVERVIEW_TRANSITION)

    def proceed_to_find_transaction(self):
        self.click_element(TransferFundsLocators.FIND_TRANSACTIONS_TRANSITION)

    def proceed_to_bill_pay(self):
        self.click_element(TransferFundsLocators.BILL_PAY_TRANSITION)

    def proceed_to_update_profile(self):
        self.click_element(TransferFundsLocators.UPDATE_CONTACT_TRANSITION)

    def proceed_to_open_account(self):
        self.click_element(TransferFundsLocators.OPEN_ACCOUNT_TRANSITION)

    def proceed_to_request_loan(self):
        self.click_element(TransferFundsLocators.REQUEST_LOAN_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(TransferFundsLocators.LOG_OUT_TRANSITION)
        