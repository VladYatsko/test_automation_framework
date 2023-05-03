import allure
from generator.generator import generated_data
from locators.update_profile_locators import UpdatedProfileLocators
from pages.base_page import BasePage


class UpdateProfilePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    @allure.step('Validation that update profile page is opened.')
    def update_profile_page_is_expected(self):
        assert self.get_url() == UpdatedProfileLocators.URL
    
    @allure.step('Specify first name.')
    def specify_first_name(self):
        created_data = next(generated_data())
        try:
            return self.send_text(UpdatedProfileLocators.FIRST_NAME, created_data.first_name)
        except ValueError:
            self.find_visible_element(UpdatedProfileLocators.FIRST_NAME)
            return self.send_text(UpdatedProfileLocators.FIRST_NAME, created_data.first_name)
    
    @allure.step('Specify last name.')
    def specify_last_name(self):
        created_data = next(generated_data())
        try:
            return self.send_text(UpdatedProfileLocators.LAST_NAME, created_data.last_name)
        except ValueError:
            self.find_visible_element(UpdatedProfileLocators.LAST_NAME)
            return self.send_text(UpdatedProfileLocators.LAST_NAME, created_data.last_name)
    
    @allure.step('Specify address.')
    def specify_address(self):
        created_data = next(generated_data())
        try:
            return self.send_text(UpdatedProfileLocators.ADDRESS, created_data.address)
        except ValueError:
            self.find_visible_element(UpdatedProfileLocators.ADDRESS)
            return self.send_text(UpdatedProfileLocators.ADDRESS, created_data.address)
    
    @allure.step('Specify city.')
    def specify_city(self):
        created_data = next(generated_data())
        try:
            return self.send_text(UpdatedProfileLocators.CITY, created_data.city)
        except ValueError:
            self.find_visible_element(UpdatedProfileLocators.CITY)
            return self.send_text(UpdatedProfileLocators.CITY, created_data.city)
    
    @allure.step('Specify state.')
    def specify_state(self):
        created_data = next(generated_data())
        try:
            return self.send_text(UpdatedProfileLocators.STATE, created_data.state)
        except ValueError:
            self.find_visible_element(UpdatedProfileLocators.STATE)
            return self.send_text(UpdatedProfileLocators.STATE, created_data.state)
    
    @allure.step('Specify zip code.')
    def specify_zip_code(self):
        created_data = next(generated_data())
        try:
            return self.send_text(UpdatedProfileLocators.ZIP_CODE, created_data.zip_code)
        except ValueError:
            self.find_visible_element(UpdatedProfileLocators.ZIP_CODE)
            return self.send_text(UpdatedProfileLocators.ZIP_CODE, created_data.zip_code)
    
    @allure.step('Specify phone number.')
    def specify_phone_num(self):
        created_data = next(generated_data())
        try:
            return self.send_text(UpdatedProfileLocators.PHONE_NUM, created_data.phone_number)
        except ValueError:
            self.find_visible_element(UpdatedProfileLocators.PHONE_NUM)
            return self.send_text(UpdatedProfileLocators.PHONE_NUM, created_data.phone_number)
    
    @allure.step('Specify register.')
    def submit_register(self):
        self.click_element(UpdatedProfileLocators.UPDATE_PROFILE_BTN)
    
    @allure.step('Validation that profile is updated.')
    def is_successful(self):
        assert self.find_visible_element(UpdatedProfileLocators.SUCCESS_MSG).is_displayed()
    
    @allure.step('Validation that profile was not updated.')
    def is_not_successful(self):
        assert self.find_visible_element(UpdatedProfileLocators.ERROR_MSG).is_displayed()
    
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
