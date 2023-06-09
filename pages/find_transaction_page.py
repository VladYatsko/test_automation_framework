from datetime import datetime
import allure
from locators.find_transaction_locators import FindTransactionLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class FindTransactionPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    @allure.step('Validation that find transaction page is opened.')
    def find_transaction_page_is_expected(self):
        assert self.get_url() == FindTransactionLocators.URL
    
    @allure.step('Select account number from list by index.')
    def select_account_by_index(self, index):
        try:
            select = Select(self.driver.find_element(*FindTransactionLocators.SELECT_ACCOUNT))
            select.select_by_index(index)
        except IndexError:
            select = Select(self.driver.find_element(*FindTransactionLocators.SELECT_ACCOUNT))
            select.select_by_index(0)
    
    @allure.step('Specify transaction ID number')
    def specify_transaction_id(self, transaction_id):
        self.send_text(FindTransactionLocators.TRANSACTION_ID, transaction_id)
    
    @allure.step('Click search button.')
    def submit_by_transaction_id(self):
        self.click_element(FindTransactionLocators.FIND_BY_ID_BTN)
    
    @allure.step('Specify date.')
    def specify_date(self):
        self.send_text(FindTransactionLocators.FIND_BY_DATE, datetime.today().strftime('%m-%d-%Y'))
    
    @allure.step('Click search button.')
    def submit_by_date(self):
        self.click_element(FindTransactionLocators.FIND_BY_DATE_BTN)
    
    @allure.step('Specify start date.')
    def specify_range_start(self, value):
        self.send_text(FindTransactionLocators.FIND_BY_START_DATE, value)
    
    @allure.step('Specify end date.')
    def specify_range_end(self, value):
        self.send_text(FindTransactionLocators.FIND_BY_END_DATE, value)
    
    @allure.step('Click search button.')
    def submit_by_range(self):
        self.click_element(FindTransactionLocators.RANGE_SEARCH_BTN)
    
    @allure.step('Specify amount.')
    def specify_amount(self, value):
        self.send_text(FindTransactionLocators.AMOUNT, value)
    
    @allure.step('Click search button.')
    def submit_amount(self):
        self.click_element(FindTransactionLocators.AMOUNT_SEARCH_BTN)
    
    @allure.step('Validation that search is successful.')
    def is_successful(self):
        assert self.find_visible_element(FindTransactionLocators.IS_SUCCESSFUL).is_displayed() is True
    
    @allure.step('Validation that search is not successful.')
    def is_not_successful(self):
        assert self.find_visible_element(FindTransactionLocators.ERROR_MSG).is_displayed() is True
    
    def proceed_to_home(self):
        self.click_element(FindTransactionLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(FindTransactionLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_accounts_overview(self):
        self.click_element(FindTransactionLocators.ACCOUNTS_OVERVIEW_TRANSITION)

    def proceed_to_transfer_funds(self):
        self.click_element(FindTransactionLocators.TRANSFER_FUNDS_TRANSITION)

    def proceed_to_bill_pay(self):
        self.click_element(FindTransactionLocators.BILL_PAY_TRANSITION)

    def proceed_to_update_profile(self):
        self.click_element(FindTransactionLocators.UPDATE_CONTACT_TRANSITION)

    def proceed_to_open_account(self):
        self.click_element(FindTransactionLocators.OPEN_ACCOUNT_TRANSITION)

    def proceed_to_request_loan(self):
        self.click_element(FindTransactionLocators.REQUEST_LOAN_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(FindTransactionLocators.LOG_OUT_TRANSITION)
    