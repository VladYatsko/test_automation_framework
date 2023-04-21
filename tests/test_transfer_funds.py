import allure
from locators.account_overview_locators import AccountOverviewLocators
from locators.open_account_locators import OpenAccountLocators
from locators.register_locators import RegisterPageLocators
from locators.transfer_funds_locators import TransferFundsLocators
from pages.account_overview_page import AccountOverviewPage
from pages.open_account_page import OpenAccountPage
from pages.register_page import RegisterPage
from pages.transfer_funds_page import TransferFundsPage


class TestTransferFunds:
    @allure.title("Validation that user can't perform transfer with no amount specified.")
    def test_with_no_amount(self, driver):
        with allure.step('Proceed to registration page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        with allure.step('Validation that registration page is opened.'):
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields and click submit button.'):
            register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Validation that open account page is opened.'):
            open_account.open_account_page_is_expected()
        with allure.step('Proceed to transfer funds page.'):
            open_account.proceed_to_transfer_funds()
        with allure.step('Validation that transfer funds page is opened.'):
            transfer_funds = TransferFundsPage(driver, TransferFundsLocators.URL)
            transfer_funds.transfer_funds_page_is_expected()
        with allure.step('Click transfer button.'):
            transfer_funds.move_to_element_and_submit(TransferFundsLocators.TRANSFER_BUTTON)
        with allure.step('Validation that transfer was not performed.'):
            transfer_funds.is_not_successful()
    
    @allure.title("Validation that user can't transfer funds with amount > current balance")
    def test_with_invalid_amount(self, driver):
        with allure.step('Proceed to registration page.'):
            register_page = RegisterPage(driver, RegisterPageLocators.URL)
            register_page.open_page()
        with allure.step('Validation that registration page is opened.'):
            register_page.register_page_is_expected()
        with allure.step('Specify all the fields and click submit button.'):
            register_page.full_register()
        with allure.step('Proceed to open account page.'):
            open_account = OpenAccountPage(driver, OpenAccountLocators.URL)
            open_account.open_page()
        with allure.step('Validation that open account page is opened.'):
            open_account.open_account_page_is_expected()
        with allure.step('Proceed to account overview page.'):
            open_account.proceed_to_accounts_overview()
        with allure.step('Validation that account overview page is opened.'):
            account_overview = AccountOverviewPage(driver, AccountOverviewLocators.URL)
            account_overview.account_overview_page_is_expected()
        current_balance = float(account_overview.get_balance())
        with allure.step('Proceed to transfer funds page.'):
            account_overview.proceed_to_transfer_funds()
        with allure.step('Validation that transfer funds page is opened.'):
            transfer_funds = TransferFundsPage(driver, TransferFundsLocators.URL)
            transfer_funds.transfer_funds_page_is_expected()
        with allure.step('Specify amount.'):
            transfer_funds.specify_amount(current_balance + 1)
        with allure.step('Click transfer button.'):
            transfer_funds.move_to_element_and_submit(TransferFundsLocators.TRANSFER_BUTTON)
        with allure.step('Validation that transfer was not performed.'):
            transfer_funds.is_not_successful()
        