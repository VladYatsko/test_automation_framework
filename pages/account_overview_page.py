from locators.account_overview_locators import AccountOverviewLocators
from pages.base_page import BasePage


class AccountOverviewPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def account_overview_page_is_expected(self):
        assert self.get_url() == AccountOverviewLocators.URL
        
    def get_account_id(self):
        return self.get_text(AccountOverviewLocators.ACCOUNT_ID)
        
    def get_into_account(self):
        assert self.find_presenting_element(AccountOverviewLocators.ACCOUNT_ID).is_displayed()
        self.find_presenting_element(AccountOverviewLocators.ACCOUNT_ID).click()

    def proceed_to_home(self):
        self.click_element(AccountOverviewLocators.HOME_TRANSITION)

    def proceed_to_open_account(self):
        self.click_element(AccountOverviewLocators.OPEN_ACCOUNT_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(AccountOverviewLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_request_loan(self):
        self.click_element(AccountOverviewLocators.REQUEST_LOAN_TRANSITION)

    def proceed_to_transfer_funds(self):
        self.click_element(AccountOverviewLocators.TRANSFER_FUNDS_TRANSITION)

    def proceed_to_bill_pay(self):
        self.click_element(AccountOverviewLocators.BILL_PAY_TRANSITION)

    def proceed_to_find_transactions(self):
        self.click_element(AccountOverviewLocators.FIND_TRANSACTIONS_TRANSITION)

    def proceed_to_update_profile(self):
        self.click_element(AccountOverviewLocators.UPDATE_CONTACT_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(AccountOverviewLocators.LOG_OUT_TRANSITION)
    