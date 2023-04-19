from generator.generator import generated_data
from locators.customer_care_locators import CustomerCarePageLocators
from pages.base_page import BasePage


class CustomerCarePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        
    def customer_care_page_is_expected(self):
        assert CustomerCarePageLocators.URL in self.get_url()
        
    def input_name(self):
        created_data = next(generated_data())
        return self.send_text(CustomerCarePageLocators.NAME, f'{created_data.first_name} {created_data.last_name}')
    
    def input_email(self):
        created_data = next(generated_data())
        return self.send_text(CustomerCarePageLocators.EMAIL, created_data.email)
    
    def input_phone(self):
        created_data = next(generated_data())
        return self.send_text(CustomerCarePageLocators.PHONE, created_data.phone_number)
    
    def input_text(self):
        return self.send_text(CustomerCarePageLocators.MESSAGE, 'Custom text to be sent.')
        
    def submit_message(self):
        self.click_element(CustomerCarePageLocators.SEND_MESSAGE_BUTTON)

    def proceed_to_home(self) -> None:
        self.click_element(CustomerCarePageLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self) -> None:
        self.click_element(CustomerCarePageLocators.REGISTER_TRANSITION)
        
    def review_error_message(self):
        return self.find_visible_element(CustomerCarePageLocators.ERROR_MESSAGE)
    
    def review_success_message(self):
        return self.find_visible_element(CustomerCarePageLocators.SUCCESS_MESSAGE)
    