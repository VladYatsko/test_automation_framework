from locators.customer_care_locators import CustomerCarePageLocators
from pages.customer_care_page import CustomerCarePage


class TestCustomerCare:
    def test_successful_form_sent(self, driver):
        customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
        customer_care.open_page()
        customer_care.customer_care_page_is_expected()
        customer_care.input_name()
        customer_care.input_email()
        customer_care.input_phone()
        customer_care.input_text()
        customer_care.submit_message()
        assert customer_care.review_success_message().is_displayed() is True
        
    def test_sending_with_no_arguments(self, driver):
        customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
        customer_care.open_page()
        customer_care.customer_care_page_is_expected()
        customer_care.submit_message()
        assert customer_care.review_error_message().is_displayed() is True
        
    def test_sending_with_missing_argument(self, driver):
        customer_care = CustomerCarePage(driver, CustomerCarePageLocators.URL)
        customer_care.open_page()
        customer_care.customer_care_page_is_expected()
        customer_care.input_name()
        customer_care.input_email()
        customer_care.input_phone()
        customer_care.submit_message()
        assert customer_care.review_error_message().is_displayed() is True
        