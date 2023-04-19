import random
from generator.generator import generated_data
from locators.bill_pay_locators import BillPayLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class BillPayPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def update_profile_page_is_expected(self):
        assert self.get_url() == BillPayLocators.URL
        
    def select_another_account(self):
        select = Select(self.driver.find_element(*BillPayLocators.FROM_ACCOUNT))
        select.select_by_index(1)

    def specify_first_name(self):
        created_data = next(generated_data())
        return self.send_text(BillPayLocators.PAYEE_NAME, created_data.first_name)

    def specify_address(self):
        created_data = next(generated_data())
        return self.send_text(BillPayLocators.ADDRESS, created_data.address)

    def specify_city(self):
        created_data = next(generated_data())
        return self.send_text(BillPayLocators.CITY, created_data.city)

    def specify_state(self):
        created_data = next(generated_data())
        return self.send_text(BillPayLocators.STATE, created_data.state)

    def specify_zip_code(self):
        created_data = next(generated_data())
        return self.send_text(BillPayLocators.ZIP_CODE, created_data.zip_code)

    def specify_phone_num(self):
        created_data = next(generated_data())
        return self.send_text(BillPayLocators.PHONE_NUM, created_data.phone_number)
    
    def specify_account_and_verify(self):
        acc_number = random.randint(10000, 100000)
        self.send_text(BillPayLocators.ACCOUNT_NUM, str(acc_number))
        self.send_text(BillPayLocators.VERIFY_ACC_NUM, str(acc_number))
    
    def specify_amount(self):
        amount = random.randint(100, 1001)
        return self.send_text(BillPayLocators.PHONE_NUM, str(amount))

    def send_payment(self):
        self.click_element(BillPayLocators.SEND_PAYMENT_BTN)

    def is_successful(self):
        assert self.find_visible_element(BillPayLocators.SUCCESS_PAYEE).is_displayed() is True
        assert self.find_visible_element(BillPayLocators.SUCCESS_AMOUNT).is_displayed() is True
        assert self.find_visible_element(BillPayLocators.SUCCESS_ACC_ID).is_displayed() is True

    def is_not_successful(self):
        assert self.find_visible_element(BillPayLocators.ERROR_MSG).is_displayed() is True

    def proceed_to_home(self):
        self.click_element(BillPayLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(BillPayLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_accounts_overview(self):
        self.click_element(BillPayLocators.ACCOUNTS_OVERVIEW_TRANSITION)

    def proceed_to_transfer_funds(self):
        self.click_element(BillPayLocators.TRANSFER_FUNDS_TRANSITION)

    def proceed_to_update_contact(self):
        self.click_element(BillPayLocators.UPDATE_CONTACT_TRANSITION)

    def proceed_to_find_transactions(self):
        self.click_element(BillPayLocators.FIND_TRANSACTIONS_TRANSITION)

    def proceed_to_open_account(self):
        self.click_element(BillPayLocators.OPEN_ACCOUNT_TRANSITION)

    def proceed_to_request_loan(self):
        self.click_element(BillPayLocators.REQUEST_LOAN_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(BillPayLocators.LOG_OUT_TRANSITION)
