import allure
from locators.account_activity_locators import AccountActivityLocators
from locators.account_overview_locators import AccountOverviewLocators
from locators.home_locators import HomePageLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.account_overview_page import AccountOverviewPage
from pages.home_page import HomePage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


@allure.suite('Account overview page test suit.')
class TestAccountOverviewPage:
    @allure.title("Validation that initial account is displayed for newly created user.")
    def test_account_is_displayed(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        register_page.full_register()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Validation that account number is displayed.'):
            assert account_overview.find_visible_element(AccountOverviewLocators.ACCOUNT_ID).is_displayed() is True
    
    @allure.title("Validation that if user opens new account 2 accounts are displayed.")
    def test_new_account_is_displayed(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Select "Savings" account type and submit.'):
            open_account.select_savings()
            open_account.submit_creation()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
        with allure.step('Validation that 2 account numbers are displayed.'):
            assert len(account_overview.find_visible_elements(AccountOverviewLocators.ACCOUNT_ID)) == 2
    
    @allure.title("Validation that funds are transferred to new account properly.")
    def test_sum_of_balance(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Select "Savings" account type and submit.'):
            open_account.select_savings()
            open_account.submit_creation()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
            account_overview.account_overview_page_is_expected()
        with allure.step('Validation that sum of balances for accounts matches total value.'):
            assert account_overview.count_balance_sum() == float(account_overview.get_total())
    
    @allure.title("Validation that funds are transferred as amount to new account properly.")
    def test_sum_of_amount(self, driver):
        with allure.step('Proceed to register page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Select "Savings" account type and submit.'):
            open_account.select_savings()
            open_account.submit_creation()
        with allure.step('Proceed to account overview page.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.open_page()
            account_overview.account_overview_page_is_expected()
        with allure.step('Validation that amount of funds for accounts matches total.'):
            assert account_overview.count_amount_sum() == float(account_overview.get_total())
    
    @allure.title("Validation that user is able to get into account for additional details.")
    def test_get_into_existing_account(self, driver):
        with allure.step('Proceed to home page.'):
            home_page = HomePage(driver, HomePageLocators.URL)
            home_page.open_page()
        with allure.step('Proceed to register page.'):
            home_page.proceed_to_registration()
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.register_page_is_expected()
        register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Proceed to account overview page.'):
            open_account.proceed_to_accounts_overview()
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.get_into_account()
        with allure.step('Validation that user is redirected to details of existing account.'):
            assert AccountActivityLocators.URL in account_overview.get_url()
