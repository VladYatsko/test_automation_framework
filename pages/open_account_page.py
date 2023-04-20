import random
from selenium.webdriver import ActionChains
from locators.open_account_locators import OpenAccountLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class OpenAccountPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        
    def open_account_page_is_expected(self):
        assert OpenAccountLocators.URL in self.get_url()
        
    def select_checking(self):
        select = Select(self.driver.find_element(*OpenAccountLocators.ACCOUNT_TYPE))
        select.select_by_index(0)
        
    def select_savings(self):
        select = Select(self.driver.find_element(*OpenAccountLocators.ACCOUNT_TYPE))
        select.select_by_index(1)
        
    def select_account(self):
        select = Select(self.driver.find_element(*OpenAccountLocators.ACCOUNT_TO_TAKE))
        select.select_by_index(0)
        
    def submit_creation(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_visible_element(OpenAccountLocators.OPEN_ACC_BTN)).perform()
        self.click_element(OpenAccountLocators.OPEN_ACC_BTN)
        
    def get_new_account_id(self):
        return self.find_visible_element(OpenAccountLocators.NEW_ACC_ID)
    
    def proceed_to_home(self):
        self.click_element(OpenAccountLocators.HOME_TRANSITION)
        
    def proceed_to_customer_care(self):
        self.click_element(OpenAccountLocators.CUSTOMER_CARE_TRANSITION)
    
    def proceed_to_accounts_overview(self):
        self.click_element(OpenAccountLocators.ACCOUNTS_OVERVIEW_TRANSITION)
        
    def proceed_to_transfer_funds(self):
        self.click_element(OpenAccountLocators.TRANSFER_FUNDS_TRANSITION)
        
    def proceed_to_bill_pay(self):
        self.click_element(OpenAccountLocators.BILL_PAY_TRANSITION)
        
    def proceed_to_find_transactions(self):
        self.click_element(OpenAccountLocators.FIND_TRANSACTIONS_TRANSITION)
        
    def proceed_to_update_profile(self):
        self.click_element(OpenAccountLocators.UPDATE_CONTACT_TRANSITION)
        
    def proceed_to_request_loan(self):
        self.click_element(OpenAccountLocators.REQUEST_LOAN_TRANSITION)
        
    def proceed_to_log_out(self):
        self.click_element(OpenAccountLocators.LOG_OUT_TRANSITION)
        