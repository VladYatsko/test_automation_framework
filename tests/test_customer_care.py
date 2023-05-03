import allure
from locators.customer_care_locators import CustomerCarePageLocators
from pages.customer_care_page import CustomerCarePage


@allure.suite('Customer care page test suit.')
class TestCustomerCare:
    @allure.title("Validation that user is able to send the message to support.")
    def test_successful_form_sent(self, driver):
        with allure.step('Proceed to customer care page page.'):
            customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
            customer_care.open_page()
            customer_care.customer_care_page_is_expected()
        with allure.step('Specify all the fields and click send button.'):
            customer_care.input_name()
            customer_care.input_email()
            customer_care.input_phone()
            customer_care.input_text()
            customer_care.submit_message()
        with allure.step('Validation that message is sent.'):
            assert customer_care.review_success_message().is_displayed() is True
    
    @allure.title("Validation that message can't be sent without arguments.")
    def test_sending_with_no_arguments(self, driver):
        with allure.step('Proceed to customer care page page.'):
            customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
            customer_care.open_page()
            customer_care.customer_care_page_is_expected()
        customer_care.submit_message()
        with allure.step('Validation that message is not sent.'):
            assert customer_care.review_error_message().is_displayed() is True
    
    @allure.title("Validation that message can't be sent with missing argument.")
    def test_sending_with_missing_argument(self, driver):
        with allure.step('Proceed to customer care page page.'):
            customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
            customer_care.open_page()
            customer_care.customer_care_page_is_expected()
        with allure.step('Specify all the fields, leave one field blank and click send button.'):
            customer_care.input_name()
            customer_care.input_email()
            customer_care.input_phone()
            customer_care.submit_message()
        with allure.step('Validation that message is not sent.'):
            assert customer_care.review_error_message().is_displayed() is True
