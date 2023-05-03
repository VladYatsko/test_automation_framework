import time
import allure
from locators.account_activity_locators import AccountActivityLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class AccountActivityPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    @allure.step('Get account number.')
    def get_acc_number(self) -> str:
        return self.get_text(AccountActivityLocators.ACCOUNT_ID)
    
    @allure.step('Get account type.')
    def get_acc_type(self) -> str:
        return self.get_text(AccountActivityLocators.ACCOUNT_TYPE)
    
    @allure.step('Get actual balance.')
    def get_balance(self) -> str:
        balance = self.get_text(AccountActivityLocators.BALANCE).replace("$", "")
        return balance
    
    @allure.step('Get available funds.')
    def get_available(self) -> str:
        available = self.get_text(AccountActivityLocators.AVAILABLE_FUNDS).replace("$", "")
        return available
    
    @allure.step('Select month.')
    def select_month(self, month: str):
        select = Select(self.driver.find_element(*AccountActivityLocators.ACTIVITY_PERIOD))
        select.select_by_value(month)
    
    @allure.step('Select account type.')
    def select_type(self, index: int):
        select = Select(self.driver.find_element(*AccountActivityLocators.TYPE))
        select.select_by_index(index)
    
    @allure.step('Click search for activity button.')
    def search_for_activity(self):
        self.click_element(AccountActivityLocators.GO_BUTTON)
    
    @allure.step('Click received activity.')
    def select_activity(self):
        self.click_element(AccountActivityLocators.TRANSACTION_ID)
    
    @allure.step('Click activity from the list by index.')
    def select_activity_by_index(self, index: int):
        time.sleep(1)
        account_array = self.find_visible_elements(AccountActivityLocators.TRANSACTION_ID)
        try:
            element = account_array[index]
            element.click()
        except IndexError:
            element = account_array[len(account_array) - 1]
            element.click()

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
        