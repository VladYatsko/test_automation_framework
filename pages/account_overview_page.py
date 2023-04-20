import time
from locators.account_overview_locators import AccountOverviewLocators
from pages.base_page import BasePage


class AccountOverviewPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def account_overview_page_is_expected(self):
        assert AccountOverviewLocators.URL in self.get_url()
        
    def get_account_id(self):
        return self.get_text(AccountOverviewLocators.ACCOUNT_ID)
    
    def get_into_account_by_index(self, index):
        time.sleep(1)
        account_array = self.find_visible_elements(AccountOverviewLocators.ACCOUNT_ID)
        try:
            element = account_array[index]
            element.click()
        except IndexError:
            element = account_array[len(account_array)-1]
            element.click()
        
    def get_into_account(self):
        assert self.find_visible_element(AccountOverviewLocators.ACCOUNT_ID).is_displayed()
        self.find_visible_element(AccountOverviewLocators.ACCOUNT_ID).click()
        
    def get_balance(self):
        time.sleep(1)
        balance = self.get_text(AccountOverviewLocators.BALANCE).replace("$", "")
        return balance
        
    def get_balance_by_index(self, index: int):
        time.sleep(1)
        account_ids = [element.text for element in self.find_visible_elements(AccountOverviewLocators.BALANCE)]
        account_ids.remove(account_ids[-1])
        try:
            balance = str(account_ids[index]).replace("$", "")
            return balance
        except IndexError:
            balance = str(account_ids[len(account_ids)-1]).replace("$", "")
            return balance
    
    def get_available_amount(self):
        time.sleep(1)
        amount = self.get_text(AccountOverviewLocators.AVAILABLE_AMOUNT).replace("$", "")
        return amount
    
    def get_total(self):
        time.sleep(1)
        total = self.get_text(AccountOverviewLocators.TOTAL).replace("$", "")
        return total
    
    def count_balance_sum(self):
        self.find_visible_element(AccountOverviewLocators.BALANCE)
        time.sleep(2)
        elements = self.find_visible_elements(AccountOverviewLocators.BALANCE)
        acc_balance = [element.text[1:] for element in elements]
        acc_balance.remove(acc_balance[-1])
        result = 0
        for element in acc_balance:
            result += float(element)
        return result
    
    def count_amount_sum(self):
        self.find_visible_element(AccountOverviewLocators.AVAILABLE_AMOUNT)
        time.sleep(2)
        elements = self.find_visible_elements(AccountOverviewLocators.AVAILABLE_AMOUNT)
        acc_balance = [element.text[1:] for element in elements]
        acc_balance.remove(acc_balance[-1])
        result = 0
        for element in acc_balance:
            result += float(element)
        return result

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
    