import allure
import pytest
from locators.home_locators import HomePageLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.home_page import HomePage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


class TestRegisterPage:
    @allure.title("Validation that user can be registered with all the fields specified.")
    def test_successful_registration(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Validation that home page is opened.'):
            home_page.home_page_is_expected()
        with allure.step('Proceed to registration page.'):
            home_page.proceed_to_registration()
        with allure.step('Validation that registration page is opened.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields.'):
            register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account_page = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account_page.open_page()
        with allure.step('Validation that open account page is opened.'):
            open_account_page.open_account_page_is_expected()
 
    @pytest.mark.xfail
    @allure.title("Validation that user can't be registered with no arguments sent.")
    def test_register_with_no_fields(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Validation that home page is opened.'):
            home_page.home_page_is_expected()
        with allure.step('Proceed to registration page.'):
            home_page.proceed_to_registration()
        with allure.step('Validation that registration page is opened.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.register_page_is_expected()
        with allure.step('Click Submit button.'):
            register_page.submit_register()
        with allure.step('Validation that 11 messages are displayed.'):
            assert len(register_page.get_error_messages()) == 11
    
    @allure.title("Validation that user can't be registered with missing argument.")
    def test_with_one_missing_arg(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Validation that home page is opened.'):
            home_page.home_page_is_expected()
        with allure.step('Proceed to registration page.'):
            home_page.proceed_to_registration()
        with allure.step('Validation that registration page is opened.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.register_page_is_expected()
        with allure.step('Specify first name.'):
            register_page.specify_first_name()
        with allure.step('Specify last name.'):
            register_page.specify_last_name()
        with allure.step('Specify address.'):
            register_page.specify_address()
        with allure.step('Specify city.'):
            register_page.specify_city()
        with allure.step('Specify state.'):
            register_page.specify_state()
        with allure.step('Specify zip code.'):
            register_page.specify_zip_code()
        with allure.step('Specify phone number.'):
            register_page.specify_phone_number()
        with allure.step('Specify SSN.'):
            register_page.specify_ssn()
        with allure.step('Specify password.'):
            register_page.specify_password()
        with allure.step('Click Submit button.'):
            register_page.submit_register()
        with allure.step('Validation that user is not registered.'):
            assert register_page.get_error_message().is_displayed() is True
        