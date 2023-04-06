from generator.generator import generated_data
from locators.update_profile_locators import UpdatedProfileLocators
from pages.base_page import BasePage


class UpdateProfilePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        
    def update_profile_page_is_expected(self):
        assert self.get_url() == UpdatedProfileLocators.URL

    def specify_first_name(self):
        created_data = next(generated_data())
        return self.send_text(UpdatedProfileLocators.FIRST_NAME, created_data.first_name)
    
    def specify_last_name(self):
        created_data = next(generated_data())
        return self.send_text(UpdatedProfileLocators.LAST_NAME, created_data.last_name)
    
    def specify_address(self):
        created_data = next(generated_data())
        return self.send_text(UpdatedProfileLocators.ADDRESS, created_data.address)
    
    def specify_city(self):
        created_data = next(generated_data())
        return self.send_text(UpdatedProfileLocators.CITY, created_data.city)
    
    def specify_state(self):
        created_data = next(generated_data())
        return self.send_text(UpdatedProfileLocators.STATE, created_data.state)
    
    def specify_zip_code(self):
        created_data = next(generated_data())
        return self.send_text(UpdatedProfileLocators.ZIP_CODE, created_data.zip_code)
    
    def specify_phone_num(self):
        created_data = next(generated_data())
        return self.send_text(UpdatedProfileLocators.PHONE_NUM, created_data.phone_number)
    
    def submit_register(self):
        self.click_element(UpdatedProfileLocators.UPDATE_PROFILE_BTN)

    def is_successful(self):
        assert self.find_presenting_element(UpdatedProfileLocators.SUCCESS_MSG).is_displayed() is True
        
    def is_not_successful(self):
        assert self.find_presenting_element(UpdatedProfileLocators.SUCCESS_MSG).is_displayed() is False

    def proceed_to_home(self):
        self.click_element(UpdatedProfileLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self):
        self.click_element(UpdatedProfileLocators.CUSTOMER_CARE_TRANSITION)

    def proceed_to_accounts_overview(self):
        self.click_element(UpdatedProfileLocators.ACCOUNTS_OVERVIEW_TRANSITION)

    def proceed_to_transfer_funds(self):
        self.click_element(UpdatedProfileLocators.TRANSFER_FUNDS_TRANSITION)

    def proceed_to_bill_pay(self):
        self.click_element(UpdatedProfileLocators.BILL_PAY_TRANSITION)

    def proceed_to_find_transactions(self):
        self.click_element(UpdatedProfileLocators.FIND_TRANSACTIONS_TRANSITION)

    def proceed_to_open_account(self):
        self.click_element(UpdatedProfileLocators.OPEN_ACCOUNT_TRANSITION)

    def proceed_to_request_loan(self):
        self.click_element(UpdatedProfileLocators.REQUEST_LOAN_TRANSITION)

    def proceed_to_log_out(self):
        self.click_element(UpdatedProfileLocators.LOG_OUT_TRANSITION)
        