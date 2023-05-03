import allure
from generator.generator import generated_data
from locators.customer_care_locators import CustomerCarePageLocators
from pages.base_page import BasePage


class CustomerCarePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
    
    @allure.step('Validation that customer care page is opened.')
    def customer_care_page_is_expected(self):
        assert CustomerCarePageLocators.URL in self.get_url()
    
    @allure.step('Specify name.')
    def input_name(self):
        created_data = next(generated_data())
        return self.send_text(CustomerCarePageLocators.NAME, f'{created_data.first_name} {created_data.last_name}')
    
    @allure.step('Specify email.')
    def input_email(self):
        created_data = next(generated_data())
        return self.send_text(CustomerCarePageLocators.EMAIL, created_data.email)
    
    @allure.step('Specify phone.')
    def input_phone(self):
        created_data = next(generated_data())
        return self.send_text(CustomerCarePageLocators.PHONE, created_data.phone_number)
    
    @allure.step('Specify text of message.')
    def input_text(self):
        return self.send_text(CustomerCarePageLocators.MESSAGE, 'Custom text to be sent.')
    
    @allure.step('Submit sending')
    def submit_message(self):
        self.click_element(CustomerCarePageLocators.SEND_MESSAGE_BUTTON)

    def proceed_to_home(self) -> None:
        self.click_element(CustomerCarePageLocators.HOME_TRANSITION)

    def proceed_to_customer_care(self) -> None:
        self.click_element(CustomerCarePageLocators.REGISTER_TRANSITION)
    
    @allure.step('Validation that message is not sent.')
    def review_error_message(self):
        return self.find_visible_element(CustomerCarePageLocators.ERROR_MESSAGE)
    
    @allure.step('Validation that message was successfully sent.')
    def review_success_message(self):
        return self.find_visible_element(CustomerCarePageLocators.SUCCESS_MESSAGE)
    