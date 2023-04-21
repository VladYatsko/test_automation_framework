import allure
from locators.customer_care_locators import CustomerCarePageLocators
from pages.customer_care_page import CustomerCarePage


class TestCustomerCare:
    @allure.title("Validation that user is able to send the message to support.")
    def test_successful_form_sent(self, driver):
        with allure.step('Proceed to customer care page.'):
            customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
            customer_care.open_page()
        with allure.step('Validation that customer care page is opened.'):
            customer_care.customer_care_page_is_expected()
        with allure.step('Specify name of sender.'):
            customer_care.input_name()
        with allure.step('Specify email of sender.'):
            customer_care.input_email()
        with allure.step('Specify phone of sender.'):
            customer_care.input_phone()
        with allure.step('Specify text of message.'):
            customer_care.input_text()
        with allure.step('Click Send message button.'):
            customer_care.submit_message()
        with allure.step('Validation that message is sent.'):
            assert customer_care.review_success_message().is_displayed() is True
    
    @allure.title("Validation that message can't be sent without arguments.")
    def test_sending_with_no_arguments(self, driver):
        with allure.step('Proceed to customer care page.'):
            customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
            customer_care.open_page()
        with allure.step('Validation that customer care page is opened.'):
            customer_care.customer_care_page_is_expected()
        with allure.step('Click Send message button.'):
            customer_care.submit_message()
        with allure.step('Validation that message is not sent.'):
            assert customer_care.review_error_message().is_displayed() is True
    
    @allure.title("Validation that message can't be sent with missing argument.")
    def test_sending_with_missing_argument(self, driver):
        with allure.step('Proceed to customer care page.'):
            customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
            customer_care.open_page()
        with allure.step('Validation that customer care page is opened.'):
            customer_care.customer_care_page_is_expected()
        with allure.step('Specify name of sender.'):
            customer_care.input_name()
        with allure.step('Specify email of sender.'):
            customer_care.input_email()
        with allure.step('Specify phone of sender.'):
            customer_care.input_phone()
        with allure.step('Click Send message button.'):
            customer_care.submit_message()
        with allure.step('Validation that message is not sent.'):
            assert customer_care.review_error_message().is_displayed() is True
        