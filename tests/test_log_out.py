import allure
from locators.home_locators import HomePageLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


@allure.suite('Log out test suit.')
class TestlogOut:
    @allure.title("Validation that active user can log out.")
    def test_log_out(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Logout.'):
            open_account.proceed_to_log_out()
        with allure.step('Validation that user is logged out.'):
            assert HomePageLocators.URL in open_account.get_url()
