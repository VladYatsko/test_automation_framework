from locators.account_activity_locators import AccountActivityLocators
from locators.account_overview_locators import AccountOverviewLocators
from locators.home_locators import HomePageLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from pages.account_overview_page import AccountOverviewPage
from pages.home_page import HomePage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage


class TestAccountOverviewPage:
    def test_account_is_displayed(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.full_register()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        assert account_overview.find_visible_element(AccountOverviewLocators.ACCOUNT_ID).is_displayed() is True
    
    def test_new_account_is_displayed(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.select_savings()
        open_account.submit_creation()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        assert len(account_overview.find_visible_elements(AccountOverviewLocators.ACCOUNT_ID)) == 2
    
    def test_sum_of_balance(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.select_savings()
        open_account.submit_creation()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        account_overview.account_overview_page_is_expected()
        account_overview.get_balance()
        assert account_overview.count_balance_sum() == float(account_overview.get_total())
        
    def test_sum_of_amount(self, driver):
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.open_page()
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.select_savings()
        open_account.submit_creation()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.open_page()
        account_overview.account_overview_page_is_expected()
        account_overview.count_amount_sum()
        assert account_overview.count_amount_sum() == float(account_overview.get_total())
        
    def test_get_into_existing_account(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.proceed_to_registration()
        register_page = RegisterPage(driver, RegisterPageLocators.URL)
        register_page.register_page_is_expected()
        register_page.full_register()
        open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
        open_account.open_page()
        open_account.proceed_to_accounts_overview()
        account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
        account_overview.get_into_account()
        assert AccountActivityLocators.URL in account_overview.get_url()
