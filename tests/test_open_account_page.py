import allure
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


@allure.suite('Open account page test suit.')
class TestOpenAccountPage:
    @allure.title('Validation that user is able to create account of checking type.')
    def test_create_new_checking_account(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account_page = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account_page.open_page()
            open_account_page.open_account_page_is_expected()
        with allure.step('Create account of "Checking" type.'):
            open_account_page.select_checking()
            open_account_page.select_account()
            open_account_page.submit_creation()
        with allure.step('Validation that new account is created.'):
            assert open_account_page.get_new_account_id().is_displayed() is True
    
    @allure.title('Validation that user is able to create account of savings type.')
    def test_create_new_savings_account(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account_page = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account_page.open_page()
            open_account_page.open_account_page_is_expected()
        with allure.step('Create account of "Savings" type.'):
            open_account_page.select_savings()
            open_account_page.select_account()
            open_account_page.submit_creation()
        with allure.step('Validation that new account is created.'):
            assert open_account_page.get_new_account_id().is_displayed() is True
