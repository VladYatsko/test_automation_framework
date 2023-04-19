from locators.home_locators import HomePageLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


class TestlogOut:
    def test_log_out(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.proceed_to_log_out()
        assert HomePageLocators.URL in open_account.get_url()
        