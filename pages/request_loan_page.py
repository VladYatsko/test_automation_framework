import allure
from locators.request_loan_locators import RequestLoanLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class RequestLoanPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    @allure.step('Validation that request loan page is opened.')
    def request_loan_page_is_expected(self):
        assert self.get_url() == RequestLoanLocators.URL
    
    @allure.step('Specify loan amount.')
    def input_loan_amount(self, value):
        return self.send_text(RequestLoanLocators.LOAN_AMOUNT, value)
    
    @allure.step('Specify down payment.')
    def input_down_payment(self, value):
        return self.send_text(RequestLoanLocators.DOWN_PAYMENT, value)
    
    @allure.step('Select from which account to request loan.')
    def select_from_which_account(self, index):
        try:
            select = Select(self.driver.find_element(*RequestLoanLocators.FROM_ACC_ID))
            select.select_by_index(index)
        except IndexError:
            select = Select(self.driver.find_element(*RequestLoanLocators.FROM_ACC_ID))
            select.select_by_index(0)
    
    @allure.step('Click apply button.')
    def apply_for_loan(self):
        self.click_element(RequestLoanLocators.APPLY_BUTTON)
    
    @allure.step('Validation that loan is approved.')
    def is_approved(self):
        assert self.find_visible_element(RequestLoanLocators.APPROVED).is_displayed() is True
    
    @allure.step('Validation that loan is declined.')
    def is_declined(self):
        assert self.find_visible_element(RequestLoanLocators.NOT_APPROVED).is_displayed() is True
    
    @allure.step('Validation that loan can\'t be requested with existing input.')
    def is_blocked(self):
        assert self.find_visible_element(RequestLoanLocators.ERROR_MSG).is_displayed() is True
    
    @allure.step('Get new account ID number.')
    def get_new_account_id(self):
        return self.find_visible_element(RequestLoanLocators.NEW_ACCOUNT_ID).text

    def proceed_to_home(self):
        self.click_element(RequestLoanLocators.HOME_TRANSITION)
        
    def proceed_to_open_account(self):
        self.click_element(RequestLoanLocators.OPEN_ACCOUNT_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(RequestLoanLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_accounts_overview(self):
        self.click_element(RequestLoanLocators.ACCOUNTS_OVERVIEW_TRANSITION)

    def proceed_to_transfer_funds(self):
        self.click_element(RequestLoanLocators.TRANSFER_FUNDS_TRANSITION)

    def proceed_to_bill_pay(self):
        self.click_element(RequestLoanLocators.BILL_PAY_TRANSITION)

    def proceed_to_find_transactions(self):
        self.click_element(RequestLoanLocators.FIND_TRANSACTIONS_TRANSITION)

    def proceed_to_update_profile(self):
        self.click_element(RequestLoanLocators.UPDATE_CONTACT_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(RequestLoanLocators.LOG_OUT_TRANSITION)
    