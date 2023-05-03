import allure
from generator.generator import generated_data
from locators.register_locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    @allure.step('Validation that register page is opened.')
    def register_page_is_expected(self):
        assert RegisterPageLocators.URL in self.get_url()
    
    @allure.step('Specify first name.')
    def specify_first_name(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.FIRST_NAME, created_data.first_name)
    
    @allure.step('Specify last name.')
    def specify_last_name(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.LAST_NAME, created_data.last_name)
    
    @allure.step('Specify address.')
    def specify_address(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.ADDRESS, created_data.address)
    
    @allure.step('Specify city.')
    def specify_city(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.CITY, created_data.city)
    
    @allure.step('Specify state.')
    def specify_state(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.STATE, created_data.state)
    
    @allure.step('Specify zip code.')
    def specify_zip_code(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.ZIP_CODE, created_data.zip_code)
    
    @allure.step('Specify phone number.')
    def specify_phone_number(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.PHONE_NUM, created_data.phone_number)
    
    @allure.step('Specify SSN.')
    def specify_ssn(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.SSN, created_data.social_security_num)
    
    @allure.step('Specify user name.')
    def specify_user_name(self):
        created_data = next(generated_data())
        return self.send_text(RegisterPageLocators.USERNAME, created_data.username)
    
    @allure.step('Specify password.')
    def specify_password(self):
        created_data = next(generated_data())
        original_password = self.send_text(RegisterPageLocators.PASSWORD, created_data.password)
        self.send_text(RegisterPageLocators.CONFIRM_PASS, created_data.password)
        return original_password
    
    @allure.step('Click submit button to register user.')
    def submit_register(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)
    
    @allure.step('Specify all the fields and click submit button.')
    def full_register(self):
        self.specify_first_name()
        self.specify_last_name()
        self.specify_address()
        self.specify_city()
        self.specify_state()
        self.specify_zip_code()
        self.specify_phone_number()
        self.specify_ssn()
        self.specify_user_name()
        self.specify_password()
        self.submit_register()
    
    @allure.step('Validation that user is not registered when multiple fields are not entered.')
    def get_error_messages(self):
        return self.find_visible_elements(RegisterPageLocators.ERROR_MESSAGE)
    
    @allure.step('Validation that user is not registered when single argument is not specified.')
    def get_error_message(self):
        return self.find_visible_element(RegisterPageLocators.ERROR_MESSAGE)
    
    def proceed_to_home(self):
        self.click_element(RegisterPageLocators.HOME_TRANSITION)
        
    def proceed_to_customer_care(self):
        self.click_element(RegisterPageLocators.CUSTOMER_CARE_TRANSITION)
    