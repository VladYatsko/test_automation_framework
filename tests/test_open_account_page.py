from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


class TestOpenAccountPage:
    def test_create_new_checking_account(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.full_register()
        open_account_page = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account_page.open_page()
        open_account_page.open_account_page_is_expected()
        open_account_page.select_checking()
        open_account_page.select_account()
        open_account_page.submit_creation()
        assert open_account_page.get_new_account_id().is_displayed() is True
        
    def test_create_new_savings_account(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.full_register()
        open_account_page = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account_page.open_page()
        open_account_page.open_account_page_is_expected()
        open_account_page.select_savings()
        open_account_page.select_account()
        open_account_page.submit_creation()
        assert open_account_page.get_new_account_id().is_displayed() is True
    